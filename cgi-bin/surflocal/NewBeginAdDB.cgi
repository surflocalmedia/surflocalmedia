#!/usr/local/bin/perl5.22
######################
#          SURFLOCAL EASY WEB SITE, COUPON AND AD CREATOR PACKAGE HEADER
######################

#######################

#The suite requires three libraries. It will not function without them.
require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

####### VARIABLES #######
$newform = "cgi-bin/surflocal/NewBeginAdDB.cgi";
$IndexTemplate = "$TemplatesDir" . "IndexTemplate.html";
$HandleRequest = "cgi-bin/surflocal/NewBeginAdDB.cgi";
$Hed{T} = "Surflocal Ad Creation";
#########################

#These subs are in SurfLocalLib.pl
&Parse;
&ShortenValues;

#####################
&Disclaimer unless ($Action);
if ($Action eq "Agree") {&StartAd;}
if ($Action eq "Disagree") {&Disagree;}
if ($Action eq "GetUserInfo") {&GetUserInfo;}
if ($Action eq "RecordData") {&RecordData;}
exit;
#####################
#    SCRIPT WORK FLOW
#1) Disclaimer
#2) Businessname/AdType
#3) Set cookie, Get user information
#4) Make database
#5) Send to next script

####### PRINT RECORD STUFF
sub PrintRecordStuff
{
	#This subroutine is only called if the user messed something up in their
	#registration information. 
	#Receives errorcode from calling subroutine.
	$TheError = join(//,@_);
	
	#Print httpsd header
	&Header;
	#Print SurfLocal header (in templates folder)
	&PHed;
	
	#If the error contains a value, I want to report the error code to the
	#user to tell them what they screwed up.
	if ($TheError ne "")
	{
                print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
                print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br></center>\n";	
		print "<font size=+2><font color=000000><center>Some of your data was entered incorrectly <br></font>\n";
		print "<font color=000000><font size=-1>The error message:<b> $TheError</b><br>\n";
		print "You must correct this before you can continue.<br>\n";
	
	#If there's no error code, they've left something incomplete
	}else{
                print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
                print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br></center>\n";	
		print "<h2><font color=000000><center>Incomplete Data<br></h2>\n";
		print "<font color=000000>You didn't fill out all the required fields. You must fill them out before you can continue.<br>\n";
	}
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<center><table border=1><tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>Your first name: </td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=FirstName></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>Your last name:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=LastName></td></tr>\n";
	print "<tr><td colspan=2 BGCOLOR=\"FFFFFF\"><center><font size=-1>Billing address:</center></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>Address 1:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Address1></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>Address 2:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Address2></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>City:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=City value=\"$City\"></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>State:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><select name=State>\n";
	&GetStateList;
	print "</select></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>ZIP code:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Zip></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>Phone number with area code:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">(<input type=text size=3 name=Area>) <input type=text name=Prefix size=3>  -   <input type=text name=Number size=5></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><font size=-1>E-mail address:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Email></td></tr>\n";
	print "<tr><td colspan=2 BGCOLOR=\"FFFFFF\"><center><input type=submit value=\"Record my data\"></form></td></tr></table>\n";
	exit;
}


####### RECORD DATA
sub RecordData
{
	&GetCookieValues;
	if (($BizName eq "") || ($CityState eq ""))
	{
		#If I didn't get any cookie values, the user most likely has turned cookies off.
		&Error("You must enable your browser to receive cookies to use the SurfLocal Web suite. Please enable cookies and begin again.");
	}
	#Phone number comes in three different textboxes. Combine them here.
	$Phone = $in{Area} . "-" . $in{Prefix} . "-" . $in{Number};
	
	#If we're missing any required values, give the user the chance to fix them. This is necessary because we've
	#already recorded the BizName in our database, and it won't let them start again because of that.
	&PrintRecordStuff unless (($in{City}) && ($in{Address1}) && ($in{FirstName}) && ($in{LastName}) && ($in{Zip}) && ($in{Area}) && ($in{Prefix}) && ($in{Number}) && ($in{Email}));
	
	#I need a five-digit ZIP code; check for that and scold the user if I don't get it.
	if ($in{Zip} !~ /\d{5}/)
	{
		&PrintRecordStuff("Zip code must be an actual ZIP code. Please enter a correct ZIP code. DO NOT use extended Zip codes \(i.e.: 11111-111\)");
	}
	#Phone number must be all digits. If it's not, the user must pay.
	if ($Phone !~ /\d{3}-\d{3}-\d{4}/)
	{
		&PrintRecordStuff("Phone number MUST be an actual phone number.");
	}
	#Email must be an actual e-mail address -- or at least a really good fake.
	if ($in{Email}	!~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/)
	{
		&PrintRecordStuff("You must enter an actual e-mail address. The one you entered is not an e-mail address.");
	}	
	
	#### RANDOM NUMBER STUFF
	#My random number must be nine digits long. I seed it with the number
	#in $number.
	$number=61369;
	srand();
	#Use the time as a way to increase the seed's randomness.
	$time = `date +"%T"`;
	($hour,$minute,$second) = split(/:/, $time);
	$SeedNumber = "$hour" . "$second" . "$minute";
	#Add time to my random number
	$RandomNumber = int(rand($number)) + $SeedNumber;
	#To increase its randomness, multiply it by itself
	$RandomNumber = ($RandomNumber * $RandomNumber);
	#Get the length of it.
	$ItsLength = length($RandomNumber);
	#If it's greater than 9 digits in length, I have to chop it down to size.
	if ($ItsLength > 9)
	{
		until (length($RandomNumber) == 9)
		{
			#Chop hacks off the last character.
			chop($RandomNumber);
		}
	}
	#If the number is less than 9 characters, I have to build it up.
	elsif ($ItsLength < 9)
	{
		$Count = 0;
		until (length($RandomNumber) == 9)
		{
			$Count++;
			$AddNumber = int(rand($Count));
			$RandomNumber .= $AddNumber;
		}
	}
	##### END RANDOM NUMBER STUFF
	
	#create new directory for this businessname. 
	#$dirname comes from the cookies sub in SurfLocalLib
	mkdir ($dirname,0755)||&Error("Can't make directory $dirname. Reason:$!");
        chmod (0755, "$SAVE_DIRECTORY\/$Filename");
	
	#&OpenMyDatabase is in the SurfLocalLib 
	&OpenMyDatabase;
	#Add the values gotten from the user entering his data.
	$MyData{"FirstName"} = $in{FirstName};
	$MyData{"LastName"} = $in{LastName};
	$MyData{"Address1"} = $in{Address1};
	$MyData{"Address2"} = $in{Address2} if ($in{Address2});
	$MyData{"Zip"} = $in{Zip};
	$MyData{"Phone"} = $Phone;
	$MyData{"Email"} = $in{Email};
	$MyData{"RandomNumber"} = $RandomNumber;
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";	
	print "<font size=+1><b><font color=800000><img src=\"https://surflocalmedia.com/images/info-recorded.jpg\">Your information was recorded: $BizName!<p></font></b>\n";

	
	#Most of the other scripts use this call in the beginning. This one couldn't because it
	#hadn't yet assigned the necessary data. Call it here and get the AdType.
	&OpenCityDatabase;
	$MyAdType=$CityData{$BizName};
	&CloseCityDatabase;
	if ($MyAdType =~ /Button/)
	{
		$NextScript = $ButtonScript;
	}
	elsif ($MyAdType =~ /Text/)
	{
		$NextScript = $TextScript;
	}
	elsif ($MyAdType =~ /Coupon/)
	{
		$NextScript = $CouponScript;
	}
	else
	{
		&Error("Can't determine what kind of ad \'$MyAdType\' is.");
	}
	print "<form action=$NextScript method=POST>\n";
	print "<input type=submit value=\"Click here to go to the next step\"></form></td></tr></table></center>\n";
	exit;
}
####### GETUSERINFO
sub GetUserInfo
{
	#Check to see that fields are filled out
	&Error("You must enter an ad type and business name.") unless (($AdType) && ($BizName));
	$Statey = $Abbrevs{$State};
	$CityState = $City . $Statey;
	
	
	#This sub is in SurfLocalLib.pl
	#This will create the database if it doesn't already exist.
	&OpenCityDatabase;
	if (defined $CityData{$BizName})
	{
		#&Error("The business name $BizName already exists in our database. You have either already registered, or someone already owns that name. Please select a new name or contact that business.");
	}
	else 
	{
		#The AdType is stored in the MainData for easy perusal, not in the individual database.
		$CityData{$BizName} = $AdType;
	}
	#In SurfLocalLib.pl
	&CloseCityDatabase;
	
	#If we've gotten this far, the business name doesn't exist. Set the cookie with the businessname and citystate.
	$TheCookieInfo = $BizName . "\|" . $CityState;
	&CookieHeader;
	&SetCookies("User",$TheCookieInfo);
	&CookieFooter;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";		
	#Get user's information to populate his individual database.
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"></center>\n";
	print "<b><font color=000000><center><font size=+2>Next: Your Billing Information</font></b></center>\n";
	print "<font color=000000><b>To build your ad, we must first get some information from you.</b> ";
	print "<font color=000000>If you have not pre-paid or have a special offer from Surflocal,  you will receive a invoice for your services via e-mail shortly. ";
	print "<font color=000000>All fields are required.\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<center><table width=550 border=1><tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">Your first name: </td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=FirstName></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">Your last name:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=LastName></td></tr>\n";
	print "<tr><td colspan=2 BGCOLOR=\"FFFFFF\"><center>Billing Address:</center></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">Address:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Address1></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">City:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=City value=\"$City\"></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">State:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><select name=State>\n";
	&GetStateList;
	print "</select></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">ZIP code:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Zip></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">Phone number with area code:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">(<input type=text size=3 name=Area>) <input type=text name=Prefix size=3>  -   <input type=text name=Number size=5></td></tr>\n";
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">E-mail address:</td><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><input type=text name=Email></td></tr>\n";
	print "<tr><td colspan=2 BGCOLOR=\"FFFFFF\"></center><br><input type=submit value=\"Record my data\"><br></form></td></tr></table>\n";
	exit;
}

####### GET STATE LIST
sub GetStateList
{
	for ($i=0;$i<=50;$i++)
	{
		print "<option value=\"$StateAbs[$i]\">$StateAbs[$i]</option>\n";
	}
}
	

####### DISCLAIMER
sub Disclaimer
{
	#Simply opens up the disclaimer from the templates directory and restates it
	#for the user.
    $AdType = $in{0};
    $State = $in{'1'};
    $City = $in{'2'};
    &Header;
    $DisclaimerLocation = "$TemplatesDir" . "Disclaimer";
    open(DISC,"$DisclaimerLocation") || &Error("Can't open $DisclaimerLocation in Disclaimer sub. Reason: $!");
    @Disc=<DISC>;
    close(DISC);
    foreach (@Disc)
    {
    	#This is really the only reason we can't dispense with the &SubstituteValues sub in
    	#the SurfLocalLib
    	&SubstituteValues;
       print "$_";
    }
}

####### START AD
sub StartAd
{
    &Header;
    &PHed;
    print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
    print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
<tr><td>\n";
    	
    print "<b><br><p><font color=000000><font size=+1>Step One: Ad Type</b><p><br></font>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=GetUserInfo>\n";
    print "<input type=hidden name=State value=\"$State\">\n";
    print "<input type=hidden name=City value=\"$City\">\n";
    if ($AdType eq "Button")
    {
	print " <input type=radio name=AdType value=ButtonOnly><i><font color=000000><b>Button Ad</i></b><br><br><br>\n";
	print " <input type=radio name=AdType value=ButtonPlus><i><b>Button Ad and Webpage</i></b><br><br>\n";
    }
    elsif ($AdType eq "TextAd")
    {
        print " <input type=radio name=AdType value=TextAdOnly><i><b>Text Ad</i></b><br><br>\n";
	print " <input type=radio name=AdType value=TextAdPlus><i><b>Text Ad and Webpage</i></b> <br></i>\n";
        
        
    }
    elsif ($AdType eq "Coupon")
    {
        print " <input type=radio name=AdType value=CouponOnly><b>Marketing Ad</b><br><br>\n";
    	print " <input type=radio name=AdType value=CouponPlus><b>Marketing Ad and Webpage</b> <br>\n";
    }
    else
    {
        &Error("The ad type specified in the input, $AdType, is not a valid ad type.");
    }
        print "<p><br><b><font color=000000><font size=+1>Step Two: Enter the Name of Your Industry<br></b><br></b></font>\n"; 
        print "</center><font color=000000><font size=-1><b>Your Industry Name:</b><br> <input type=text name=BizName  size=50><br><font size=-1> <b>Example: <font color=800000>myindustryname</font>   (all lower case, no spaces)<br>
           (So, type this in small letters all together with no spaces at the end</font>) <br><br>\n";
    
        print "<input type=submit value=\"Continue to the next step.\"></center>\n";
        print "</form></td></tr></table>\n";
    exit;
}


####### ENTER BIZ NAME
sub EnterBizName
{
    &Error("You must select one of the two choices on the previous page.") unless ($AdType ne "");
    if ($AdType =~ /Button/)
    {
        $NextScript = $ButtonScript;
    }
    elsif ($AdType =~ /Text/)
    {
        $NextScript = $TextScript;
    }
    elsif ($AdType =~ /Coupon/)
    {
	$NextScript = $CouponScript;
    }
    else
    {
        &Error("Can't determine what kind of ad \'$AdType\' is.");
    }
    
    &Header;
    print "<h1>Step two: Enter your business name</h1>\n";
    
    print "<form action=$NextScript method=POST>\n";
    &PrintHiddenValues;
    
    print "Your e-mail address: <input type=text name=Email><br>\n";
    print "<input type=submit value=\"Click here to continue\"> ";
    print "<input type=reset value=\"Clear form and start over\"><br>\n";
    print "</form>\n";
    exit;
}





####### DISAGREE
sub Disagree
{
    &Header;
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
    #print "Got to disagree beginning.";
    
    $SecondChance = "$newform";
    &PHed;
    print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
<tr><td>\n";
    print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
    print "<h1><font color=000000><center>We Cannot Process <br>Your Request</center></h1></center>\n";
    print "<font color=000000>Thank you for your interest in surflocalmedia.com. Unfortunately, we cannot process your ";
    print "request if you disagree with our <a href=\"https://www.surflocalmedia.com/terms.html\" target=\"new\"><font color=800000>Terms and Conditions for Placing an Ad.<br></font></a><br>\n";
    print "<font color=000000>For more information on our terms and conditions, please feel free ";
    print "to <a href=\"mailto:agent\@surflocalmedia.com\"> <font color=800000>E-mail the administrator.</font></a> or Call us at 806 340 6761  ";
    exit;
}
