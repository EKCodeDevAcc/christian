$(document).ready(function () {
    // when the user click search button in the index.html page
    $('#submit').click(function () {

        // get input value as product id
        var product_id = $('#search').val();

        // validate a input is given
        if (product_id == "") {
            alert("Please enter the valid value.");

        } else {
            // redirect the user to /product/<product_id> url
            detail_view = "product/" + product_id;
            $(location).attr('href', detail_view);
        }
    });

    // TODO: press enter to trigger clicking search button event
    // var search_input = document.getElementById("search");
    //
    // search_input.addEventListener("keyup", function(event) {
    //     if (event.keyCode == 13) {
    //         event.preventDefault();
    //         document.getElementById("#submit").click();
    //     }
    // });
});
