// function showSuccessMsg() {
//     $('.popup_con').fadeIn('fast', function() {
//         setTimeout(function(){
//             $('.popup_con').fadeOut('fast',function(){});
//         },1000)
//     });
// }
//
// function getCookie(name) {
//     var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
//     return r ? r[1] : undefined;
// }


$(document).ready(function () {
    $('#form-avatar').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/user/profile/',
            type: 'PATCH',
            dataType: 'json',
            success: function (msg) {
                $('#success').html('上传成功')
                $('#user-avatar').attr('src', msg.image_url)
            },
            error: function (msg) {
                $('#success').html('上传失败')
            }
        })
        return false;
    })
    $('#form-name').submit(function () {
         var name = $('#user-name').val()
        $.ajax({
            url: '/user/update_name/',
            type: 'PATCH',
            dataType: 'json',
            data: {'name': name},
            success: function (msg) {
                if (msg.code=='1008') {
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + msg.msg)
                    $('.error-msg').show()
                } else {
                    $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + '修改成功')
                    $('#user-name').val(msg.name)
                    $('.error-msg').show()
                }
            },
            error: function (msg) {
                alert('请求失败')
            }

        })
        return false;
    })
})

function hide_error() {
    $('.error-msg').hide()
}
