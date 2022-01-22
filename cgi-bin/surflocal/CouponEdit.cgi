#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-present
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

####### SET VARIABLES
$newform = "/cgi-bin/surflocal/CouponEdit.cgi";
$TemplatesFile = "$TemplatesDir" . "CouponTemplates.html";
$ImageWidth=250;
$Hed{T} = "Editing Your Coupon";
$FinishScript = "/cgi-bin/surflocal/FinalizeEdit.cgi";
&Parse;
&GetCookieValues;
#&Error("You must first go through the registration process.") if (($BizName eq "") || ($CityState eq ""));
$Action=$in{action};

####### CONDITIONALS
&GetDecision unless ($Action);
if ($Action eq "CalledFromEdit") {&PreviewCoupon;}
if ($Action eq "SelectEditItem") {&SelectEditItem;}
if ($Action eq "ExecuteEdit") {&ExecuteEdit;}
if ($Action eq "Preview") {&PreviewCoupon;}

####### EXECUTE EDIT
sub ExecuteEdit
{
	$MasterFile = $TemplatesDir . "CouponMasterData.txt";
	open(CMASTER,"$MasterFile") || &Error("Can't open $MasterFile. Reason: $!");
	@CouMas=<CMASTER>;
	close(CMASTER);	
	foreach (@CouMas)
	{
		($thKey,$thValue)=split(/\|/,$_);
		if (exists($in{$thKey}))
		{
			$TheItem=$thKey;
			$EditThis=$in{$thKey};
		}
	}
	if ($TheItem ne "")
	{
		&OpenMyDatabase;
		$MyData{$TheItem} = $EditThis;
		&CloseMyDatabase;
		&GetDecision("True");
	}
	else
	{
		&Header;
		print "I didn't find a match for anything you entered.<br>\n";
		exit;
	}
}

####### SELECT EDIT ITEM
sub SelectEditItem
{
	&Error("You must select one item.") unless ($in{EditItem});
	$EditItem=$in{EditItem};
	&Header;
	&PHed;
	if ($EditItem =~ /Image/)
	{
		&PrepareUpload;
	}
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<font size=+1><center><img src=\"https://surflocalmedia.com/images/edit-text.jpg\"><font color=800000> Edit Your Ad</font>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ExecuteEdit>\n";
	&OpenMyDatabase;
	$ThisItem=$MyData{$EditItem};
	&CloseMyDatabase;
	print "<font size=+1><font color=000000>Edit: <b><i>$EditItem</font></b></i><br>\n";
	print "<textarea rows=5 cols=65 name=$EditItem>\n";
	print "$ThisItem";
	print "</textarea>\n";	
	print "<p></center></center><input type=submit value=\"Make change\"><p></td></tr></table>\n";
	#print "<iframe name=\"inlineframe\" src=\"https://www.surflocalmedia.com/information/codingc.html\" frameborder=\"0\" scrolling=\"yes\" width=\"800\" height=\"800\" marginwidth=\"1\" marginheight=\"1\" ></iframe>\n";
    	
	
	exit;
}


####### GET DECISION
sub GetDecision
{
	$Incoming=join(//,@_);
	&Header;
	&PHed;
	if ($Incoming ne "")
	{
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=900>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";
	print "<font size=+1><img src=\"https://surflocalmedia.com/images/info-recorded.jpg\"><font color=800000><B>Success! <font size=-1><font color=000000>Edit another item below or <FONT COLOR=800000>\"POST UPDATE\" <FONT COLOR=000000> when you finish to <FONT COLOR=800000>GO LIVE.</FONT></B></center></font>\n";
	}
	else
	{
	
	print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=900 bordercolor=000000>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";
        print "<font size=+1><b>$BizName, Choose the items you want to edit below.</b><br> \n";
        
        }
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=SelectEditItem>\n";
        print "</center><blockquote><font size=+1><input type=radio name=EditItem value=TitleTag><font color=000000> 1-Title Tag:</i> <font color=000000><font size=+1>Business name, phone number and a brief description of ad<br>\n";
        print "<input type=radio name=EditItem value=DescriptionTag><font color=000000><font size=+1> 2-Description Tag:</i> <font size=+1><font color=000000>Searchable phrases that describe your ad.<br>\n";
        print "<input type=radio name=EditItem value=Keywords><FONT COLOR=000000><font size=+1> 3-Keywords:</i> <font color=000000><font size=+1>Separate each word by commas.<br>\n";
        
        print "<input type=radio name=EditItem value=CouponEmailAddress> <FONT COLOR=000000><font size=+1>4-E-Mail Address:</i> <font size=+1><font color=000000>Type in your e-mail address </b><br>\n";
        print "<input type=radio name=EditItem value=CouponEmailText> <font color=000000><font size=+1>5-Coupon E-Mail Text:</i> <font size=+1><font color=000000>Text on your e-mail link \"E-mail Us\"</b><br>\n";
        print "<input type=radio name=EditItem value=CouponBusinessLink> <font color=000000><font size=+1>6-Your Website Link:</i><font size=+1> <font color=000000>Website address i.e. \"https://www.surflocalmedia.com\" </b><br>\n";
        print "<input type=radio name=EditItem value=CouponBusinessLinkText> <font color=000000><font size=+1>7-Website Link Text:</i> <font size=+1><font color=000000>Text on link i.e.  \"Visit My Website\"</b> <br>\n";
        print "<input type=radio name=EditItem value=CouponType> <font color=000000><font size=+1>8-Value of Gift Certificate </i> <font color=000000><font size=+1>(top left)- Simple Coupon Only<br>\n";
        print "<input type=radio name=EditItem value=CouponImage1> <font color=000000><font size=+1>9-Upload Top Image-</i> <FONT COLOR=000000><font size=+1> Upload your picture - size 250w X 200h only<br>\n";
        print "<input type=radio name=EditItem value=Category> <font color=000000><font size=+1>10-Bottom Category Tagline:</i> <font color=000000><font size=+1>Text found under the ad that describes the offer in searchable phrases</b><br>\n";
       
        print "<input type=radio name=EditItem value=CouponOfferText> <FONT COLOR=000000><font size=+1>11-Offer:</i> <font color=000000><font size=+1>Detailed offer that will motivate your customer to shop with you  <br>\n";
        print "<input type=radio name=EditItem value=CouponBusinessName> <font color=000000><font size=+1>12-Business Name or Upload Video:</i> <font color=000000><font size=+1>Business name that you want to appear on your ad <br>\n";
        print "<input type=radio name=EditItem value=CouponAddress> <font color=000000><font size=+1>13-Address:</i> <font color=000000><font size=+1>Full Business Address including city, state and zip<br>\n";
        print "<input type=radio name=EditItem value=CouponPhoneNumber> <font color=000000><font size=+1>14-Phone Number:</i> <font color=000000><font size=+1>Business Phone Number <br>\n";
        print "<input type=radio name=EditItem value=GiftValue> <font color=000000><font size=+1>15-Gift Value:</i> <font color=000000><font size=+1> (bottom)- Simple Coupon Only<br>\n";
        print "<input type=radio name=EditItem value=CouponVideo> <font color=000000><font size=+1>16-Video Upload -</i><FONT COLOR=000000><font size=+1> Upload your video or buy now source code- size 250w X 200h only<br>\n";
        print "<input type=radio name=EditItem value=CouponGoodThru> <font color=000000><font size=+1>17-Coupon Expiration Date:</i> <font color=000000><font size=+1>Change the date the coupon expires<br>\n";
        print "<input type=radio name=EditItem value=BarCodeImage> <font color=000000><font size=+1>18-Upload Bottom Image</b></B><FONT COLOR=000000> <font size=+1>Upload your barcode or logos<br>\n";
        print "<input type=radio name=EditItem value=CouponImage3> <FONT COLOR=000000><font size=+1> <font color=000000>19-Upload Existing Artwork - </i> <font size=+1>Upload a jpg or gif. 749 W X 300 H<br>\n";
        print "<input type=radio name=EditItem value=CouponImage2> <font color=000000><font size=+1>Coupon/Incentive ad-</i><FONT COLOR=000000><font size=+1> Upload your picture for coupon ad - size 250w X 200h only<br>\n";
        print "<input type=radio name=EditItem value=CouponImage1> <font color=000000><font size=+1>Gift Certificate-</i> <FONT COLOR=000000><font size=+1> Upload your picture for gift certificate- size 250w X 200h only<br>\n";
        print "<input type=radio name=EditItem value=CouponVideo> <font color=000000><font size=+1>Shopping Coupon -</i><FONT COLOR=000000><font size=+1> Upload your video or buy now source code- size 250w X 200h only<br>\n";
        print "<input type=radio name=EditItem value=CouponShoppingVid><font color=000000><font size=+1>Combo Shopping Coupon</b></i><FONT COLOR=000000><font size=+1> Embed code for video<br>\n";
        print "<input type=radio name=EditItem value=CouponShopping> <font color=000000><font size=+1>Combo Shopping</b></B><FONT COLOR=000000><font size=+1> Embed code for buy now<br>\n";
        print "<input type=radio name=EditItem value=CouponImage5> <font color=000000><font size=+1>Shopping with Branding</b></B><FONT COLOR=000000> <font size=+1>Upload your branding (350 pixels wide)<BR>\n";
        
        




        #$MasterFile = $TemplatesDir . "CouponMasterData.txt";
	#open(CMASTER,"$MasterFile") || &Error("Can't open $MasterFile. Reason: $!");
	#@CouMas=<CMASTER>;
	#close(CMASTER);
	#foreach (@CouMas)
	{
		($thKey,$thValue)=split(/\|/,$_);
		#print "<input type=radio name=EditItem value=\"$thKey\"> $thKey<br>\n";
	}
        print "<p><center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=600>
        <tr><td>\n";
	print "<P><input type=submit value=\"START UPDATE\"></form></td>\n";
	print "<td><form action=$newform method=POST></td>\n";
	print "<td><input type=hidden name=action value=Preview><input type=submit value=\"PREVIEW UPDATE\"></form></td>\n";
	print "<td><form action=FinalizeEdit.cgi method=POST><input type=submit value=\"POST UPDATE\"></form><td></tr></table>\n";
        print "<font size=-1><B><FONT COLOR=000000>Remember to click <FONT COLOR=800000>\"POST UPDATE\" <FONT COLOR=000000> when you finish to <FONT COLOR=800000>GO LIVE.</FONT><BR><BR><FONT SIZE=+2>EXAMPLE DIAGRAM OF ITEMS TO EDIT</center></FONT><BR><IMG SRC=\"/images/COUPON-DIAGRAM.jpg\"></B> \n";
	exit;
}

####### PREVIEW COUPON
sub PreviewCoupon
{
	#This sub is taken almost wholesale from the Page.cgi
	#script. It simply opens the Coupon template
	#and swaps html comments with their associated
	#values from the user's database.
	&Header;
	&PHed;
	&OpenMyDatabase;
	$Template=$MyData{CouponTemplate};
	$TheTemplate= $TemplatesDir . $Template . ".ctemp";
	open (PAG,"$TheTemplate") || &Error("Can't open $TheTemplate. Reason: $!");
	@Pag=<PAG>;
	close(PAG);
	foreach (@Pag)
	{
		#inserts user's business name throughout the page
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;
		#Looks for an html comment
		#IMPORTANT! This looks for comments with
		#no spaces between the dashes and the acutal
		#comment text. That's important because if you
		#want html comments in your page, you must 
		#put a space before and after the actual comment
		#to avoid the script trying to swap them.
		if ($_ =~ /<!--(\w*)-->/)
		{
			#$1 represents the word matched by \w* above.
			$TheKey = $1;
			$TheThingy=$MyData{$TheKey};
			$TheThingy =~ s/\[/</gi;
			$TheThingy =~ s/\]/>/gi;
			if ($TheKey eq "CouponEmailAddress")
			{
				$_ =~ s/<!--$TheKey-->/<a href=\"mailto:$TheThingy\">/gi;
			}
			elsif ($TheKey eq "CouponBusinessLink")
			{
				$_ =~ s/<!--$TheKey-->/<a href=\"$TheThingy\">/gi;
			}
			else
			{
				$_ =~ s/<!--$TheKey-->/$TheThingy/gi;
			}
		}#end if tag loop
		print "$_";
   	 }#end foreach loop
    	&CloseMyDatabase;
     print "<hr noshade size=1>";
    print "<table border=0><tr><td bgcolor=white><font color=black>---------- NOTHING BELOW THIS LINE WILL BE ON YOUR FINAL COUPON ---------<br>\n";
    print "</td></tr></table>\n";
    print "<form action=$newform method=POST>";
    print "<input type=submit value=\"Click here to continue making changes\">\n";
    print "</form>\n";
    print "<form action=FinalizeEdit.cgi method=POST>\n";
    print "<input type=submit value=\"Click here to accept this coupon and proceed to the next step.\"></form>\n";
    exit;
}


####### PREPARE UPLOAD
sub PrepareUpload
{
	#&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=735>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br>\n";	
	print "<font size=+1><font color=800000><img src=\"https://surflocalmedia.com/images/edit-image.jpg\">Upload Your Image</h1><br></center></font> \n";  
        print "<font size=-1><b><blockquote><blockquote><blockquote>To upload your image file use the <i>BROWSE</i> button to navigate to the image file on your computer. Double Click on the image file to select, then click the <i>Upload This Image</i> button. \n";
	print "<form action=CouponEditUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=TheItem value=\"$EditItem\">\n";
         print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";

	print "Select an image to upload: <input type=\"FILE\" name=\"file-to-upload-1\"><br><br>\n";
	print "<p><input type=submit value=\"Upload this image\"><br>Press the button ONLY ONCE. The image upload may take a few moments.</form></center>\n";
	exit;
}
