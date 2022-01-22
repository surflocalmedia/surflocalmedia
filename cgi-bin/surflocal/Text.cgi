#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2004-2022
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

#####set variables here######
$newform = "/cgi-bin/surflocal/Text.cgi";
$Hed{T} = "Building Your Surflocal Ad";
$FinalizeScript = "/cgi-bin/surflocal/Finalize.cgi";
###################
&Parse;
&GetCookieValues;
&OpenCityDatabase;
$AdType=$CityData{$BizName};
&CloseCityDatabase;
&BeginAd unless $in{action};
$Action=$in{action};
# Getting City, State, AdType and BizName
if (($Action eq "") || ($Action eq "BeginAd")) {&BeginAd;}
if ($Action eq "PreviewTextAd") {&PreviewTextAd;}
if ($Action eq "ChooseFontStuff") {&ChooseFontStuff;}
if ($Action eq "FinalizeText") {&FinalizeText;}
####### BEGIN TEXT AD
sub BeginAd
{
   &Header;
    &PHed;
    print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
    print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
    print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";   
    print "<font size=+1><center><img src=\"https://surflocalmedia.com/images/edit-text.jpg\"><b>Enter Text and Web Address</b></b></b></center></font>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=ChooseFontStuff>\n";
    print "</center></center><font color=000000>Enter Text for your ad: Example: 'Automobiles' <input type=text name=Text maxlength=25><br>\n";
   
    $TheirUrl = "$baseurl" . "$CityState" . "/" . "$BizName" . "/" . "index.html";
    &OpenCityDatabase;
    $DisAdType=$CityData{$BizName};
    &CloseCityDatabase;
    if ($DisAdType =~ /Plus/)
    {
	$Linkage = "$TheirUrl";
	
	print "<p>Your Text Ad will link to your new , or to a website you already have set up.  ";
	print "<p>If you are creating a new  Marketing Page, the web address will already be in the box. <font color=800000>DO NOT CHANGE IT. ";
	print "<font color=000000><p>If you are linking to an existing website, simply type in the web address of that site.";
	print "<p><input type=text name=TextUrl size=50 value=\"$Linkage\"><br>\n";
    }
    else
    {
        print "<p>Your ad must link to a Web page. In the box below, type the url \(web address\) ";
        print "of your Web site.<p>\n";
        print "<p><input type=text size=50 name=TextUrl value=\"https://\"><font color=800000><i> <br>For example: https://www.surflocalmedia.com </i><br><br>\n";
    }
    print "<p><input type=submit value=\"Enter Info and Preview Ad\"><p><Br>\n";
    print "</form></center>\n";
    exit;
}

####### CHOOSE FONT STUFF
sub ChooseFontStuff
{
	#Getting "TextURL" and "Text"
	&Error("You must fill in both fields") unless (($in{TextUrl}) && ($in{Text}));
	&OpenMyDatabase;
	$MyData{TextAdText} = $in{Text};
	$MyData{TextAdUrl} = $in{TextUrl};
	&CloseMyDatabase;
	&Header;
	$TheTemplate = $basedir . "Templates" . "/" . "TextAdTemplate.html";
	open(TEMPL,"$TheTemplate") || &Error("No on $TheTemplate. $!");
	@Temp=<TEMPL>;
	close(TEMPL);
	foreach (@Temp)
	{
		print "$_";
	}
	exit;
}

####### PREVIEW TEXT AD
sub PreviewTextAd
{
	#Getting "font" and "fontColor"
	&Error("You must choose a font and a font color") unless (($in{font}) && ($in{fontColor}));
	&OpenMyDatabase;
	$MyData{TextAdFont} = $in{font};
	$MyData{TextAdFontColor}=$in{fontColor};
	$Font=$MyData{TextAdFont};
	$FontColor=$MyData{TextAdFontColor};
	$TheText=$MyData{TextAdText};
	$TheUrl=$MyData{TextAdUrl};
	&CloseMyDatabase;
    &Header;
    &PHed;
    print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
    print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";   	
    print "<font size=+1><b><center><img src=\"https://surflocalmedia.com/images/info-recorded.jpg\"> Preview your text ad for $BizName<br></b></b></font>\n";
    print "<font color=000000></b>Your ad will appear as below <p>\n";
    print "<center><table border=0><tr>\n";
    print "<td><font face=\"$Font\"><a href=\"$TheUrl\" target=\"_new\"><b><font color=\"$FontColor\">$TheText</font></b></a>";
    print "</font></b></td></tr></table>\n";
    print "<p>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=FinalizeText>\n";
    print "</center></center></center><input type=submit value=\"I am SATISFIED with this ad. Go to the next step\"></form><p>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=submit value=\"I am NOT satisfied with this ad. I want to try again.\"></form>\n";
    exit;
}

####### FINALIZE TEXT AD

sub FinalizeText
{
	&Header;
	&PHed;
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";   
	print "<font size=+1><b><center><img src=\"https://surflocalmedia.com/images/success.jpg\"> Text Ad Successfully Recorded: $Bizname<p></font></b>\n";
	print "</center></center><font color=000000>Your text ad has been successfully recorded in our database. <br>To proceed to the next step, click \"Continue\"<p>\n";
	
	if ($AdType eq "TextAdOnly")
	{
		print "<form action=$FinalizeScript method=POST>\n";
	}
	else
	{
		print "<form action=\"Page.cgi\" method=POST>\n";
	}
	print "</center></center><input type=submit value=\"Continue\"><br><br>\n";
	exit;
}
