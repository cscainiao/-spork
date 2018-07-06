function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function () {
    $('#form-auth').submit(function () {
        var real_name = $('#real-name').val()
        var id_card = $('#id-card').val()
        $.ajax({
            url: '/user/auth/',
            type: 'PATCH',
            dataType: 'json',
            data: {'real_name': real_name, 'id_card': id_card},
            success: function (msg) {
                if (msg.code=='200') {
                    $('.btn-success').hide()
                } else {
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + msg.msg)
                    $('.error-msg').show()
                }
            },
            error: function (msg) {
                alert('请求失败')
            }
        })
        return false
    })
})


$(document).ready(function () {
    $.get('/user/auth_show/', function (msg) {
    if (msg.code=='200') {
        $('#real-name').val(msg.user.id_name)
        $('#id-card').val(msg.user.id_card)

    }
    if (msg.user.id_name) {
        $('.btn-success').hide()
    }
    })
})