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
                <form action="#" method="POST">
            <td>${id}</td>
            <td>${order_user}</td>
            <td> <input type="text" name="input_desk_no" value="${desk_no}"></td>
            <td>
                {% csrf_token %}
                    <select id="menu" class="select-management" name="cuisine_select" required>
                        <option class="disabled" name="${name_of_cuisine}" value=${name_of_cuisine}>${name_of_cuisine}</option>
                        {% for menu in menus %}
                            <option class="" value="{{ menu.name_of_cuisine }}" name="{{ menu.name_of_cuisine }}">{{ menu.name_of_cuisine }}</option>
                        {% endfor %}
                    </select>
            </td>
            <td> <input type="text" name="input_amount" value="${amount}"></td>
            <td> <select id="menu" class="select-management" name="input_status" required>
                <option class="disabled" value="${status}">${status}</option>
                <option class="" value="Pending">Pending</option>
                <option class="" value="Completed">Completed</option>
            </td>
           
            <td> ${price}</td>
            
            <td>{% csrf_token %}
                    <select id="store" class="select-management" name="store_select" required>
                        <option class="disabled" name="${store}" value=${store}>${store}</option>
                        {% for store in stores %}
                            <option class="" value="{{ store.id }}" name="{{ store.id }}">{{ store.name }}</option>
                        {% endfor %}
                    </select>
            </td>
               
            <td>
                        {% csrf_token %}
                <button class="waves-effect waves-light btn" name = "OrderUpdate" id="{{ order.id }}" value="{{ order.id }}" type="submit">Update</button>
            </td>
            <td>
                    {% csrf_token %}
            <button class="waves-effect waves-light btn" name = "DeleteUpdate" id="{{ order.id }}" value="{{ order.id }}" type="submit">Delete</button>
        </td>
            </form>
          </tr>{% endfor %}    
                      </tr>`;
                      $('#order_').append(rows);

            }
        }
    })

}
setInterval('reload()',5000);
    