#!/usr/local/bin/perl5.22


require 'SurfLocalLib.pl';
require 'cookie.lib';
require 'web-lib.pl';
require 'UploadLib.pl';
#BEGIN {
	&SetMyVars;
#}
$| = 1;
&GetCookieValues;
&OpenMyDatabase;
#Got $BizName and $CityState
	
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
	$MyData{$TheItem} = "<img SRC=\"" . $TheThingie . "\">";
	#$MyData{$TheItem} =~ s/ /\%20/gi;
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<center><h1>Upload completed!</h1>\n";
	print "If your image does not show up correctly when you preview ";
	print "the coupon, right click on it and reload it.<br>\n";
	print "<form action=CouponEdit.cgi method=POST>\n";
   	print "<input type=submit value=\"Continue\"></form>\n";
	exit;	
}
