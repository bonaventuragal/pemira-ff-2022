$(document).ready(() => {
    $("#logout-btn").click(() => {
        $.post("/panitia/logout/", {}, (data, status) => {
            window.location.href = "/panitia/";
        });
    });
});