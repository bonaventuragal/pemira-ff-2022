const showFailModal = () => {
  $("#fail-modal").removeClass("hidden");
}

const hideFailModal = () => {
  $("#fail-modal").addClass("hidden");
}

const loginNPM = () => {
  const npm = $("#npm-input").val()
  $.post("/login/npm/", {
      npm,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
  },
  (data, status) => {
      window.location.href = `/login/${npm}/`;
  })
  .fail(() => {
      showFailModal();
  }).always(() => {
      $("#npm-input").val("");
  });
}

const logout = () => {
  $.post("/logout/", {}, (data, status) => {
      window.location.href = "/";
  });
}

$(document).ready(() => {
  $("#login-btn").click(() => {
      loginNPM();
  });

  $("#close-fail-modal").click(() => {
      hideFailModal();
  })
});