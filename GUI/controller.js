$(document).ready(function () {
    
      // Expose DisplayMessage to Python
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        console.log("Message from Python:", message);
        $(".siri-message").text(message);
    }

    // Expose ShowHood to Python (to show hood again)
    eel.expose(ShowHood);
    function ShowHood() {
        console.log("Returning to hood screen...");
        $("#SiriWave").css("display", "none");   // hide SiriWave
        $("#oval").css("display", "block");      // show main hood
    }

    // Mic button click → start listening
    $("#Micbtn").click(function () {
        console.log("Mic clicked → switching to SiriWave");
        $("#oval").css("display", "none");
        $("#SiriWave").css("display", "block");

        eel.takecommand();                          // call Python
    });

});
