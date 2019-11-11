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

function addItems() {
    console.log('add items js triggered!')
    console.log("this is the  id")

  
    var data = {};
    var desk_no = document.getElementById("desk_no").value;
    var amount = document.getElementById("amount").value;
    console.log(desk_no);
    console.log(amount);
    // desk_no: $("input[name=desk_no]").val(),
    var  storeselect=document.getElementById("store");
              
    var storeselectid = storeselect.options[storeselect.selectedIndex].value;
    var  menuselect=document.getElementById("menu");
           
    var meuselectid = menuselect.options[menuselect.selectedIndex].value;

    console.log(meuselectid, storeselectid)
    // var store: $("select[name=store_select]").val();
    //     name_of_cuisine: $(this).siblings().filter($("select[name=menu_select]")).val(),
    //     amount: $(this).siblings().filter($("input[name=amount]")).val(),
    data['desk_no'] = desk_no;
    data['store'] = storeselectid;
    data['name_of_cuisine'] = meuselectid;
    data['amount'] = amount;
    data['status'] = "pending";
    console.log("data to be sent to server: " + data);


$.ajax({

    

    url:  '/add_order/',
    type:  'post',
    dataType:  'json',
    data: data,
    success: function  (response) {
       
        console.log(response)
        // response = response["order"]
        // data.orders.forEach(order => {
        // var id = response['id'];

        //YOU MUST USE DOUBLE QUOTO HERE
        var id = response["id"];
        console.log(id)
        var price = response["price"];
        console.log(price)
        var name_of_cuisine = response["name_of_cuisine"];
        var desk_no = response["desk_no"];
        var status = response["status"];
        var store = response["store"]
    let rows = `
            <tr>
            <td>
            ${id}
            </td>
            <td>${name_of_cuisine}
            </td>
            <td>${amount}
            </td>
            <td>
            ${price}
            </td>
            <td>
            ${store}
            </td>
            <td>
            ${desk_no}
            </td>
            <td>
            ${status} 
            </td> 
            <td>      
            <button class="waves-effect waves-light btn deleteBtn" data-id="${id}">Remove</button>
            </td>
            </tr>`;
            console.log(rows)

$('#order_part').append(rows);
$('.deleteBtn').each((i, elm) => 
    {
        $(elm).on("click",  (e) => 
        {
            deleteOrders ($(elm))
        }         )
    }               )

}}).fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem! Did you choose a store and choose a menu?");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
            });
}

function  deleteOrders(el){
    console.log('delete item js triggered!');
    orderId = $(el).data('id')
    data = {'id': orderId};
    console.log(data)
    console.log('order id: ' + orderId);
    $.ajax({
        url:  '/delete_order/',
        type:  'post',
        dataType:  'json',
        data: data,
        success:  function (data) {
            console.log("sucess deleted")
            $(el).parents()[1].remove()
        }
    });
}
