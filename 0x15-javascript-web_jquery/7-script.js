// Wait for the DOM to be fully loaded
$(document).ready(function() {
    // Make a GET request to fetch character data
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
        // Update the text of the #character div with the character name
        $("#character").text(data.name);
    });
});

