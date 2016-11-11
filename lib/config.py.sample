#!/usr/bin/env python
"""
config.py 
set paramater of your server
"""
### Menus
keyuri = "key"
tokenuri = "token"

### Database
mongohost = "localhost"
mongoport = 27017

### Security module
key = "your key 16 char"
iv = "your iv 16 char"
tokenurl = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="
iss = "accounts.google.com"
aud = "WEB_CLIENT_ID"
domainacl = "poltekpos.ac.id"
urltimeout = 3600

### HTML
html_begin = """
<html lang="en">
  <head>
    <meta name="google-signin-scope" content="profile email">
    <meta name="google-signin-client_id" content="1092799040278-3dcl923ahbmbr3amtblha5mcblhim5a6.apps.googleusercontent.com">
	<link href='http://www.ngabara.ga/favicon.ico' rel='icon' type='image/x-icon'/>
    <script src="https://apis.google.com/js/platform.js" async defer></script>
  <title>Sign App</title>
<style>
.square {
    background: #f2f2f2;
    width: 35vw;
    height: initial;
    margin-left: 1vw;
}
.square h1 {
    color: #000;
}
input[type="text"] { font-size: 10vw; width: 15vw;}
.button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 1vw 1vw;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 3vw;
}
</style>	
</head>
  <body>
"""

html_form = """
<div class="square" id="square">
Pembahasan : <br>
<textarea rows="10vw" cols="20vw" id="pemb"></textarea>
<br>
Nilai : <br>
<input type="text" id="numb" maxlength="2"><br>
<input type="hidden" id="npm" value="NPMVALUE"><br>
<button class="button" type="button" onclick="myFunction()">Submit</button>
</div>
"""

html_signout = """
<a href="#" onclick="signOut();">Please change to institution email, Sign out here</a>
"""

html_end = """
<br><div id="Message"></div><br>
    <div class="g-signin2" id="button" data-onsuccess="onSignIn"></div>
	<div id="signout"><a href="#" onclick="signOut();">Please change to institution email, Sign out here</a></div>
<script>
	var id_token;
	document.getElementById('square').style.visibility = "hidden";
	document.getElementById('signout').style.visibility = "hidden";	

      function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
        var profile = googleUser.getBasicProfile();
	document.getElementById('square').style.visibility = "visible";
        document.getElementById('signout').style.visibility = "hidden";
        document.getElementById('button').style.visibility = "hidden";
	document.getElementById('Message').innerHTML = "Login Sebagai : " + profile.getEmail();
	console.log("ID: " + profile.getId()); // Don't send this directly to your server!
        console.log('Full Name: ' + profile.getName());
        console.log('Given Name: ' + profile.getGivenName());
        console.log('Family Name: ' + profile.getFamilyName());
        console.log("Image URL: " + profile.getImageUrl());
        console.log("Email: " + profile.getEmail());
	//document.getElementById('Message').innerHTML = profile.getEmail();
        // The ID token you need to pass to your backend:
        id_token = googleUser.getAuthResponse().id_token;
        console.log("ID Token: " + id_token);
	//var xhr = new XMLHttpRequest();
	//xhr.open('POST', './TOKENURIPARAM');
	//xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	//xhr.onload = function() {
  	//	console.log('Signed in as: ' + xhr.responseText);
	//	document.getElementById('Message').innerHTML = "Login Sebagai : " + xhr.responseText;
	//};
	//xhr.send('token=' + id_token);
      };
	function myFunction() {

        var x,y,z,text;

        // Get the value of the input field with id="numb"
        x = document.getElementById("numb").value;
	y = document.getElementById("npm").value;
	z = document.getElementById("pemb").value;

        // If x is Not a Number or less than one or greater than 10
        if (isNaN(x) || x < 1 || x > 10) {
        text = "Nilai tidak valid";
	document.getElementById("Message").innerHTML = text;
        } else {
		console.log("ID Token: " + id_token);
        	var xhr = new XMLHttpRequest();
        	xhr.open('POST', './TOKENURIPARAM');
        	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        	xhr.onload = function() {
                	if(xhr.responseText == "invalid"){
			console.log('Signed in as: ' + xhr.responseText);
			document.getElementById('Message').innerHTML = "Bukan email institusi,klik log out dibawah dan login kembali";
			document.getElementById('square').style.visibility = "hidden";
			document.getElementById('signout').style.visibility = "visible";
			}else if((xhr.responseText == "exist")){
			document.getElementById('Message').innerHTML = "Masih ada hari esok yang cerah untuk bimbingan kembali :) ";
                        document.getElementById('square').style.visibility = "hidden";
			}else if((xhr.responseText == "expire")){
                        document.getElementById('Message').innerHTML = "Session Expire, silahkan scan ulang kembali";
                        document.getElementById('square').style.visibility = "hidden";
			}else{
			console.log('Signed in as: ' + xhr.responseText);
                        document.getElementById('Message').innerHTML = "Sudah Masuk : " + xhr.responseText;
                        document.getElementById('square').style.visibility = "hidden";
			}
		};
		xhr.send('token=' + id_token +'&NPM='+ y +"&Nilai="+ x +"&Topik="+ z );
		console.log("NPM: " + y);
		console.log("Nilai: " + x);
		console.log("Topik: " + z)
		console.log("respon: " + text);
        }
        }

	function signOut() {
                var auth2 = gapi.auth2.getAuthInstance();
                auth2.signOut().then(function () {
                console.log('User signed out.');
		document.getElementById('signout').style.visibility = "hidden";
        	document.getElementById('button').style.visibility = "visible";
                });
        }
    </script>
</body>
</html>
"""

