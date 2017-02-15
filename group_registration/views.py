from django.shortcuts import render
from .forms import BasicInfoForm, SpectatorForm, PlayerForm
from django.http import HttpResponse
import logging
LOG = logging.getLogger("app")


def register(request):

    if request.method == 'POST':
        basic_info_form = BasicInfoForm(request.POST)
        option = request.POST.get('user_type')
        if option is not None:
            if option == '1':
                LOG.debug("user_type 1")
                second_form = SpectatorForm(request.POST)

            if option == '2':
                LOG.debug("user_type 2")
                second_form = PlayerForm(request.POST)

        if basic_info_form.is_valid():
            LOG.debug("BASIC INFO FORM VALID")
            user = basic_info_form.save()
            LOG.debug("new user pk = " + str(user.pk))
            userid = user.pk

            if second_form.is_valid():
                second_form.save(user=user)

                return HttpResponse("<h1>SUCCESS!!</h1>")
            else:
                return render(request, 'new.html',
                              {'basic_info_form': basic_info_form.as_table(),
                               'second_form': second_form.as_table()})

    else:
        basic_info_form = BasicInfoForm()
        option = request.GET.get('option')
        if option is not None:
            if option == 'Player':
                second_form = PlayerForm()

            if option == 'Spectator':
                second_form = SpectatorForm()

            return HttpResponse(second_form.as_table())

    return render(request, 'new.html',
                  {'basic_info_form': basic_info_form.as_table()
                   })
