
$(document).ready(function() {
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();

        $.ajax({
            url: '/user/login/',
            type: 'POST',
            dataType: 'json',
            data: {'mobile': mobile, 'password': passwd},
            success: function (data) {
                if (data.code=='200') {
                    location.href = '/user/my/'

                } else {
                    location.href = '/user/login/'
                    $("#password-err span").html(data.msg);
                    $("#password-err").show();

                }
            },
            error: function () {
                alert('请求失败')
            }
        })
        return false
    });
})