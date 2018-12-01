$(document).ready(function() {
  $("body").click(function(event) {
    if (
      $(".navbar-collapse").is(":visible") &&
      $(".navbar-toggle").is(":visible")
    ) {
      $(".navbar-collapse").collapse("toggle");
    }
  });
});

$(".nav a").on("click", function() {
  $(".navbar-toggle").click();
});

$(".after").click(function() {
  $(".after").unbind(".image-container");
});

$('a[href^="#"]').on("click", function(event) {
  var target = $(this.getAttribute("href"));
  if (target.length) {
    event.preventDefault();
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: target.offset().top
        },
        2000
      );
  }
});
$(function() {
  $(".col-sm-6").matchHeight();
});
