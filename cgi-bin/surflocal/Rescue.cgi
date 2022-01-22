#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2004-2022
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####set variables here######
$MasterDatabase = "$basedir" . "Secure" . "/" . "MasterDatabase.txt";
$newform = "$baseurl" . "Finalize.cgi";
$Hed{T} = "Finalize your ad";
###################
&Parse;
#&GetCookieValues;
#        This gives me $BizName and $CityState
$BizName=$in{0};
$CityState=$in{1};

&OpenCityDatabase;
$AdType=$CityData{$BizName};
&CloseCityDatabase;
$dirname = $basedir . $CityState . "/" . $BizName . "/";
&OpenMyDatabase;

#### RECORD ME IN MAIN DATABASE
$ToWrite = $CityState . "\|" . $BizName . "\|" . $AdType;
open (WRITEMASTER,">>$MasterDatabase") || &Error("Can't open $MasterDatabase for writing in RecordData sub. Reason: $!");
print WRITEMASTER "$ToWrite";
close(WRITEMASTER);

#### WRITE TO CITY'S AD TYPE DATABASE
#Essentially, I'm just dumping information to be written into the city's ad type database.
#Each ad type has its own database.
if ($AdType =~ /Coupon/)
{
	#Coupons are created on the fly. As such, all I need to know in this database
	#is the category and the coupon's biz name.
	$Prefix = "Coupon";
	$ToRecord = $Category . "\|" . "$BizName\n";
}
elsif ($AdType =~ /Text/)
{
	#Text ads are generated on IndexPage initialization. Therefore, I need
	#to store all text ad data in this file, with the addition of the BizName, in
	#case I need to edit the data later. Store items in key/value pairs so
	#I can later use them as a handy hash.
	$Prefix = "Text";
	$ToRecord = "Text=" . $MyData{TextAdText};
	$ToRecord .= "\|" . "Font=" . $MyData{TextAdFont};
	$ToRecord .= "\|" . "BizName=" . $BizName;
	$ToRecord .= "\|" . "FontColor=" . $MyData{TextAdFontColor};
	$ToRecord .= "\|" . "Url=" . $MyData{TextAdUrl} . "\n";
}
else 
{
	#Same thing here as Text ads.
	$Prefix = "Button";
	$ToRecord = "BackgroundImage=" . $MyData{ButtonBackgroundImage};
	$ToRecord .= "\|" . "Color=" . $MyData{ButtonColor};
	$ToRecord .= "\|" . "Font=" . $MyData{ButtonFont};
	$ToRecord .= "\|" . "BizName=" . $BizName;
	$ToRecord .= "\|" . "FontColor=" . $MyData{ButtonFontColor};
	$ToRecord .= "\|" . "Text=" . $MyData{ButtonText};
	$MyData{ButtonUrl} =~ s/ /\%20/gi;
	$ToRecord .= "\|" . "Url=" . $MyData{ButtonUrl} . "\n";
}

#Set location of the ad type database, based on the "Prefix" value above
$CityAdTypeDatabase = $basedir . $CityState . "/" . $Prefix . ".data";

#Just append, since alphabetical order isn't important.
open (CITYAD,">>$CityAdTypeDatabase") || &Error("Can't open $CityAdTypeDatabase. Reason: $!");
print CITYAD "$ToRecord";
close(CITYAD);

#### MAIL LINK INFO
#Compose the link for the user to be able to edit their databases.
	$TheLink = "Edit.cgi" . "\?" . $CityState . "\&" . "$BizName" . "\&" . $MyData{RandomNumber};
	$TheLink =~ s/ /\%20/gi;
	$TheLink = $baseurl . $TheLink;
	#If this isn't an e-mail address, there could be trouble down the road.
	$EmailTo = $MyData{Email};
	$FirstName = $MyData{FirstName};

	#We're piping information directly to the sendmail program, which is a potential
	#security risk. That risk is limited by the fact that the user has no direct input
	#ability at this juncture. The $mailprog and $admin scalars are set in the
	#SurfLocalLib, and have no programmatic way to change them here. 
	#If there are security breaches, we'll need to rethink this part of the program.
	open (MAIL, "|$mailprog $EmailTo") || &Error("Can\'t open $mailprog in MailMe sub! Reason: $!");
	print MAIL "Reply-to: SurfLocal Administrator <$admin>\n";
	print MAIL "To: $FirstName <$EmailTo>\n";
	print MAIL "From: SurfLocal Administrator <$admin>\n";
	print MAIL "Subject: Your new SurfLocal ad!\n\n";
	print MAIL "Dear $FirstName,\n\n";
	print MAIL "Your new SurfLocal ad is ready!\n";
	print MAIL "Below is a link you will need to use in the future to edit your ad.\n";
	print MAIL "If you need to edit your ad, use this link (If your e-mail program does not";
	print MAIL " support clickable links, copy and paste this link. If the link stretches over";
	print MAIL " two lines, be sure to copy the entire link):\n";
	print MAIL "----LINK BEGINS BELOW----\n";
	print MAIL "$TheLink\n";
	print MAIL "----END OF LINK----\n";
	print MAIL "If you created a Web page, at the bottom of your page is a small link that ";
	print MAIL "will take you to edit your page. The program will ask you for a passcode. ";
	print MAIL "That passcode is: $MyData{RandomNumber}\n";
	close (MAIL);

#Mail the admin.
	open (MAIL, "|$mailprog $admin") || &Error("Can\'t open $mailprog in MailMe sub for admin! Reason: $!");
	print MAIL "Reply-to: SurfLocal Administrator <$admin>\n";
	print MAIL "To: Administrator <$admin>\n";
	print MAIL "From: SurfLocal Administrator <$admin>\n";
	print MAIL "Subject: SurfLocal ad for $CityState by $BizName\n\n";
	print MAIL "Dear administrator,\n\n";
	print MAIL "$BizName has made a new $AdType ad at $CityState\n";
	close(MAIL);

#Give the user feedback. This is the last time he'll be dealing with this program package
#in this session.
#Kill the cookie for future iterations.
&CookieHeader;
&SetCookies("User","");
&CookieFooter;
#Print SurfLocal header based on template.
&PHed;	
print "<h1>Congratulations! You are done!</h1>\n";
print "Your information was sucessfully recorded, and you're ready to use your new SurfLocal ad!<br>\n";
print "Your ad in $CityState is here.  Click on the link to go there: ";
print "<a href=\"$baseurl$CityState\">$baseurl$CityState</a>\n";

#If they built a Web page, they'll want to know how to get there
if ($AdType =~ /Plus/)
{
	$TheWeb = $basurl . $CityState . "/" . $BizName . "/" . "index.html";
	print "<br>Your New Web page is here: Click the link to go there now. <a href=\"$TheWeb\">$TheWeb</a>\n";
	print "<br>Copy this link for your future reference.\n";
}
print "<br>In the future, if you ever want to edit your ad, you'll need this link.";
print "(it has also been e-mailed to $MyData{Email}) <br>Your passcode is the last 9 numbers in the link ";

print ": <a href=\"$TheLink\">$TheLink</a><br>\n";
exit;
