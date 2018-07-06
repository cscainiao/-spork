


$(document).ready(function(){
    $.get('/user/auth_show/', function (msg) {
        if (msg.user.id_name) {
            $('.auth-warn').hide()
            $('#houses-list').show()
        } else {
            $('.auth-warn').show()
            $('#houses-list').hide()
        }
    })
    $.get('/house/show_my_house/', function (msg) {
            var house_info = ''
        for (var i=0; i<msg.house_info.length; i++) {
            var house_str = ''
            house_str += '<li><a href="/house/house_detail/?house_id='+ msg.house_info[i].id + '"><div class="house-title"><h3>房屋ID:' + msg.house_info[i].id + ' —— 房屋标题: ' + msg.house_info[i].title +'</h3></div>'
            house_str += '<div class="house-content"><img style="width: 150px; height: 150px" src="' + msg.house_info[i].image + '">'
            house_str += '<div class="house-text"><ul><li>位于：' + msg.house_info[i].area + '</li><li>价格：￥' + msg.house_info[i].price +'/晚</li>'
            house_str += '<li>发布时间：' + msg.house_info[i].create_time + '</li></ul></div> </div></a></li>'
            house_info += house_str
        }
        $('#houses-list').append(house_info)

    })
})