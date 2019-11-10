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
            console.log(response)
            for (order in response) {
                console.log(order)
                var id = response[order]["id"];
                console.log(id)
                var price = response[order]["price"];
                console.log(price)
                var name_of_cuisine =response[order]["name_of_cuisine"];
                var desk_no = response[order]["desk_no"];
                var status = response[order]["status"];
                var store = response[order]["store"]
                var order_user = response[order]["order_user"];
                var amount = response[order]["amount"];
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
    