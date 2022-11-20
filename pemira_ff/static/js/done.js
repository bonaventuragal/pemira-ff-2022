$(document).ready(() => {
    var count = 3;
    $("#redirect-count").html(count);
    setInterval(() => {
        $("#redirect-count").html(--count);
        if(count <= 0) window.location.href = "/";
    }, 1000);
});