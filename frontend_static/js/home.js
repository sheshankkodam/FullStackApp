/**
 * Created by saksham.ghimire on 8/10/16.
 */
var name_url = "/api/v1/name";

$('#submit').click(function (e) {
    console.log("im here")
    $.ajax({
        url: name_url,
        type: 'GET',
        contentType: 'application/json',
        success: function (result) {
            document.getElementById('app_name').value = result.name;
        },
        error: function (result) {
            console.log("error occurred", result)
        }
    })
});
