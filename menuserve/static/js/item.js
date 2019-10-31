
$(document).ready(function() {

   var $whole_page = $("#whole_page");
   var $content_part = $("#content_part");
   var $post_button = $("#post_button");
   var $post_subject = $("#post_subject");
   var $post_text = $("#post_text");
   var $comment_button = $("button[data-id=comment_button]");
   var $remove_comment_button = $("i[name=remove_comment]");
   var $comment_part = $("div[data-id=comment_part]");

   $whole_page.hide().fadeIn('slow', function() {
       $whole_page.show();
   });

   //This part sets up ajax setting to use csrf token. This part of code is from Django Document.
   function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '=')) {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }
   var csrftoken = getCookie('csrftoken');

   function csrfSafeMethod(method) {
       // these HTTP methods do not require CSRF protection
       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
   }

   function sameOrigin(url) {
       // test that a given url is a same-origin URL
       // url could be relative or scheme relative or absolute
       var host = document.location.host; // host + port
       var protocol = document.location.protocol;
       var sr_origin = '//' + host;
       var origin = protocol + sr_origin;
       // Allow absolute or scheme relative URLs to same origin
       return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
           (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
           // or any other URL that isn't scheme relative or absolute i.e relative.
           !(/^(\/\/|http:|https:).*/.test(url));
   }
   $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
               // Send the token to same-origin, relative URLs only.
               // Send the token only if the method warrants CSRF protection
               // Using the CSRFToken value acquired earlier
               xhr.setRequestHeader("X-CSRFToken", csrftoken);
           }
       }
   });

   //template html code for new order
   var orderTemplate = "" +
   "<tr><td>{{order.id}}</td>" +
   "<td>{{order.name_of_cuisine}}</td>" +
   "<td>{{order.amount}}</td>" +
   "<td>{{order.price}}</td>" +
   "<td>{{order.store.name}}</td>" +
   "<td>{{order.desk_no}}</td>" +
   "<td>{{order.status}}</td></tr>" 
/* <td>
{{order.time}}
</td> */
    function addComment(data) {
    var output = Mustache.render(commentTemplate, data);

    $(output).hide().insertAfter("#add_order").slideDown(300);
};

$content_part.on('click', 'button[data-id=orderMenu_button]', function(event) {
    var newOrder = {
        desk_no: $(this).siblings().filter($("input[name=desk_no]")).val(),
        // Need to process
        store: $(this).siblings().filter($("select[name=store_select]")).val(),
        amount: $(this).siblings().filter($("input[name=amount]")).val(),
    };

    var currentButton = $(this);

        $.ajax({
                url: '/add_comment',
                type: 'POST',
                dataType: 'json',
                data: JSON.stringify(newComment),
            })
            .done(function(data) {
                var output = Mustache.render(orderTemplate, data);
                var order_section = currentButton.parent().siblings().filter($("div[data-id=comment_part]"));
                console.log(order_section);
                //$(output).prependTo($(this).parent());
                $(output).hide().prependTo(order_section).slideDown(300);
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });


    });

  
   
})