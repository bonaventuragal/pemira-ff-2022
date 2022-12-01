const voteBpm = (id) => {
    $("#ya-btn").prop("disabled", true);
    $.post("/vote/anggota-bpm/post/", {
        idBpm: id
    },
    () => {
        window.location.href = "/vote/ketua-bem/";
    });
}

const voteBem = (id) => {
    $("#ya-btn").prop("disabled", true);
    $.post("/vote/ketua-bem/post/", {
        idBem: id
    },
    () => {
        window.location.href = "/done/";
    });
}

const showConfirmModalBpm = (id) => {
    $("#ya-btn").prop("disabled", false);
    $("#confirm-modal").removeClass("hidden");
    $("#ya-btn").attr("onClick", `voteBpm(${id})`);
}

const showConfirmModalBem = (id) => {
    $("#ya-btn").prop("disabled", false);
    $("#confirm-modal").removeClass("hidden");
    $("#ya-btn").attr("onClick", `voteBem(${id})`);
}

const hideConfirmModal = () => {
    $("#confirm-modal").addClass("hidden");
    $("#ya-btn").removeAttr("onClick");
}