#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 1996-2021
# See suite header in BeginAdDB script
# for copyright and usage information.
#######################

#The suite requires three libraries. It will not function without them.
require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
####### VARIABLES #######
$newform = "/cgi-bin/surflocal/Edit.cgi";
$IndexTemplate = "$TemplatesDir" . "IndexTemplate.html";
$HandleRequest = "/cgi-bin/surflocal/BeginAdDB.cgi";
$Hed{T} = "Your Editing Tools Menu";

#########################

#These subs are in SurfLocalLib.pl
&Parse;
&ShortenValues;

#####################
&PassGamut unless ($Action);
if ($Action eq "Agree") {&StartAd;}
if ($Action eq "VerifyPasscode") {&VerifyPasscode;}
if ($Action eq "GetUserInfo") {&GetUserInfo;}
if ($Action eq "MailPasscode") {&MailPasscode;}
if ($Action eq "ChooseEditAction") {&ChooseEditAction;}
if ($Action eq "RecordData") {&RecordData;}
if ($Action eq "ContactModify") {&ContactModify;}
exit;

####### CHOOSE EDIT ACTION
sub ChooseEditAction
{
	
	#
	&Error("You must select a type of action to take before proceeding. Please go back and do so.") unless ($in{EditAction});
	#EditAction=
	#	EditWebPage
	#	Edit[AdType]
	#	Create[AdType]
	#	DeleteAd => AdToDelete (WebPage|[AdType])
	#	ModifyContactInfo
	&GetCookieValues;
	$EditAction=$in{EditAction};
	if ($EditAction eq "DeleteAd")
	{
		&DeleteWarn;
		#Needs to delete information from user's database for each specific ad type,
		#then it needs to delete that information from the appropriate city ad database.
		#Need to think about what to do if they delete their primary ad.
	}
	if ($EditAction eq "ModifyContactInfo")
	{
		&ModifyContactInfo;
		#Lets them change their contact information; E-mails administrator
		#giving him the notice that the user has changed his contact information,
		#then records old information in a separate database in case something
		#freaky is going on.
	}
	if ($EditAction =~ /Edit/)
	{
		&EditThis;
		#Take them to separate (but almost identical) script that deals with their
		#existing data instead of creating the data from scratch. FinalizeEdit script
		#will simply confirm that the action they've taken is what they really want.
	}
	if ($EditAction =~ /Create/)
	{
		&CreateThis;
		#Take them to regular script that lets them add an ad and finalize it
		#using the main finalize script, which treats them differently because
		#this is a subsequent ad.
	}
	
}

####### MODIFY CONTACT INFO
sub ModifyContactInfo
{
	&Header;
	&PHed;
	&OpenMyDatabase;
	print "<h1>Modify contact info</h1>\n";
	print "WARNING! Editing your contact information will change the information with which SurfLocal Media ";
	print "contacts you. Your old information will be stored in a separate file, so it won't be completely lost, ";
	print "but it <b><i>will</i></b> be a major hassle for <b>you</b> if you need us to retrieve the data for you.<br>\n";
	print "Edit your contact information with extreme caution to avoid problems later on.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ContactModify>\n";
	print "<table border=1><tr><td>Your first name: </td><td><input type=text name=FirstName value=\"$MyData{FirstName}\"></td></tr>\n";
	print "<tr><td>Your last name:</td><td><input type=text name=LastName value=\"$MyData{LastName}\"></td></tr>\n";
	print "<tr><td colspan=2><center>Billing address:</center></td></tr>\n";
	print "<tr><td>Address 1:</td><td><input type=text name=Address1 value=\"$MyData{Address1}\"></td></tr>\n";
	print "<tr><td>Address 2:</td><td><input type=text name=Address2 value=\"$MyData{Address2}\"></td></tr>\n";
	print "<tr><td>City:</td><td><input type=text name=City value=\"$MyData{City}\"></td></tr>\n";
	print "<tr><td>State:</td><td><select name=State>\n";
	&GetStateList;
	print "</select></td></tr>\n";
	print "<tr><td>ZIP code:</td><td><input type=text name=Zip value=\"$MyData{Zip}\"></td></tr>\n";
	print "<tr><td>Phone number with area code:</td><td>(<input type=text name=Phone value=\"$MyData{Phone}\"></td></tr>\n";
	print "<tr><td>E-mail address:</td><td><input type=text name=Email value=\"$MyData{Email}\"></td></tr>\n";
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	&CloseMyDatabase;
}
####### GET STATE LIST
sub GetStateList
{
	for ($i=0;$i<=50;$i++)
	{
		if ($StateAbs[$i] eq $MyData{State})
		{
			print "<option value=\"$StateAbs[$i]\" SELECTED>$StateAbs[$i]</option>\n";
		}else{
			print "<option value=\"$StateAbs[$i]\">$StateAbs[$i]</option>\n";
		}
	}
}

####### CREATE THIS
sub CreateThis
{
	#If user chose to create an ad, I need to set a cookie with that ad type and biz name,
	#then send him onto a script specifically for the creation of that ad type.
	#This means SubsequentPage.cgi,SubsequentCoupon.cgi,SubsequentButton.cgi,SubsequentText.cgi  --- Changed to TXT file in this script ---
	#From there, SubsequentFinalize.cgi This will simplify the processes inside the other scripts.
	$ThisAdType=$EditAction;
	$ThisAdType=~ s/Create//gi;
	if ($ThisAdType =~ /Button/){$NextScript = "SubsequentButton.txt";} 
	if ($ThisAdType =~ /TextAd/){$NextScript = "SubsequentText.txt";}
	if ($ThisAdType =~ /Coupon/){$NextScript = "SubsequentCoupon.txt";}
	if ($ThisAdType =~ /WebPage/){$NextScript = "SubsequentPage.txt";}
	&DropCreateCookie;
	&PHed;
	print "<h1>All the hard stuff is done! Now we're ready to create your $ThisAdType ad</h1>\n";
	print "<form action=$NextScript method=POST>\n";
	print "<input type=submit value=\"Click here to begin\"></form>\n";
	exit;
}
sub DropCreateCookie
{
	#my($Kinda) = join(//,@_);
	$TheCookieInfo = $ThisAdType;
	&CookieHeader;
	&SetCookies("Subsequent",$TheCookieInfo);
	&CookieFooter;
	#Cookie "Subsequent" contains: AdType|BizName
}

####### EDIT THIS
sub EditThis
{
	$ThisAdType=$EditAction;
	$ThisAdType =~ s/Edit//gi;
	#&Header;
	#print "Got this kind of ad: $ThisAdType.\n";
	if ($ThisAdType =~ /Button/){$NextScript = "/cgi-bin/surflocal/ButtonEdit.cgi";}
	if ($ThisAdType =~ /TextAd/){$NextScript = "/cgi-bin/surflocal/TextEdit.cgi";}
	if ($ThisAdType =~ /Coupon/){$NextScript = "/cgi-bin/surflocal/CouponEdit.cgi";}
	if ($ThisAdType =~ /WebPage/){$NextScript = "/cgi-bin/surflocal/PageEdit.cgi";}
	&DropEditCookie;
	
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br></center>\n";	
	print "<h2><font color=000000>We're ready to Update!</h2>\n";
	print "<form action=$NextScript method=POST>\n";
	print "<input type=submit value=\"Click here to begin\"></form></center>\n";
	exit;
}

####### DROP EDIT COOKIE
sub DropEditCookie
{
	#my($Kinda) = join(//,@_);
	$TheCookieInfo = $ThisAdType;# . "\|" . $Kinda;
	&CookieHeader;
	&SetCookies("Edit",$TheCookieInfo);
	&CookieFooter;
}


####### DELETE WARN
sub DeleteWarn
{
	$Hed{Bg}="red";
	$Hed{FontColor}="000040";
	$Hed{Font}="Verdana,Arial,Helvetica";
	$Hed{T}="WARNING! No undo for this action!";
	&Header;
	print "<h1>WARNING! Delete has no undo!</h1>\n";
	print "Are you sure you want to delete your $in{AdToDelete} ad? You will <b>NOT</b> be able to undo this ";
	print "action once you have taken it.<br>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ConfirmDelete>\n";
	print "<input type=hidden name=AdToDelete value=\"$in{AdToDelete}\">\n";
	print "<input type=radio name=Confirmation value=Yes> Yes. I want to DELETE my $in{AdToDelete} ad.<br>\n";
	print "<input type=radio name=Confirmation value=No SELECTED> NO! I DO NOT want to delete my $in{AdToDelete} ad.<br>\n";
	print "<input type=submit value=\"Execute the choice I have made above\"></form>\n";
	exit;
}

####### MAIL PASSCODE
sub MailPasscode
{
	#action=MailPasscode\&CityState=$CityState\&BizName=$BizName\">"
	&Error("You must provide a city and business name") unless (($in{CityState}) && ($in{BizName}));
	$CityState=$in{CityState};
	$BizName=$in{BizName};
	$TheDatabase = $basedir . $CityState . "/" . $BizName . "/" . "Database.db";
use DB_File;
	dbmopen(%MyData,$TheDatabase,0666) || &Error("Can't open the database for $BizName. Reason: $!");
	$EmailTo = $MyData{Email};
	$FirstName = $MyData{FirstName};
	$TheLink = "cgi-bin/surflocal/Edit.cgi" . "\?" . $CityState . "\&" . "$BizName" ;
	$TheLink =~ s/ /\%20/gi;
	$TheCode=$MyData{RandomNumber};
	$TheLink = $baseurl . $TheLink;
	dbmclose %MyData;
	open (MAIL, "|$mailprog $EmailTo") || &Error("Can\'t open $mailprog in MailPasscode sub! Reason: $!");
	print MAIL "Reply-to:Surflocal Media Administrator <$admin>\n";
	print MAIL "From:Surflocal Media Administrator <$admin>\n";
	print MAIL "To: $FirstName <$EmailTo>\n";
	print MAIL "Subject: $BizName Surflocal Media Passcode\n\n";
        
	print MAIL "Dear $FirstName,\n\n";
        print MAIL "You will receive this every time your advertisement is submitted to one of the major search engines.   \n";
        print MAIL "  \n";
        
        print MAIL "Your Passcode for your Surflocal Media Advertising is below. You will need to use this link and the 9 digit passcode to edit your account, simply click on this link\n";
	print MAIL "  \n";
        print MAIL "  \n";
	print MAIL "Editing Tools Link: $TheLink\n";
        print MAIL "  \n";
        print MAIL "  \n";
        print MAIL "Put your passcode in the text box. Your passcode is $TheCode (make sure there is no extra spaces before or after the passcode)\n";
        print MAIL "  \n";
	print MAIL "or on your ad there will be a small gold image on your front page. Click on that dot to be taken to your pass code window. At that window, you will only need to enter the 9 digit code.  If you forget your pass code, that same window will have a link for you to request that we send you a copy of your pass code. With your pass code, you can access your account from any internet ready computer in the world.\n";
        print MAIL "  \n";
        print MAIL "  \n";
        print MAIL "Thank you for advertising with Surflocalmedia.com \n";	
        print MAIL "  \n";	
        #print MAIL "1-806-340-6761 \n";
        print MAIL "Customer Relations \n";	
        print MAIL "agent\@surflocalmedia.com \n";	 	        
close (MAIL);
	&Header;
	&PHed;
       
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<font size=+1><font color=800000><img src=\"https://surflocalmedia.com/images/password.jpg\"><b> PASSCODE SENT</b> \n";
	print "<font color=000000>Your passcode has been e-mailed to <b>$EmailTo</b>.\n";
	print "<p></center><font color=000000>That e-mail will contain the link to your editing tools and your passcode. If you do not receive the e-mail within a few minutes, ";
	print "contact the <a href=mailto:$admin><font color=800000>Surflocal Media System Administrator</font></a><br><br>\n";
        print "<center><font size=+2><a href=\"https://www.surflocalmedia.com\"><font size=+2><font color=000000>Click to go back to Surflocal Media</font></a>\n";   
	exit;
}

####### PASS GAMUT
sub PassGamut
{
	&Error("This program will not operate without input") unless (($in{0}) && ($in{1}));
	#$TheLink = $baseurl . "Edit.cgi" . "\?" . $CityState . "\&" . "$BizName" . "\&" . $MyData{RandomNumber};
    	$CityState = $in{0};
    	$BizName = $in{'1'};
    	$Password = $in{'2'};
    	if ($Password eq "")
    	{
    		&Header;
    		&PHed;
       print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
     
    		print "<form action=$newform method=POST>\n";
    		print "<input type=hidden name=action value=VerifyPasscode>\n";
    		print "<input type=hidden name=CityState value=\"$CityState\">\n";
    		print "<input type=hidden name=BizName value=\"$BizName\">\n";
                print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
                print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
                <tr><td>\n";
                print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
    		print "<font size=+1><font color=000000><b>Enter your Surflocal Media Passcode: $BizName</b><p>\n";
    		print "<font color=000000>When you signed up with Surflocal Media, you received a passcode to enable you access ";
    		print "<font color=000000>your Editing Tools. Enter that passcode in the box below to continue.<p>";
    		print "</center><font color=000000>Enter Passcode:</b> <input type=text name=Passcode><p><input type=submit value=\"Submit Passcode\"></form><br>\n";
                print "<font color=000000>If you forgot your passcode, click on \"I forgot my passcode\" to have it emailed to you. \n";
    		print "<a href=\"$newform?action=MailPasscode\&CityState=$CityState\&BizName=$BizName\">";
    		print "<font color=800000><b>I forgot my passcode</b></font></a></center><br><br>\n";
                print "<center><font size=+2><a href=\"https://www.surflocalmedia.com\"><font color=000000>Click to go back to Surflocal Media</font></a>\n";
    	}
    	else
    	{
    		&VerifyPasscode;
    	}
    	exit;
}

####### CREATE COOKIE
sub CreateCookie
{
	$TheCookieInfo = $BizName . "\|" . $CityState;
	&CookieHeader;
	&SetCookies("User",$TheCookieInfo);
	&CookieFooter;
}
	
####### VERIFY PASSCODE
sub VerifyPasscode
{
	$BizName=$in{BizName} if ($in{BizName});
	$CityState=$in{CityState} if ($in{CityState});
	$Password = $in{Passcode} if ($in{Passcode});
	$TheDatabase = $basedir . $CityState . "/" . $BizName . "/" . "Database.db";
use DB_File;
	dbmopen(%MyData,$TheDatabase,0666) || &Error("Can't open the database for $BizName in $CityState. Reason: $!");
	if ($Password ne $MyData{RandomNumber})
	{
		&Header;
		&PHed;
                print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
                print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
                <tr><td>\n";
                print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
		print "<font size=+1><font color=000000> PASSCODE MISMATCH\n";
		print "<font color=000000>The passcode you entered for $BizName did not match the one in our database.<br>\n";
		#print "(Comment this out: Wanted: $MyData{RandomNumber} . Got: $Password)\n";
		print "<form action=$newform method=POST>\n";
		print "<input type=hidden name=action value=VerifyPasscode>\n";
		print "<input type=hidden name=CityState value=\"$CityState\">\n";
    		print "<input type=hidden name=BizName value=\"$BizName\">\n";
		print "</center>Passcode: <input type=text name=Passcode><p><input type=submit value=\"Submit Passcode\"></form>\n";
                print "<a href=\"$newform?action=MailPasscode\&CityState=$CityState\&BizName=$BizName\">\n";
    		print "<font color=800000><font size=-1>I forgot my passcode</font></a>\n";
    		print "<p><font size=+1><font color=000000>If you forgot your passcode, click on \"I forgot my passcode\" to have it emailed to you \n";
    		
                print "or contact the <a href=mailto:$admin?Subject=LoginTrouble>Administrator</a> for help.<br>\n";
	}
	else
	{
		&CreateCookie;
		&PrintAdChoices;
	}
}

####### PRINT AD CHOICES
sub PrintAdChoices
{
	#&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<font size=+2><font color=000000>Welcome to Your Editing Tools, <font color=800000>$BizName!<p></font></center>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ChooseEditAction>\n";
	&OpenCityDatabase;
	$AdType=$CityData{$BizName};
	&CloseCityDatabase;
               print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";

print "<center><table border=0 width=100%><tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"> \n";
	if ($AdType =~ /Plus/)
	{
		$TheAd = $AdType;
		$TheAd =~ s/Plus//gi;
		print "<font color=000000>You have a Private Marketing Category and a Multimedia Ad with us. To update one of your ";
		print "items, select your choice below.<br><br>\n";
		print " <input type=radio name=EditAction value=\"Edit$TheAd\"> Update Your Marketing Ad:  <br><br>\n";
		print " <input type=radio name=EditAction value=\"EditWebPage\"> Update Your Marketing Page : <br></td></tr>\n";
	}
	else
	{

		$TheAd=$AdType;
		print "</center><b>To edit your Marketing, click the button below.</b><br><br>\n";
		print "</center>Edit your Marketing Ad: <input type=radio name=EditAction value=\"Edit$AdType\"><br><br>\n";
             
	}
	if ($MyData{SubsequentAd})
	{
		print "<tr><td><b>Edit your $MyData{SubsequentAd} ad</b>.<br>\n";
		$Ad2=$MyData{SubsequentAd};
		print "Edit $Ad2 ad: <input type=hidden name=EditAction value=\"Edit$Ad2\"></td></tr>\n";
	}
	if ($MyData{SubsequentAd2})
	{
		print "<tr><td><b>Edit your $MyData{SubsequentAd2} ad</b>.<br>\n";
		$Ad2=$MyData{SubsequentAd2};
		print "Edit $MyData{SubsequentAd2} ad: <input type=hidden name=EditAction value=\"Edit$MyData{SubsequentAd2}\"></td></tr>\n";
	}
	else
	{
		#print "<tr><td><b>At SurfLocal Media, you also have the opportunity to create more ads in addition to the $AdType ad ";
		#print "you already own.</b> To make one of these additional ads, select its type below. <br>\n";
		#if (($TheAd !~ /Button/) && ($MyData{SubsequentAd2} !~ /Button/) && ($MyData{SubsequentAd} !~ /Button/))
		#{
		#	print "Create Button ad: <input type=radio name=EditAction value=\"CreateButton\"><br>\n";
		#}
		#if (($TheAd !~ /Text/) && ($MyData{SubsequentAd2} !~ /Text/) && ($MyData{SubsequentAd} !~ /Text/))
		#{
		#	print "Create Text ad: <input type=radio name=EditAction value=\"CreateTextAd\"><br>\n";
		#}
		#if (($TheAd !~ /Coupon/) && ($MyData{SubsequentAd2} !~ /Coupon/) && ($MyData{SubsequentAd} !~ /Coupon/))
		#{
		#	print "Create Coupon ad: <input type=radio name=EditAction value=\"CreateCoupon\"><br>\n";
		#}
		#if (($TheAd !~ /Plus/) && ($MyData{SubsequentAd2} !~ /WebPage/) && ($MyData{SubsequentAd} !~ /WebPage/))
		#{
		#	print "Create Web page: <input type=radio name=EditAction value=\"CreateWebPage\"><br>\n";
		#}
		#print "</td></tr>\n";
	}
	######### DELETE AD (Don't wanna mess with it right now)
	#print "<tr><td><b>Delete an ad</b><br>\n";
	#print "If you have an existing ad you'd like to delete, click the button to the left of the list and then select ";
	#print "the ad you want to delete from the list below.<br>\n";
	#print "Delete ad: <input type=radio name=EditAction value=\"DeleteAd\"> ";
	#print "<select name=AdToDelete>";
	#if ($AdType =~ /Plus/)
	#{
	#	print "<option value=\"WebPage\">Web page</option>\n";
	#}
	#print "<option value=\"$TheAd\">$TheAd</option>\n";
	#if ($MyData{SubsequentAd})
	#{
	#	print "<option value=\$Ad2\">$Ad2</option>\n";
	#}
	#print "</select></td></tr>\n";
	############################
	
	########## MODIFY CONTACT INFO (Also don't wanna mess with this)
	#print "<tr><td><b>Modify contact information</b><br>\n";
	#print "If your contact information has changed, select the button below to update our database.<br>\n";
	#print "Modify contact information: <input type=radio name=EditAction value=\"ModifyContactInfo\"></td></tr>\n";
	############################
	
	print "<tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\"><br><input type=submit value=\"Continue\"></form></td></tr></table>\n";
	dbmclose %MyData;
	exit;
}	

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
		print "<h1>Some of your data was entered incorrectly</h1>\n";
		print "The error message:<b>$TheError</b><p>\n";
		print "You must correct this before you can continue.<br>\n";
	
	#If there's no error code, they've left something incomplete
	}else{
		print "<h1>Incomplete data</h1>\n";
		print "You didn't fill out all the required fields. You must fill them out before you can continue.<br>\n";
	}
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<table border=1><tr><td>Your first name: </td><td><input type=text name=FirstName value=\"$in{FirstName}\"></td></tr>\n";
	print "<tr><td>Your last name:</td><td><input type=text name=LastName value=\"$in{LastName}\"></td></tr>\n";
	print "<tr><td colspan=2><center>Billing address:</center></td></tr>\n";
	print "<tr><td>Address 1:</td><td><input type=text name=Address1 value=\"$in{Address1}\"></td></tr>\n";
	print "<tr><td>Address 2:</td><td><input type=text name=Address2 value=\"$in{Address2}\"></td></tr>\n";
	print "<tr><td>City:</td><td><input type=text name=City value=\"$City\"></td></tr>\n";
	print "<tr><td>State:</td><td><select name=State>\n";
	&GetStateList;
	print "</select></td></tr>\n";
	print "<tr><td>ZIP code:</td><td><input type=text name=Zip value=\"$in{Zip}\"></td></tr>\n";
	print "<tr><td>Phone number with area code:</td><td>(<input type=text size=3 name=Area value=\"$in{Area}\">)";
	print " <input type=text name=Prefix size=3 value=\"$in{Prefix}\"><input type=text name=Number size=3 value=\"$in{Number}\"></td></tr>\n";
	print "<tr><td>E-mail address:</td><td><input type=text name=Email value=\"$in{Email}\"></td></tr>\n";
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	exit;
}


####### RECORD DATA
sub RecordData
{
	&GetCookieValues;
	if (($BizName eq "") || ($CityState eq ""))
	{
		#If I didn't get any cookie values, the user most likely has turned cookies off.
		&Error("You must enable your browser to receive cookies to use the SurfLocal Media Ad Creation Suite. Please enable cookies and begin again.");
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
	#in $number. Ideally, I'd seed it with a random number, but this is secure
	#enough.
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
			#Chop is as brutal as it sounds. It just hacks off the last character.
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
	mkdir ($dirname,0777)||&Error("Can't make directory $dirname. Reason:$!");
	
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
	print "<h1>Your information was recorded!</h1>\n";
	print "Great! Now you're on your way to making a Promote Local Business ad!. The next step will begin taking you ";
	print "through the process of creating your ad. Please read all the instructions carefully, and making your ad ";
	print "will be a cinch!\n";
	
	#Most of the other scripts use this call in the beginning. This one, however, couldn't because it
	#hadn't yet assigned the necessary data. Therefore, Call it here and get the AdType.
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
	print "<input type=submit value=\"Click here to go to the next step\"></form>\n";
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
		&Error("The business name $BizName already exists in our database. You have either already registered, or someone already owns that name. Please select a new name or contact that business.");
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
	#Get user's information to populate his individual database.
	print "<h1>Next step: User information</h1>\n";
	print "To build your ad, we must first get some information from you. Please rest assured that ";
	print "your information is safe at SurfLocal Media. We will NEVER share your information with any other ";
	print "parties. It is for SurfLocal Media use only, and you will never receive any solicitations because of ";
	print "the information you submit here.<br>All fields except for Address 2 are required.\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<table border=1><tr><td>Your first name: </td><td><input type=text name=FirstName></td></tr>\n";
	print "<tr><td>Your last name:</td><td><input type=text name=LastName></td></tr>\n";
	print "<tr><td colspan=2><center>Billing address:</center></td></tr>\n";
	print "<tr><td>Address 1:</td><td><input type=text name=Address1></td></tr>\n";
	print "<tr><td>Address 2:</td><td><input type=text name=Address2></td></tr>\n";
	print "<tr><td>City:</td><td><input type=text name=City value=\"$City\"></td></tr>\n";
	print "<tr><td>State:</td><td><select name=State>\n";
	&GetStateList;
	print "</select></td></tr>\n";
	print "<tr><td>ZIP code:</td><td><input type=text name=Zip></td></tr>\n";
	print "<tr><td>Phone number with area code:</td><td>(<input type=text size=3 name=Area>) <input type=text name=Prefix size=3><input type=text name=Number size=3></td></tr>\n";
	print "<tr><td>E-mail address:</td><td><input type=text name=Email></td></tr>\n";
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
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

####### START AD
sub StartAd
{
    &Header;
    &PHed;
    print "<h1>Step one: Choosing the type of service you want</h1>\n";
    print "Select one of the choices below and continue.<br>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=GetUserInfo>\n";
    print "<input type=hidden name=State value=\"$State\">\n";
    print "<input type=hidden name=City value=\"$City\">\n";
    if ($AdType eq "Button")
    {
	print "<input type=radio name=AdType value=ButtonOnly>Marketing link<br>\n";
	print "<input type=radio name=AdType value=ButtonPlus> Marketing link and Webpage<br>\n";
    }
    elsif ($AdType eq "TextAd")
    {
        print "<input type=radio name=AdType value=TextAdOnly>Marketing link <br>\n";
	print "<input type=radio name=AdType value=TextAdPlus>Marketing link and Webpage<br>\n";
    }
    elsif ($AdType eq "Coupon")
    {
        print "<input type=radio name=AdType value=CouponOnly>Marketing Ad<br>\n";
	print "<input type=radio name=AdType value=CouponPlus> Marketing Ad and Webpage<br>\n";
    }
    else
    {
        &Error("The ad type specified in the input, $AdType, is not a valid ad type.");
    }
    print "<font size=+2>Enter your business name\n";
    print "<font size=-1><b>Everything on SurfLocal Media revolves around the name of your business -- after all, ";
    print "it's what makes you unique! Enter it below to continue to the next step.<Br>\n";
    print "Your business name: <input type=text name=BizName><br>\n";
    print "<input type=submit value=\"Press this button to continue to the next step.\">\n";
    print "<input type=reset value=\"Reset this form and start over\">\n";
    print "</form>\n";
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
    #print "Got to disagree beginning.";
    
    $SecondChance = "$newform";
    &PHed;
    print "<h1>Thank you</h1>\n";
    print "Thank you for your interest in SurfLocal Media. Unfortunately, we cannot process your ";
    print "request if you disagree with our <a href=$SecondChance>terms and conditions</a>. <br>\n";
    print "If you would like to further discuss the terms and conditions, please feel free ";
    print "to <a href=mailto:$Administrator>e-mail the administrator.</a> Thank you and God ";
    print "bless.";
    exit;
}
