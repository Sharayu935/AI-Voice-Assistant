$(document).ready(function () {

  // Animate text
  $('.text').textillate({
    loop: true,
    sync: true,
    in: { effect: "bounceIn" },
    out: { effect: "bounceOut" }
  });

  // Siri Wave configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style: "ios9",
    autostart: true
  });

  // Siri message animation
  $('.siri-message').textillate({
    loop: true,
    sync: true,
    in: { effect: "fadeInUp", sync: true },
    out: { effect: "fadeOutUp", sync: true }
  });

  // Mic button click
  $("#Micbtn").click(function () {
    $("#oval").css("display", "none");
    $("#SiriWave").css("display", "block");
    eel.allCommands();
  });

  // Send button click
  $("#sendBtn").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  // Detect typing in chatbox
  $("#chatbox").on("input", function () {
    let message = $(this).val();
    ShowHiddenButton(message);
  });

  // --- Functions ---
  function PlayAssistant(message) {
    if (message.trim() !== "") {
      $("#oval").hide();
      $("#SiriWave").show();
      eel.allCommands(message);
      $("#chatbox").val("");
      $("#Micbtn").show();
      $("#sendBtn").hide();
    }
  }

  function ShowHiddenButton(message) {
    if (message.trim().length === 0) {
      $("#Micbtn").show();
      $("#sendBtn").hide();
    } 
    else {
      $("#Micbtn").hide();

      // Force show send button even if Bootstrap hides it
      $("#sendBtn").prop("hidden", false).css("display", "inline-block");
    }
  }

});
