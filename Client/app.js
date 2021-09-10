axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

var app = new Vue({
    el: "#app",
    data: {
      allBoletes: [],
    //   currentRoute: window.location.pathname
    },
    mounted: function () {
      axios.get("http://127.0.0.1:8000/api").then(function (response) {
        app.allBoletes = response.data;
      });
    },
  });