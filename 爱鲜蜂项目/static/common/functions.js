
function addCart(goods_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/axf/addCart/',
        type: 'POST',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.code == 200) {
                $('#num_' + goods_id).text(msg.c_num)
                $('#totalMoney').text(msg.totalMoney)
            } else {
                alert(msg.msg)
            }
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}


function delCart(goods_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
       url: '/axf/delCart/',
       type: 'POST',
       data: {'goods_id': goods_id},
       dataType: 'json',
       headers: {'X-CSRFToken': csrf},
       success(msg){
            $('#totalMoney').text(msg.totalMoney)
           if (msg.c_num!==0){
                $('#num_' + goods_id).text(msg.c_num)
           }
           else {
                $('#num_' + goods_id).text(msg.c_num)
                $('#menuList' + goods_id).remove()
           }
       },
       error(msg){

       }
    })
}


function changeCartState(cart_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/axf/changeCartState/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success(msg){
            $('#totalMoney').text(msg.totalMoney)
            if (msg.is_select){
                $('#cart_' + cart_id).text('√')

            } else {
                $('#cart_' + cart_id).text('x')
            }
        },
        error(msg){
            alert('请求失败')
        }

    })
    
}


function selectAll() {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/axf/selectAll/',
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success(msg){
            $('#selectall span').text('√')
            $('#totalMoney').text(msg.totalMoney)
            $('#checkall').text('√')
        },
        error(msg){
            alert('请求错误')
        }
    })
}


function clearAll() {
     var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/axf/clearAll/',
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success(msg){
            $('#selectall span').text('x')
            $('#totalMoney').text(msg.totalMoney)
            $('#checkall').text('x')
        },
        error(msg){
            alert('请求错误')
        }
    })
}


$(document).ready(function () {
    
    $.get('/axf/showMoney', function (msg) {
        $('#totalMoney').text(msg.totalMoney)
    })
})


function alipay(order_id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/axf/alipay/',
        type: 'POST',
        data: {'order_id': order_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if(msg.code = 1) {
                location.href = '/axf/mine/'
            }
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}