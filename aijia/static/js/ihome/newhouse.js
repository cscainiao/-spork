function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $.get('/house/new_house_show/', function (msg) {
        var areas = ''
        for (var i=0; i<msg.area.length; i++) {
            var area = '<option value="' + msg.area[i].id + '">' + msg.area[i].name + '</option>'
            areas += area
        }
        var facilitys = ''
        $('#area-id').html(areas)
        for (var j=0; j<msg.facility.length; j++) {
            var facility = '<li><div class="checkbox"><label><input type="checkbox" name="facility" value="' + msg.facility[j].id +'">' +msg.facility[j].name +'</label></div></li>'
            facilitys += facility
        }
        $('.house-facility-list').html(facilitys)
    })
})


$('#form-house-info').submit(function () {

    $.post('/house/publish_house/', $(this).serialize(), function (msg) {
        if (msg.code=='200') {
            $('#form-house-image').show()
            $('#form-house-info').hide()
            $('#house-id').val(msg.house_id)
        }
    })
    return false
})


$('#form-house-image').submit(function () {
    $(this).ajaxSubmit({
        url: '/house/add_house_img/',
        type: 'POST',
        dataType: 'json',
        success: function (msg) {
            if (msg.code=='200') {
                var house_imgs = ''
                for (var i=0; i<msg.house_imgs.length; i++) {
                    // alert(msg.house_imgs[i].url)
                    var img = '<img src="' +msg.house_imgs[i].url + '" style="width: 200px; height: 200px">'
                    house_imgs += img
                }
                $('.house-image-cons').html(house_imgs)
            }
        },
        error: function (msg) {
            alert('添加失败')
        }
    })
    return false
})