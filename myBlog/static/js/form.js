// This function gets cookie with a given name
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
/* The functions below will create a header with csrftoken */
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

$(function() {
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        create_post();
    });
    function create_post() {
        var name = $('#name').val()
        var email = $('#email').val()
        var subject = $('#subject').val()
        var message = $('#message').val()
        $.ajax({
            url: 'create_post/',
            type: "POST",
            data: { 'name': name, 'email': email, 'subject': subject, 'message': message },
            success: function(json) {
                $('#name').val('')
                $('#email').val('')
                $('#subject').val('')
                $('#message').val('');
                $('#results').html("<b>"+json.result+"</b>");
            },
            error: function(xhr,errmsg,err) {
                $('#results').html("<div>Произошла ошибка: "+errmsg+"</div>");
            }
        });
    };

$(function() {
    $('#subscribe-form').on('submit', function(event){
        event.preventDefault();
        create_post();
    });

    function subscribe() {
        var name = $('#name').val()
        var email = $('#email').val()
        $.ajax({
            url: 'subscribe_post/',
            type: "POST",
            data: {'name': name, 'email': email},
            success: function(json) {
                $('#name').val('')
                $('#email').val('')
                $('#results').html("<b>"+json.result+"</b>");
            },
            error: function(xhr, errmsr, err) {
                $('#results').html("<div>Произошла ошибка!"+errmsg+"</div>");
            }
        })
    }
});



