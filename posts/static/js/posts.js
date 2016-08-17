$(document).ready(function() {

  $(".votes").each(function() {
    var counter = 0;
    var div = this;

    $("#plus", div).click(function(){
      counter++;
      $("#count", div).text(counter);
    });

    $("#minus", div).click(function(){
      counter--;
      $("#count", div).text(counter);
    });
  });

});
