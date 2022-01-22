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
$Filename=$TheItem . ".jpg";
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
	#$MyData{$TheItem} =~ s/ /\%20/gi;
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg\"><br>\n";
	print "<h1><font color=000000>Upload completed!</h1>\n";
	print "<form action=Coupon.cgi method=POST>\n";
  	print "<input type=hidden name=action value=DisplayPage>\n";
   	print "<input type=submit value=\"Continue\"></form>\n";
	exit;	
}
