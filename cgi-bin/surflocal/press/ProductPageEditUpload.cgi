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
	$MyData{$ThePhrase}="<img SRC=\"" . $TheUrly . "\">";
	&CloseMyDatabase;
	&Header;
	&PHed;
	print "<h1>Photo uploaded!</h1>\n";
	print "Your photo was successfully uploaded.<br>\n";
	print "<form action=PageEdit.cgi method=POST>\n";
   	print "<input type=submit value=\"Continue editing\"></form>\n";
 	print "<br>(NOTE: When you see the page, your new image may not show up correctly.";
    	print " This is because your browser has cached the previous image. Right-click on the ";
    	print "image you just replaced and select \"reload image\" or its equivalent from the popup menu.)\n";
	exit;	
}
