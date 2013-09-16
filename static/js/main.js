function OnLoad(){
	
}

function show_terms(){
	alert("Terms of Agreement\n\nWishing Light Operating Instructions\n1: After the distribution of fuel to packaging equipment Kong Cross wire in the side of the field again deduction presses The fuel-pressure lock firmly.\n2: A person wishing light take ip a Top;	Another person fuel ignited the four angle.\n3: Wait for that the heat enough light, lantems person lets loose A top hand, changes grips under the light to encircle. Has when the lifting force may let go releases for flying.\n4: Wishing light rose slowly the sky, do not forget Wishing oh---------\n\nNotice item:\n1: Should choose at the option open, calm environment released for flight. No fire ban in areas, the tall building the floor, and so on have covers under the thing to release for flight, must leave outside the airport 10 kilometers from flying.\n2: Wishing light can only be used for the distribution the special-purpose fuel,prohibited by any burning Replace.\n3: Wishing light are on the rise, that of the flying, cannot the long time not put, and the Flight not to be append the foreign body.\n4: Children must be under the custody of the adults use.\nWishing Light light\n\nDeclaration: Wishing light for the fire flying,because of environmental ingredient suchas improper use of security incidents caused by the release of the commitment. Production enterprisies, vendors,transport operators,without any responsibility. You use both, then you understand and accept on behalf of the declaration.*\n\nThumbs up to you if you actually read this. We hope you enjoyed yourself!\n\n*This text was taken from the instructions for a Chinese wishing light.");
}

function ShowTermsPopUp(){
	var myWindow = window.open('','','width=800,height=600')
	var terms = "<div class=\"container\">\n	<h1>Terms of Agreement</h1><h3>Wishing Light Operating Instructions</h3><p>1: After the distribution of fuel to packaging equipment Kong Cross wire in the side of the field again deduction presses The fuel-pressure lock firmly.</p><p>2: A person wishing light take ip a Top;\n	Another person fuel ignited the four angle.</p><p>3: Wait for that the heat enough light, lantems person lets loose A top hand, changes grips under the light to encircle. Has when the lifting force may let go releases for flying.</p><p>4: Wishing light rose slowly the sky, do not forget Wishing oh---------</p><h3>Notice item:</h3><p>1: Should choose at the option open, calm environment released for flight. No fire ban in areas, the tall building the floor, and so on have covers under the thing to release for flight, must leave outside the airport 10 kilometers from flying.</p><p>2: Wishing light can only be used for the distribution the special-purpose fuel,prohibited by any burning Replace.</p><p>3: Wishing light are on the rise, that of the flying, cannot the long time not put, and the Flight not to be append the foreign body.</p><p>4: Children must be under the custody of the adults use.</p><h3>Wishing Light light</h3><p>Declaration: Wishing light for the fire flying,because of environmental ingredient suchas improper use of security incidents caused by the release of the commitment. Production enterprisies, vendors,transport operators,without any responsibility. You use both, then you understand and accept on behalf of the declaration.*</p><p>Thumbs up to you if you actually read this. We hope you enjoyed yourself!</p><sub id=\"disclaimer\">*This text was taken from the instructions for a Chinese wishing light.</sub></div>"
	myWindow.document.write(terms)
	myWindow.focus()
}

function PopUp(){
	var ScreenWidth=window.screen.width;
	var ScreenHeight=window.screen.height;
	var movefromedge=0;
	placementx=(ScreenWidth/2)-((400)/2);
	placementy=(ScreenHeight/2)-((300+50)/2);
	WinPop=window.open("About:Blank","","width=400,height=300,toolbar=0,location=0,directories=0,status=0,scrollbars=0,menubar=0,resizable=0,left="+placementx	+",top="+placementy+",scre enX="+placementx+",screenY="+placementy+",");
	varSayWhat = "<p><font color='blue'>This is what the windows text is</font></p><p>Hello World!</p>"; 
	WinPop.document.write('<html>\n<head>\n</head>\n<body>'+SayWhat+'</body></html>');
}

var toolbox = document.getElementById("toolbox");

function ShowToolbox(){
}

function Calendar(){
   alert("Calendar!");
}




