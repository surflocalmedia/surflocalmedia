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
$ProductsNumber = $MyData{NumberOfProductPages};
my $TheNumber    = $query->param('ProductNumber');
$Filename = "Product_" . $TheNumber . ".jpg";
&MainUploadRoutine;
if ($SUCCESS_LOCATION !~ /^\s*$/) 
{
	print $query->redirect($SUCCESS_LOCATION);
} 
else 
{
	$TheUrly = $baseurl . $CityState . "/" . $BizName . "/" . $Filename;
	$TheUrly =~ s/ /\%20/gi;
	$ThePhrase="ProductImage_" . $TheNumber;
	$MyData{$ThePhrase}="<img SRC=\"" . $TheUrly . "\" >";
	&CloseMyDatabase;
	&Header;
	&PHed;
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table border=7 width=800 bordercolor=800000><tr><td background=\"http://www.surflocalmedia.com/images/white_table.jpg\">\n";
        print "<center><img src=\"http://surflocalmedia.com/\sm_banner_MKTG3.gif\"><p>\n";
	print "<font size=+1><b><font color=000000><img src=\"http://surflocalmedia.com/images/info-recorded.jpg\">Upload Completed!</font>\n";
	print "<form action=Page.cgi method=POST>\n";
	print "<input type=hidden name=TheNumber value=\"$ProductsNumber\">\n";
	print "<input type=hidden name=action value=CheckForUploads>\n";
	print "<input type=submit value=\"Continue editing\"></form></center><br><br>\n";
	#print "<br><font color=000000><b><font size=-1><blockquote><blockquote><blockquote>(NOTE: When you see the page, your new image may not show up correctly. This is because your browser has cached the previous image. Right-click on the image you just replaced and select \"reload image\" or its equivalent from the popup menu.)<p>\n";
	exit;	
}
