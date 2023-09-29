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
    call_asana();
});

function success_callback(data){
    console.log(data);
    alert("GID: "+ data);
}

function error_callback(data){
    console.log(data);
    alert(data);
}

function call_asana(){
    var url = "project/"
    ajaxGet(url, data={}, success_callback, error_callback);
}