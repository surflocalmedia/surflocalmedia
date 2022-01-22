#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2021- present
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

#####set variables here######
$newform = "$baseurl" . "cgi-bin/surflocal/Button.cgi";
$ImageWidth=150;
$Hed{T} = "Building Your Display Ad";
$FinishScript = "$baseurl" . "cgi-bin/surflocal/Finalize.cgi";
$ButtonTemplate = "$basedir" . "Templates" . "/" . "ButtonTemplate.html";
$ImageDir = "https://www.surflocalmedia.net/images";
###################
&Parse;
&GetCookieValues;
#        This gives me $BizName and $CityState
###################

####### CONDITIONALS
&BeginButton unless $in{action};
$Action=$in{action};
if ($Action eq "ButtonText") {&ButtonText;}
if ($Action eq "PreviewButton") {&PreviewButton;}
if ($Action eq "FinalizeButton") {&FinalizeButton;}


####### BEGIN BUTTON
sub BeginButton
{
	#Open Button Template from Templates directory
	#and display it
    &Header;
    &PHed;
    open(TEMPLT, "$ButtonTemplate") || &Error("Can't open $ButtonTemplate in BeginButton sub. Reason: $!");
    @Templt=<TEMPLT>;
    close(TEMPLT);
    foreach (@Templt)
    {
    	$_ =~ s/\%\%BizName\%\%/$BizName/gi;
	$_ =~ s/\%\%ImageDir\%\%/$ImageDir/gi;
        print "$_";
    }
    exit;
}

####### BUTTON TEXT
sub ButtonText
{
	#Get button text and url. Also record data from button template
    &Header;
    &PHed;
    
    #Can't go on if user didn't enter a choice for any of the 
    #items in the button template.
    if (($in{BackgroundImage} eq "") || ($in{ButtonColor} eq "") || ($in{Font} eq "") || ($in{FontColor} eq ""))
    {
        &Error("<font color=000000>You must choose one item in each section to complete your ad build.  Please go back and complete the form.");
    }
    &OpenMyDatabase;
    $MyData{ButtonBackgroundImage} = $in{BackgroundImage};
    $MyData{ButtonColor} = $in{ButtonColor};
    $MyData{ButtonFont} = $in{Font};
    $MyData{ButtonFontColor} = $in{FontColor};
    &CloseMyDatabase;
    print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
    print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550><tr><td>\n";
    print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";	
    print "<b><font color=000000><font size=+1><img src=\"https://surflocalmedia.com/images/edit-text.jpg\">Enter Business Name or Category</center></b></font></center>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=PreviewButton>\n";
    print "<font color=000000><font size=-1><B>Example: <font color=800000>ABC Printing Company or Trade Show Sign Printing:<p> <input type=text name=ButtonText maxlength=40><br><br>\n";
    
    if (&GetCookies("Edit") eq "1")
    {
    	$AdType=$Cookies{"Edit"};
	$SubsequentAd = "true";
    }
    else
    {
    	&OpenCityDatabase;
    	$AdType=$CityData{$BizName};
    	&CloseCityDatabase;
    }
    $TheirUrl = $baseurl . $CityState . "/" . $BizName . "/" . "index.html";
    
    #If they've chosen to build a button and a Web page, I need to record their
    #SurfLocal Web address as the URL on their button. So I fill it automatically
    #in the form generated below. Otherwise, give them a chance to put in
    #their own Web site's url instead.
    if ($AdType eq "ButtonPlus")
    {
	$Linkage = "$TheirUrl";
	print "<font size=-1>Your Display Ad will link to your new Surflocal web site, or to a web site you already have set up.  ";
	print "<b><font color=000000>You are creating a new Surflocal web site and the web address will already be in the box.  </b>";
	print "<p><font color=000000>If you are linking to an existing web site, simply type in the web address of that site.";
	print "<p><font color=800000>The web address: <input type=text name=ButtonUrl size=50 value=\"$Linkage\"> Do Not Change<br>\n";
    }
    else
    {
        print "<font color=000000>In the box below, type the url \(web address\) to your web site ";
        print "of your web site. <p>\n";
        
        print "<font color=000000>The url to your web site: <input type=text size=50 name=ButtonUrl value=\"https://\">  <font color=800000><i> <br>For example: https://www.surflocalmedia.com </i><br><br>\n";
    }
    print "<p><input type=submit value=\"Enter my info and preview my display\"><p><input type=reset value=\"Reset the form and start over\"><Br>\n";
    print "</form>\n";
    exit;
}

####### PREVIEW BUTTON
sub PreviewButton
{
    &Header;
    &PHed;
    &OpenMyDatabase;
    #Set local variables based on database info
    $BackgroundImage = $MyData{ButtonBackgroundImage};
    $ButtonColor = $MyData{ButtonColor};
    $Font = $MyData{ButtonFont};
    $FontColor = $MyData{ButtonFontColor};
    #Set local variables based on incoming httpsd info
    $ButtonText = $in{ButtonText};
    $ButtonUrl = $in{ButtonUrl};
    #Set new database variables
    $MyData{ButtonText} = $ButtonText;
    $MyData{ButtonUrl} = $ButtonUrl;
    &CloseMyDatabase;
    
    #Open the template file from the Templates directory.
    $ButtonPreview = "$TemplatesDir" . "ButtonPreview.html";
    open(PREVIEW, "$ButtonPreview") || &Error("Can't open $ButtonPreview in PreviewButton sub. Reason: $!");
    @Preview=<PREVIEW>;
    close(PREVIEW);
    foreach(@Preview)
    {
        &SubstituteValues;
        #The buttons are composed on the fly based on the BackgroundImage the user
        #chose preceded by the ButtonColor they chose. Thus, if they chose "weave" as
        #the background and "black" as the color, if black is 0_0, their final image would
        #be named 0_0-weave.jpg
	# so it's ButtonColor-BackgroundImage.jpg
	$_ =~ s/\%\%BackgroundImage\%\%/$BackgroundImage/gi;
	$_ =~ s/\%\%ButtonColor\%\%/$ButtonColor/gi;
	$_ =~ s/\%\%Font\%\%/$Font/gi;
	$_ =~ s/\%\%FontColor\%\%/$FontColor/gi;
	$_ =~ s/\%\%ButtonText\%\%/$ButtonText/gi;
	$_ =~ s/\%\%ButtonUrl\%\%/$ButtonUrl/gi;
	print "$_";
    }
    exit;
}

####### FINALIZE BUTTON
sub FinalizeButton
{
	#The user has decided he wants to keep the button as he
	#has seen it on the preview page. Actually, I don't think this
	#part is necessary anymore, since the Finalize script actually does
	#the same thing in a more efficient way.
    &OpenMyDatabase;
    $BackgroundImage = $MyData{ButtonBackgroundImage};
    $ButtonColor = $MyData{ButtonColor};
    $Font = $MyData{ButtonFont};
    $FontColor = $MyData{ButtonFontColor};
    $ButtonText = $MyData{ButtonText};
    $ButtonUrl = $MyData{ButtonUrl};
    #$StateCode = $Abbrevs{$State};    
    $ButtonDatabase = $basedir . $CityState . "/" . "Buttons.db";
use DB_File;
    dbmopen(%ButtonData,$ButtonDatabase,0666) || &Error("Can't open the button database, $ButtonDatabase. Reason: $!");
    $ToWrite = $BackgroundImage . "\|";
    $ToWrite .= $ButtonText . "\|" . $ButtonUrl . "\|" . $Font . "\|";
    $ToWrite .= $FontColor . "\|" . $ButtonColor;
    $ButtonData{$BizName} = $ToWrite;
    dbmclose %ButtonData;
    &Finalize;
}

sub Finalize
{
	&Header;
	&PHed;
    print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<br><font size=+1><b><font color=800000><img src=\"https://surflocalmedia.com/images/info-recorded.jpg\">Your Display Ad was successfully recorded.</font></b>\n";
	print "<font color=000000><br>To proceed to the next step, click \'Continue\' below.</b><p>\n";
	&OpenCityDatabase;
	$AdType=$CityData{$BizName};
	&CloseCityDatabase;
	if ($AdType eq "ButtonOnly")
	{
		print "<form action=$FinalizeScript method=POST>\n";
	}
	elsif ($AdType eq "ButtonPlus")
	{
		print "<form action=/cgi-bin/surflocal/Page.cgi method=POST>\n";
	}
	else
	{
		&Error("Got a strange value from the City database. The AdType value is $AdType.");
	}
	print "<input type=submit value=\"Continue\"></form></center>\n";
	exit;
}
