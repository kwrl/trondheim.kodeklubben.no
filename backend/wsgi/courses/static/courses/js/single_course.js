function getCookie(name) {
    var cookieValue = null;
    if(document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for(var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0,name.length+1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length+1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    var host = document.location.host;
    var protocol = document.location.protocol;
    var sr_origin = '//'+host;
    var origin = protocol +sr_origin;

    return (url==origin || url.slice(0, origin.length +1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length+1) == sr_origin + '/') ||
        !(/^(\/\/|http:|https:).*/.test(url));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function prepare_looks() {
    $(".course-limit").hide();
    $(".course-desc").hide();
    $(".course-taken").hide();
    $(".course-sign-up").hide();
    $(".course-sign-off").hide();
    $(".course-id").hide();
    $(".course-url").hide();
    $(".course-msg").hide();
    $(".course").each(set_bar);
}

function register_handlers() {
    $(".course").mouseover(function() {
        $(this).find(".course-name").removeClass("text-primary");
        $(this).addClass("active");
    });

    $(".course").mouseout(function() {
        $(this).find(".course-name").addClass("text-primary");
        $(this).removeClass("active");
    });

    $(".course").click(function() {
        $(this).find(".course-desc").toggle();
        $(this).find(".course-sign-up").toggle();
        $(this).find(".course-sign-off").toggle();
        $(this).find(".course-msg").toggle();
    });

    $(".course-sign-up").click(function(event) {
        event.stopPropagation();
        var url, id, data;
        url = $(this).siblings(".course-url").text();
        id  = $(this).siblings(".course-id").text();
        data = {sign_up:'1', course_id: id};

        $.post( url, data );
        delayed_reload(1000);
    });

    $(".course-sign-off").click(function(event) {
        event.stopPropagation();
        var url, id, data;
        url = $(this).siblings(".course-url").text();
        id  = $(this).siblings(".course-id").text();
        data = {sign_up:'0', course_id: id};

        $.post( url, data );
        delayed_reload(1000);
    });
}

function delayed_reload(delay) {
    setTimeout(function() {
        location.reload();
    }, delay);
}

function set_bar() {
    var taken, limit,percentage;

    taken = parseInt($(this).find(".course-taken").text());
    limit = parseInt($(this).find(".course-limit").text());
   
    if(taken>limit) {
        percentage = 100;
    } else {
        percentage = (taken/limit)*100;  
    }

    $(this).find(".progress-bar").width(percentage+"%");
}

$(document).ready(function() {
    prepare_looks();
    register_handlers();
});
