https<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 TRANSITIONAL//EN">
   <meta https-equiv="Content-Type" content="text/html; charset=iso-8859-1">
   <meta https-equiv="PICS-Label" content="(PICS-1.1 "https://www.classify.org/safesurf/" L gen true for "https://surflocalmedia.com/" r (SS~~000 1))">
   <meta name="Author" content="  www.surflocalmedia.com  intake@surflocalmedia.com">
   <meta name="GENERATOR" content="Edit Pad">
   <META NAME="GOOGLEBOT" CONTENT="index, follow">
   <meta name="Robots" content="index,follow">
   <meta name="revisit after" content="every 3 days">
   <meta name="distribution" content="global">
   <meta name="alexaVerifyID" content="24UKub4tiTWkQV9iQ65d4IJinxo" />
   <meta http-equiv="REFRESH" content="1;url=https://www.surflocalmedia.com/">
   
<meta name="msvalidate.01" content="5DD343A760FE4F379D5290E32DAF7B23" />
<meta name="verify-v1" content="YgF16AbA6Aa0JkeEPCTs5c4ky9s2osaJi61RrYfLE/Q=" />
<meta https-equiv="imagetoolbar" content="no">
	<meta https-equiv="Content-Script-Type" content="text/javascript">
	<!-- wz_jsgraphics.js is not a part of this distribution. Source:
	https://www.walterzorn.com/jsgraphics/jsgraphics_e.htm#download -->
	<script type="text/javascript" src="/cvi_tip_lib.js"></script>
	<script type="text/javascript" src="/wz_jsgraphics.js"></script>
	<script type="text/javascript" src="/maputil.js"></script>
	<script type="text/javascript" src="/mapper.js"></script>
	<script type="text/javascript">	
	<!--
	function showCoords(map,area,x,y,w,h) {
		function parseDMS(v,n){var d,m,s; d=parseInt(v); m=Math.abs(parseFloat(v-d)*60); s=Math.abs(parseFloat(parseInt(m)-m)*60); return Math.abs(d)+"° "+parseInt(m)+"' "+parseInt(s)+"'' "+n;}	
		if(map=="map_of_world") {
			var obj, country = "", lon = (x*360/w)-180, lat = 90-(y*180/h);
			lon = parseDMS(lon,lon!=0?(lon<0?"W":"E"):""); lat = parseDMS(lat,lat!=0?(lat<0?"S":"N"):"");
			if(area!=0) {obj = document.getElementById(area); country = "  ("+(obj.title||obj.alt)+")";} 
			document.getElementById("map_of_world_blind").innerHTML = "<p class='coords'>Latitude: "+lat+"  Longitude: "+lon+country+"<\/p>";
		}
	}
	-->
	</script>
	
	<link rel="stylesheet" type="text/css" href="tooltip.css" />
<!--[if lt IE 7]>
<style type="text/css">
#cvi_tooltip {
	width:expression(this.offsetWidth>240?'240px':'auto');
}
</style>
<![endif]-->
   <title>Surflocal USA- Map Navigation We also provide the following services, Local Search Placement, Local Website Marketing, Local Business Networking, Local Shopping Network, Local Coupon Download, Local Shopping Coupons, Local Business Directories,  Online Shopping Coupons, Compare local Hotels, Discount Coupons, Local Coupon Directories, Local Coupon Marketing Instant Access to Local Merchants Local Website and Discount Coupon Creator  </title>
<link REL="SHORTCUT ICON" HREF="https://www.surflocalmedia.com/tp.ico">

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>

<link href="/style.css" rel="stylesheet" type="text/css" />

<script language="javascript">



/*

Auto center window script- Eric King (https://redrival.com/eak/index.shtml)

Permission granted to Dynamic Drive to feature script in archive

For full source, usage terms, and 100's more DHTML scripts, visit https://dynamicdrive.com

*/



var win = null;

function NewWindow(mypage,myname,w,h,scroll){

LeftPosition = (screen.width) ? (screen.width-w)/2 : 0;

TopPosition = (screen.height) ? (screen.height-h)/2 : 0;

settings =

'height='+h+',width='+w+',top='+TopPosition+',left='+LeftPosition+',scrollbars='+scroll+',resizable'

win = window.open(mypage,myname,settings)

}



</script>



<script type="text/javascript">

      

/***********************************************

* Ultimate Fade-In Slideshow (v1.51): � Dynamic Drive (https://www.dynamicdrive.com)

* This notice MUST stay intact for legal use

* Visit https://www.dynamicdrive.com/ for this script and 100s more.

***********************************************/

 

var fadeimages=new Array()

//SET IMAGE PATHS. Extend or contract array as needed

fadeimages[0]=["https://www.surflocalmedia.com/images/front/1.jpg", "", ""] //plain image syntax

fadeimages[1]=["https://www.surflocalmedia.com/images/front/2.jpg", "", ""] //plain image syntax

fadeimages[2]=["https://www.surflocalmedia.com/images/front/3.jpg", "", ""] //plain image syntax

fadeimages[3]=["https://www.surflocalmedia.com/images/front/4.jpg", "", ""] //plain image syntax

fadeimages[4]=["https://www.surflocalmedia.com/images/front/5.jpg", "", ""] //plain image syntax

fadeimages[5]=["https://www.surflocalmedia.com/images/front/6.jpg", "", ""] //plain image syntax

fadeimages[6]=["https://www.surflocalmedia.com/images/front/7.jpg", "", ""] //plain image syntax

fadeimages[7]=["https://www.surflocalmedia.com/images/front/8.jpg", "", ""] //plain image syntax



var fadebgcolor="black"



////NO need to edit beyond here/////////////

 

var fadearray=new Array() //array to cache fadeshow instances

var fadeclear=new Array() //array to cache corresponding clearinterval pointers

 

var dom=(document.getElementById) //modern dom browsers

var iebrowser=document.all

 

function fadeshow(theimages, fadewidth, fadeheight, borderwidth, delay, pause, displayorder){

this.pausecheck=pause

this.mouseovercheck=0

this.delay=delay

this.degree=10 //initial opacity degree (10%)

this.curimageindex=0

this.nextimageindex=1

fadearray[fadearray.length]=this

this.slideshowid=fadearray.length-1

this.canvasbase="canvas"+this.slideshowid

this.curcanvas=this.canvasbase+"_0"

if (typeof displayorder!="undefined")

theimages.sort(function() {return 0.5 - Math.random();}) //thanks to Mike (aka Mwinter) :)

this.theimages=theimages

this.imageborder=parseInt(borderwidth)

this.postimages=new Array() //preload images

for (p=0;p<theimages.length;p++){

this.postimages[p]=new Image()

this.postimages[p].src=theimages[p][0]

}

 

var fadewidth=fadewidth+this.imageborder*2

var fadeheight=fadeheight+this.imageborder*2

 

if (iebrowser&&dom||dom) //if IE5+ or modern browsers (ie: Firefox)

document.write('<div id="master'+this.slideshowid+'" style="position:relative;width:'+fadewidth+'px;height:'+fadeheight+'px;overflow:hidden;"><div id="'+this.canvasbase+'_0" style="position:absolute;width:'+fadewidth+'px;height:'+fadeheight+'px;top:0;left:0;filter:progid:DXImageTransform.Microsoft.alpha(opacity=10);opacity:0.1;-moz-opacity:0.1;-khtml-opacity:0.1;background-color:'+fadebgcolor+'"></div><div id="'+this.canvasbase+'_1" style="position:absolute;width:'+fadewidth+'px;height:'+fadeheight+'px;top:0;left:0;filter:progid:DXImageTransform.Microsoft.alpha(opacity=10);opacity:0.1;-moz-opacity:0.1;-khtml-opacity:0.1;background-color:'+fadebgcolor+'"></div></div>')

else

document.write('<div><img name="defaultslide'+this.slideshowid+'" src="'+this.postimages[0].src+'"></div>')

 

if (iebrowser&&dom||dom) //if IE5+ or modern browsers such as Firefox

this.startit()

else{

this.curimageindex++

setInterval("fadearray["+this.slideshowid+"].rotateimage()", this.delay)

}

}



function fadepic(obj){

if (obj.degree<100){

obj.degree+=10

if (obj.tempobj.filters&&obj.tempobj.filters[0]){

if (typeof obj.tempobj.filters[0].opacity=="number") //if IE6+

obj.tempobj.filters[0].opacity=obj.degree

else //else if IE5.5-

obj.tempobj.style.filter="alpha(opacity="+obj.degree+")"

}

else if (obj.tempobj.style.MozOpacity)

obj.tempobj.style.MozOpacity=obj.degree/101

else if (obj.tempobj.style.KhtmlOpacity)

obj.tempobj.style.KhtmlOpacity=obj.degree/100

else if (obj.tempobj.style.opacity&&!obj.tempobj.filters)

obj.tempobj.style.opacity=obj.degree/101

}

else{

clearInterval(fadeclear[obj.slideshowid])

obj.nextcanvas=(obj.curcanvas==obj.canvasbase+"_0")? obj.canvasbase+"_0" : obj.canvasbase+"_1"

obj.tempobj=iebrowser? iebrowser[obj.nextcanvas] : document.getElementById(obj.nextcanvas)

obj.populateslide(obj.tempobj, obj.nextimageindex)

obj.nextimageindex=(obj.nextimageindex<obj.postimages.length-1)? obj.nextimageindex+1 : 0

setTimeout("fadearray["+obj.slideshowid+"].rotateimage()", obj.delay)

}

}

 

fadeshow.prototype.populateslide=function(picobj, picindex){

var slideHTML=""

if (this.theimages[picindex][1]!="") //if associated link exists for image

slideHTML='<a href="'+this.theimages[picindex][1]+'" target="'+this.theimages[picindex][2]+'">'

slideHTML+='<img src="'+this.postimages[picindex].src+'" border="'+this.imageborder+'px">'

if (this.theimages[picindex][1]!="") //if associated link exists for image

slideHTML+='</a>'

picobj.innerHTML=slideHTML

}

 

 

fadeshow.prototype.rotateimage=function(){

if (this.pausecheck==1) //if pause onMouseover enabled, cache object

var cacheobj=this

if (this.mouseovercheck==1)

setTimeout(function(){cacheobj.rotateimage()}, 100)

else if (iebrowser&&dom||dom){

this.resetit()

var crossobj=this.tempobj=iebrowser? iebrowser[this.curcanvas] : document.getElementById(this.curcanvas)

crossobj.style.zIndex++

fadeclear[this.slideshowid]=setInterval("fadepic(fadearray["+this.slideshowid+"])",50)

this.curcanvas=(this.curcanvas==this.canvasbase+"_0")? this.canvasbase+"_1" : this.canvasbase+"_0"

}

else{

var ns4imgobj=document.images['defaultslide'+this.slideshowid]

ns4imgobj.src=this.postimages[this.curimageindex].src

}

this.curimageindex=(this.curimageindex<this.postimages.length-1)? this.curimageindex+1 : 0

}

 

fadeshow.prototype.resetit=function(){

this.degree=10

var crossobj=iebrowser? iebrowser[this.curcanvas] : document.getElementById(this.curcanvas)

if (crossobj.filters&&crossobj.filters[0]){

if (typeof crossobj.filters[0].opacity=="number") //if IE6+

crossobj.filters(0).opacity=this.degree

else //else if IE5.5-

crossobj.style.filter="alpha(opacity="+this.degree+")"

}

else if (crossobj.style.MozOpacity)

crossobj.style.MozOpacity=this.degree/101

else if (crossobj.style.KhtmlOpacity)

crossobj.style.KhtmlOpacity=this.degree/100

else if (crossobj.style.opacity&&!crossobj.filters)

crossobj.style.opacity=this.degree/101

}

 

 

fadeshow.prototype.startit=function(){

var crossobj=iebrowser? iebrowser[this.curcanvas] : document.getElementById(this.curcanvas)

this.populateslide(crossobj, this.curimageindex)

if (this.pausecheck==1){ //IF SLIDESHOW SHOULD PAUSE ONMOUSEOVER

var cacheobj=this

var crossobjcontainer=iebrowser? iebrowser["master"+this.slideshowid] : document.getElementById("master"+this.slideshowid)

crossobjcontainer.onmouseover=function(){cacheobj.mouseovercheck=1}

crossobjcontainer.onmouseout=function(){cacheobj.mouseovercheck=0}

}

this.rotateimage()

}



</script>

</head> 



<center><table BORDER=2 COLS=1 WIDTH="980" style="border-collapse: collapse" bordercolor=9F8D5B>

<tr>

<TD>

<center><table BORDER=0 COLS=2 WIDTH="975" HEIGHT="239" style="background:url('/images/front/top-banner.jpg') no-repeat;">

<tr>

<td WIDTH="765" VALIGN="TOP" >

<FONT COLOR=FFFFFF><B>&nbsp;&nbsp;<font size=-1>Surflocal USA Advertising Network &nbsp;&nbsp;

<br><br><br>&nbsp;&nbsp;







<a href="/index.html"><img src="/clear.gif" border=0></A>

<br><font size=-1><b><FONT COLOR=FFFFFF>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Surflocal U.S.A. Network

<br>&nbsp;Local Regional & National Marketing</FONT></b></td>

<center>

<td width=200><div valign=bottom align="center">



<br><br>

<center>

<script type="text/javascript">

//new fadeshow(IMAGES_ARRAY_NAME, slideshow_width, slideshow_height, borderwidth, delay, pause (0=no, 1=yes), optionalRandomOrder)

new fadeshow(fadeimages, 200, 194, 0, 3000, 1, "R")

 

</script></CENTER>

 </center>



</div></td>



</tr>



</table>







<table BORDER=0 COLS=1 WIDTH="975" HEIGHT=23 BGCOLOR="#382D2C" style="background:url('/images/front/botton-nav2.gif')"  style="border-collapse: collapse">

<tr>

<TD> <center>

<CENTER>

 <center><FONT SIZE=-1><B>



</center>

</TD>



</tr>

</table></center>



<center><table BORDER=0 COLS=2 WIDTH="975">

<tr>

<td valign="top" width=177 BACKGROUND="/images/front/leftbg.gif">



<div align=right>

<p><br>



<p>


<br><br>






</div>

</td>



<td BACKGROUND="/images/front/bg.gif" VALIGN=TOP>

<!-- InstanceBeginEditable name="Content-Area" -->
    <div class="contenthold">
      <div class="wrapper">
       <center> <h1>Thank-You!</h1></center>
        <p>
          <?PHP 
$to = "intake@surflocalmedia.com"; 
$from = "intake@surflocalmedia.com";
$subject = "Results from your Referral Info Form";
$headers = "From: Surflocal Business Referral Form";
$forward = 0;
$location = "surflocalmedia.com";

$date = date ("l, F jS, Y"); 
$time = date ("h:i A"); 



$msg = "Below is a message sent from the surflocalmedia.com referral website form.
It was submitted on $date at $time.\n\n"; 

if ($_SERVER['REQUEST_METHOD'] == "POST") {
	foreach ($_POST as $key => $value) { 
		$msg .= ucfirst ($key) ." : ". $value . "\n"; 
	}
}
else {
	foreach ($_GET as $key => $value) { 
		$msg .= ucfirst ($key) ." : ". $value . "\n"; 
	}
}

mail($to, $subject, $msg, $headers); 
if ($forward == 1) { 
    header ("Location:$location"); 
} 
else { 
    echo "<b><center>Thank You ...We will be in contact as soon as possible!</center>

"; 
} 

?>
        </p>
        <br />
      </div>
    </div>
    <!-- InstanceEndEditable -->

<center> <font size=+1><b>STATE NAVIGATIONAL MAP</font></b>
<p><br><br>
<img class="mapper" src="/images/usa.gif" usemap="#map_of_usa" width="432" height="275" border="0" alt="" />
</div></div>
<map name="map_of_usa">
	<!-- color #10 -->
	<area shape="poly" id="CT" title="Connecticut" alt="Connecticut" href="https://www.surflocalmedia.com/ConnecticutUS/" coords="408,78, 407,78, 407,78, 407,78, 407,77, 408,77, 408,77, 408,77, 408,77, 408,76, 407,72, 407,72, 400,74, 400,74, 400,74, 399,74, 399,75, 399,75, 399,75, 399,75, 398,75, 394,76, 393,76, 395,83, 395,83, 394,84, 394,85, 395,85, 395,85, 395,85, 395,85, 395,85, 395,85, 396,85, 396,84, 396,84,397,84, 397,84, 397,84, 397,83, 398,83, 398,83, 398,83, 398,83, 399,83, 399,82, 400,82, 401,82, 401,81, 401,81, 402,81, 402,81, 403,81, 403,81, 403,81, 404,80, 404,80, 405,80, 405,79, 405,80, 406,79, 406,79, 406,79, 406,79, 407,79, 407,79, 407,79, 407,79, 408,79, 408,78, 408,78, 408,78" />
	<area shape="poly" id="RI" title="Rhode Island" alt="Rhode Island" href="https://www.surflocalmedia.com/Rhode-IslandUS/" coords="413,73, 413,73, 413,72, 412,72, 411,71, 409,72, 407,73, 407,74, 408,76, 408,77, 408,77, 408,77, 408,77, 408,77, 407,77, 407,78, 407,78, 408,78, 408,78, 408,78, 408,78, 408,79, 408,79, 408,78, 409,78, 409,78, 410,78, 411,77, 413,76, 413,76, 413,76, 413,75, 413,75, 413,75, 413,75, 414,75,414,74, 415,74, 414,74, 414,74, 413,73, 413,73, 413,73" />
	<area shape="poly" id="MA" title="Massachussets" alt="Massachussets" href="https://www.surflocalmedia.com/MassachusettsUS/" coords="410,63, 409,63, 409,63, 409,64, 409,64, 409,64, 408,64, 408,64, 408,64, 408,64, 408,64, 408,64, 408,65, 408,65, 407,65, 407,65, 407,65, 407,66, 406,66, 406,66, 406,66, 406,66, 399,68, 399,68, 393,70, 392,70, 393,74, 393,76, 394,76, 398,75, 399,75, 399,75, 399,75, 399,75, 399,74, 400,74,400,74, 400,74, 400,74, 407,72, 407,72, 407,73, 411,71, 412,72, 413,72, 413,73, 413,73, 413,73, 413,73, 414,74, 414,74, 414,74, 414,74, 415,73, 415,73, 415,73, 416,73, 416,72, 416,73, 417,73, 417,73, 417,74, 417,74, 417,75, 417,74, 418,74, 419,73, 420,72, 420,72, 421,71, 421,71, 421,72, 421,72, 421,72, 422,72, 421,70, 421,69,421,67, 420,67, 420,66, 419,66, 419,66, 418,66, 418,66, 418,66, 419,66, 419,66, 419,66, 419,66, 420,67, 420,67, 420,68, 420,68, 420,68, 420,68, 420,69, 420,69, 420,69, 420,70, 419,70, 418,70, 418,70, 418,71, 417,70, 418,70, 418,70, 417,70, 416,70, 416,69, 415,68, 415,68, 414,67, 414,67, 414,66, 413,66, 413,66, 413,66, 412,66,412,66, 412,66, 412,66, 412,65, 412,65, 412,65, 412,65, 412,65, 412,64, 411,64, 411,64, 411,63, 410,63, 410,63" />
	<area shape="poly" id="VT" title="Vermont" alt="Vermont" href="https://www.surflocalmedia.com/VermontUS/" coords="386,45, 386,45, 386,45, 386,45, 386,45, 385,45, 385,46, 386,46, 386,48, 386,49, 386,49, 386,48, 386,48, 386,48, 387,48, 387,49, 387,49, 387,50, 387,50, 387,50, 387,51, 387,51, 387,51, 387,51, 387,52, 387,52, 387,52, 387,53, 387,53, 387,53, 387,53, 387,53, 387,54, 387,54, 387,54, 387,56,387,57, 387,58, 387,58, 387,59, 387,59, 387,59, 388,60, 388,61, 388,61, 388,61, 388,61, 388,61, 388,62, 388,62, 388,62, 388,62, 388,63, 388,63, 388,63, 389,62, 389,62, 389,63, 390,63, 390,63, 390,63, 390,63, 390,63, 390,63, 392,69, 392,70, 392,70, 393,70, 399,68, 399,68, 399,68, 398,68, 398,67, 398,67, 399,66, 399,66, 399,66,399,66, 399,66, 399,65, 399,65, 399,65, 399,65, 399,65, 399,65, 399,64, 399,64, 398,64, 398,64, 398,64, 398,63, 398,62, 398,62, 398,61, 398,60, 398,59, 398,59, 398,58, 398,58, 398,58, 398,56, 398,55, 398,54, 398,54, 398,54, 398,53, 398,53, 398,53, 397,53, 397,53, 398,53, 398,52, 398,52, 398,51, 399,51, 399,50, 399,50, 399,50,400,49, 400,49, 400,49, 399,49, 399,48, 399,48, 399,48, 398,48, 398,47, 399,47, 399,47, 399,46, 399,46, 399,45, 399,45, 399,45, 399,44, 399,44, 399,44, 399,44, 399,44, 399,44, 399,44, 399,43, 399,43, 399,43, 399,42, 399,42, 398,42, 398,41, 398,41, 398,41, 398,41, 398,41, 392,42, 387,43, 386,44, 386,44, 386,45" />
	<area shape="poly" id="NH" title="New Hampshire" alt="New Hampshire" href="https://www.surflocalmedia.com/New-HampshireUS/" coords="410,61, 410,61, 410,61, 410,61, 409,61, 409,60, 409,60, 409,59, 409,59, 409,59, 408,59, 408,59, 408,58, 408,58, 408,57, 405,48, 402,36, 402,36, 402,36, 402,36, 402,37, 402,38, 402,38, 401,39, 401,39, 400,39, 400,39, 400,39, 399,39, 399,39, 399,39, 398,40, 398,40, 398,40, 398,41, 398,41,398,41, 398,41, 398,42, 399,42, 399,42, 399,43, 399,43, 399,44, 399,44, 399,44, 399,44, 399,44, 399,44, 399,45, 399,45, 399,45, 399,45, 399,46, 399,46, 399,47, 399,47, 398,48, 399,48, 399,48, 399,49, 400,49, 400,49, 400,49, 400,49, 399,50, 399,50, 399,51, 398,52, 398,52, 398,52, 398,53, 397,53, 398,53, 398,53, 398,54, 398,54,398,55, 398,55, 398,56, 398,58, 398,58, 398,59, 398,61, 398,62, 398,63, 398,63, 398,64, 398,64, 399,64, 399,64, 399,65, 399,65, 399,65, 399,65, 399,65, 399,66, 399,66, 399,66, 399,66, 399,66, 399,66, 398,67, 398,67, 399,68, 399,68, 399,68, 406,66, 406,66, 406,66, 407,66, 407,65, 407,65, 407,65, 408,65, 408,65, 408,64, 408,64,408,64, 408,64, 408,64, 408,64, 409,64, 409,64, 409,64, 409,63, 409,63, 409,63, 410,63, 410,63, 411,63, 411,62, 411,62, 411,62, 411,62, 411,61, 410,61" />
	<area shape="poly" id="ME" title="Maine" alt="Maine" href="https://www.surflocalmedia.com/MaineUS/" coords="431,30, 430,30, 430,29, 429,29, 429,30, 428,30, 428,29, 428,28, 427,28, 427,28, 427,27, 427,27, 426,27, 425,27, 424,27, 424,26, 423,26, 422,25, 419,11, 418,10, 417,10, 416,9, 415,9, 414,9, 414,10, 413,10, 412,10, 411,10, 411,10, 410,11, 410,11, 410,11, 409,11, 409,11, 408,10, 406,20, 406,21,406,22, 406,23, 406,23, 407,25, 407,27, 407,28, 407,29, 407,30, 406,30, 406,32, 406,33, 405,34, 405,33, 404,34, 405,35, 405,35, 404,36, 404,36, 403,36, 402,36, 402,36, 405,48, 408,57, 408,58, 408,58, 408,59, 409,59, 409,59, 409,60, 409,60, 410,61, 410,61, 410,61, 411,61, 411,62, 411,60, 411,59, 411,58, 411,57, 411,56, 412,55,413,54, 413,53, 412,53, 413,52, 414,52, 414,51, 413,50, 414,49, 414,50, 415,50, 415,50, 416,49, 416,49, 415,48, 416,47, 416,46, 417,47, 418,46, 419,45, 420,43, 420,41, 419,40, 419,40, 420,39, 420,39, 421,40, 422,41, 422,41, 423,40, 423,39, 423,39, 424,39, 425,39, 425,39, 426,38, 426,37, 427,37, 427,37, 427,36, 427,36, 428,35,429,35, 429,35, 430,34, 430,34, 430,33, 431,33, 431,33, 431,31, 431,30" />
	<!-- color #9 -->
	<area shape="poly" id="NJ" title="New Jersey" alt="New Jersey" href="https://www.surflocalmedia.com/New-JerseyUS/" coords="387,87, 386,87, 386,87, 386,87, 387,88, 387,88, 387,88, 386,88, 386,89, 386,89, 386,90, 386,91, 386,91, 386,91, 386,91, 386,91, 386,92, 386,92, 386,92, 386,93, 386,93, 386,93, 386,94, 387,94, 387,94, 387,94, 387,94, 387,94, 387,94, 387,94, 387,94, 388,95, 388,95, 389,96, 389,97, 389,97,389,97, 389,97, 388,97, 388,97, 387,98, 387,99, 387,99, 387,99, 387,99, 386,100, 386,100, 386,100, 386,100, 386,100, 386,101, 385,101, 385,101, 385,101, 385,102, 385,102, 385,102, 385,102, 385,102, 385,103, 386,103, 386,104, 386,104, 386,105, 387,106, 389,108, 389,108, 389,108, 390,108, 390,108, 390,109, 390,110, 390,110,390,111, 390,111, 391,111, 391,111, 391,111, 391,110, 392,109, 392,108, 393,107, 394,107, 395,104, 396,103, 397,102, 398,101, 398,101, 398,98, 398,97, 397,95, 396,94, 396,92, 394,91, 394,91, 394,91, 394,91, 394,91, 394,91, 393,91, 393,91, 393,91, 393,91, 393,91, 393,91, 393,91, 393,90, 393,90, 393,89, 393,88, 392,88, 387,87" />
	<area shape="poly" id="NY" title="New York" alt="New York" href="https://www.surflocalmedia.com/New-YorkUS/" coords="394,85, 394,84, 395,83, 395,83, 393,74, 392,70, 392,70, 390,63, 390,63, 390,63, 390,63, 389,63, 389,62, 389,62, 389,62, 389,63, 388,63, 388,63, 388,63, 388,63, 388,63, 388,63, 388,62, 388,62, 388,62, 388,62, 388,62, 388,61, 388,61, 388,61, 388,61, 388,60, 387,59, 387,59, 387,59, 387,58,387,58, 387,57, 387,56, 387,54, 387,54, 387,54, 387,54, 387,53, 387,53, 387,53, 387,53, 387,52, 387,52, 387,52, 387,51, 387,51, 387,51, 387,51, 387,51, 387,51, 387,50, 387,50, 387,50, 387,50, 387,49, 387,49, 387,48, 386,48, 386,48, 386,48, 386,49, 386,49, 386,49, 386,49, 386,48, 386,47, 386,46, 385,46, 385,45, 386,45, 386,45,386,45, 386,45, 386,44, 386,44, 386,44, 384,44, 383,45, 382,45, 380,45, 378,46, 376,47, 374,48, 373,50, 372,51, 372,52, 371,53, 371,54, 370,55, 370,56, 370,56, 370,56, 371,56, 371,56, 371,57, 371,57, 371,57, 370,58, 370,58, 371,59, 371,60, 371,63, 371,64, 370,64, 370,64, 369,64, 369,65, 368,66, 368,66, 367,67, 367,66, 366,67,363,68, 362,68, 362,67, 361,67, 358,67, 355,68, 353,69, 352,70, 352,70, 352,71, 352,73, 353,76, 353,78, 352,78, 351,80, 348,82, 347,83, 348,85, 380,80, 380,80, 380,80, 380,80, 381,80, 382,81, 382,82, 383,82, 383,83, 383,83, 383,84, 383,84, 384,84, 384,84, 384,84, 384,85, 384,85, 384,85, 384,85, 384,85, 384,86, 385,86, 385,86,385,86, 386,86, 386,86, 386,87, 386,87, 386,87, 386,87, 387,87, 392,88, 393,88, 393,88, 393,88, 393,89, 394,89, 394,89, 394,88, 394,88, 394,88, 395,87, 394,87, 394,86, 395,85, 395,85, 394,85" />
	<area shape="poly" id="SI" title="New York" alt="New York" href="https://www.surflocalmedia.com/New-YorkUS/" coords="407,83, 405,83, 405,83, 407,82, 408,81, 407,81, 406,82, 404,83, 403,83, 403,83, 401,83, 400,84, 400,85, 399,85, 398,85, 398,86, 397,86, 397,87, 396,87, 396,87, 395,88, 395,88, 395,89, 395,89, 396,89, 397,89, 397,89, 398,89, 398,88, 398,88, 399,88, 399,88, 398,89, 399,89, 399,89, 400,88,403,86, 404,86, 406,84, 408,83, 410,81, 408,82, 407,83" />
	<!-- color #8 -->
	<area shape="poly" id="WV" title="West Virginia" alt="West Virginia" href="https://www.surflocalmedia.com/West-VirginiaUS/" coords="347,110, 346,110, 345,100, 345,100, 345,100, 344,100, 343,101, 343,101, 343,102, 343,102, 343,102, 344,102, 344,103, 344,103, 344,104, 344,104, 344,105, 344,105, 344,106, 343,108, 341,113, 341,113, 341,113, 340,114, 341,115, 341,116, 340,116, 340,116, 340,116, 339,116, 338,117, 338,117,337,119, 337,119, 337,119, 336,120, 336,120, 337,121, 337,121, 336,121, 336,121, 335,121, 335,122, 335,122, 335,122, 336,123, 336,123, 336,123, 336,123, 335,123, 335,124, 335,124, 335,124, 335,124, 335,123, 334,123, 334,123, 334,123, 334,123, 334,124, 334,124, 334,124, 334,125, 333,125, 333,125, 333,126, 333,126, 332,126,332,127, 331,127, 331,127, 331,127, 332,127, 332,128, 333,128, 333,128, 333,129, 333,129, 334,130, 335,130, 335,131, 335,131, 335,132, 335,132, 336,134, 337,135, 337,137, 337,138, 338,138, 338,138, 338,138, 339,139, 339,140, 340,140, 341,139, 341,139, 341,139, 342,139, 342,138, 342,138, 343,139, 344,139, 345,138, 345,138,346,138, 347,137, 347,137, 347,137, 347,137, 348,136, 348,136, 348,136, 349,136, 350,136, 351,136, 352,135, 354,133, 354,133, 354,132, 353,132, 353,132, 353,131, 353,130, 354,129, 354,129, 355,128, 355,127, 356,127, 356,125, 356,123, 356,122, 357,121, 357,121, 357,121, 358,122, 358,123, 359,124, 359,124, 360,124, 360,124,360,124, 360,124, 360,123, 361,122, 361,122, 362,119, 362,119, 362,119, 362,118, 362,118, 362,118, 363,119, 363,119, 363,119, 364,117, 364,117, 365,116, 365,116, 366,116, 366,115, 367,114, 367,114, 368,113, 368,113, 369,112, 369,111, 369,111, 369,111, 369,111, 368,110, 368,110, 367,110, 367,110, 367,110, 366,110, 366,109,366,109, 366,109, 366,109, 365,109, 365,109, 365,109, 365,108, 365,108, 364,108, 364,108, 364,108, 364,108, 363,108, 363,108, 363,108, 363,108, 363,108, 362,108, 362,108, 362,108, 361,108, 361,108, 361,108, 361,108, 361,108, 361,108, 361,109, 361,109, 360,109, 360,109, 360,109, 360,109, 360,110, 360,110, 360,110, 360,110,359,110, 359,110, 359,110, 359,110, 358,110, 358,110, 358,110, 358,111, 358,111, 358,111, 358,111, 358,111, 358,112, 358,112, 357,112, 357,113, 357,113, 357,113, 356,114, 356,115, 355,115, 355,115, 355,112, 355,108, 347,110" />
	<area shape="poly" id="M2" title="Maryland" alt="Maryland" href="https://www.surflocalmedia.com/MarylandUS/" coords="387,121, 387,123, 388,126, 388,126, 389,127, 389,127, 389,126, 390,126, 390,125, 390,124, 390,122, 390,120, 390,120, 389,120, 387,121, 387,121" />
	<area shape="poly" id="VA" title="Virginia" alt="Virginia" href="https://www.surflocalmedia.com/VirginiaUS/" coords="383,116, 382,116, 382,116, 381,116, 380,115, 379,115, 379,115, 379,115, 378,115, 378,115, 378,115, 378,115, 378,114, 378,114, 378,114, 379,114, 379,114, 379,114, 378,113, 378,113, 377,113, 377,113, 376,113, 376,113, 376,113, 375,115, 369,111, 369,111, 369,111, 369,111, 369,112, 368,113,368,113, 367,114, 366,115, 366,116, 365,116, 364,117, 364,117, 363,119, 363,119, 363,119, 362,118, 362,118, 362,119, 362,119, 362,119, 361,122, 361,122, 360,123, 360,124, 360,124, 360,124, 360,124, 360,124, 359,124, 359,124, 358,123, 358,122, 357,121, 357,121, 357,121, 356,122, 356,123, 356,125, 356,127, 355,127, 355,128,354,129, 354,129, 353,130, 353,131, 353,132, 353,132, 354,132, 354,133, 354,133, 352,135, 351,136, 350,136, 349,136, 348,136, 348,136, 348,136, 347,137, 347,137, 347,137, 347,137, 346,138, 346,138, 345,138, 344,139, 343,139, 342,138, 342,138, 342,139, 341,139, 341,139, 341,139, 340,140, 339,140, 339,139, 338,138, 338,138,338,138, 337,138, 337,139, 337,139, 336,140, 335,141, 335,141, 335,141, 334,141, 334,142, 334,142, 333,142, 333,142, 333,143, 333,143, 332,144, 332,144, 331,144, 331,145, 331,145, 331,145, 330,145, 330,146, 330,146, 329,146, 329,147, 329,147, 328,147, 327,148, 327,148, 327,148, 328,148, 341,146, 342,146, 350,144, 352,144,353,144, 361,142, 364,142, 380,138, 380,138, 392,135, 392,135, 391,134, 390,133, 389,131, 388,131, 387,131, 386,132, 385,132, 385,131, 383,130, 381,129, 382,129, 383,129, 385,129, 386,129, 386,128, 386,127, 386,126, 386,126, 385,125, 383,124, 383,123, 384,122, 384,121, 383,121, 382,121, 381,121, 379,121, 380,120, 381,119,382,119, 383,118, 383,117, 383,116, 383,116, 383,116" />
	<area shape="poly" id="MD" title="Maryland" alt="Maryland" href="https://www.surflocalmedia.com/MarylandUS/" coords="384,102, 384,102, 361,107, 355,108, 355,112, 355,115, 356,114, 357,113, 357,113, 357,112, 357,112, 358,112, 358,112, 358,111, 358,111, 358,111, 358,111, 358,110, 358,110, 358,110, 359,110, 359,110, 359,110, 359,110, 359,110, 360,110, 360,110, 360,110, 360,110, 360,109, 360,109, 360,109,360,109, 361,109, 361,109, 361,108, 361,108, 361,108, 361,108, 361,108, 361,108, 362,108, 362,108, 362,108, 362,108, 363,108, 363,108, 363,108, 363,108, 363,108, 363,108, 364,108, 364,108, 364,108, 364,108, 365,108, 365,109, 365,109, 365,109, 366,109, 366,109, 366,109, 366,109, 366,109, 366,110, 367,110, 367,110, 367,110,368,110, 368,110, 369,110, 369,111, 375,115, 376,113, 376,113, 376,113, 377,113, 377,113, 378,113, 378,113, 378,113, 379,114, 379,114, 379,114, 379,114, 378,114, 378,114, 378,115, 378,115, 378,115, 379,115, 379,115, 379,115, 379,115, 380,115, 380,115, 381,116, 382,116, 382,116, 383,116, 383,116, 383,116, 383,116, 382,115,382,115, 381,114, 381,113, 381,112, 381,111, 380,111, 380,110, 380,110, 380,110, 380,108, 379,108, 379,108, 380,108, 379,107, 379,105, 380,104, 380,104, 380,103, 381,104, 381,105, 381,105, 381,106, 381,106, 381,107, 382,108, 382,109, 382,110, 383,110, 382,110, 382,111, 383,111, 384,113, 385,114, 385,114, 386,115, 387,116,386,116, 386,117, 386,117, 386,118, 386,118, 386,118, 387,119, 387,120, 387,121, 387,121, 387,121, 389,120, 390,120, 390,119, 390,119, 390,119, 390,118, 390,118, 391,118, 391,117, 391,116, 391,114, 386,114, 384,102" />
	<area shape="poly" id="DE" title="Delaware" alt="Delaware" href="https://www.surflocalmedia.com/DelawareUS/" coords="385,102, 385,102, 385,102, 385,102, 385,101, 385,101, 385,101, 385,101, 385,101, 384,102, 384,102, 386,114, 391,114, 391,112, 390,112, 390,112, 389,111, 389,110, 388,109, 388,108, 387,107, 387,106, 386,105, 386,104, 385,103, 385,103, 385,103, 385,102, 385,102" />
	<area shape="poly" id="PA" title="Pennsylvania" alt="Pennsylvania" href="https://www.surflocalmedia.com/PennsylvaniaUS/" coords="345,100, 346,110, 347,110, 361,107, 384,102, 384,102, 384,102, 384,101, 385,101, 385,101, 385,101, 386,101, 386,100, 386,100, 386,100, 386,100, 387,99, 387,99, 387,99, 387,98, 387,98, 388,97, 388,97, 389,97, 389,97, 389,97, 389,96, 388,95, 387,94, 387,94, 387,94, 387,94, 387,94, 387,94,386,94, 386,93, 386,93, 386,93, 386,93, 386,92, 386,92, 386,91, 386,91, 386,91, 386,91, 386,91, 386,90, 386,89, 386,89, 387,88, 386,87, 386,87, 386,87, 386,87, 386,87, 386,87, 386,87, 386,87, 386,86, 386,86, 385,86, 385,86, 385,86, 385,86, 384,86, 384,85, 384,85, 384,85, 384,85, 384,85, 384,85, 384,84, 384,84, 384,84, 383,84,383,84, 383,83, 383,83, 383,83, 383,82, 382,82, 382,82, 382,81, 381,80, 380,80, 380,80, 380,80, 348,85, 347,83, 347,83, 347,84, 346,84, 345,84, 344,85, 343,85, 342,86, 343,90, 345,100, 345,100" />
	<!-- color #7 -->
	<area shape="poly" id="SC" title="South Carolina" alt="South Carolina" href="https://www.surflocalmedia.com/South-CarolinaUS/" coords="364,161, 355,162, 355,162, 354,161, 354,161, 354,161, 353,161, 353,160, 353,160, 353,160, 344,160, 344,161, 344,161, 341,161, 338,163, 334,164, 334,164, 334,164, 334,164, 333,164, 333,164, 333,165, 333,165, 332,165, 332,166, 332,166, 331,166, 331,166, 331,167, 331,167, 332,167, 332,167,332,168, 332,168, 333,168, 333,168, 333,168, 334,169, 334,169, 334,169, 335,169, 335,169, 335,169, 336,169, 336,169, 336,169, 337,170, 337,170, 338,171, 339,171, 339,172, 340,173, 341,175, 343,176, 344,177, 344,177, 346,178, 346,178, 347,179, 347,180, 348,180, 348,180, 349,180, 349,180, 349,180, 350,181, 350,181, 351,182,351,182, 351,182, 352,183, 352,183, 352,183, 352,183, 352,183, 353,184, 353,184, 353,184, 353,185, 353,185, 353,185, 353,185, 353,187, 353,187, 353,187, 353,187, 354,187, 354,187, 354,188, 354,188, 355,188, 355,188, 355,188, 355,189, 355,189, 356,189, 356,190, 356,190, 357,190, 357,190, 357,190, 357,190, 357,189, 357,189,357,188, 358,188, 358,188, 359,187, 358,186, 358,185, 358,185, 359,185, 359,185, 359,186, 360,186, 360,186, 361,185, 361,184, 360,183, 360,183, 361,182, 362,182, 362,183, 362,183, 363,183, 363,183, 363,182, 364,181, 364,180, 364,179, 364,179, 365,180, 365,180, 366,180, 367,179, 367,178, 368,177, 368,177, 369,177, 370,177,370,176, 371,175, 371,174, 371,173, 372,172, 372,171, 373,169, 375,168, 364,161, 364,161" />
	<area shape="poly" id="NC" title="North Carolina" alt="North Carolina" href="https://www.surflocalmedia.com/North-CarolinaUS/" coords="380,138, 364,142, 361,142, 355,144, 353,144, 352,144, 350,144, 345,145, 343,146, 342,147, 341,147, 341,147, 341,148, 341,148, 341,149, 341,150, 341,150, 341,150, 341,150, 341,150, 341,150, 340,150, 340,150, 340,150, 340,150, 339,151, 339,151, 339,152, 338,152, 338,153, 337,153, 337,153,337,153, 336,153, 336,153, 336,153, 336,153, 336,153, 335,153, 335,154, 335,154, 334,154, 334,155, 334,155, 334,155, 334,155, 333,156, 333,156, 333,156, 333,156, 333,156, 333,156, 332,156, 332,156, 332,155, 332,155, 332,155, 332,155, 332,155, 331,155, 331,156, 330,158, 330,158, 330,158, 330,159, 329,159, 329,159, 328,159,328,160, 328,160, 327,160, 327,160, 327,160, 326,160, 326,161, 326,161, 326,161, 326,162, 326,162, 326,162, 326,163, 326,163, 326,163, 326,163, 325,163, 325,163, 325,163, 325,164, 325,164, 324,165, 324,165, 324,165, 328,165, 329,165, 329,164, 334,164, 336,163, 338,163, 341,161, 344,161, 344,161, 344,161, 344,160, 353,160,353,160, 353,160, 353,160, 353,160, 353,161, 354,161, 354,161, 354,161, 354,161, 355,162, 355,162, 364,161, 364,161, 364,161, 375,168, 375,168, 376,167, 379,165, 379,165, 378,164, 378,164, 379,165, 380,165, 380,164, 381,163, 380,163, 380,163, 380,162, 381,160, 384,157, 388,154, 388,154, 389,153, 389,152, 388,152, 387,152,386,153, 384,153, 383,152, 384,152, 385,152, 386,151, 387,150, 387,150, 387,149, 387,149, 386,149, 385,148, 385,148, 387,148, 388,149, 390,149, 391,149, 392,148, 392,147, 393,145, 393,144, 394,144, 394,143, 393,141, 392,141, 391,141, 391,142, 391,143, 391,144, 391,144, 390,142, 389,142, 389,142, 388,142, 387,142, 385,143,385,143, 385,142, 384,141, 382,140, 383,140, 384,140, 385,140, 386,140, 388,140, 389,140, 390,139, 391,139, 391,138, 391,137, 391,137, 391,137, 391,136, 392,136, 392,136, 392,136, 392,135, 392,135, 380,138, 380,138" />
	<area shape="poly" id="FL" title="Florida" alt="Florida" href="https://www.surflocalmedia.com/FloridaUS/" coords="354,207, 353,207, 353,207, 352,207, 352,207, 351,206, 351,206, 350,206, 350,207, 350,207, 350,207, 350,207, 349,207, 349,207, 349,207, 349,208, 349,208, 350,209, 350,209, 350,209, 351,210, 351,211, 351,211, 350,211, 350,212, 350,212, 350,213, 349,213, 349,213, 348,212, 348,212, 348,212,348,212, 348,212, 348,211, 347,211, 347,210, 347,210, 347,210, 347,210, 326,212, 326,212, 326,212, 326,212, 326,211, 326,211, 325,210, 324,210, 324,209, 322,210, 318,210, 299,212, 299,212, 299,213, 299,213, 299,214, 299,214, 300,214, 301,215, 301,215, 301,215, 301,215, 301,216, 301,216, 301,217, 301,217, 301,217, 300,218,300,218, 300,218, 300,218, 303,218, 304,217, 304,217, 304,216, 304,216, 305,215, 306,216, 306,216, 306,217, 306,217, 306,217, 308,217, 309,216, 312,216, 312,216, 313,216, 313,215, 313,215, 314,215, 315,215, 315,215, 314,215, 314,216, 315,216, 315,216, 319,216, 319,216, 317,217, 317,217, 317,217, 318,217, 319,217, 320,218,320,219, 320,221, 320,221, 319,221, 319,220, 318,220, 319,221, 320,222, 320,222, 322,222, 324,221, 325,221, 327,219, 328,219, 330,217, 331,216, 331,216, 332,216, 334,216, 334,217, 335,218, 336,218, 337,218, 338,218, 338,219, 338,221, 339,221, 341,221, 344,224, 346,226, 347,229, 347,233, 347,235, 348,238, 348,238, 349,238,349,237, 349,237, 348,236, 348,235, 349,235, 350,236, 350,234, 351,235, 351,236, 351,236, 351,237, 350,239, 349,240, 348,240, 349,241, 350,242, 352,245, 352,244, 353,245, 354,245, 354,245, 354,244, 354,244, 355,244, 355,244, 356,243, 356,242, 356,243, 356,244, 356,245, 356,249, 357,249, 357,248, 358,247, 358,248, 358,251,360,254, 364,256, 367,256, 368,257, 367,258, 367,258, 368,258, 368,259, 367,260, 367,261, 368,262, 368,262, 367,262, 366,262, 365,263, 367,263, 369,263, 370,262, 371,262, 374,260, 375,260, 375,258, 376,257, 377,255, 377,253, 377,253, 377,249, 375,241, 375,240, 370,234, 368,231, 367,229, 366,227, 366,225, 366,225, 364,223,365,224, 365,224, 365,224, 365,224, 364,222, 363,221, 361,218, 357,212, 356,209, 355,207, 355,207, 354,207" />
	<area shape="poly" id="GA" title="Georgia" alt="Georgia" href="https://www.surflocalmedia.com/GeorgiaUS/" coords="356,190, 356,190, 356,189, 355,189, 355,189, 355,188, 355,188, 355,188, 354,188, 354,188, 354,188, 354,187, 354,187, 353,187, 353,187, 353,187, 353,187, 353,185, 353,185, 353,185, 353,184, 353,184, 352,183, 352,183, 351,183, 351,182, 351,182, 351,182, 350,181, 350,181, 349,180, 349,180,349,180, 348,180, 348,180, 347,180, 347,180, 347,179, 346,178, 346,178, 345,178, 344,177, 343,176, 341,175, 340,173, 339,172, 339,171, 338,171, 337,170, 337,170, 336,169, 336,169, 335,169, 335,169, 334,169, 334,169, 334,169, 333,168, 333,168, 332,168, 332,168, 332,167, 332,167, 331,167, 331,167, 331,166, 331,166, 331,166,332,166, 332,166, 332,165, 333,165, 333,165, 333,164, 333,164, 334,164, 334,164, 334,164, 334,164, 334,164, 329,164, 329,165, 328,165, 324,165, 324,165, 314,166, 312,166, 319,189, 320,190, 320,190, 321,191, 321,191, 321,192, 321,192, 321,192, 321,192, 321,192, 321,193, 321,193, 321,193, 321,193, 322,194, 322,194, 322,194,322,194, 322,194, 322,194, 322,194, 322,194, 322,195, 322,195, 322,195, 322,195, 322,196, 322,196, 322,196, 322,197, 322,197, 322,198, 321,199, 321,199, 321,200, 321,200, 321,200, 322,201, 322,201, 322,201, 322,202, 323,203, 323,203, 323,203, 323,204, 323,204, 323,204, 323,205, 323,205, 323,205, 323,206, 323,206, 323,207,323,207, 323,207, 323,207, 323,208, 324,209, 324,209, 324,209, 324,210, 325,210, 326,211, 326,211, 326,211, 326,212, 326,212, 326,212, 347,210, 347,210, 347,210, 347,210, 347,210, 347,211, 348,211, 348,212, 348,212, 348,212, 348,212, 349,213, 349,213, 350,213, 350,212, 350,212, 350,211, 351,211, 351,210, 350,209, 350,209,349,208, 349,208, 349,207, 349,207, 349,207, 350,207, 350,206, 350,207, 350,207, 350,207, 350,206, 351,206, 351,206, 352,207, 352,207, 353,207, 353,207, 354,207, 355,207, 355,207, 354,205, 354,205, 354,205, 353,205, 354,205, 355,204, 355,204, 354,204, 354,204, 353,204, 354,203, 355,203, 355,202, 355,202, 355,202, 355,201,354,201, 354,200, 355,200, 355,199, 355,199, 355,198, 356,198, 356,198, 356,198, 356,197, 357,197, 356,197, 356,196, 356,196, 355,196, 355,196, 355,195, 356,195, 356,195, 355,194, 355,194, 355,194, 355,193, 355,193, 356,193, 356,192, 356,192, 357,192, 357,191, 357,191, 357,191, 357,190, 357,190, 356,190" />
	<area shape="poly" id="AL" title="Alabama" alt="Alabama" href="https://www.surflocalmedia.com/AlabamaUS/" coords="300,218, 301,217, 301,217, 301,217, 301,217, 301,216, 301,216, 301,215, 301,215, 301,215, 301,215, 300,214, 299,214, 299,214, 299,213, 299,213, 299,212, 299,212, 318,210, 324,209, 323,208, 323,207, 323,207, 323,207, 323,207, 323,206, 323,206, 323,205, 323,205, 323,204, 323,204, 323,204,323,203, 323,203, 323,202, 322,201, 322,201, 321,200, 321,200, 321,200, 321,199, 321,199, 322,198, 322,197, 322,197, 322,196, 322,196, 322,196, 322,195, 322,195, 322,195, 322,195, 322,195, 322,194, 322,194, 322,194, 322,194, 322,194, 322,194, 322,194, 322,194, 321,193, 321,193, 321,193, 321,193, 321,192, 321,192, 321,192,321,192, 321,192, 321,191, 321,191, 320,190, 320,190, 319,189, 312,166, 305,167, 304,167, 289,168, 289,168, 290,168, 290,168, 290,169, 290,169, 290,169, 290,169, 290,170, 290,171, 290,191, 290,202, 291,210, 292,219, 292,219, 292,219, 292,218, 293,218, 293,218, 293,218, 293,218, 293,218, 293,217, 293,216, 294,215, 294,215,295,215, 295,216, 296,217, 296,218, 297,218, 297,219, 297,219, 297,219, 296,219, 295,219, 295,219, 296,219, 297,219, 299,219, 300,218, 300,218, 300,218" />
	<area shape="poly" id="MS" title="Mississippi" alt="Mississippi" href="https://www.surflocalmedia.com/MississippiUS/" coords="290,202, 290,202, 290,191, 290,171, 290,170, 290,169, 290,169, 290,169, 290,169, 290,168, 289,168, 275,169, 275,169, 275,170, 275,170, 275,171, 275,171, 275,171, 274,171, 274,171, 274,172, 273,172, 273,172, 273,172, 273,172, 273,173, 272,173, 272,173, 272,173, 272,173, 272,174, 272,174,272,174, 272,175, 272,175, 272,175, 272,175, 272,175, 272,176, 272,176, 272,177, 271,177, 271,177, 271,177, 271,177, 270,177, 270,178, 270,178, 270,178, 270,178, 270,178, 270,179, 270,179, 270,179, 269,179, 269,180, 268,180, 268,180, 268,180, 268,181, 268,181, 269,181, 269,181, 269,181, 269,181, 270,181, 270,181, 270,181,270,182, 270,182, 270,182, 270,182, 269,183, 268,183, 267,183, 267,183, 267,184, 267,184, 267,184, 267,184, 267,184, 267,185, 267,185, 267,185, 267,185, 267,185, 267,186, 267,186, 267,186, 267,186, 266,187, 266,187, 266,187, 265,187, 265,188, 265,188, 265,188, 266,188, 266,188, 267,188, 267,188, 267,188, 267,188, 267,189,267,189, 266,189, 266,190, 266,190, 266,190, 266,190, 267,190, 267,190, 267,190, 267,191, 267,191, 267,191, 267,191, 267,191, 267,191, 266,192, 266,192, 266,192, 266,192, 267,192, 267,193, 267,193, 266,193, 266,193, 266,193, 266,193, 266,193, 266,194, 266,194, 266,194, 266,195, 266,195, 266,195, 266,195, 266,195, 266,196,266,196, 266,196, 266,196, 266,196, 266,196, 266,196, 266,197, 266,197, 266,197, 267,197, 267,197, 267,197, 267,197, 267,197, 267,198, 267,198, 267,198, 267,198, 266,198, 266,198, 266,199, 266,199, 266,199, 266,200, 267,200, 267,200, 267,200, 267,201, 268,201, 268,201, 268,201, 269,201, 269,201, 269,201, 269,201, 269,201,269,202, 269,202, 269,202, 268,203, 268,203, 267,203, 267,203, 267,203, 266,203, 266,203, 266,203, 266,204, 266,204, 266,204, 266,204, 266,204, 266,204, 266,204, 267,205, 267,205, 267,205, 267,205, 267,205, 267,205, 267,205, 268,205, 268,205, 268,205, 268,205, 268,206, 267,206, 267,206, 267,206, 267,207, 267,207, 267,207,267,207, 267,207, 267,207, 267,208, 266,208, 266,208, 266,208, 266,209, 266,209, 266,209, 266,210, 266,210, 266,210, 266,210, 266,211, 266,211, 266,211, 265,211, 266,212, 266,212, 266,212, 266,213, 266,213, 266,213, 266,213, 266,213, 266,213, 266,214, 266,214, 266,214, 266,214, 265,215, 265,215, 265,215, 266,216, 265,216,265,216, 264,216, 279,216, 279,217, 279,217, 279,218, 280,218, 280,218, 281,219, 281,219, 283,220, 283,220, 284,221, 284,221, 284,221, 284,220, 284,220, 285,220, 285,220, 285,220, 286,220, 286,220, 287,220, 287,220, 286,220, 286,219, 286,219, 287,219, 287,220, 288,220, 288,220, 289,220, 289,220, 289,219, 290,219, 290,219,290,219, 290,219, 292,219, 291,210, 290,202" />
	<area shape="poly" id="TN" title="Tennessee" alt="Tennessee" href="https://www.surflocalmedia.com/TennesseeUS/" coords="325,148, 305,150, 304,151, 296,151, 292,152, 292,151, 291,151, 289,151, 289,152, 289,153, 289,153, 278,155, 278,155, 278,155, 278,155, 278,156, 278,156, 278,156, 278,157, 278,157, 278,157, 278,157, 278,158, 278,158, 278,158, 278,158, 278,158, 277,159, 277,159, 277,159, 277,159, 277,159,277,159, 277,160, 277,160, 277,160, 277,160, 277,161, 277,161, 277,161, 277,161, 277,161, 277,161, 277,162, 277,162, 277,162, 277,162, 277,162, 277,162, 277,163, 276,163, 276,163, 276,163, 276,163, 276,163, 276,163, 276,164, 276,164, 276,164, 276,164, 275,165, 275,165, 275,165, 275,165, 274,166, 274,166, 274,166, 274,166,274,167, 274,167, 274,167, 274,167, 274,168, 274,168, 274,168, 274,168, 275,169, 275,169, 289,168, 289,168, 304,167, 305,167, 314,166, 324,165, 324,165, 324,165, 324,165, 324,165, 325,164, 325,163, 325,163, 325,163, 326,163, 326,163, 326,163, 326,162, 326,162, 326,162, 326,161, 326,161, 326,161, 326,160, 327,160, 327,160,327,160, 328,160, 328,160, 328,159, 329,159, 329,159, 329,159, 330,158, 330,158, 330,158, 331,156, 331,155, 332,155, 332,155, 332,155, 332,155, 332,155, 332,155, 332,156, 332,156, 333,156, 333,156, 333,156, 333,156, 333,156, 334,155, 334,155, 334,155, 334,154, 335,154, 335,153, 336,153, 336,153, 336,153, 336,153, 336,153,337,153, 337,153, 337,153, 338,153, 338,152, 339,152, 339,151, 339,151, 340,150, 340,150, 340,150, 341,150, 341,150, 341,150, 341,150, 341,150, 341,149, 341,148, 341,148, 341,147, 341,147, 342,147, 343,146, 341,146, 328,148, 327,148, 327,148, 327,148, 325,148" />
	<area shape="poly" id="KY" title="Kentucky" alt="Kentucky" href="https://www.surflocalmedia.com/KentuckyUS/" coords="337,138, 337,137, 337,135, 336,134, 335,132, 335,132, 335,131, 335,131, 335,130, 334,130, 333,129, 333,129, 333,128, 333,128, 332,128, 332,127, 331,127, 331,127, 330,127, 330,127, 330,127, 330,127, 330,127, 329,127, 329,126, 329,126, 329,126, 329,126, 328,126, 328,126, 328,126, 327,125,327,125, 327,125, 327,126, 326,126, 326,126, 326,126, 326,127, 325,127, 325,127, 325,126, 324,127, 324,127, 324,127, 323,126, 323,126, 323,126, 322,126, 322,126, 322,126, 321,126, 321,126, 321,126, 320,126, 320,126, 320,126, 319,126, 319,125, 319,125, 319,125, 318,124, 318,124, 317,124, 317,124, 316,124, 316,124, 316,124,316,124, 315,124, 315,124, 315,124, 315,124, 314,124, 314,125, 314,125, 314,126, 314,126, 314,126, 313,126, 313,126, 313,126, 313,127, 313,127, 314,127, 314,127, 314,127, 314,127, 314,127, 314,128, 314,128, 314,128, 314,128, 314,128, 314,128, 314,128, 313,129, 313,129, 312,129, 312,129, 311,128, 311,128, 311,128, 310,128,310,129, 310,129, 309,129, 309,129, 309,130, 309,130, 309,131, 309,131, 309,131, 309,131, 308,131, 308,132, 308,132, 308,132, 308,133, 308,133, 308,133, 307,133, 307,133, 307,133, 307,133, 307,134, 306,134, 306,135, 305,136, 305,136, 305,136, 305,136, 305,136, 304,136, 304,136, 304,136, 304,136, 304,135, 303,135, 303,134,303,134, 303,134, 303,134, 303,134, 303,134, 303,134, 302,135, 302,135, 302,135, 302,135, 302,135, 302,135, 302,136, 301,136, 301,136, 301,137, 301,137, 301,137, 300,137, 300,137, 300,137, 300,136, 299,136, 299,136, 299,136, 299,136, 298,137, 298,137, 298,137, 298,137, 298,137, 298,137, 298,138, 297,138, 297,138, 297,138,296,138, 296,137, 296,137, 296,137, 296,137, 296,137, 295,137, 295,137, 295,137, 295,137, 295,137, 294,137, 294,138, 294,138, 293,139, 293,139, 292,139, 292,139, 291,139, 291,139, 291,139, 291,139, 290,139, 290,139, 290,139, 290,140, 290,140, 289,141, 289,141, 289,141, 289,142, 289,142, 289,142, 289,142, 289,142, 289,143,289,143, 289,144, 289,144, 288,144, 288,144, 289,144, 289,145, 289,145, 289,145, 289,145, 289,145, 289,145, 289,146, 288,146, 288,146, 288,146, 288,146, 287,145, 287,146, 286,146, 286,146, 286,146, 286,147, 286,147, 286,147, 287,147, 287,148, 287,148, 287,148, 287,148, 287,148, 287,149, 287,149, 287,149, 287,149, 287,149,286,149, 284,150, 284,150, 284,151, 283,151, 283,152, 282,151, 282,151, 282,151, 282,151, 282,152, 282,152, 282,152, 282,152, 282,152, 281,152, 281,152, 281,153, 281,153, 281,154, 281,154, 281,154, 280,154, 279,154, 279,154, 278,155, 289,153, 289,153, 289,151, 291,151, 292,151, 292,152, 304,151, 305,150, 325,148, 327,148,327,148, 328,147, 329,147, 329,147, 329,146, 329,146, 330,145, 330,145, 331,145, 331,145, 331,145, 331,144, 332,144, 333,143, 333,143, 333,142, 333,142, 334,142, 334,141, 335,141, 335,141, 336,140, 337,139, 337,139, 337,138, 337,138, 338,138, 338,138, 338,138, 337,138" />
	<!-- color #6 -->
	<area shape="poly" id="OH" title="Ohio" alt="Ohio" href="https://www.surflocalmedia.com/OhioUS/" coords="308,94, 314,126, 314,126, 314,125, 314,125, 314,125, 315,124, 315,124, 315,124, 315,124, 315,124, 316,124, 316,124, 316,124, 317,124, 317,124, 317,124, 318,124, 318,124, 318,124, 319,125, 319,125, 319,125, 319,125, 319,126, 320,126, 320,126, 320,126, 320,126, 321,126, 321,126, 321,126,322,126, 322,126, 322,126, 322,126, 323,126, 323,126, 323,126, 324,127, 324,127, 324,127, 325,126, 325,127, 325,127, 326,127, 326,126, 326,126, 326,126, 327,126, 327,125, 327,125, 327,125, 328,126, 328,126, 328,126, 329,126, 329,126, 329,126, 329,126, 329,126, 329,127, 330,127, 330,127, 330,127, 330,127, 331,127, 331,127,331,127, 332,127, 332,126, 333,126, 333,126, 333,125, 333,125, 334,125, 334,124, 334,124, 334,124, 334,123, 334,123, 334,123, 334,123, 335,123, 335,124, 335,124, 335,124, 335,124, 335,123, 336,123, 336,123, 336,123, 336,123, 335,122, 335,122, 335,122, 335,121, 336,121, 336,121, 337,121, 337,121, 336,120, 336,120, 337,119,337,119, 337,119, 337,119, 338,117, 338,117, 339,116, 340,116, 340,116, 340,116, 341,116, 341,115, 340,114, 341,113, 341,113, 341,113, 343,108, 344,106, 344,105, 344,105, 344,104, 344,104, 344,103, 344,103, 344,102, 343,102, 343,102, 343,102, 343,101, 343,101, 344,100, 345,100, 345,100, 343,90, 342,86, 342,86, 341,86, 338,88,336,90, 334,91, 333,91, 333,92, 332,92, 331,93, 330,93, 330,93, 329,93, 329,93, 328,94, 326,94, 325,94, 325,94, 326,94, 326,93, 327,93, 328,93, 327,92, 327,92, 327,92, 327,93, 326,93, 325,93, 324,93, 324,92, 323,92, 323,93, 323,93, 322,93, 321,93, 322,92, 321,92, 317,93, 308,94" />
	<area shape="poly" id="IN" title="Indiana" alt="Indiana" href="https://www.surflocalmedia.com/IndianaUS/" coords="293,130, 293,130, 293,130, 293,130, 292,130, 292,130, 292,130, 292,130, 292,130, 291,131, 291,131, 291,131, 291,132, 291,132, 291,132, 292,132, 292,132, 292,132, 292,132, 292,133, 292,133, 292,134, 292,134, 292,134, 292,134, 292,134, 291,134, 291,134, 291,135, 291,135, 291,135, 291,135,291,136, 291,136, 290,137, 290,137, 290,138, 290,138, 290,139, 290,139, 290,139, 290,139, 290,139, 290,139, 291,139, 291,139, 291,139, 292,139, 292,139, 292,139, 293,139, 293,139, 294,138, 294,137, 295,137, 295,137, 295,137, 295,137, 296,137, 296,137, 296,137, 296,137, 296,138, 297,138, 297,138, 298,138, 298,137, 298,137,298,137, 298,137, 298,137, 298,137, 298,137, 299,136, 299,136, 299,136, 299,136, 300,136, 300,137, 300,137, 301,137, 301,137, 301,136, 302,136, 302,135, 302,135, 302,135, 302,135, 302,135, 303,134, 303,134, 303,134, 303,134, 303,134, 303,134, 304,135, 304,136, 304,136, 304,136, 305,136, 305,136, 305,136, 305,136, 306,134,306,134, 307,134, 307,133, 307,133, 307,133, 307,133, 307,133, 308,133, 308,133, 308,132, 308,132, 308,132, 308,131, 309,131, 309,131, 309,130, 309,130, 309,129, 309,129, 310,129, 310,129, 310,128, 311,128, 311,128, 311,128, 312,129, 312,129, 313,129, 313,129, 313,129, 314,128, 314,128, 314,128, 314,128, 314,128, 314,128,314,128, 314,127, 314,127, 314,127, 314,127, 313,127, 313,127, 313,126, 313,126, 313,126, 313,126, 314,126, 314,126, 308,94, 294,96, 294,97, 293,97, 292,98, 292,98, 291,98, 290,98, 290,97, 289,97, 289,97, 289,97, 293,130" />
	<area shape="poly" id="IL" title="Illinois" alt="Illinois" href="https://www.surflocalmedia.com/IllinoisUS/" coords="287,92, 266,93, 266,93, 266,94, 267,94, 267,94, 267,95, 267,96, 268,96, 268,96, 268,96, 268,97, 268,97, 268,97, 268,98, 268,98, 268,99, 268,99, 268,100, 268,100, 268,100, 268,101, 268,101, 268,101, 267,101, 267,101, 267,102, 266,102, 266,102, 265,102, 265,102, 264,103, 263,103, 263,103,263,104, 263,104, 262,105, 262,105, 262,106, 262,106, 263,106, 263,107, 263,108, 263,108, 263,108, 263,109, 263,109, 263,109, 263,109, 263,109, 263,110, 263,110, 263,110, 263,111, 263,111, 262,111, 262,111, 262,111, 262,111, 262,112, 262,112, 261,112, 260,113, 260,113, 260,115, 260,115, 260,115, 260,115, 260,115, 260,116,260,116, 260,116, 261,117, 261,117, 261,117, 261,117, 261,118, 261,118, 261,118, 261,118, 261,118, 261,119, 261,119, 261,119, 261,120, 261,120, 261,120, 261,120, 262,121, 262,121, 262,121, 262,122, 263,122, 263,122, 263,123, 263,123, 264,124, 264,124, 265,124, 265,124, 265,125, 266,125, 266,125, 266,125, 266,126, 266,126,266,126, 266,127, 266,127, 266,128, 266,128, 266,128, 267,129, 267,129, 267,130, 267,130, 268,130, 268,130, 268,130, 268,130, 268,130, 268,129, 268,129, 269,129, 269,129, 270,129, 270,129, 270,129, 271,129, 271,130, 272,131, 272,132, 272,132, 272,132, 272,133, 272,133, 272,133, 272,133, 271,134, 271,134, 271,134, 271,135,271,136, 271,136, 270,136, 270,136, 270,136, 270,137, 270,137, 270,138, 270,138, 271,138, 271,138, 272,139, 274,140, 274,140, 274,140, 275,141, 275,141, 276,141, 276,142, 276,143, 276,143, 277,143, 277,144, 277,144, 278,144, 278,145, 278,145, 278,145, 279,146, 279,146, 279,146, 279,146, 279,147, 279,147, 278,147, 278,148,278,148, 279,148, 279,149, 280,149, 280,149, 280,150, 280,150, 280,150, 280,150, 281,150, 281,150, 281,150, 281,149, 281,149, 281,149, 281,149, 281,149, 281,149, 281,149, 281,150, 282,150, 282,151, 282,151, 282,151, 283,152, 283,151, 284,151, 284,150, 284,150, 286,149, 287,149, 287,149, 287,149, 287,149, 287,148, 287,148,287,147, 286,147, 286,147, 286,147, 286,146, 286,146, 287,146, 287,145, 288,146, 288,146, 288,146, 289,146, 289,145, 289,145, 289,144, 288,144, 288,144, 289,144, 289,144, 289,143, 289,143, 289,142, 289,142, 289,142, 289,142, 289,142, 289,141, 289,141, 289,141, 289,141, 290,140, 290,140, 290,139, 290,139, 290,139, 290,139,290,138, 290,138, 290,137, 290,137, 291,136, 291,136, 291,135, 291,135, 291,135, 291,134, 291,134, 292,134, 292,134, 292,134, 292,133, 292,133, 292,133, 292,133, 292,132, 292,132, 292,132, 292,132, 291,132, 291,132, 291,132, 291,131, 291,131, 291,131, 292,130, 292,130, 292,130, 292,130, 293,130, 293,130, 293,130, 289,97,289,97, 289,97, 289,97, 288,96, 288,95, 287,95, 287,95, 287,93, 287,92, 287,92" />
	<area shape="poly" id="I2" title="Michigan" alt="Michigan" href="https://www.surflocalmedia.com/MichiganUS/" coords="321,92, 321,92, 321,91, 321,91, 321,90, 321,90, 322,89, 322,89, 322,88, 322,87, 323,86, 324,85, 324,84, 324,84, 324,83, 325,83, 326,83, 326,83, 327,83, 327,83, 327,82, 327,81, 327,80, 327,79, 325,73, 323,69, 322,68, 321,67, 321,67, 320,68, 320,68, 319,69, 318,69, 318,70, 319,70, 319,70,318,71, 318,71, 318,71, 317,72, 317,73, 316,74, 315,74, 314,74, 314,74, 313,72, 313,71, 313,70, 314,70, 314,69, 314,69, 314,68, 315,67, 315,67, 315,66, 316,65, 316,63, 317,62, 316,62, 317,61, 319,61, 318,61, 318,59, 316,59, 317,58, 317,58, 316,57, 315,56, 313,56, 313,56, 312,55, 311,54, 311,54, 310,54, 310,54, 309,53, 307,52,305,51, 305,52, 303,54, 303,56, 303,57, 303,58, 304,58, 304,59, 303,59, 302,59, 301,58, 301,59, 301,60, 301,61, 301,62, 300,63, 300,62, 300,61, 300,61, 300,62, 300,63, 299,62, 299,61, 299,60, 299,60, 299,60, 299,59, 299,59, 298,60, 298,62, 298,63, 297,63, 296,64, 296,64, 296,65, 296,66, 296,67, 295,67, 295,68, 295,69, 296,70,295,72, 295,74, 295,75, 295,75, 296,75, 295,76, 295,76, 297,79, 298,80, 298,80, 298,81, 297,82, 297,83, 298,84, 299,86, 299,88, 297,91, 294,95, 294,96, 317,93, 321,92" />
	<area shape="poly" id="MI" title="Michigan" alt="Michigan" href="https://www.surflocalmedia.com/MichiganUS/" coords="264,48, 264,48, 264,48, 264,49, 265,49, 266,50, 273,53, 273,53, 274,52, 274,52, 275,52, 276,52, 276,52, 277,52, 277,52, 277,52, 277,52, 277,52, 277,53, 277,53, 277,53, 277,53, 277,53, 277,53, 278,53, 278,53, 279,53, 279,53, 279,54, 280,54, 280,54, 280,55, 281,55, 281,56, 281,56, 281,56,281,56, 281,57, 281,57, 281,57, 281,57, 281,58, 281,58, 281,58, 281,58, 282,58, 282,58, 282,58, 282,57, 282,57, 283,57, 283,57, 283,57, 283,57, 284,58, 284,58, 284,58, 284,58, 284,59, 283,59, 283,59, 283,59, 283,59, 283,60, 283,60, 283,60, 283,60, 283,60, 284,61, 284,61, 285,61, 285,59, 286,58, 287,54, 288,54, 288,54, 288,54,288,54, 289,53, 289,54, 289,55, 289,56, 289,56, 290,56, 290,54, 291,53, 292,53, 293,53, 293,53, 293,52, 293,52, 294,51, 295,51, 296,51, 297,50, 298,50, 299,50, 300,50, 300,50, 301,51, 302,51, 303,51, 302,50, 302,50, 302,49, 302,49, 303,49, 304,50, 305,50, 306,50, 306,50, 308,50, 310,50, 311,49, 312,49, 313,48, 313,48, 312,47,312,47, 311,46, 310,46, 310,45, 310,44, 309,43, 308,43, 308,44, 307,44, 306,44, 306,44, 305,44, 304,44, 304,43, 303,42, 303,41, 302,41, 300,42, 299,42, 297,42, 297,42, 296,42, 295,43, 294,44, 293,44, 292,45, 292,45, 292,46, 291,45, 290,45, 290,45, 289,45, 288,46, 287,46, 286,45, 285,44, 284,44, 284,43, 283,43, 283,42, 282,42,280,42, 280,42, 279,42, 279,42, 279,41, 279,41, 278,42, 277,43, 277,44, 276,43, 276,42, 277,40, 278,39, 279,38, 279,37, 281,37, 281,36, 281,36, 280,36, 279,36, 278,37, 276,38, 275,39, 274,41, 273,42, 272,43, 270,44, 269,44, 268,44, 268,44, 267,45, 265,46, 264,47, 263,47, 263,47, 263,48, 264,48" />
	<area shape="poly" id="WI" title="Wisconsin" alt="Wisconsin" href="https://www.surflocalmedia.com/WisconsinUS/" coords="252,47, 252,52, 252,53, 252,53, 251,54, 251,54, 251,55, 251,55, 250,56, 249,56, 248,56, 248,56, 248,56, 248,57, 247,58, 247,58, 247,58, 247,60, 247,60, 247,61, 247,61, 247,61, 248,61, 248,61, 248,61, 249,62, 249,62, 249,62, 249,62, 249,63, 249,65, 249,66, 249,67, 249,68, 249,68, 249,68,249,69, 250,70, 250,70, 250,70, 250,70, 250,70, 251,70, 252,71, 252,71, 253,72, 253,72, 253,72, 253,72, 254,72, 254,73, 254,73, 254,73, 255,74, 255,74, 256,74, 257,75, 258,77, 258,77, 258,78, 258,79, 259,80, 259,81, 259,81, 259,82, 259,82, 259,82, 259,83, 260,83, 260,83, 260,84, 260,84, 260,84, 260,84, 259,85, 259,85, 260,86,260,86, 261,87, 261,88, 261,88, 261,89, 261,89, 262,89, 262,89, 262,89, 262,89, 263,90, 263,90, 263,90, 264,91, 264,91, 264,91, 264,91, 264,91, 265,92, 265,92, 265,92, 266,93, 266,93, 266,93, 266,93, 266,93, 287,92, 287,92, 287,92, 287,92, 286,91, 286,91, 285,88, 285,85, 285,82, 285,80, 285,79, 285,77, 285,76, 285,75, 286,73,286,73, 286,72, 287,70, 288,67, 288,66, 288,65, 288,64, 288,64, 288,64, 287,64, 287,64, 286,65, 286,66, 285,66, 285,67, 285,67, 284,67, 284,67, 284,66, 284,64, 284,63, 284,62, 285,62, 285,61, 285,61, 285,61, 284,61, 284,61, 283,60, 283,60, 283,60, 283,60, 283,59, 283,59, 283,59, 283,59, 284,59, 284,58, 284,58, 284,58, 283,57,283,57, 282,57, 282,58, 282,58, 282,58, 281,58, 281,58, 281,58, 281,58, 281,57, 281,57, 281,57, 281,57, 281,57, 281,56, 281,56, 281,56, 281,55, 280,55, 280,54, 280,54, 279,53, 279,53, 278,53, 278,53, 277,53, 277,53, 277,53, 277,53, 277,53, 277,53, 277,52, 277,52, 277,52, 276,52, 276,52, 275,52, 274,52, 273,53, 273,53, 266,50,265,49, 264,49, 264,48, 264,48, 263,48, 263,47, 262,47, 262,46, 261,46, 261,46, 262,47, 261,47, 260,47, 259,48, 259,48, 259,47, 260,46, 260,46, 260,45, 261,45, 261,45, 261,44, 261,44, 260,44, 259,44, 258,45, 257,45, 257,46, 256,46, 255,46, 255,47, 254,46, 254,46, 254,45, 253,46, 253,46, 253,47, 252,47, 252,47, 252,47, 252,47,252,47" />
	<area shape="poly" id="MN" title="Minnesota" alt="Minnesota" href="https://www.surflocalmedia.com/MinnesotaUS/" coords="216,26, 217,29, 216,31, 216,31, 216,32, 216,33, 216,33, 216,34, 216,34, 216,35, 216,35, 216,35, 216,35, 216,36, 217,36, 217,36, 217,37, 217,37, 217,37, 218,38, 218,38, 218,38, 218,38, 218,39, 218,39, 218,40, 219,40, 219,41, 219,41, 219,43, 218,45, 218,46, 218,47, 218,48, 218,48, 219,50,219,50, 219,51, 219,51, 219,51, 219,52, 219,54, 219,54, 219,56, 220,57, 220,58, 220,58, 220,58, 220,60, 220,60, 220,61, 220,62, 220,63, 220,63, 221,64, 221,64, 221,64, 221,64, 221,64, 222,65, 222,65, 222,65, 222,65, 222,82, 242,81, 251,81, 259,81, 259,81, 259,80, 258,79, 258,78, 258,77, 257,76, 256,74, 255,74, 255,74, 254,73,254,73, 254,73, 254,72, 253,72, 253,72, 253,72, 252,71, 252,71, 251,70, 250,70, 250,70, 250,70, 250,70, 250,70, 250,70, 249,69, 249,68, 249,68, 249,68, 249,68, 249,67, 249,65, 249,63, 249,62, 249,62, 249,62, 248,61, 248,61, 248,61, 247,61, 247,61, 247,61, 247,61, 247,60, 247,60, 247,58, 247,58, 247,58, 248,57, 248,56, 248,56,248,56, 248,56, 249,56, 250,55, 251,55, 251,54, 251,54, 252,53, 252,52, 252,47, 252,47, 252,47, 252,47, 252,46, 252,45, 253,45, 254,43, 254,42, 255,41, 257,39, 260,37, 263,34, 266,33, 268,31, 267,31, 266,31, 265,31, 264,31, 263,31, 262,31, 262,31, 261,30, 261,30, 260,31, 259,31, 258,32, 257,31, 257,31, 256,31, 255,31, 254,31,254,31, 252,30, 251,29, 250,29, 250,30, 249,30, 249,29, 248,30, 248,30, 247,29, 247,28, 247,28, 246,27, 244,27, 244,27, 242,27, 241,27, 240,27, 239,27, 239,27, 239,26, 238,26, 237,26, 236,26, 234,26, 233,26, 232,26, 232,25, 232,24, 231,24, 227,24, 216,24, 216,25, 216,26" />
	<!-- color #5 -->
	<area shape="poly" id="LA" title="Louisiana" alt="Louisiana" href="https://www.surflocalmedia.com/LouisianaUS/" coords="281,219, 281,219, 281,219, 280,218, 280,218, 279,218, 279,217, 279,217, 279,216, 264,216, 265,216, 266,216, 265,215, 265,214, 266,214, 266,214, 266,214, 266,214, 266,213, 266,213, 266,213, 266,213, 266,213, 266,212, 266,212, 266,212, 265,211, 265,211, 266,211, 266,211, 266,211, 266,210,266,210, 266,210, 266,210, 266,210, 266,209, 266,209, 266,209, 266,208, 266,208, 267,208, 267,207, 267,207, 267,207, 267,207, 267,206, 267,206, 267,206, 268,206, 268,205, 268,205, 268,205, 267,205, 267,205, 267,205, 267,205, 267,205, 267,205, 266,204, 266,204, 266,204, 266,204, 266,204, 266,204, 266,204, 266,204, 266,203,266,203, 266,203, 266,203, 267,203, 267,203, 267,203, 268,203, 268,203, 268,202, 269,201, 269,201, 269,201, 269,201, 268,201, 268,201, 267,201, 267,200, 267,200, 267,200, 266,200, 266,199, 266,199, 266,199, 266,198, 266,198, 267,198, 267,198, 267,198, 267,197, 267,197, 267,197, 267,197, 267,197, 266,197, 266,196, 266,196,266,196, 266,196, 266,196, 266,195, 266,195, 266,195, 266,195, 266,195, 266,194, 266,194, 266,194, 263,194, 242,194, 242,194, 243,209, 244,210, 244,210, 245,211, 245,211, 245,211, 245,212, 245,213, 245,213, 245,213, 245,213, 245,213, 245,213, 245,214, 245,214, 246,214, 246,215, 246,215, 246,215, 246,216, 246,216, 246,216,246,216, 246,217, 245,217, 245,218, 245,218, 245,219, 245,219, 245,220, 245,220, 245,220, 245,221, 245,221, 245,222, 245,222, 245,222, 245,222, 245,222, 245,222, 245,222, 245,223, 245,224, 245,224, 245,224, 245,225, 245,225, 245,225, 245,226, 245,227, 245,227, 245,227, 245,228, 245,227, 246,227, 247,227, 249,227, 251,228,254,229, 256,229, 256,228, 255,228, 254,227, 254,226, 255,226, 255,227, 257,226, 257,226, 257,227, 258,228, 258,228, 259,229, 261,229, 261,228, 260,227, 260,227, 260,225, 260,225, 259,224, 258,223, 257,222, 256,221, 256,220, 257,221, 258,221, 259,223, 261,224, 261,225, 260,225, 261,227, 262,227, 262,228, 263,230, 265,230,266,231, 267,233, 268,233, 270,234, 271,232, 272,232, 273,232, 274,233, 275,234, 276,234, 277,234, 277,232, 278,232, 279,232, 278,230, 277,228, 274,227, 272,226, 270,225, 270,224, 273,226, 274,226, 274,225, 276,227, 278,228, 278,229, 279,229, 280,230, 281,231, 283,232, 283,232, 283,234, 283,234, 285,233, 285,234, 287,233,288,232, 289,231, 288,231, 287,230, 285,229, 283,229, 281,227, 283,227, 285,227, 286,227, 285,227, 285,226, 284,225, 284,224, 283,224, 283,223, 284,222, 283,221, 283,222, 283,222, 282,222, 281,223, 280,223, 280,223, 277,223, 277,222, 277,222, 278,221, 278,221, 278,220, 276,220, 274,221, 273,220, 273,219, 274,218, 275,218,277,219, 278,219, 280,220, 279,220, 278,221, 280,221, 281,221, 283,220, 283,220, 281,219" />
	<area shape="poly" id="AR" title="Arkansas" alt="Arkansas" href="https://www.surflocalmedia.com/ArkansasUS/" coords="275,169, 274,168, 274,168, 274,168, 274,168, 274,168, 274,167, 274,167, 274,167, 274,167, 274,167, 274,166, 274,166, 274,166, 275,165, 275,165, 275,165, 275,165, 276,164, 276,164, 276,164, 276,163, 276,163, 276,163, 276,163, 276,163, 276,163, 277,163, 277,162, 277,162, 277,162, 277,162,277,162, 277,162, 277,161, 277,161, 277,161, 277,161, 276,161, 274,161, 273,161, 273,161, 272,161, 272,161, 272,161, 272,161, 272,161, 272,160, 272,159, 273,159, 273,158, 273,158, 273,158, 274,157, 274,157, 274,157, 274,156, 274,156, 273,156, 273,156, 273,156, 273,155, 263,155, 243,156, 236,156, 236,156, 237,160, 239,164,239,164, 239,188, 240,188, 240,188, 240,188, 240,188, 240,188, 241,188, 241,188, 241,188, 241,188, 242,188, 242,189, 242,194, 266,194, 266,194, 266,193, 266,193, 266,193, 266,193, 267,193, 267,193, 267,192, 266,192, 266,192, 266,192, 266,192, 267,191, 267,191, 267,191, 267,191, 267,190, 267,190, 267,190, 266,190, 266,190,266,190, 266,190, 266,190, 266,189, 267,189, 267,189, 267,189, 267,188, 267,188, 267,188, 267,188, 266,188, 265,188, 265,188, 265,188, 265,188, 265,188, 266,187, 266,187, 267,186, 267,186, 267,186, 267,185, 267,185, 267,185, 267,185, 267,184, 267,184, 267,184, 267,184, 267,184, 267,184, 267,183, 267,183, 267,183, 268,183,269,183, 270,182, 270,182, 270,182, 270,182, 270,181, 270,181, 269,181, 269,181, 269,181, 268,181, 268,181, 268,181, 268,180, 268,180, 268,180, 269,180, 269,179, 270,179, 270,179, 270,178, 270,178, 270,178, 270,178, 270,177, 271,177, 271,177, 271,177, 271,177, 272,177, 272,176, 272,176, 272,175, 272,175, 272,175, 272,175,272,174, 272,174, 272,174, 272,173, 272,173, 272,173, 273,173, 273,172, 273,172, 273,172, 273,172, 274,172, 274,171, 274,171, 275,171, 275,171, 275,170, 275,170, 275,169, 275,169, 275,169" />
	<area shape="poly" id="TX" title="Texas" alt="Texas" href="https://www.surflocalmedia.com/TexasUS/" coords="245,227, 245,226, 245,225, 245,225, 245,225, 245,224, 245,224, 245,224, 245,223, 245,222, 245,222, 245,222, 245,222, 245,222, 245,221, 245,220, 245,220, 245,220, 245,219, 245,219, 245,218, 245,218, 245,217, 246,217, 246,216, 246,216, 246,215, 246,215, 246,214, 245,214, 245,214, 245,213,245,213, 245,213, 245,213, 245,212, 245,211, 245,211, 245,211, 244,210, 244,210, 243,209, 242,194, 242,194, 242,189, 242,188, 241,188, 241,188, 241,188, 240,188, 240,188, 240,188, 240,188, 239,188, 239,188, 237,187, 237,187, 234,186, 233,186, 232,185, 230,185, 229,185, 229,185, 228,185, 227,185, 227,185, 227,185, 226,185,225,186, 225,186, 224,186, 224,187, 223,187, 222,187, 221,188, 221,188, 221,187, 220,187, 220,187, 220,187, 220,186, 219,185, 218,185, 218,185, 218,185, 218,185, 217,185, 217,185, 216,186, 216,186, 216,186, 215,186, 215,186, 215,186, 214,186, 214,186, 214,187, 213,188, 213,188, 213,188, 212,187, 212,187, 212,186, 212,186,211,186, 211,186, 211,186, 211,186, 210,186, 210,186, 209,185, 208,186, 207,186, 207,185, 207,185, 206,185, 206,185, 206,184, 206,184, 206,184, 206,184, 205,184, 204,184, 203,184, 202,184, 202,184, 202,184, 202,183, 202,183, 202,183, 201,183, 200,183, 200,183, 199,183, 198,183, 198,183, 197,183, 197,183, 197,183, 197,182,197,182, 197,182, 196,181, 196,181, 196,180, 195,180, 194,180, 194,180, 194,180, 194,180, 194,181, 194,180, 193,180, 193,180, 193,179, 193,179, 192,179, 192,179, 192,179, 191,179, 191,158, 191,158, 176,158, 176,158, 175,158, 166,158, 166,158, 163,201, 126,201, 126,204, 126,205, 128,208, 129,209, 130,211, 132,213, 133,214,135,217, 136,220, 137,222, 138,223, 139,227, 141,228, 147,231, 151,232, 153,233, 154,233, 156,233, 158,235, 159,235, 160,233, 162,231, 162,230, 163,227, 164,226, 165,226, 168,227, 170,227, 172,227, 174,228, 175,229, 177,229, 178,230, 180,232, 182,234, 182,236, 184,240, 185,243, 187,244, 188,248, 189,251, 191,253, 192,254,194,258, 194,260, 196,262, 198,263, 200,264, 201,265, 202,266, 204,266, 205,267, 207,267, 210,269, 213,270, 213,269, 212,268, 212,267, 211,267, 212,267, 212,267, 210,261, 209,257, 209,255, 208,254, 208,254, 210,254, 211,253, 211,251, 210,250, 209,250, 209,249, 210,249, 212,249, 213,247, 211,247, 211,246, 213,246, 213,245,213,245, 213,246, 213,247, 214,247, 216,245, 216,245, 215,243, 216,243, 216,243, 217,244, 217,243, 219,241, 219,240, 218,240, 216,239, 216,238, 217,238, 218,239, 220,239, 221,238, 221,239, 221,239, 222,239, 225,239, 225,240, 223,242, 226,241, 229,239, 231,237, 232,234, 233,232, 234,231, 233,231, 232,230, 231,228, 232,228,234,227, 235,227, 235,229, 236,229, 237,229, 237,230, 236,230, 236,231, 236,231, 237,230, 242,228, 245,228, 245,227, 245,227, 245,227" />
	<area shape="poly" id="OK" title="Oklahoma" alt="Oklahoma" href="https://www.surflocalmedia.com/OklahomaUS/" coords="239,164, 237,160, 236,156, 236,156, 236,156, 236,152, 211,152, 200,151, 187,151, 180,151, 177,151, 175,151, 175,151, 166,151, 166,151, 166,158, 175,158, 176,158, 176,158, 191,158, 191,158, 191,179, 192,179, 192,179, 192,179, 192,179, 193,179, 193,179, 193,180, 193,180, 193,180, 193,180,194,180, 194,180, 194,180, 194,180, 194,180, 194,180, 194,180, 195,180, 196,180, 196,180, 196,181, 196,181, 197,182, 197,182, 197,182, 197,182, 197,183, 197,183, 198,183, 198,183, 198,183, 199,183, 200,183, 200,183, 200,183, 201,183, 202,183, 202,183, 202,183, 202,183, 202,184, 202,184, 202,184, 203,184, 204,184, 205,184,205,184, 206,184, 206,184, 206,184, 206,184, 206,184, 206,185, 206,185, 206,185, 207,185, 207,185, 207,185, 207,186, 208,186, 209,185, 210,186, 210,186, 210,186, 211,186, 211,186, 211,186, 211,186, 212,186, 212,186, 212,187, 212,187, 212,187, 213,188, 213,188, 214,187, 214,186, 214,186, 214,186, 215,186, 215,186, 215,186,215,186, 215,186, 216,186, 217,185, 217,185, 217,185, 218,185, 218,185, 218,185, 218,185, 218,185, 219,185, 220,186, 220,187, 220,187, 221,187, 221,188, 221,188, 222,187, 223,187, 224,187, 224,186, 225,186, 225,186, 225,186, 226,185, 227,185, 227,185, 227,185, 227,185, 228,185, 228,185, 228,185, 229,185, 229,185, 230,185,232,185, 233,186, 234,186, 237,187, 237,187, 238,187, 239,188, 239,188, 239,164, 239,164" />
	<area shape="poly" id="NM" title="New Mexico" alt="New Mexico" href="https://www.surflocalmedia.com/New-MexicoUS/" coords="166,151, 166,151, 163,151, 162,150, 158,150, 150,150, 142,149, 139,149, 132,148, 124,148, 121,147, 113,146, 113,146, 107,194, 105,207, 110,207, 111,203, 126,204, 126,201, 163,201, 166,151" />
	<!-- color #4 -->
	<area shape="poly" id="KS" title="Kansas" alt="Kansas" href="https://www.surflocalmedia.com/KansasUS/" coords="235,130, 235,129, 235,129, 235,129, 235,129, 235,129, 235,129, 235,128, 234,128, 234,128, 233,128, 233,127, 233,127, 233,127, 233,127, 233,126, 233,126, 233,126, 233,126, 233,126, 232,125, 232,125, 232,125, 231,125, 231,125, 232,124, 232,124, 232,124, 232,124, 233,124, 233,123, 233,123,232,123, 232,123, 232,123, 232,123, 232,122, 232,122, 232,122, 232,122, 231,122, 230,122, 230,122, 230,120, 221,120, 209,120, 191,120, 179,119, 177,119, 177,119, 175,151, 175,151, 177,151, 180,151, 192,151, 200,151, 211,152, 236,152, 235,130, 235,130" />
	<area shape="poly" id="MO" title="Missouri" alt="Missouri" href="https://www.surflocalmedia.com/MissouriUS/" coords="260,116, 260,115, 259,115, 259,115, 259,114, 258,114, 258,114, 258,113, 258,113, 257,113, 257,113, 241,113, 235,113, 229,113, 229,113, 229,113, 229,113, 229,114, 229,115, 229,115, 229,116, 230,117, 229,117, 229,118, 229,118, 230,119, 230,119, 230,120, 230,120, 230,121, 230,122, 231,122,231,122, 232,122, 232,122, 232,122, 232,122, 232,123, 232,123, 232,123, 232,123, 232,123, 233,123, 233,123, 233,124, 232,124, 232,124, 232,124, 232,124, 231,125, 231,125, 232,125, 232,125, 232,125, 233,126, 233,126, 233,126, 233,126, 233,126, 233,126, 233,127, 233,127, 233,127, 233,127, 233,128, 234,128, 234,128, 234,128,235,128, 235,129, 235,129, 235,129, 235,129, 235,129, 235,129, 235,129, 235,130, 236,152, 236,153, 236,156, 243,156, 263,155, 273,155, 273,156, 273,156, 274,156, 274,156, 274,157, 274,157, 274,157, 273,158, 273,158, 273,159, 272,159, 272,160, 272,161, 272,161, 272,161, 272,161, 273,161, 276,161, 277,161, 277,161, 277,161,277,161, 277,160, 277,160, 277,160, 277,160, 277,159, 277,159, 277,159, 277,159, 277,159, 277,159, 278,158, 278,158, 278,158, 278,158, 278,157, 278,157, 278,157, 278,156, 278,156, 278,156, 278,156, 278,155, 278,155, 278,155, 278,155, 279,154, 280,154, 281,154, 281,154, 281,154, 281,153, 281,152, 281,152, 282,152, 282,152,282,152, 282,151, 282,151, 282,150, 281,150, 281,149, 281,149, 281,149, 281,149, 281,149, 281,150, 281,150, 281,150, 281,150, 280,150, 280,150, 280,150, 280,150, 280,150, 280,149, 280,149, 279,149, 279,148, 278,148, 278,148, 278,147, 279,147, 279,146, 279,146, 279,146, 278,145, 278,145, 277,144, 277,144, 277,144, 277,143,276,143, 276,143, 276,143, 276,142, 276,141, 275,141, 274,140, 274,140, 272,139, 271,138, 271,138, 271,138, 270,138, 270,138, 270,138, 270,137, 270,137, 270,136, 270,136, 270,136, 270,136, 271,136, 271,136, 271,135, 271,135, 271,134, 271,134, 272,133, 272,133, 272,133, 272,133, 272,132, 272,132, 272,131, 271,130, 271,129,270,129, 270,129, 269,129, 269,129, 268,129, 268,129, 268,130, 268,130, 268,130, 268,130, 268,130, 268,130, 268,130, 267,130, 267,130, 267,129, 266,129, 266,128, 266,128, 266,127, 266,127, 266,126, 266,126, 266,126, 266,125, 266,125, 265,125, 265,124, 265,124, 264,124, 264,124, 263,123, 263,123, 263,122, 263,122, 263,122,262,122, 262,121, 262,121, 261,120, 261,120, 261,120, 261,120, 261,119, 261,119, 261,119, 261,118, 261,118, 261,118, 261,118, 261,118, 261,117, 261,117, 260,117, 260,116" />
	<area shape="poly" id="IA" title="Iowa" alt="Iowa" href="https://www.surflocalmedia.com/IowaUS/" coords="221,82, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83, 221,84, 221,84, 221,84, 221,84, 221,84, 221,84, 220,85, 220,85, 220,85, 220,85, 221,85, 221,86, 221,86, 221,86, 221,86, 222,86, 222,86, 222,86, 222,87, 222,87, 222,87, 222,88, 222,88, 222,89, 222,89,222,89, 222,89, 222,90, 222,90, 222,91, 222,91, 222,91, 222,91, 222,91, 222,92, 222,94, 222,95, 222,96, 222,96, 222,96, 222,96, 222,96, 222,96, 222,97, 223,97, 223,97, 223,98, 223,98, 223,98, 223,98, 223,99, 223,99, 223,99, 224,99, 224,100, 224,100, 224,100, 224,101, 225,102, 225,102, 225,103, 226,103, 226,104, 226,104,226,104, 226,104, 226,105, 226,105, 226,105, 226,105, 226,106, 227,107, 227,107, 227,108, 227,108, 228,108, 228,108, 228,108, 228,109, 228,109, 228,109, 228,109, 228,109, 228,110, 227,110, 227,110, 228,111, 228,112, 228,112, 228,112, 228,112, 228,112, 228,112, 229,113, 229,113, 229,113, 230,113, 238,113, 241,113, 257,113,257,113, 258,113, 258,113, 258,114, 258,114, 259,114, 259,115, 259,115, 260,115, 260,116, 260,116, 260,115, 260,115, 260,115, 260,115, 260,114, 260,113, 261,113, 261,112, 262,112, 262,112, 262,111, 262,111, 262,111, 263,111, 263,110, 263,110, 263,110, 263,109, 263,109, 263,108, 263,108, 263,107, 263,106, 262,106, 262,106,262,105, 262,105, 262,104, 263,104, 263,103, 263,103, 264,103, 265,102, 265,102, 266,102, 266,102, 267,102, 267,101, 268,101, 268,101, 268,100, 268,100, 268,100, 268,100, 268,99, 268,98, 268,98, 268,97, 268,97, 268,97, 268,96, 268,96, 267,96, 267,95, 267,94, 266,94, 266,94, 266,93, 266,93, 266,93, 266,93, 266,93, 266,93,265,92, 265,92, 265,92, 264,91, 264,91, 264,91, 264,91, 264,91, 263,90, 263,90, 263,90, 262,89, 262,89, 262,89, 261,89, 261,89, 261,89, 261,88, 261,88, 261,87, 260,86, 259,85, 259,85, 259,85, 259,85, 260,84, 260,84, 260,84, 260,83, 259,83, 259,82, 259,82, 259,82, 259,82, 259,81, 259,81, 251,81, 242,81, 221,82, 221,82" />
	<area shape="poly" id="NE" title="Nebraska" alt="Nebraska" href="https://www.surflocalmedia.com/NebraskaUS/" coords="179,119, 179,119, 191,120, 209,120, 221,120, 230,120, 230,120, 230,120, 230,119, 230,119, 229,118, 229,118, 229,118, 229,117, 230,117, 229,116, 229,115, 229,115, 229,114, 229,113, 229,113, 229,113, 229,113, 228,112, 228,112, 228,112, 228,112, 228,112, 228,112, 228,112, 228,111, 227,110,227,110, 228,110, 228,109, 228,109, 228,109, 228,109, 228,108, 228,108, 227,108, 227,108, 227,107, 226,106, 226,105, 226,105, 226,105, 226,105, 226,104, 226,104, 226,104, 226,103, 225,103, 224,100, 224,100, 224,100, 224,100, 223,99, 223,99, 223,99, 223,99, 223,99, 223,98, 223,98, 223,97, 222,97, 222,96, 222,96, 222,96, 222,96,222,96, 222,96, 221,95, 221,95, 220,94, 220,94, 219,94, 218,94, 218,94, 217,94, 217,93, 216,93, 215,93, 215,93, 215,92, 214,92, 213,92, 212,92, 212,92, 212,92, 211,92, 210,92, 209,91, 209,91, 209,91, 208,91, 208,91, 207,91, 207,91, 206,91, 206,91, 206,91, 205,91, 205,90, 205,90, 205,90, 204,89, 203,88, 203,88, 202,88, 195,88,180,88, 175,88, 172,88, 164,87, 162,108, 162,108, 163,108, 177,109, 177,119, 179,119" />
	<!-- color #3 -->
	<area shape="poly" id="SD" title="South Dakota" alt="South Dakota" href="https://www.surflocalmedia.com/South-DakotaUS/" coords="164,87, 165,87, 170,88, 175,88, 180,88, 195,88, 202,88, 203,88, 203,88, 204,89, 205,90, 205,90, 205,91, 206,91, 206,91, 207,91, 207,91, 208,91, 208,91, 209,91, 209,91, 209,91, 209,91, 210,92, 211,92, 212,92, 212,92, 213,92, 214,92, 215,92, 215,93, 216,93, 217,93, 217,94, 218,94, 218,94,219,94, 220,94, 220,94, 221,95, 221,95, 222,96, 222,95, 222,94, 222,92, 222,91, 222,91, 222,91, 222,90, 222,90, 222,89, 222,89, 222,89, 222,88, 222,88, 222,87, 222,87, 222,86, 222,86, 221,86, 221,86, 221,86, 221,85, 220,85, 220,85, 220,85, 221,84, 221,84, 221,84, 221,84, 221,84, 221,83, 221,83, 221,83, 221,83, 221,83, 221,83,221,83, 221,82, 222,82, 222,82, 222,82, 222,66, 222,65, 222,65, 222,65, 222,64, 221,64, 221,64, 221,64, 220,63, 220,63, 220,62, 220,60, 220,60, 219,60, 209,59, 195,58, 191,58, 188,58, 174,57, 167,57, 166,57, 166,65, 164,86, 164,87" />
	<area shape="poly" id="ND" title="North Dakota" alt="North Dakota" href="https://www.surflocalmedia.com/North-DakotaUS/" coords="167,57, 188,58, 191,58, 195,58, 219,60, 220,60, 220,58, 220,58, 220,57, 219,56, 219,54, 219,54, 219,54, 219,52, 219,51, 219,51, 219,51, 219,50, 218,48, 218,48, 218,47, 218,46, 218,43, 219,41, 218,40, 218,39, 218,39, 218,38, 218,38, 218,38, 217,37, 217,37, 217,37, 217,36, 217,36, 216,36,216,35, 216,35, 216,35, 216,35, 216,34, 216,34, 216,33, 216,33, 216,32, 216,31, 216,31, 216,29, 216,28, 216,26, 216,25, 216,24, 211,24, 202,24, 189,24, 181,24, 173,23, 170,23, 168,35, 166,57, 167,57" />
	<area shape="poly" id="CO" title="Colorado" alt="Colorado" href="https://www.surflocalmedia.com/ColoradoUS/" coords="166,151, 166,151, 175,151, 177,109, 163,108, 162,108, 162,108, 159,108, 147,107, 142,107, 135,106, 132,106, 124,105, 120,105, 119,105, 119,105, 119,106, 119,107, 118,108, 113,146, 120,147, 124,148, 132,148, 142,149, 150,150, 158,150, 163,151, 166,151, 166,151, 166,151" />
	<area shape="poly" id="UT" title="Utah" alt="Utah" href="https://www.surflocalmedia.com/UtahUS/" coords="119,106, 119,105, 119,105, 118,105, 117,104, 114,104, 109,103, 101,102, 103,92, 99,91, 92,90, 91,90, 86,89, 82,89, 82,89, 72,140, 73,140, 76,140, 90,143, 90,143, 95,144, 101,145, 108,146, 113,146, 119,107, 119,106" />
	<area shape="poly" id="WY" title="Wyoming" alt="Wyoming" href="https://www.surflocalmedia.com/WyomingUS/" coords="101,102, 105,103, 109,103, 114,104, 117,104, 120,105, 124,105, 132,106, 142,107, 147,107, 159,108, 162,108, 164,87, 164,86, 166,67, 159,66, 156,66, 153,66, 143,66, 143,66, 141,66, 133,65, 120,64, 118,64, 117,63, 108,62, 108,62, 107,67, 107,67, 105,75, 105,77, 105,80, 104,84, 104,85, 103,89,103,91, 101,102, 101,102" />
	<area shape="poly" id="MT" title="Montana" alt="Montana" href="https://www.surflocalmedia.com/MontanaUS/" coords="80,26, 80,27, 80,29, 80,30, 81,30, 81,31, 80,32, 80,32, 80,33, 80,33, 80,33, 81,33, 81,34, 82,35, 82,35, 82,35, 82,36, 83,38, 83,38, 83,39, 84,41, 85,41, 85,41, 85,42, 86,42, 86,42, 86,43, 86,43, 86,44, 86,44, 86,44, 86,44, 86,45, 86,45, 85,45, 85,46, 84,47, 84,47, 84,47, 84,48, 84,49,84,51, 85,51, 85,52, 85,52, 85,52, 86,52, 86,52, 86,52, 86,52, 86,52, 86,52, 87,52, 87,52, 87,52, 87,53, 87,53, 88,53, 88,54, 88,54, 88,54, 88,55, 89,56, 90,57, 90,58, 90,58, 90,59, 91,60, 91,60, 91,61, 91,62, 92,63, 92,63, 92,63, 93,63, 93,63, 94,64, 94,64, 95,64, 96,65, 96,65, 97,65, 97,65, 97,65, 97,65, 98,64, 98,64,99,64, 100,65, 100,65, 100,65, 101,65, 102,65, 102,65, 103,65, 103,65, 103,65, 103,65, 104,65, 104,65, 104,65, 104,65, 104,65, 104,65, 105,66, 105,66, 106,67, 106,67, 106,67, 106,67, 106,67, 106,67, 107,67, 107,67, 108,62, 108,62, 117,63, 120,64, 133,65, 141,66, 143,66, 153,66, 155,66, 159,66, 166,67, 166,65, 166,57, 168,35,168,35, 170,23, 152,22, 139,21, 125,19, 108,17, 91,15, 83,13, 82,13, 80,26, 80,26" />
	<!-- color #2 -->
	<area shape="poly" id="H1" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="7,182, 4,183, 4,184, 4,185, 4,185, 5,185, 6,186, 7,186, 9,186, 9,185, 9,184, 10,183, 9,182, 7,182" />
	<area shape="poly" id="H2" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="20,189, 21,189, 21,188, 21,187, 20,186, 18,185, 18,184, 17,184, 17,185, 15,186, 14,186, 15,186, 16,188, 17,189, 17,189, 18,189, 19,189, 20,189, 20,189" />
	<area shape="poly" id="H3" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="30,190, 31,190, 33,190, 33,189, 33,189, 30,189, 28,189, 27,189, 26,189, 25,190, 25,191, 25,192, 26,191, 28,191, 30,190" />
	<area shape="poly" id="H4" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="30,192, 29,193, 29,193, 30,193, 30,194, 31,195, 32,195, 32,194, 32,193, 32,192, 30,192" />
	<area shape="poly" id="H5" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="35,196, 34,196, 33,197, 33,198, 35,197, 36,197, 36,197, 36,197, 35,196, 34,196" />
	<area shape="poly" id="H6" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="39,192, 37,191, 36,191, 35,191, 34,191, 34,191, 33,192, 35,193, 36,194, 37,195, 38,196, 40,195, 41,194, 41,193, 39,192" />
	<area shape="poly" id="H7" title="Hawaii" alt="Hawaii" href="https://www.surflocalmedia.com/HawaiiUS/" coords="53,204, 53,203, 51,202, 48,200, 44,199, 43,200, 44,202, 44,203, 42,204, 42,205, 42,207, 43,207, 43,209, 43,212, 43,213, 45,214, 47,216, 48,214, 50,212, 54,209, 56,208, 56,207, 54,205, 53,204" />
	<area shape="poly" id="NV" title="Nevada" alt="Nevada" href="https://www.surflocalmedia.com/NevadaUS/" coords="79,88, 77,88, 69,86, 60,84, 58,83, 58,83, 53,82, 52,82, 45,80, 37,78, 37,79, 31,108, 64,160, 64,160, 64,158, 64,157, 65,156, 65,156, 65,155, 65,154, 65,153, 65,151, 65,151, 65,150, 65,150, 65,150, 65,150, 65,150, 65,149, 65,149, 65,149, 65,149, 66,148, 66,149, 66,149, 66,149, 67,149, 67,149,67,149, 67,149, 67,150, 67,150, 67,150, 68,150, 69,150, 69,150, 70,150, 70,149, 70,149, 72,140, 72,140, 82,89, 79,88" />
	<area shape="poly" id="CA" title="California" alt="California" href="https://www.surflocalmedia.com/CaliforniaUS/" coords="59,183, 60,183, 60,182, 60,182, 61,182, 61,182, 61,182, 61,182, 61,181, 61,181, 60,181, 60,180, 60,180, 59,180, 59,180, 59,180, 59,180, 59,180, 59,179, 59,179, 60,179, 60,179, 60,179, 60,178, 61,178, 61,178, 61,176, 61,176, 61,175, 61,174, 62,173, 62,173, 62,172, 63,171, 63,170, 63,170,64,169, 65,169, 66,169, 66,168, 67,168, 66,168, 66,167, 66,167, 66,167, 66,167, 65,165, 64,165, 64,165, 64,165, 64,164, 64,164, 64,164, 64,163, 64,161, 64,161, 64,160, 64,160, 64,160, 64,160, 31,108, 37,79, 37,78, 23,74, 8,70, 7,70, 7,70, 7,71, 6,74, 5,77, 4,80, 4,81, 4,81, 3,81, 3,81, 3,80, 2,79, 2,79, 2,80, 1,81, 1,84,1,85, 1,86, 1,87, 1,88, 2,88, 3,90, 3,91, 3,92, 2,94, 2,96, 2,98, 2,99, 3,101, 3,102, 3,103, 4,104, 4,105, 5,106, 5,107, 4,108, 4,108, 4,108, 4,110, 4,110, 5,110, 5,111, 5,112, 5,113, 6,113, 7,114, 7,114, 8,113, 8,113, 8,112, 8,111, 8,110, 8,110, 8,110, 9,110, 10,110, 11,111, 12,111, 12,112, 12,113, 12,113, 11,113, 10,113,10,113, 10,114, 11,114, 11,115, 11,116, 11,116, 11,118, 11,118, 10,118, 10,117, 9,117, 8,116, 8,116, 7,116, 7,117, 8,118, 8,120, 8,122, 9,123, 10,125, 11,126, 11,126, 10,127, 8,128, 8,128, 7,129, 7,129, 8,130, 8,131, 8,132, 8,133, 8,134, 9,135, 10,135, 11,136, 11,138, 11,139, 14,143, 15,144, 15,146, 15,147, 14,149, 14,150,14,152, 15,152, 15,153, 17,153, 18,154, 19,154, 23,158, 25,159, 25,160, 28,162, 30,163, 30,164, 30,164, 31,165, 32,166, 33,167, 34,169, 34,170, 35,171, 36,173, 37,178, 36,178, 36,180, 58,182, 58,182, 58,183, 58,183, 59,183, 59,183" />
	<area shape="poly" id="AZ" title="Arizona" alt="Arizona" href="https://www.surflocalmedia.com/ArizonaUS/" coords="113,146, 113,146, 108,146, 101,145, 95,144, 90,143, 88,142, 81,142, 73,140, 72,140, 72,140, 70,149, 70,149, 70,150, 70,150, 69,150, 69,150, 69,150, 68,150, 67,150, 67,150, 67,150, 67,149, 67,149, 67,149, 66,149, 66,149, 66,149, 66,149, 66,149, 65,149, 65,149, 65,149, 65,149, 65,150, 65,150,65,150, 65,150, 65,151, 65,151, 65,151, 65,153, 65,154, 65,154, 65,154, 65,155, 65,156, 65,156, 64,157, 64,158, 64,160, 64,160, 64,160, 64,160, 64,160, 64,160, 64,161, 64,161, 64,161, 64,164, 64,164, 64,164, 64,165, 64,165, 65,165, 66,167, 66,167, 66,167, 66,167, 66,168, 67,168, 66,168, 66,169, 65,169, 64,169, 63,170, 63,170,63,170, 63,171, 62,172, 62,173, 62,173, 62,173, 61,174, 61,175, 61,175, 61,176, 61,176, 61,178, 61,178, 61,178, 60,178, 60,179, 60,179, 60,179, 59,179, 59,180, 59,180, 59,180, 59,180, 60,180, 60,180, 60,181, 61,181, 61,181, 61,182, 61,182, 61,182, 61,182, 61,182, 61,182, 60,182, 60,182, 60,183, 59,183, 59,183, 59,183, 58,183,58,184, 58,184, 87,204, 105,207, 107,194, 113,146, 113,146" />
	<!-- color #1 -->
	<area shape="poly" id="A1" title="Alaska" alt="Alaska" href="https://www.surflocalmedia.com/AlaskaUS/" coords="133,269, 131,268, 128,268, 120,263, 118,262, 116,261, 115,262, 114,264, 113,264, 113,264, 112,263, 110,262, 109,260, 107,261, 106,261, 105,260, 103,229, 103,229, 101,228, 100,228, 99,228, 98,229, 97,228, 95,227, 94,226, 93,226, 93,225, 90,223, 90,222, 88,223, 87,222, 85,223, 84,223, 82,224,80,226, 78,226, 77,225, 76,227, 76,228, 77,230, 76,232, 78,233, 77,235, 79,236, 77,236, 76,236, 76,236, 75,234, 75,234, 75,233, 74,233, 73,232, 72,233, 71,232, 70,232, 69,233, 69,233, 69,234, 69,234, 68,236, 68,236, 68,237, 69,238, 70,238, 71,239, 72,240, 73,240, 75,240, 76,240, 74,240, 74,242, 74,243, 73,243, 72,243, 71,243,70,244, 69,243, 68,242, 68,242, 66,242, 65,243, 65,244, 62,244, 62,246, 62,246, 62,248, 62,249, 61,248, 61,249, 62,250, 61,251, 62,252, 64,253, 65,253, 64,254, 64,254, 63,257, 63,257, 64,258, 66,258, 66,258, 68,260, 68,261, 69,260, 70,260, 70,261, 72,261, 71,262, 69,264, 69,265, 66,266, 61,266, 60,267, 60,267, 62,268, 64,268,66,268, 67,267, 71,267, 75,266, 78,266, 79,265, 81,264, 80,263, 79,262, 80,262, 84,260, 85,259, 85,260, 84,261, 84,262, 84,263, 84,264, 87,263, 91,262, 91,262, 93,260, 94,259, 95,261, 96,261, 98,261, 99,262, 100,263, 102,263, 105,263, 107,264, 108,263, 111,265, 116,267, 116,266, 116,265, 117,265, 117,266, 117,267, 117,267,118,268, 123,273, 124,273, 125,273, 125,272, 126,272, 127,274, 129,275, 130,275, 133,274, 134,273, 134,270, 133,269" />
	<area shape="poly" id="A2" title="Alaska" alt="Alaska" href="https://www.surflocalmedia.com/AlaskaUS/" coords="81,265, 80,266, 79,267, 78,268, 77,267, 76,268, 76,269, 76,270, 78,270, 78,269, 81,269, 82,268, 82,267, 82,266, 83,266, 82,265, 81,265" />
	<area shape="poly" id="A3" title="Alaska" alt="Alaska" href="https://www.surflocalmedia.com/AlaskaUS/" coords="58,265, 57,265, 56,265, 54,265, 52,265, 48,264, 48,264, 48,264, 48,265, 49,265, 51,266, 51,266, 53,266, 53,266, 56,267, 57,267, 58,267, 59,267, 60,267, 60,266, 59,265, 58,265" />
	<area shape="poly" id="ID" title="Idaho" alt="Idaho" href="https://www.surflocalmedia.com/IdahoUS/" coords="69,39, 68,40, 68,42, 68,42, 68,43, 68,43, 68,44, 69,44, 69,44, 69,44, 69,44, 70,45, 70,45, 70,46, 70,46, 70,47, 70,47, 70,48, 70,49, 69,50, 68,52, 68,52, 66,54, 65,55, 65,55, 64,55, 64,56, 64,56, 64,57, 63,58, 63,58, 63,60, 63,62, 63,62, 63,63, 63,64, 63,65, 63,65, 63,65, 63,66, 62,68,58,83, 58,83, 58,83, 60,84, 69,86, 77,88, 79,88, 82,89, 82,89, 86,89, 91,90, 98,91, 103,92, 103,91, 103,89, 103,89, 104,86, 104,85, 104,84, 104,83, 104,81, 105,80, 105,77, 105,76, 105,75, 107,67, 106,67, 106,67, 106,67, 106,67, 106,67, 106,67, 105,66, 105,66, 104,66, 104,65, 104,65, 104,65, 104,65, 104,65, 103,65, 103,65,103,65, 102,65, 102,65, 101,65, 100,65, 100,65, 100,65, 99,64, 98,64, 98,64, 97,65, 97,65, 97,65, 97,65, 97,65, 96,65, 96,65, 96,65, 94,64, 94,64, 93,63, 93,63, 92,63, 92,63, 92,63, 92,63, 91,62, 91,61, 91,60, 91,60, 90,59, 90,58, 90,57, 90,57, 89,56, 88,55, 88,54, 88,54, 88,53, 87,53, 87,53, 87,53, 87,52, 86,52, 86,52,86,52, 86,52, 86,52, 85,52, 85,52, 85,52, 85,52, 85,51, 84,51, 84,49, 84,48, 84,47, 84,47, 84,47, 84,46, 85,45, 86,45, 86,44, 86,44, 86,44, 86,43, 86,43, 86,42, 85,42, 85,41, 84,41, 83,39, 83,38, 83,38, 82,37, 82,36, 82,35, 82,35, 81,34, 81,33, 80,33, 80,33, 80,32, 80,32, 81,31, 81,30, 80,29, 80,29, 80,29, 80,27, 80,27,80,26, 80,26, 82,13, 79,12, 76,12, 76,12, 75,12, 69,36, 69,39" />
	<area shape="poly" id="WA" title="Washington" alt="Washington" href="https://www.surflocalmedia.com/WashingtonUS/" coords="22,28, 23,28, 23,28, 23,28, 23,28, 24,28, 24,28, 24,29, 25,29, 25,30, 25,30, 26,30, 26,30, 26,30, 27,31, 27,31, 27,31, 27,31, 27,32, 27,32, 27,32, 27,33, 27,34, 27,34, 27,34, 27,34, 27,34, 28,35, 28,36, 28,36, 28,36, 28,36, 28,36, 28,37, 28,37, 29,37, 29,37, 29,38, 29,38, 30,38, 30,38,30,38, 30,38, 31,38, 32,38, 33,38, 34,38, 34,38, 34,38, 35,38, 35,38, 35,38, 35,37, 36,37, 36,38, 36,38, 37,38, 37,38, 37,38, 38,38, 38,38, 39,38, 40,38, 40,39, 40,39, 40,39, 41,39, 41,39, 41,39, 41,39, 42,40, 42,40, 42,40, 42,40, 43,40, 43,41, 43,41, 44,41, 45,41, 47,41, 48,41, 48,41, 48,41, 48,41, 49,41, 50,42, 51,42,52,41, 52,41, 53,41, 53,41, 53,41, 53,40, 54,40, 54,40, 54,40, 54,41, 54,41, 55,41, 55,41, 55,41, 56,41, 57,42, 58,42, 59,42, 60,42, 61,42, 62,42, 62,42, 62,42, 63,42, 63,42, 63,42, 64,43, 64,43, 65,43, 65,43, 66,43, 67,43, 67,43, 68,43, 68,42, 68,42, 68,40, 68,40, 69,36, 75,12, 72,11, 63,9, 56,7, 46,4, 39,2, 37,1, 37,2,37,2, 37,3, 38,4, 39,4, 39,4, 38,6, 37,6, 37,7, 37,8, 38,9, 38,9, 38,11, 38,11, 37,13, 36,15, 36,15, 35,16, 34,16, 34,16, 34,15, 35,14, 35,14, 35,13, 35,12, 35,11, 35,10, 34,10, 34,10, 34,10, 33,9, 33,9, 32,9, 31,9, 31,9, 30,8, 30,8, 28,8, 26,7, 25,7, 25,6, 24,6, 23,5, 23,5, 23,5, 22,5, 22,6, 22,7, 22,9, 22,10, 22,11, 22,13,22,15, 22,15, 23,16, 23,17, 23,18, 23,18, 24,19, 25,19, 25,19, 24,20, 24,20, 24,20, 23,21, 23,21, 23,21, 22,21, 22,21, 22,22, 22,22, 23,22, 24,23, 24,23, 24,23, 24,24, 24,24, 24,24, 24,24, 23,24, 23,24, 23,24, 22,24, 22,25, 22,25, 22,26, 22,27, 22,28, 22,28, 22,28" />
	<area shape="poly" id="OR" title="Oregon" alt="Oregon" href="https://www.surflocalmedia.com/OregonUS/" coords="23,74, 37,78, 53,82, 58,83, 58,83, 58,83, 62,68, 63,66, 63,65, 63,65, 63,65, 63,64, 63,63, 63,62, 63,62, 63,62, 63,60, 63,58, 63,58, 64,57, 64,56, 64,55, 65,55, 67,53, 67,52, 68,52, 69,50, 70,49, 70,48, 70,47, 70,47, 70,46, 70,45, 70,45, 69,44, 69,44, 69,44, 69,44, 68,44, 68,43, 67,43,66,43, 65,43, 64,43, 64,43, 64,43, 63,42, 63,42, 62,42, 62,42, 61,42, 61,42, 60,42, 59,42, 58,42, 57,42, 56,41, 55,41, 55,41, 54,41, 54,41, 54,40, 54,40, 53,40, 53,41, 53,41, 53,41, 53,41, 52,41, 51,42, 50,42, 49,41, 48,41, 48,41, 47,41, 45,41, 44,41, 43,41, 43,41, 43,40, 42,40, 42,40, 42,40, 42,40, 42,40, 41,39, 41,39,41,39, 40,39, 40,39, 40,38, 39,38, 38,38, 38,38, 37,38, 36,38, 36,38, 36,38, 35,38, 35,38, 35,38, 34,38, 34,38, 34,38, 33,38, 32,38, 31,38, 30,38, 30,38, 30,38, 29,38, 29,38, 29,37, 28,37, 28,37, 28,36, 28,36, 28,36, 28,36, 28,36, 28,35, 27,34, 27,34, 27,34, 27,34, 27,33, 27,33, 27,32, 27,32, 27,32, 27,31, 27,31, 26,30,26,30, 25,30, 25,29, 24,29, 24,28, 24,28, 23,28, 23,28, 23,28, 22,28, 22,28, 22,28, 22,28, 22,30, 21,31, 20,33, 20,34, 20,34, 20,35, 20,36, 21,36, 21,37, 21,37, 20,37, 20,38, 19,38, 18,38, 18,39, 17,40, 16,42, 16,44, 15,46, 14,46, 14,47, 14,48, 13,49, 13,50, 13,50, 12,53, 11,54, 11,55, 10,56, 10,56, 9,57, 8,57, 7,58, 7,58,7,59, 7,60, 7,64, 7,65, 7,66, 7,67, 7,68, 7,70, 7,70, 8,70, 23,74" />
	<!-- mutliple area selectors -->
	<area shape="circle" id="col1" rel="ID,WA,OR,A1,A2,A3" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="168,8,8" />
	<area shape="circle" id="col2" rel="NV,CA,AZ,H1,H2,H3,H4,H5,H6,H7" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="192,8,8" />
	<area shape="circle" id="col3" rel="SD,ND,CO,UT,WY,MT" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="216,8,8" />
	<area shape="circle" id="col4" rel="LA,AR,TX,OK,NM" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="240,8,8" />
	<area shape="circle" id="col5" rel="KS,MO,IA,NE" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="264,8,8" />
	<area shape="circle" id="col6" rel="OH,IL,IN,I2,MI,WI,MN" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="288,8,8" />
	<area shape="circle" id="col7" rel="SC,NC,FL,GA,AL,MS,TN,KY" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="312,8,8" />
	<area shape="circle" id="col8" rel="WV,MD,M2,VA,DE,PA" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="336,8,8" />
	<area shape="circle" id="col9" rel="NJ,NY,SI" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="360,8,8" />
	<area shape="circle" id="col10" rel="CT,RI,MA,VT,NH,ME" class="iborder000000 iopacity01" title="$560/mo" alt="$560/mo" href="#" coords="384,8,8" />
	<!-- mutliple area selectors with forced attributes -->
	
</map>





<p><p><p><p><p><p>

</TD>
</tr>
</table>

</TD>
</tr>
</table></center>

    


<tr>





</td>



</tr>

</table></center>

</TD>

</tr>

</table></center>

<center><table BORDER=0 COLS=1 WIDTH="975" HEIGHT=23 BACKGROUND="/images/front/botton-nav2.gif"  style="border-collapse: collapse">

<tr>

<TD VALIGN=CENTER align="center"> 

<CENTER>

 <center><FONT SIZE=-1><B>



</center>



</TD>



</tr>

</table></center>





</body>

</html>