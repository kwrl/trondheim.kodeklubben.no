function init() {
    $(".course-limit").hide();
    $(".course-taken").hide();

}

$(document).ready(function() {

    $(".course").on('hover', function() {
        $(this).addClass("active");
    });
});
