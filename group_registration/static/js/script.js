$(document).ready(function() {
    $("#id_user_type").change(function () {
        $.ajax({
            url: '/register/new',
            data: {option: $("#id_user_type option:selected").text()},
            success: function (html) {
                $("#form2").html(html);
            },
            method: 'GET'
        });
    })
})