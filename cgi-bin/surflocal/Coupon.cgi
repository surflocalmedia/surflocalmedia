#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 1996-PRESENT
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

####### SET VARIABLES
$newform = "/cgi-bin/surflocal/Coupon.cgi";
$TemplatesFile = "$TemplatesDir" . "CouponTemplates.html";
$ImageWidth=300;
$MasterDataFile = $TemplatesDir . "CouponMasterData.txt";
$CategoryListLocation = "$basedir" . "Templates" . "/" . "CategoryList";
$Hed{T} = "Building Your Coupon";
$FinishScript = "/cgi-bin/surflocal/Finalize.cgi";
&Parse;
&GetCookieValues;
&Error("You must first go through the registration process.") if (($BizName eq "") || ($CityState eq ""));
$Action=$in{action};

####### CONDITIONALS
&SelectCategory unless ($Action);
if ($Action eq "CalledFromEdit") {&PreviewCoupon;}
if ($Action eq "SelectATemplate") {&SelectATemplate;}
if ($Action eq "BeginCouponEdit") {&WriteMasterDataItems;}
if ($Action eq "DisplayPage"){&DisplayPage;}
if ($Action eq "MakeEdit"){&MakeEdit;}
if ($Action eq "ExecuteEdit") {&ExecuteEdit;}
if ($Action eq "FinishEditing") {&FinishEditing;}
if ($Action eq "PreviewCoupon") {&PreviewCoupon;}
if ($Action eq "RecordCoupon") {&RecordCoupon;}

####### RECORD COUPON
sub RecordCoupon
{
	#Gets user ready for next step, based on whether they have chosen a 
	#web page along with their ad or not.
	&Header;
	&PHed;
 print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";	
	print "<center><font color=800000><font size=+1><b><img src=\"https://surflocal.net/images/success.jpg\">You are finished creating your ad!<p></font>\n";
	if (&GetCookies("Edit") eq "1")
	{
    		$MyAdType=$Cookies{"Edit"};
		$SubsequentAd = "true";
	}
	else
	{
		&OpenCityDatabase;
		$MyAdType=$CityData{$BizName};
		&CloseCityDatabase;
	}
	#if ($SubsequentAd = "true")
	#{
	#	print "<form action=FinalizeEdit.cgi method=POST>\n";
	#	print "<input type=hidden name=From value=Coupon>\n";
	#}
	if ($MyAdType eq "CouponPlus")
	{
		print "<form action=Page.cgi method=POST>\n";
	}
	else
	{
		print "<form action=$FinishScript method=POST>\n";
	}
	print "<input type=submit value=\"Click here for the next step\">\n";
	exit;
}

####### PREVIEW COUPON
sub PreviewCoupon
{
	#This sub is stolen almost wholesale from the Page.cgi
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
    print "<input type=hidden name=action value=DisplayPage>\n";
    print "<input type=submit value=\"Click here to continue making changes\">\n";
    print "</form>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=\"RecordCoupon\">\n";
    print "<input type=submit value=\"Click here to accept this coupon and proceed to the next step.\"></form>\n";
    exit;
}


####### PRINT FINISH CHANCE
sub PrintFinishChance
{
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=FinishEditing>\n";
    print "<input type=submit value=\"Click here if you\'re finished making changes\">\n";
    print "</form>\n";
}

####### FINISH EDITING
sub FinishEditing
{
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0  WIDTH=800>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";	
	print "<font size=+2><center><img src=\"https://surflocal.net/images/edit-text.jpg\"><FONT COLOR=80000>Finish Editing</font></center>\n";
	print "<FONT COLOR=00000><font size=+1><blockquote><blockquote><blockquote>You have two choices at this point. You can <FONT COLOR=800000><b>Preview</b> <FONT COLOR=000000>your finished coupon,";
	print " <FONT COLOR=000000>or if you're confident in the changes you made, you can proceed to the next step.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=radio name=action value=\"PreviewCoupon\" CHECKED> Preview the Coupon<br>\n";
	print "<input type=radio name=action value=\"RecordCoupon\"> Skip the preview and proceed to the next step<br>\n";
	print "<p><input type=submit value=\"Continue\"></form>\n";
	exit;
}

####### PREPARE UPLOAD
sub PrepareUpload
{
	&Header;
	&PHed;
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0  WIDTH=800>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br>\n";
	print "<p><font size=+2><font color=800000><img src=\"https://surflocal.net/images/edit-image.jpg\">Upload Your Image</h1><br></center></font> \n"; 
        print "<font color=000000><font size=+1><blockquote><blockquote><blockquote>To upload your image file use the <i>BROWSE</i> button to navigate to the image file on your system. Double Click on the image file to select, then click the <i>Upload This Image</i> button. \n";
	print "<form action=CouponUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=TheItem value=\"$TheItem\">\n";
	print "Select an image to upload:<input type=\"FILE\" name=\"file-to-upload-1\"><br><br>\n";
	print "<input type=submit value=\"Upload this image\"><p><b>Press the button ONLY ONCE.</b> The image upload may take a few moments.</form>\n";
	exit;
}

####### EXECUTE EDIT
sub ExecuteEdit
{
	$TheItem = $in{TheItem};
	$EditThis = $in{EditThis};
	if (($TheItem eq "") || ($EditThis eq ""))
	{
		&Error("You cannot enter empty values. Please go back and re-edit.");
	}
	&OpenMyDatabase;
	$MyData{$TheItem} = $EditThis;
	&CloseMyDatabase;
	&DisplayPage;
}


####### MAKE EDIT
sub MakeEdit
{
	&Header;
    	&PHed;
    	&Error("You must select an item to edit") unless ($in{item} ne "");
    	$TheItem=$in{item};
    	if ($TheItem =~ /Image/)
    	{
    		&PrepareUpload;
    	}
    	&OpenMyDatabase;
 print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
    	print "<font size=+2><center><font color=800000><img src=\"https://surflocal.net/images/edit-text.jpg\">Change $TheItem</font>\n";
    	print "<form action=$newform method=POST>\n";
    	print "<input type=hidden name=action value=ExecuteEdit>\n";
    	print "<input type=hidden name=TheItem value=$TheItem>\n";
    	#print "<font size=-1>If you need formatting for your coupon ad, use the key below the text box:<br><br></center>\n";
    	
    	print "<b>Edit $TheItem below:<br>\n";
    	print "<textarea rows=10 cols=50 name=EditThis>";
    	print "$MyData{$TheItem}";
    	print "</textarea>\n";
    	print "<br><input type=submit value=\"Change $TheItem\"><input type=Reset></form>\n";
	#print "<iframe name=\"inlineframe\" src=\"https://www.surflocal.net/information/coding.html\" frameborder=\"0\" scrolling=\"yes\" width=\"800\" height=\"800\" marginwidth=\"1\" marginheight=\"1\" ></iframe>\n";
    	&CloseMyDatabase;
    	exit;
}



####### WRITE MASTER DATA ITEMS
sub WriteMasterDataItems
{
	&Error("You must select a template") unless ($in{Template} ne "");
	&OpenMyDatabase;
	$MyData{CouponTemplate} = $in{Template};
	$MasterFile = $TemplatesDir . "CouponMasterData.txt";
	open(CMASTER,"$MasterFile") || &Error("Can't open $MasterFile. Reason: $!");
	@CouMas=<CMASTER>;
	close(CMASTER);
	foreach (@CouMas)
	{
		($thKey,$thValue)=split(/\|/,$_);
		$MyData{$thKey}=$thValue;
	}
	&OpenCityDatabase;
	$AdType=$CityData{$BizName};
	&CloseCityDatabase;
	if ($AdType =~ /Plus/)
	{
		$TheLink = $baseurl . $CityState . "/" . $BizName . "/" . "index.html";
		$MyData{CouponBusinessLink} = $TheLink;
	}
	&CloseMyDatabase;
	&DisplayPage;
}

####### DISPLAY PAGE
sub DisplayPage
{
	&Header;
	#print "<font color=white>Got to the DisplayPage sub.<br>\n";
	&PHed;
	&OpenMyDatabase;
	
	#print "<font color=white>Got past opening the database<br>\n";
	$Template=$MyData{CouponTemplate};
	#print "The template is $Template.<br>\n";
	$TheTemplate= $TemplatesDir . $Template . ".ctemp";
	#print "The template file is $TheTemplate<br>\n";
	open (PAG,"$TheTemplate") || &Error("Can't open $TheTemplate. Reason: $!");
	@Pag=<PAG>;
	close(PAG);
	#print "Got the template data.<br>\n";
	foreach (@Pag)
	{
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;			
		if ($_ =~ /<!--(\w*)-->/)
		{
			$TheKey = $1;
			$TheThingy=$MyData{$TheKey};
			$TheThingy =~ s/\[/</gi;
			$TheThingy =~ s/\]/>/gi;
			$_ =~ s/<!--$TheKey-->/$TheThingy/gi;
			$_ .= "\n<form action=$newform method=POST>\n";
			$_ .= "<input type=hidden name=action value=MakeEdit>\n";
			$_ .= "<input type=hidden name=item value=\"$TheKey\">\n";
			if ($TheKey =~ /Image/)
			{
				$_ .= "<input type=submit value=\"Upload a different image\"></form><p>\n";
			}
			else
			{
				$_ .= "<input type=submit value=\"Edit $TheKey\"></form><p>\n";
			}
			
		}#end if tag loop
		print "$_";
   	 }#end foreach loop
    	&CloseMyDatabase;
    	&PrintFinishChance;
    	exit;
}


####### SELECT CATEGORY
sub SelectCategory
{
	&Header;
    &PHed;
 print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0  WIDTH=800>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";		
    print "<font size=+1><center><b><img src=\"https://surflocal.net/images/edit-text.jpg\">Select a Primary Marketing Category</center></b></font>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=SelectATemplate>\n";    
    print "<FONT COLOR=000000><font size=+1><b><blockquote><blockquote><blockquote>Select a category that describes your business: <br><select name=Category>\n"; 
    
    #list categories
    open(CATLIST,"$CategoryListLocation") || &Error("Can't open $CategoryListLocation in SelectCategory sub. Reason: $!");
    @CatList=<CATLIST>;
    close(CATLIST);
    foreach $cat (@CatList)
    {
    	chomp($cat);
       print "<option value=\"$cat\">$cat</option>\n";
    }
    
    print "</select><br>\n";
    print "<br><FONT COLOR=000000>Custom category add dash <font color=800000> (I.E. Letter-Numbers-Only)</font><br> <input type=text name=other><br>\n";
    print "<p><input type=submit value=\"Continue\"><input type=reset value=\"Clear form\"></form>\n";
   
    exit;
}

####### SELECT A TEMPLATE
sub SelectATemplate
{
	&Error("You must select a category") unless (($in{Category}) || ($in{other}));
	&OpenMyDatabase;
	if ($in{other} ne "")
	{
		$MyData{CouponCategory} = $in{other};
	}
	else
	{
		$MyData{CouponCategory} = $in{Category};
	}
	&CloseMyDatabase;
    	&Header;
    	&PHed; 
 print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
	
    	print "<h2>Select your Layout</font></h2>\n";
    	print "<form action=$newform method=POST>\n";
    	print "<input type=hidden name=action value=BeginCouponEdit>\n";
    	print "Select from the Design Layout choices below:<hr noshade size=1>\n";
    	
    	open(TEMPLATE, "$TemplatesFile") || &Error("Couldn\'t open $TemplatesFile in SelectATemplate. Reason: $!");
    	@TheFiles=<TEMPLATE>;
    	close(TEMPLATE);
    	foreach $Filer (@TheFiles)
    	{
    	    print "$Filer";
    	}    
    exit;
}
