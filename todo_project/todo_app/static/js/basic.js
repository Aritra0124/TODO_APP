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

function delete_success_callback(){
    $(".loading_modal").show();
    alert("Task Deleted");
    get_tasks($("#project_name").val());
}
function create_task_success_callback(data){
    get_tasks($("#project_name").val());
    $(".modal .close").click();
    alert(data.status);
}

function task_success_callback(data){
    var task_data = data.task;
    $('#task-div').html("");
    $.each(task_data, function(index, cardData) {
    var card = $('<div class="card" id="card_' + index + '" style="width: 18rem;">');
    card.append('<h2>' + cardData.task_name + '</h2>');
    card.append('<span class="delete_card" onclick=delete_task("' + cardData.task_gid + '")>' +
            '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">' +
            '<path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/></svg>' +
            '</span>');
    card.append(`
    <span onclick="edit_task(${cardData.task_gid}, ${index})">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
        </svg>
    </span>
`);
    card.append('<h4 class="task_note">' + cardData.task_note + '</h4>');
    card.append('<p value="'+cardData.task_section_gid+'">' + cardData.task_section_name + '</p>');
    // Add more data to the card as needed
    $('#task-div').append(card);
});
$("#task").show();
//$(".loading_modal").hide();
$(".modal").hide()
}

function project_success_callback(data){
    var project_data = data.project;
    get_tasks(project_data.gid);
    $("#project_name").html(project_data.project_name);
    $("#project_name").val(project_data.gid);
}

function error_callback(data){
    alert(data.status);
}

function get_project(){
    var url = "project/"
    ajaxGet(url, data={}, project_success_callback, error_callback);
}

function get_tasks(gid){
    var url = "task/"
    ajaxGet(url, data={"gid": gid}, task_success_callback, error_callback);
}

function get_sections(){
    var project_gid = $("#project_name").val();
    var url = "get_sections/"
    ajaxGet(url, data={"gid": project_gid}, section_success_callback, error_callback);
}

function create_task(){
    var project_gid = $("#project_name").val();
    var task_name = $("#task_name").val();
    var task_note = $("#task_note").val();
    var section_gid = $("#section_dropdown").val();
    var url = "create_task/"
    ajaxPost(url, data={"project_gid": project_gid, "task_name": task_name, "task_note": task_note,"section_gid": section_gid}, 50000, create_task_success_callback, error_callback)
}

function edit_task(data, index){
    $("#exampleModalLabel").html("Edit Task");
    $("#task").click();
    $("#task_operation").attr("onclick", "edit_selected_task(" + data + ")");
    $("#task_operation").html("Change");
    var card_id = "#card_" + index;
    var task_name = $(card_id + " h2").html();
    var task_note = $(card_id + " .task_note").html();
    var task_gid = data;
    var section_gid = $(card_id + " p").attr("value");
    $("#task_name").val(task_name);
    $("#task_note").val(task_note);
    $('#section_dropdown option').remove();
    function setDropdownValue() {
        if ($('#section_dropdown option').length > 1) {
            $("#section_dropdown").val(section_gid);
        } else {
            setTimeout(setDropdownValue, 500);
        }
    }
    setDropdownValue();
}

function edit_selected_task(task_gid){
    var task_name = $("#task_name").val();
    var task_note = $("#task_note").val();
    var section_gid = $("#section_dropdown").val();
    var url = "edit_task/"
    ajaxPost(url, data={"task_gid": task_gid, "task_name": task_name, "task_note": task_note, "section_gid": section_gid}, 50000, create_task_success_callback, error_callback)

}

function delete_task(gid){
    var url = "delete_task/"
    $(".loading_modal").show();
    ajaxGet(url, data={"gid": gid}, delete_success_callback, error_callback);
}

function section_success_callback(data){
    let dropdown_options = "";
    var dropdown_element = $("#section_dropdown");
    dropdown_element.empty();
    dropdown_element.append(new Option("Select a Section", 0));
    $.each(data.sections, function (index,value) {
             dropdown_element.append($("<option></option>").attr("value", value["section_gid"]).text(value["section_name"]));
    })
    dropdown_element.show();
}
