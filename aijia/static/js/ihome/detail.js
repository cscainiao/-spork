function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    })
    $(".book-house").show();


    $.get('/house/house_details/'+ location.search.split('=')[1] + '/'+ '', function (msg) {
        var house_imgs = ''
        for (var i=0; i<msg.house_info.images.length; i++) {
            var house_img = '<li class="swiper-slide"><img style="height: 800px; width: 1080px" src="'+ msg.house_info.images[i] + '"></li>'
            house_imgs += house_img
        }
        $('.swiper-wrapper').html(house_imgs)
        $('.house-price span').text(msg.house_info.price)
        $('.house-title').text(msg.house_info.title)
        $('.landlord-pic img').attr('src', msg.house_info.user_pic)
        $('.landlord-name span').text(msg.house_info.user_name)
        $('.text-center li').text(msg.house_info.address)
        var href = '/order/book_house/?house_id='+ msg.house_info.id + '/' + ''
        $('.book-house').attr('href', href)

    })
})