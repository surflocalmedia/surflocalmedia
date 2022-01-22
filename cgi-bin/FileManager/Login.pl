#!/usr/local/bin/perl5.22
use CGI::Carp qw(fatalsToBrowser);

##########################################################################
######################## iDC File Manager - Login ########################
##########################################################################
##########################################################################

##########################################################################
# i Dot Communications © 2004-2006 Copyright Mark Roberts / Alexandre Golovkine
##########################################################################

##########################################################################
# For Instructions / Questions / Comments etc... Please visit:
# Help Forum:   https://www.idotcommunications.co.uk/OnlineSupportArea/Forum/
##########################################################################

####Main Login Screen Title###############################################

my $Logintitle = "Surflocal.Net - Agent Office";
#Change the "Main Login Screen Title" to the name of your website or company etc...

##########################################################################

####Main File Manager Name################################################

my $FileManagerName = "Surflocal.Net";
#Do not modify the Main File Manager Name unless you hold an OEM License

##########################################################################

####About Screen URL##################################################

my $AboutScreenURL = "http://www.surflocal.net/cgi-bin/FileManager/About.shtml";
#Change the url to the "About Screen" to your servers url to the File Manager About.shtml

##########################################################################

####About Screen URL##################################################

my $ShowSignupOption = "hidden";
#Enable the iDC Account Creation sign-up tab to appear on the Login Page
#Change to $ShowSignupOption = "visible"; to show the tab
#Change to $ShowSignupOption = "hidden"; to hide the tab

my $SignupURL = "http://www.surflocal.net/AccountCreation/Application.html";
#Enter the URL of the iDC Account Creation "Application.html" sign-up form.

my $SignupText = "Click here to sign-up";
#Configure the text that appears in the sign-up tab

my $Signupposition = "69%";
#Configure position of sign-up tab (either in px or %)


##########################################################################

####Main Image Directory##################################################

my $htmlDataFolder = "http://www.surflocal.net/FileManagerData/";
#Change the url to the "Main Image Directory" to your servers url to the File Manager Image Directory
#For example:
#e.g. Main Main Image Directory ("http://www.yoursite.com/FileManagerData")

##########################################################################

##########################################################################

#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!


##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################

use CGI qw(:standard);
my $message = "<div id='Oobj6' style='position:absolute;z-index:4;visibility:visible; left:151px;top:61px;width:297px;height:34px;'><div id='Grtf18' class='dfltt'><div align='center'><font face='Verdana' class='error'><B>Error: Account Not Yet Activated Or Incorrect Username And Password Entered!</B></font><font face='Verdana' class='fsx01'><br></font></div></div></div>" if param('error');

my $lp = param('error');
$lp &&= qq~<script type="text/javascript">\nshowLogin($lp)\n</script>~;

print "Content-type: text/html\n\n";
print <<EOD;

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>$Logintitle</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="Description" content="iDC File Manager is a powerful multilingual web based system which allows you to store, manage and distribute every format of digital media, including, documents, images, audio, video, publishing layouts, presentations and PDF files.">
<META CONTENT="web based file manager,web file manager,web based system,archive files online,browse file structure,multilingual online file manager,online file storage,FTP,multiple upload,download,store,manage and distribute, compress files and directories,online file sharing,upload file manager,web file management,web file system,web based file,web based file system,web based file sharing,content management,software,website,digital media,documents,images,audio,video,publishing layouts,presentations,PDF files">
<meta name="robots" content="all" >
<style type="text/css">
.fsx01 {font-size: 11px;}
.txdec {text-decoration: none;}
#Oobj2 {position:absolute;z-index:9;visibility:visible;left:1px;top:38px;width:541px;height:346px;font-size:1px;}
#Oobj4 {position:absolute;z-index:9;visibility:visible;left:2px;top:254px;width:539px;height:98px;font-size:1px;}
#Oobj17 {position:absolute;z-index:9;visibility:visible;text-align:left;left:3px;top:40px;width:538px;height:215px;}
#Oobj38 {position:absolute;z-index:9;visibility:visible;text-align:left;left:96px;top:3px;width:294px;height:27px;}
#Oobj19 {position:absolute;z-index:9;visibility:visible;text-align:left;left:303px;top:323px;width:215px;height:19px;}
#Oobj4a {position:absolute;z-index:9;visibility:visible;text-align:left;left:28px;top:283px;width:79px;height:70px;}
#Oobj4b {position:absolute;z-index:9;visibility:visible;text-align:left;left:107px;top:283px;width:79px;height:70px;}
#Oobj4c {position:absolute;z-index:9;visibility:visible;text-align:left;left:186px;top:284px;width:79px;height:69px;}

.dfltt {font-family:Times New Roman;font-size:14px;font-weight:normal;text-decoration:none;text-align:left;}
body {margin:0;height:100%;width:100%; background-repeat:repeat;
}
#Grtf19{
font-family:arial;
color: #727272;
font-weight:bold;
text-align: right;
}
a:link {
  color: #000000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration:none
}
a:visited {
  color: #000000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration:none
}
a:active {
  color: #000080;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
a:hover {
  color: #000080;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
td {
  color: #000000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
.error {
  color: #ff0000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
body {
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
input {
  color: #000000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none;
border:outset 1px #ccc;
background:#999;
padding: 1px 0px;
background: #EEEEEE;
background:url($htmlDataFolder/formbg.gif) repeat-x left top;
}
textarea {
  color: #FFFFF;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none;
  background: #F7F7F7;
  border: 1 solid #C0C0C0;
}
select {
  color: #000000;
  font: normal 7.5pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none;
  background: #EEEEEE;
  border: 1 solid #C0C0C0;
}
.small {
  color: #000000;
  font: 6pt Verdana, Arial, Helvetica, sans-serif;
  font-weight: none;
  text-decoration: none
}
pre {
  font: normal 7.5pt verdana;
}
#navigation {
text-align: center;
float: left;
}
#navigation ul {
        font-family: Verdana;
        font-size: 12px;
        font-weight: normal;
        text-decoration: none;
        margin: 0;
        padding: 0;
        list-style:none;
}
#navigation li {
        display: inline;
        background: url($htmlDataFolder/signupbg.png) repeat-x center top;
        text-align: center;
        padding: 0;
        margin-right: 4px;
        float: left;
}
#navigation a {
        color: Black;
        background: url($htmlDataFolder/signupleft.png) no-repeat left top;
        float: left;
        margin:        0;
        padding-left:7px;
        text-decoration: none;
}
#navigation a span {
        background: url($htmlDataFolder/signupright.png) no-repeat right top;
        display: block;
        padding:7px 13px 4px 5px;
}
#navigation a span {
        float: none;
}
option.selectflag {
padding: 0px 0 1px 20px;
background-repeat: no-repeat;
background-position: 1px 1px;
vertical-align: middle;
width: 139px;
}
select.selectflag {
padding: 0px 0 2px 20px;
background-repeat: no-repeat;
background-position: 1px 1px;
vertical-align: middle;
width: 139px;
}
</style>
<script type="text/javascript"><!--
        logoCmImg = new Image;
        logoCmImg.src= "$htmlDataFolder/FileManager1.4Logo.png";

        logoFmImg = new Image;
        logoFmImg.src= "$htmlDataFolder/FileManager1.4Logo.png";

        function show(url,height, width, scroll){
                                if(!scroll) scroll = "yes";
                                newWnd=window.open(url, 'show', "height="+height+", width="+width+", top=100, left=100, status=none, scrollbars=none, location=none");
                                newWnd.focus();
                        }
        function changetext(x){
                document.getElementById('Grtf19').innerHTML=x;
        }
        function showLogin(type){
                document.getElementById('logo').style.display='none';
                if (type==1){
                        document.getElementById('logoImg').src=logoFmImg.src;
                        document.loginForm.action='Manager.pl';
                }
                else{
                        document.getElementById('logoImg').src=logoCmImg.src;
                        document.loginForm.action='ClientManager.pl';
                }
                document.getElementById('login').style.display='';
        }


//-->
</script>

</head>

<body bgcolor="#ffffff" alink="#ff0000" link="#0000ff" vlink="#800080"   background="$htmlDataFolder/uploadbg.png">

<div id="Oobj20" style="position:absolute;z-index:1;visibility:visible; left:50%;top:61px;width:544px;height:386px;margin-left:-272px;font-size:1px;">
<div id="Oobj2">
<img name="Ggeo4" SRC="$htmlDataFolder/White.png" alt="" border = 0  width="541" height="346"></div>

<div id="Oobj4">
<img name="Ggeo7" SRC="$htmlDataFolder/LoginBar.png" alt="" border = 0  width="539" height="98"></div>

<div id="Oobj4a">
<a href="#" onclick="showLogin(1); return false;"><img border="0" src="$htmlDataFolder/login.png" alt="$FileManagerName Login" onmouseover="changetext
('Client Management Login')"
onmouseout="changetext('')">
</div>


<div id="Oobj4b">
<a href="http://www.surflocal.net/marketing-programs/" ><img border="0" src="$htmlDataFolder/controlpanel.png" alt="Pricing & Information"
onmouseover="changetext('Pricing & Information')"
onmouseout="changetext('')">
</div>

<div id="Oobj4c">
<a href="http://www.surflocal.net"><img border="0" src="$htmlDataFolder/about.png"
alt="About $FileManagerName" onmouseover="changetext('About $FileManagerName')"
onmouseout="changetext('')">
</div>

<div id="Oobj4d">
<a href="http://www.idotcommunications.co.uk/"></a>
</div>



<div id="Oobj17">
<div id="Gcode17" class="dfltt">
<div id="logo" style="position:absolute;z-index:1; left:21px;top:43px;width:508px;height:127px;font-size:1px;">
<img name="Ggeo44" SRC="$htmlDataFolder/LargeFileManagerLogo.png" alt="" border = 0  width="508" height="127"></div>
</div>

<!---->

<div id="navigation" style="position:absolute;z-index:1;visibility:$ShowSignupOption; left:$Signupposition;top:-24px;width:150px;height:154px;">
<ul>
<li><a href="$SignupURL" target="_blank"><span>$SignupText</span></a></li>
</ul>
</div>

<div id='login' style='display:none'>
<div id="Oobj40" style="position:absolute;z-index:3;visibility:visible; left:259px;top:59px;width:285px;height:103px;">
<div id="Gcode45" class="dfltt">

<form method="post" name="loginForm" action="Manager.pl">
<table border="0" cellspacing="8">
<tr>
<td>Client Username: </td>
<td><input type=text name=login size=25 value=""></td>
</tr>
<tr>
<td>Client Password:</td>
<td><input type=password name=password size=25 value=""></td>
</tr>
<tr>
<td>Select Language:</td><td><select name="language" class="selectflag" style="background-image: url($htmlDataFolder/us.png);">
<option value=en class="selectflag" style="background-image: url($htmlDataFolder/us.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" selected>&nbsp;&nbsp;&nbsp;English</option>
<option value=fr class="selectflag" style="background-image: url($htmlDataFolder/fr.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Français</OPTION>
<option value=de class="selectflag" style="background-image: url($htmlDataFolder/de.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Deutsch</OPTION>
<option value=nl class="selectflag" style="background-image: url($htmlDataFolder/nl.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Nederlands</OPTION>
<option value=it class="selectflag" style="background-image: url($htmlDataFolder/it.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Italiano</OPTION>
<option value=es class="selectflag" style="background-image: url($htmlDataFolder/es.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;España</OPTION>
<option value=dk class="selectflag" style="background-image: url($htmlDataFolder/dk.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Dansk</OPTION>
<option value=sw class="selectflag" style="background-image: url($htmlDataFolder/se.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Svenska</OPTION>
<option value=nr class="selectflag" style="background-image: url($htmlDataFolder/no.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Norsk</OPTION>
<option value=fi class="selectflag" style="background-image: url($htmlDataFolder/fi.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Suomi</OPTION>
<option value=po class="selectflag" style="background-image: url($htmlDataFolder/pt.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Português BR</OPTION>
<option value=ru class="selectflag" style="background-image: url($htmlDataFolder/ru.png);" onclick="this.parentNode.setAttribute('style',this.getAttribute('style'));" >&nbsp;&nbsp;&nbsp;Russian</OPTION>
</select></td></tr>
<td></td>
<td><input type=submit name=log_in value='  Login  '>   &nbsp;<input type="reset"  value=" Reset  "></</td>
</tr>
</table></form>

</div>
</div>

<div id="Oobj76" style="position:absolute;z-index:2;visibility:visible; left:241px;top:26px;width:5px;height:165px;font-size:1px;">
<img name="Ggeo92" Align=Top SRC="$htmlDataFolder/dottedline.png" alt="" border=0 width="5" height="165"></div>

<div id="Oobj28" style="position:absolute;z-index:3;visibility:visible; left:13px;top:20px;width:220px;height:160px;font-size:1px;">
<img id="logoImg" Align=Top SRC="$htmlDataFolder/FileManager1.4Logo.png" alt="" border=0 width="220" height="160"></div>
</div>

<!---->

</div>

<div id="Oobj38">
<div id="Gcode43" class="dfltt">
$message
</div>
</div>

<div id="Oobj19">
<div id="Grtf19" class="dfltt">
<br></div>
</div>

</div>
$lp

</body>
</html>


EOD

exit;
