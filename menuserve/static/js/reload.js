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
            let rows =  '';
            for (order in response) {
                var id = order["id"];
                console.log(id)
                var price = order["price"];
                console.log(price)
                var name_of_cuisine =order["name_of_cuisine"];
                var desk_no = order["desk_no"];
                var status = order["status"];
                var store = order["store"]
                var order_user = order["order_user"];
                var amount = order["amount"];
                rows += `
                <tr>               
            <td>${id}</td>
            <td>${order_user}</td>
            <td>${desk_no}</td>
            <td>${name_of_cuisine}</td>
            <td>${amount}</td>
            <td>${status}</td>
            <td> ${price}</td>
            <td>${store}</td>
            <td>  
            </tr>`;
                      $('#order_').append(rows);

            }
        }
    })

}
setInterval('reload()',5000);
    