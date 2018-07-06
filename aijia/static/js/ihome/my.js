function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.ajax({
        url: '/user/my/',
        type: 'GET',
        dataType: 'json',
        success: function (msg) {
            alert(msg)
        },
        error: function (msg) {
            
        }
    })
})