// csrf token
var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function reload() {
    console.log('auto reload')
    $.ajax({
        url: '/reload_order/',
        type: 'get',
        dataType: 'json',
        success: function(response){
            console.log("get latest one")
        }
    })

}
setInterval('reload()',5000);
    