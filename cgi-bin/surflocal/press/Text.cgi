#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2005
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####set variables here######
$newform = "/cgi-bin/surflocal/press/Text.cgi";
$Hed{T} = "Building Your Service Directory Ad";
$FinalizeScript = "/cgi-bin/surflocal/press/Finalize.cgi";
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
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg\"></center>\n";
    print "<font size=+2><center><b><img src=\"http://surflocal.net/images/edit-text.jpg\">Type in your Press Release Headline</center></font>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=ChooseFontStuff>\n";
    print "<font color=000000><font size=-1><b>Type headline here:  <input type=text name=Text maxlength=200><br>\n";
   
    $TheirUrl = "$baseurl" . "$CityState" . "/" . "$BizName" . "/" . "index.html";
    &OpenCityDatabase;
    $DisAdType=$CityData{$BizName};
    &CloseCityDatabase;
    if ($DisAdType =~ /Plus/)
    {
	$Linkage = "$TheirUrl";
	
	#print "<p>Your Text Ad will link to your new Surflocal website, or to a website you already have set up.  ";
	print "<p>The web address to your Press Release is typed in the box below. <br><font color=800000>DO NOT CHANGE IT. ";
	#print "<font color=000000><p>If you are linking to an existing website, simply type in the web address of that site.";
	print "<p><font color=000000>The url to your press release will be:<p> <input type=text name=TextUrl size=50 value=\"$Linkage\"><br>\n";
    }
    else
    {
        print "Your ad must link to a Web page. In the box below, type the url \(web address\) ";
        print "of your Web site.<p>\n";
        print "The url to your site: <input type=text size=50 name=TextUrl value=\"http://\"><font color=800000><i> For example: http://www.surflocal.net </i><br><br>\n";
    }
    print "<br><br></center><input type=submit value=\"Click to Continue\"><Br>\n";
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
	$TheTemplate = $basedir . "Templates2" . "/" . "TextAdTemplate.html";
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
        print "<img src=\"http://surflocal.net/\sm_banner_MKTG.jpg\"></center>\n";
    print "<font size=+2><b><img src=\"http://surflocal.net/images/info-recorded.jpg\"> Press Release Heading Preview<br><br></b></font>\n";
    #print "<font color=000000><font size=+1>Your ad will appear as below<center> <p>\n";
    print "<center><table border=0><tr>\n";
    print "<td><font face=\"$Font\"><a href=\"$TheUrl\" target=\"_new\"><b><font color=\"$FontColor\">$TheText</font></b></center></a>";
    print "</font></b></td></tr></table>\n";
    print "<p>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=FinalizeText>\n";
    print "</center></center><input type=submit value=\"Click to Continue\"></form><p>\n";
    print "<form action=$newform method=POST>\n";
    print "</center><input type=submit value=\"Create Ad Again\"></form>\n";
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
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg\"></center>\n";
	print "<font size=+2><b><img src=\"http://surflocal.net/images/success.jpg\"> Press Release Headline <font color=800000>Approved:</font> $Bizname<p></font><b>\n";
	print "<font color=000000>Your headline has been successfully recorded in our database. <p>\n";
	
	if ($AdType eq "TextAdOnly")
	{
		print "<form action=$FinalizeScript method=POST>\n";
	}
	else
	{
		print "<form action=\"Page.cgi\" method=POST>\n";
	}
	print "</center><input type=submit value=\"Click to Continue\"><br><br></center>\n";
	exit;
}
