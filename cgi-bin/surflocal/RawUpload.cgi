#!/usr/local/bin/perl5.22
require 'SurfLocalLib.pl';
require 'cookie.lib';
require 'web-lib.pl';
require 'UploadLib.pl';
&SetMyVars;
$| = 1;
&GetCookieValues;
if (&GetCookies("User")) {
	$TheCookie=$Cookies{"User"};
	($BizName,$CityState) = split(/\|/,$TheCookie);
	$dirname = $basedir . $CityState . "/" . $BizName;
	if ((! $BizName) || (! $CityState)) {
		&Error("You cannot call this script directly. BizName=$BizName. CityState=$CityState. TheCookie=$TheCookie");
	}
} else {
	&Error("You either called this page directly -- a no-no, or you called it with out the www at the beginning of www.surflocal.net.")
}
&OpenMyDatabase;
use CGI qw(:standard);
$query = new CGI;
my $action	 =	$query->param('action');

if (! $action) {
	&CloseMyDatabase;
	&Header;
	&PHed;
print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"http://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<h2>Upload an image for Advanced Build</font></h2>\n";
	print "</center>Select an image to upload. IMPORTANT: YOU CAN ONLY UPLOAD .JPG or .GIF FILES OR THE UPLOAD WILL NOT WORK. </font> BE SURE to rename your image to what you want to call it. How to acomplish this is in the white text box below, delete everything except the photo name. For example, everything except your phote name of MyPhoto.gif. You must upload the file from your DESKTOP in Windows. Simply copy the photo to your windows desktop and upload from there. That's it.<br>\n";
	print "<form action=/cgi-bin/surflocal/RawUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=action value=\"Yes, please\">\n";
	print "<p></center>Select an image to upload:<p><input type=\"FILE\" name=\"file-to-upload-1\"><br>\n";
	print "<p><input type=submit value=\"Upload this image\"><p>Press the button ONLY ONCE. </font>The image upload may take a few moments.</form></td></tr></table>\n";
	exit;
}

my $TheItem    = $query->param('file-to-upload-1');
	$Filename = $TheItem . ".jpg";
&MainUploadRoutine;	
if ($SUCCESS_LOCATION !~ /^\s*$/) 
{
	print $query->redirect($SUCCESS_LOCATION);
} 
else 
{
	
	$TheThingie = $baseurl . $CityState . "/" . $BizName . "/" . $Filename;
		$TheThingie =~ s/ /\%20/gi;
	$MyData{$TheItem} = "<img SRC=\"" . $TheThingie . "\" width=200>";
	&CloseMyDatabase;
	&Header;
	&PHed;
	print "<h1><font color=#000000>Image uploaded!</font></h1>\n";
	print "Your image was successfully uploaded. Press the button to continue.<br>\n";
	print "To access the image from your web page, you'll need to type in this code (or copy and paste into your page where you want the image to be.<br>\n";
	print "<font color=000000>\&lt\;img src=\"$TheThingie\"\&gt\;</font><br>\n";
	print "<form action=RawUpload.cgi method=POST>\n";
    print "<input type=submit value=\"Upload another\"></form>\n";
    print "<br><font color=#000000>Simply minimize this window when you are finished uploading images.</font>  Use the minus button in the top right corner of this window to minimize.  After editing your presentation, then you may close this window.\n";	
	exit;	
}
