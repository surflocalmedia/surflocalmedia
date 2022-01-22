#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2004-2022
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####set variables here######
$newform = "/cgi-bin/surflocal/TextEdit.cgi";
$Hed{T} = "Editing Your Text ad";
$FinalizeScript = "/cgi-bin/surflocal/FinalizeEdit.cgi";
###################
&Parse;
&GetCookieValues;
&BeginAd unless $in{action};
$Action=$in{action};
# Getting City, State, AdType and BizName
if (($Action eq "") || ($Action eq "BeginAd")) {&BeginAd;}
if ($Action eq "MakeEdit") {&MakeEdit;}
if ($Action eq "ExecuteEdit") {&ExecuteEdit;}


####### EXECUTE EDIT
sub ExecuteEdit
{
	&OpenMyDatabase;
	$MyData{TextAdFont} = $in{TextAdFont} if ($in{TextAdFont});
	$MyData{TextAdFontColor} = $in{TextAdFontColor} if ($in{TextAdFontColor});
	$MyData{TextAdText} = $in{TextAdText} if ($in{TextAdText});
	$MyData{TextAdUrl} = $in{TextAdUrl} if ($in{TextAdUrl});
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<h1><center>Edit executed</h1></center>\n";
	print "You can continue making edits, or you can finalize your changes.<br><br></center>\n";
	&DisplayAd;
	&PrintJabber;
	exit;
}

####### MAKE EDIT
sub MakeEdit
{
	$EditItem = $in{EditItem};
	&Header;
	&PHed;
	&OpenMyDatabase;
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<center><font size=+1>Edit your Text Ad</h1></center>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ExecuteEdit>\n";
	$ThisItem = $MyData{$EditItem};
	if ($EditItem eq "TextAdFont"){&TextAdFont;}
	if ($EditItem eq "TextAdFontColor"){&TextAdFontColor;}
	if ($EditItem eq "TextAdText"){&TextAdText;}
	if ($EditItem eq "TextAdUrl"){&TextAdUrl;}
	print "<p></center></center><input type=submit value=\"Change the Item\"></form></center>\n";
	&CloseMyDatabase;
	exit;
}
####### TEXT AD URL
sub TextAdUrl
{
	print "</center>Edit your text ad's url: <input type=text size=40 name=$EditItem value=\"$ThisItem\">\n";
}

####### TEXT AD TEXT
sub TextAdText
{
	print "</center>Edit your text ad's text: <input type=text name=$EditItem value=\"$ThisItem\">\n";
}

####### TEXT AD FONT
sub TextAdFont
{
	$TheFile="TextEditFontFace";
	print "<center>Select a new font face for your text ad:<p>\n";
	&ReadTemplateFile;
}

####### TEXT AD FONT COLOR
sub TextAdFontColor
{
	$TheFile="TextEditFontColor";
	print "<center>Select a new font color for your text ad:<p>\n";
	&ReadTemplateFile;
}

####### READ TEMPLATE FILE
sub ReadTemplateFile
{
	$ThisFile = $basedir . "Templates" . "/" . $TheFile;
	open(THETEMP,"$ThisFile") || &Error("Can't open $ThisFile. Reason: $!");
	@Tempy=<THETEMP>;
	close(THETEMP);
	foreach (@Tempy)
	{
		print "$_";
	}
}


####### PRINT JABBER
sub PrintJabber
{
        	
        print "</center>Above is your ad as it appears now. Click one of the items below to change your ad.<br>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=\"MakeEdit\">\n";
	print "<img src=\"https://surflocalmedia.com/images/edit-text2.jpg\"> <input type=radio name=EditItem value=TextAdFont>Font face<br>\n";
	print "<img src=\"https://surflocalmedia.com/images/edit-text2.jpg\"> <input type=radio name=EditItem value=TextAdFontColor>Font color<br>\n";
	print "<img src=\"https://surflocalmedia.com/images/edit-text2.jpg\"> <input type=radio name=EditItem value=TextAdText>Ad text<br>\n";
	print "<img src=\"https://surflocalmedia.com/images/edit-text2.jpg\"> <input type=radio name=EditItem value=TextAdUrl>Link url<br>\n";
	print "<p><input type=submit value=\"Edit this item\"></form>\n";
	print "<p><form action=$FinalizeScript method=POST>Or, if you're done editing this ad, \n";
	print "<p><input type=submit value=\"click here to finalize your changes\"></form>\n";
}

####### BEGIN AD
sub BeginAd
{
	&Header;
    	&PHed;
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
    	print "<h1>Edit your ad:</h1>\n";
	&DisplayAd;
	&PrintJabber;
	exit;
}

####### DISPLAY AD
sub DisplayAd
{
	&OpenMyDatabase;
	$Font=$MyData{TextAdFont};
	$FontColor=$MyData{TextAdFontColor};
	$Text=$MyData{TextAdText};
	$Url=$MyData{TextAdUrl};
	&CloseMyDatabase;
	print "<center><b><a href=\"$Url\" target=\"_new\"><font face=\"$Font\" color=\"$FontColor\">$Text</a><br>\n";
	print "</font></b></center><p>\n";
}
