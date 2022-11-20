$(document).ready(() => {
    var count = 3;
    $("#redirect-count").html(count);
    setInterval(() => {
        if(count > 0){
            $("#redirect-count").html(--count);
        }
        
        if(count == 0){
            $.post("/logout/", {}, (data, status) => {
                window.location.href = "/";
            });
        }
    }, 1000);
});