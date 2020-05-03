#!/usr/bin/python3.6
print("content-type: text/html")
print()	
import cgi
import subprocess
from facereg import *

print("""
<body style='background:linear-gradient(to right, #4ca1af, #c4e0e5);'>
""")
print("<h1 align='center'>Welcome to WebApp-Docker</h1>")

print("""
<h3> Authenticate to proceed</h3>
<video id='player' controls autoplay></video>
<button id='capture'>Capture</button>
<canvas id='canvas' width=320 height=240></canvas>
<span id='result' style='display:none;'>Success</span>
<script> 
  const player = document.getElementById('player');
  const canvas = document.getElementById('canvas');
  const context = canvas.getContext('2d');
  const captureButton = document.getElementById('capture');
  const constraints = {
    video: true,
  };
  captureButton.addEventListener('click', () => {
    context.drawImage(player, 0, 0, canvas.width, canvas.height);
	var base64Data = document.getElementById('canvas').toDataURL('image/png');
	console.log(base64Data);
    // Stop all video streams.
    player.srcObject.getVideoTracks().forEach(track => track.stop());
	player.style.display = 'none';
	capture.style.display = 'none';
	result.style.display = 'block';
	upload.style.display='block';
	document.getElementById('n').value = base64Data;
	
  });
  
 
  navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
      // Attach the video stream to the video element and autoplay.
      player.srcObject = stream;
    });
</script>
""")


print("""<form action='http://192.168.43.18:9876/cgi-bin/redirection.py' method='post'>
<input type ='hidden' name='n' id='n'>
<input type='submit' id='upload' value='upload' style='display:none;'>
</form>
</body>""")
