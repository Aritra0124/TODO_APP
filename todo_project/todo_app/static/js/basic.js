$(document).ready(function() {
    $("#register_text").click(function(){
        $("#register").toggle();
        $("#login").toggle();
        $(".card-title").html("Register");
    });
    $("#login_text").click(function(){
        $("#register").toggle();
        $("#login").toggle();
        $(".card-title").html("Login");
    });
    if($(".alert").html() != ''){
        setTimeout(function() {
            $(".alert").hide()
        }, 5000);
    }
});