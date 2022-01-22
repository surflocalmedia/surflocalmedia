#!/usr/local/bin/perl5.22
require 'SurfLocalLib.pl';
require 'cookie.lib';
require 'web-lib.pl';
require 'UploadLib.pl';
&SetMyVars;
$| = 1;
&GetCookieValues;
&OpenMyDatabase;
use CGI qw(:standard);
$query = new CGI;
my $TheItem    = $query->param('TheItem');
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
	$MyData{$TheItem} = "<img SRC=\"" . $TheThingie . "\" >";
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";	
        print "<center><table border=0 width=550><tr><td background=\"https://www.surflocal.net/images/white_table.jpg\">\n";
	print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";
        print "<font size=+1><center><img src=\"https://surflocal.net/images/edit-image.jpg\">  Image Uploaded!</font></center><br>\n";
	print "Your image was successfully uploaded. Press the 'continue' button below to move on.<br>\n";
	print "Your image may not show up when you go back to continue editing your page. But don't worry,\n";
	print "If the image does not load on your page, do this: <ul>\n";
	print "<li>Right-click on the image\n";
	print "<li>Select 'reload image' or its equivalent from the popup menu</ul><p>\n";
	print "<form action=Page.cgi method=POST>\n";
    	print "<input type=hidden name=action value=DisplayPage>\n";
    	print "<input type=submit value=\"Continue\"></form>\n";	
	exit;	
}
