$(document).ready(function() {

  //For getting CSRF token
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

  //For doing AJAX post

  //When submit is clicked
   $("#submit").click(function(e) {

    //Prevent default submit. Must for Ajax post.Beginner's pit.
     e.preventDefault();

    //Prepare csrf token
     var csrftoken = getCookie('csrftoken');

    //Collect data from fields
     var post_text = $('#id_post_text').val();

     $.ajax({
           url : window.location.href, // the endpoint,commonly same url
           type : "POST", // http method
           data : { csrfmiddlewaretoken : csrftoken,
           post_text : post_text
     }, // data sent with the post request

     // handle a successful response
     success : function(json) {
       console.log(json);
       window.location.href = "/posts";
     },
     error : function(xhr,errmsg,err) {
     console.log(xhr.status + ": " + xhr.responseText);
     }
     });
  });

});
