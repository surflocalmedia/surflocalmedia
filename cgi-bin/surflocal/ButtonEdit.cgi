#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2005
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

#####set variables here######
$newform = "/cgi-bin/surflocal/ButtonEdit.cgi";
$ImageWidth=150;
$Hed{T} = "Building Your Feature Ad";
$FinishScript = "/cgi-bin/surflocal/FinalizeEdit.cgi";
$ButtonTemplate = "$basedir" . "Templates" . "/" . "ButtonTemplate.html";
$ImageDir = "https://www.surfLocal.net/images";
###################
&Parse;
&GetCookieValues;
#        This gives me $BizName and $CityState
################### 

####### CONDITIONALS
&DisplayButton unless $in{action};
$Action=$in{action};
if ($Action eq "ButtonText") {&ButtonText;}
if ($Action eq "MakeEdit") {&MakeEdit;}
if ($Action eq "ExecuteEdit") {&ExecuteEdit;}

####### EXECUTE EDIT
sub ExecuteEdit
{
	&OpenMyDatabase;
	$MyData{ButtonBackgroundImage} = $in{ButtonBackgroundImage} if ($in{ButtonBackgroundImage});
	$MyData{ButtonColor} = $in{ButtonColor} if ($in{ButtonColor});
	$MyData{ButtonFont} = $in{Font} if ($in{Font});
	$MyData{ButtonFontColor} = $in{FontColor} if ($in{FontColor});
	$MyData{ButtonText} = $in{ButtonText} if ($in{ButtonText});
	$MyData{ButtonUrl} = $in{ButtonUrl} if ($in{ButtonUrl});
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br>\n";
	print "<b>Update Complete.</b> Continue making edits, or \"Post Your Ad\".\n";
	&PreviewButton;
	&PrintJabber;
}

####### MAKE EDIT
sub MakeEdit
{
	$EditItem = $in{EditItem};
	&Header;
	&PHed;
	&OpenMyDatabase;
	print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
       print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ExecuteEdit>\n";
	$ThisItem = $MyData{$EditItem};
	if ($EditItem eq "ButtonBackgroundImage"){&ButtonBackgroundImage;}
	if ($EditItem eq "ButtonColor"){&ButtonColor;}
	if ($EditItem eq "ButtonFont"){&ButtonFont;}
	if ($EditItem eq "ButtonFontColor"){&ButtonFontColor;}
	if ($EditItem eq "ButtonText"){&ButtonText;}
	if ($EditItem eq "ButtonUrl"){&ButtonUrl;}
	print "<br></center><input type=submit value=\"Edit this\"></form></center>\n";
	&CloseMyDatabase;
	exit;
}

####### BUTTON URL
sub ButtonUrl
{
	print "Edit Your Display Ad Web Address: <br><br><input type=text size=50 name=$EditItem value=\"$ThisItem\">\n";
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
}

####### BUTTON TEXT
sub ButtonText
{
	print "Edit Your Display Ad Text: <br><br><input type=text  size=40 name=$EditItem value=\"$ThisItem\"><br><br>\n";
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
}

####### BUTTON BACKGROUND IMAGE
sub ButtonBackgroundImage
{
	$TheFile="ButtonEditBackgroundImage";
	print "Select A New Background For Your Display Ad:<p>\n";
	&ReadTemplateFile;
}

####### BUTTON FONT COLOR
sub ButtonFontColor
{
	$TheFile="ButtonEditButtonFontColor";
	print "Select A New Font Color For Your Display Ad:<p>\n";
	&ReadTemplateFile;
}

####### BUTTON FONT
sub ButtonFont
{
	$TheFile="ButtonEditButtonFont";
	print "Select A New Font Style For Your Display Ad:<p>\n";
	&ReadTemplateFile;
}

####### BUTTON COLOR
sub ButtonColor
{
	$TheFile="ButtonEditButtonColor";
	print "Select A New Color For Your Feature Ad:<p>\n";
	&ReadTemplateFile;
}

####### READ TEMPLATE FILE
sub ReadTemplateFile
{
	$ThisFile = $basedir . "Templates" . "/" . $TheFile;
	$Thedir = $baseurl . "images";
	open(THETEMP,"$ThisFile") || &Error("Can't open $ThisFile. Reason: $!");
	@Tempy=<THETEMP>;
	close(THETEMP);
	foreach (@Tempy)
	{
		$_ =~ s/\%\%ImageDir\%\%/$Thedir/gi;
		print "$_";
	}
}

####### BEGIN BUTTON
sub DisplayButton
{
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br>\n";
	&PreviewButton;

	
 
	#print "<p><font sixe=+1><center>Edit your Display Ad- Select an item below to edit your ad</font>\n";
	&PrintJabber;
}

####### PRINT JABBER
sub PrintJabber
{
	
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=\"MakeEdit\">\n";
        print "<p><font sixe=+1><center>Edit your Display Ad- Select an item below to edit your ad</font>\n";
	print "<center><table border=0 width=550 border=0><tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"> <input type=radio name=EditItem value=ButtonBackgroundImage><b></b> Change Ad Image</td><br>\n";
	print "<tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"><input type=radio name=EditItem value=ButtonColor> Change Ad Color<br></td>\n";
	print "<tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"> <input type=radio name=EditItem value=ButtonFont> Change Text Font Style<br></td>\n";
	print "<tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"> <input type=radio name=EditItem value=ButtonFontColor>Change Font Color<br></td>\n";
	print "<tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"> <input type=radio name=EditItem value=ButtonText>Change Text<br></td>\n";
	print "<tr><td><img src=\"https://surflocal.net/images/edit-text.jpg\"> <input type=radio name=EditItem value=ButtonUrl>Change Web Address<br></td>\n";
	print "</tr></table></center></center></center><p><input type=submit value=\"Edit this item\"></form>\n";
	print "<p><form action=$FinishScript method=POST><input type=submit value=\"Post Your Ad\"></form></center>\n";
	exit;
}

####### PREVIEW BUTTON
sub PreviewButton
{
    &OpenMyDatabase;
    #Set local variables based on database info
    $BackgroundImage = $MyData{ButtonBackgroundImage};
    $ButtonColor = $MyData{ButtonColor};
    $Font = $MyData{ButtonFont};
    $FontColor = $MyData{ButtonFontColor};
    #Set local variables based on incoming httpsd info
    $ButtonText = $MyData{ButtonText};
    $ButtonUrl = $MyData{ButtonUrl};
    &CloseMyDatabase;
    
    #Open the template file from the Templates directory.
   print "<center><table border=\"0\">\n";
   print "<tr><td align=\"center\" width=\"136\" background=\"https://www.surflocal.net/images/$ButtonColor-$BackgroundImage.gif\" height=\"56\">\n";
   print "<a href=\"$ButtonUrl\" target=\"_new\"><font color=\"$FontColor\" face=\"$Font\"><font size=-1>$ButtonText</font></a></td>\n";
   print "</tr></table></center>\n";
}
