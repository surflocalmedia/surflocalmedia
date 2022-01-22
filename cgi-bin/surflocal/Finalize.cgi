#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 1998-present
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####set variables here######
$MasterDatabase = "$basedir" . "Secure" . "/" . "MasterDatabase.txt";
$newform = "/cgi-bin/surflocal/Finalize.cgi";
$Hed{T} = "Finalize your ad with Surflocal";
###################
&Parse;
&GetCookieValues;
#        This gives me $BizName and $CityState

&OpenCityDatabase;
$AdType=$CityData{$BizName};
&CloseCityDatabase;

&OpenMyDatabase;
#### CHECK FOR CATEGORY 
if ($AdType =~ /Coupon/)
{
	$Category=$MyData{CouponCategory};
	
	#I don't think this is necessary anymore. We will keep it in just in case.
	use locale;
	
	#Use initial caps for the category.
	$Category =~ s/(\w+)/\u\L$1/g;
	
	#Set location of the main Category list, open it for reading.
	$MassCatList = "$basedir" . "Templates" . "/" . "CategoryList";
	open (MASSAH,"$MassCatList") || &Error("Can't open $MassCatList in CheckCatList sub. Reason: $!");
	@Massah=<MASSAH>;
	close(MASSAH);
	
	#The list contains categories. If one of the categories matches the one passed
	#to this script, we have a match and don't need to write one.
	foreach $Mssa (@Massah)
	{
		chomp($Mssa);
		if ($Mssa eq "$Category")
		{
			$Match = "yes";
		}
	}
	
	#if there's no match, we need to write the category.
	if ($Match ne "yes")
	{
		open (MASSW,">>$MassCatList") || &Error("Can't open $MassCatList to write in CheckCatList sub. Reason: $!");
		print MASSW "\n";
		print MASSW "$Category";
		close(MASSW);
	}
}

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

#If this is a coupon, I need to create a second database for the coupon display
#script. If the category doesn't exist in this database, add it. Otherwise, do nothing.
if ($AdType =~ /Coupon/)
{
	$CaterList = $basedir . $CityState . "/" . "CouponCategories.data";
	open (COCA,"$CaterList") || &Error("Can't open $CaterList. Reason: $!");
	@Caties=<COCA>;
	close(COCA);
	foreach(@Caties)
	{
		chomp($_);
		$CatList{$_} = "True";
	}
	if (exists($CatList{$Category}))
	{
		$Thanks=1;
	}
	else
	{
		open (COCB,">>$CaterList");
		print COCB "$Category\n";
		close(COCB);
	}
}
	

#### MAIL LINK INFO
#Compose the link for the user to be able to edit their databases.
	$TheLink = "cgi-bin/surflocal/Edit.cgi" . "\?" . $CityState . "\&" . "$BizName" ;
	$TheLink =~ s/ /\%20/gi;
	$TheLink = $baseurl . $TheLink;
	$TheWeb = $baseurl . $CityState . "/" . $BizName . "/" . "index.html";
        $TheWeb =~ s/ /\%20/gi;
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

	print MAIL "Reply-to: SurfLocal Administrator <$admin> \n";
	print MAIL "From: SurfLocal Administrator <$admin> \n";
	print MAIL "To: $FirstName <$EmailTo>\n";
	print MAIL "Subject: $BizName Your New Surflocal Address and Passcode\n\n";
	print MAIL "Dear $FirstName,\n\n";
        print MAIL "WELCOME to Surflocal Media: Marketing Network \n";
        print MAIL "Your ad is located at $baseurl$CityState \n";
        print MAIL "  \n";
	print MAIL "Your Surflocal Easy Editing Tool for your Surflocal Account is below.\n";
	print MAIL "You will need to use this link and the 9 digit passcode in the future to edit your ad.\n";
	print MAIL "When you get ready to update your web site or surflocal ad, simply click on this link (if your e-mail program does not";
	print MAIL " support clickable links, copy the link and paste it in the location bar of your";
	print MAIL " web browser. Be sure to copy the entire link):\n";
        print MAIL "  \n";
	print MAIL "";
	print MAIL "$TheLink\n";
	print MAIL "  \n";
        print MAIL "  \n";
        print MAIL " Put your passcode in the text box. Your passcode is $MyData{RandomNumber} \n";
	print MAIL "If you created a web site, there will be a small gold image at the bottom of your front page. Click on that dot to be taken to your passcode window.  At that window, you will only need the 9 digit code. That code is the last 9 numbers in your edit link above.  If you forget your passcode, that same window will have a link for you to request we send you a copy of your passcode.\n";
        print MAIL "  \n";
        print MAIL "You will receive your invoice for our services in your e-mail shortly.  If you need any assistance or have any questions, please feel free to contact me. \n";
        print MAIL "  \n";
        print MAIL "HAVE FUN with your new Surflocal Advertising! \n";
        print MAIL "  \n";     
        print MAIL "Go to https://www.surflocalmedia.com/office/video-library/slmv.html to view Visual Build and Edit Tutorials \n";
        print MAIL "  \n";
	print MAIL "Go to https://www.surflocalmedia.com/information/coding.html to view Extra html Coding for your ad \n";
        print MAIL "  \n";
        print MAIL "  \n";	
        #print MAIL "Agent\n";
        print MAIL "Customer Relations surflocalmedia.com\n";	
        print MAIL "agent\@surflocalmedia.com \n";	 
	close (MAIL);

#Mail the admin.
	open (MAIL, "|$mailprog $admin") || &Error("Can\'t open $mailprog in MailMe sub for admin! Reason: $!");
	print MAIL "Reply-to: SurfLocal Administrator <$admin>\n";
	print MAIL "To: Administrator <$admin>\n";
	print MAIL "From: Surflocal Administrator <$admin>\n";
	print MAIL "Subject: $BizName New Surflocal ad for $CityState\n\n";
	print MAIL "Dear David,\n\n";
	print MAIL "$BizName has made a new $AdType ad at $CityState $MyData{Zip}\n";
        print MAIL "Name: $FirstName  $MyData{LastName}\n";
        print MAIL "Address: $MyData{Address1}  Address 2: $MyData{Address2}  Phone: $MyData{Phone}\n";
        print MAIL "$TheLink\n";
        print MAIL "Passcode is $MyData{RandomNumber}\n";
        print MAIL "E-mail: $MyData{Email}\n";
        print MAIL "Thank you!\n";
	close(MAIL);

#Give the user feedback. This is the last time he'll be dealing with this program package
#in this session.
#Kill the cookie for future iterations.
&CookieHeader;
&SetCookies("User","");
&CookieFooter;
#Print SurfLocal header based on template.
&PHed;	
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
     print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=735>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";

print "<font size=+1><font color=000000><b><img src=\"https://surflocalmedia.com/images/password.jpg\">Congratulations $BizName! NOW SAVE THIS PAGE</font></center></b>\n";
print "<font color=000000><p><font size=-1><b>Save This Page or Print This Page and Keep it by your computer.<font color=000000><font size=-1>  Your information was sucessfully recorded, and your new Surflocal web site and ad are online.\n"; 
print "<br><font color=000000><font size=-1><img src=\"https://www.surflocalmedia.com/bullet-logo.gif\">(1) For Additional Help with Designing your Web site 
<a href=\"https://www.surflocalmedia.com/information/coding.html\"><font color=800000><font size=-1>(CLICK HERE)</font> </a> <font color=000000>Download a free program to edit and resize your photos, get additional design help. \n";
print "<br><br><font color=000000><font size=-1><img src=\"https://www.surflocalmedia.com/bullet-logo.gif\">(2) Your ad in $CityState is ready to use.  Click on the link to go there: ";
print "<a href=\"$baseurl$CityState\"><font color=800000><font size=-1>$baseurl$CityState </font></a><br>\n";

#If they built a Web page, they'll want to know how to get there
if ($AdType =~ /Plus/)
{
	$TheWeb = $baseurl . $CityState . "/" . $BizName . "/" . "index.html";
	print "<br><font color=000000><font size=-1><img src=\"https://www.surflocalmedia.com/bullet-logo.gif\">(3) Your New Surflocal web site is Online Now: Click the link to go there now. <a href=\"$TheWeb\"><font color=000000>$TheWeb</font></a><br>\n";
}
print "<br><font color=000000><font size=-1>In the future, if you ever want to edit your ad, you'll need the following link. ";
print "(it has also been e-mailed to $MyData{Email}) <br><br><font size=-1>Your passcode is <font color=800000>$MyData{RandomNumber} ";

print ":<p> <a href=\"$TheLink\"><font color=000000><font size=-1>$TheLink </font></a><br>\n";
	print "<br><b><font color=800000><font size=-1>REMEMBER!!</b> <font color=000000>Print This Page and Keep it by your computer, or Save this Page to your Desktop.\n";
        #print "<p><a href=\"https://www.surflocalmedia.com/payment/payment2.html\"><img src=\"/images/continue.jpg\" border=0></a></center><br>\n";

exit;
