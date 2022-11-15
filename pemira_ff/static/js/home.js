const showModal = (name) => {
    $("#login-nama").html(name);
    $("#modal").removeClass("hidden");
}

const hideModal = () => {
    $("#modal").addClass("hidden");
}

const login = () => {
    $.post("/login/", {
        token: $("#token-input").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    }, (data, status) => {
        showModal(data.nama);
    });
}

const logout = () => {
    $.post("/logout/", {}, (data, status) => {
        window.location.href = "/";
    });
}

$(document).ready(() => {
    $("#login-btn").click(() => {
        login();
    });

    $("#logout-btn").click(() => {
        logout();
    });
});