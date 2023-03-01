// ============================ [ AJAX POST ] ============================
function AjaxPost(url, datajson, success_fun=()=>{}, error_fun=()=>{}) {
    Open_Modal_Window(true, GetJson['loading']); 
    $.ajax({
        type: 'POST',
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: 'JSON',
        headers:{ "X-CSRFToken": csrftoken },
        data: JSON.stringify(datajson),
        cache: false,
        processData: false,
        success: (result) => {
            console.log(result);
            success_fun(result);
            if (result['typemessage'] == 'message') {
                $.Toast(result['text'], result['type']);
            }
            Open_Modal_Window(false, '#Loading');
        },
        error: (result) => {
            console.log(result);
            error_fun(result);
            if (result.responseJSON['typemessage'] == 'message') {
                $.Toast(result.responseJSON['text'], result.responseJSON['type']);
            }
            Open_Modal_Window(false, '#Loading');
        },
    });
}
// =======================================================================

// ============================= [ AJAX GET ] ============================
function AjaxGet(url, datajson, success_fun=()=>{}, error_fun=()=>{}) {
    Open_Modal_Window(true, GetJson['loading']); 
    $.ajax({
        type: 'GET',
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: 'JSON',
        headers:{ "X-CSRFToken": csrftoken },
        data: JSON.stringify(datajson),
        cache: false,
        processData: false,
        success: (result) => {
            console.log(result);
            success_fun(result);
            if (result['typemessage'] == 'message') {
                $.Toast(result['text'], result['type']);
            }
            Open_Modal_Window(false, '#Loading');
        },
        error: (result) => {
            console.log(result);
            error_fun(result);
            if (result.responseJSON['typemessage'] == 'message') {
                $.Toast(result.responseJSON['text'], result.responseJSON['type']);
            }
            Open_Modal_Window(false, '#Loading');
        },
    });
}
// =======================================================================