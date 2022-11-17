const voteBpm = (id) => {
    $.post("/vote/anggota-bpm/post/", {
        idBpm: id
    },
    () => {
        window.location.href = "/vote/anggota-bem/";
    });
}

const voteBem = (id) => {
    $.post("/vote/anggota-bem/post/", {
        idBem: id
    },
    () => {
        window.location.href = "/vote/anggota-bem/";
    });
}

const showConfirmModalBpm = (id) => {
    $("#confirm-modal").removeClass("hidden");
    $("#ya-btn").attr("onClick", `voteBpm(${id})`);
}

const showConfirmModalBem = (id) => {
    $("#confirm-modal").removeClass("hidden");
    $("#ya-btn").attr("onClick", `voteBem(${id})`);
}

const hideConfirmModal = () => {
    $("#confirm-modal").addClass("hidden");
    $("ya-btn").removeAttr("onClick");
}