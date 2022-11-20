const showSuccessModal = (name) => {
    $("#login-nama").html(name);
    $("#success-modal").removeClass("hidden");
}

const hideSuccessModal = () => {
    $("#success-modal").addClass("hidden");
}

const showFailModal = () => {
    $("#fail-modal").removeClass("hidden");
}

const hideFailModal = () => {
    $("#fail-modal").addClass("hidden");
}

const login = () => {
    $.post("/login/", {
        token: $("#token-input").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    (data, status) => {
        showSuccessModal(data.nama);
    })
    .fail(() => {
        showFailModal();
    }).always(() => {
        $("#token-input").val("");
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

    $("#next-btn").click(() => {
        
    });

    $("#close-fail-modal").click(() => {
        hideFailModal();
    })
});