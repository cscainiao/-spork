//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $(".order-accept").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-accept").attr("order-id", orderId);
    });
    $(".order-reject").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-reject").attr("order-id", orderId);
    });
});

$.get('/order/show_custom_orders/', function (msg) {
       if (msg.code=='200') {
           var custom_orders_html = template('custom_orders', {orders: msg.custom_orders_info})
           $('.orders-list').html(custom_orders_html)

           $(".order-accept").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-accept").attr("order-id", orderId);
            });
            $(".order-reject").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-reject").attr("order-id", orderId);
            });

       }
})

function accept_order() {
    var order_id = $(".modal-accept").attr("order-id")
    var order_status = $('#order_status_on').val()
    $.ajax({
        url: '/order/accept_order/',
        type: 'PATCH',
        dataType: 'json',
        data: {'order_id': order_id},
        success: function (msg) {
            location.href = '/order/custom_orders/'
        },
        error: function (msg) {

        }
    })
}

function refuse_order() {
    var order_id =  $(".modal-reject").attr("order-id")
    var reject_reason = $('#reject-reason').val()
    $.ajax({
        url: '/order/refuse_order/',
        type: 'PATCH',
        dataType: 'json',
        data: {'order_id': order_id, 'reject_reason': reject_reason},
        success: function (msg) {
            location.href = '/order/custom_orders/'

        },
        error: function (msg) {

        }
    })
}