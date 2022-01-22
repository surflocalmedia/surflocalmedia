#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 1998-present
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####	 variables    ######
$newform = "/cgi-bin/surflocal/PageEdit.cgi";
#$ImageWidth=200;
$Hed{T} = "Edit Your Business Website ";
###### PROGRAM CONDITIONALS, SUNDRIES #######
&Parse;
&GetCookieValues;
#     This gives me $BizName and $CityState
$ImagesDir = $baseurl . "/" . "images/";
#&Error("You must first go through the registration process.") if (($BizName eq "") || ($CityState eq ""));
$Action = $in{action} if ($in{action} ne "");
&GetDecision unless $Action;
if ($Action eq "SelectEditItem") {&SelectEditItem;}
if ($Action eq "EditSelection") {&EditSelection;}
if ($Action eq "EditPageItems") {&Header;&PHed;&EditPageItems;}
if ($Action eq "MakeEdit") {&MakeEdit;}
if ($Action eq "Preview") {&Preview;}
if ($Action eq "ExecuteEdit") {&ExecuteEdit;}
if ($Action eq "ModifyProductPagesNumber"){&ModifyProductPagesNumber;} 
if ($Action eq "ProductPage") {&ProductPage;}

####### EXECUTE EDIT
sub ExecuteEdit
{
	#template means it's a template
	
	#
	#BackgroundImage means it's a background image
	#font means it's a Font Face
	#FontColor means it's a Font Color
	&OpenMyDatabase;
	if ($in{template})
	{
		$MyData{PageTemplate}=$in{template};
	}
	elsif ($in{font})
	{
		$MyData{PageFont}=$in{font};
	}
	elsif ($in{FontColor})


	{
		$MyData{PageFontColor}=$in{FontColor};
	}
	elsif ($in{BackgroundImage})
	{
		$MyData{PageBackgroundImage}=$in{BackgroundImage};
	}
	elsif ($in{EditItem})
	{
		#EditItem means it's a product page
		#      $in{EditItem} is the name of the item to edit (ie "Product_1_Description")
		#      $in{$in{EditItem}} is the content of the item to edit (ie "This product is great")
		$TheName = $in{EditItem};
		if ($TheName =~ /Image/)
		{
			&CloseMyDatabase;
			&MakeUploadPage;
		}
		else
		{
			$TheData = $in{$TheName};
			$MyData{$TheName}=$TheData;
		}
	}
	else
	{
		&Error("I don't understand what you want to edit.");
	}
	&GetDecision("Edit made");
}

####### MAKE UPLOAD PAGE
sub MakeUploadPage
{
	&Header;
	&PHed;
	&OpenMyDatabase;
	($Thingy,$TheNum)=split(/\_/,$TheName);
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<h1>Upload image</h1></center>\n";
	print "<form action=ProductPageEditUpload.cgi name=\'UPLOAD\' method=POST ENCTYPE=\"multipart/form-data\" onSubmit=\'ValidateForm()\'>\n";
	print "<script language=\"javascript\">\n";
	print "<!--\n";
	print "function ValidateForm\(\) \{\n";
	print "	document.UPLOAD.submit.disabled = true\;\n";
	print "	/return true\;\n";
	print "\}\n";
	print "\/\/-->\n";
	print "<\/script>\n";
	print "<input type=hidden name=ProductNumber value=\"$TheNum\">\n";
	print "Select an image to upload:</td><td> <input type=\"FILE\" name=\"file-to-upload-1\"><br>\n";
	print "<input type=submit value=\"Upload this image\">\n";
	#<br>Press the button ONLY ONCE. The image upload may take a few moments.</form>\n";
	exit;
}

####### SELECT EDIT ITEM
sub SelectEditItem
{
	#######
	#
	# I need to call SelectEditItem with ProductPages
	# and the NUMBER of product pages to edit -- changing
	# however it needs to be changed.
	#
	#######
	
	$EditItem=$in{EditItem};
	&Header;
	&PHed;
	if (($EditItem ne "PageItems") && ($EditItem ne "ProductPages"))
	{
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 BACKGROUND=\"https://www.surflocal.net/images/white_table.jpg\" CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
             
		print "<form action=$newform method=POST>\n";
		print "<input type=hidden name=action value=ExecuteEdit>\n";
	}
	if ($EditItem eq "Template"){&EditTemplate;}
	if ($EditItem eq "BackgroundImage"){&EditBackgroundImage;}
	if ($EditItem eq "FontFace"){&EditFontFace;}
	if ($EditItem eq "FontColor"){&EditFontColor;}
	if ($EditItem eq "PageItems"){&EditPageItems;}
	if ($EditItem eq "PickProductPages"){&PickProductPages;}
	if ($EditItem eq "ProductPages"){&EditProductPages;}
	if ($EditItem eq "RawUpload"){&SendToRawUpload;}
	if (($EditItem ne "PageItems") && ($EditItem ne "ProductPages"))
	{
		print "<input type=submit value=\"Make change\">\n";
	}
	exit;
}

####### SEND TO RAW UPLODAD
sub SendToRawUpload {
print "<link href=\"/style-page.css\" rel=\"stylesheet\" type=\"text/css\" />\n";

	print "<font siz+1><font color=000000>Upload Additional Images</center></font>\n";
	print "<blockquote><p><b>You have chosen to upload images to your folder.</b> IMPORTANT: THESE PHOTOS MUST BE .GIF or .JPG FILES ONLY or the upload will not work. BE SURE to rename your image to what you want to call it. On the next screen you will see a white text box.  In that box you will delete everything showing except the photo name. For example, everything except your photo name of MyPhoto.gif. That's it. When you click on the link below, ";
	print "<font size=-1>a new browser window will open to allow you to do that. <p><b>REMEMBER, Do not bookmark the next page ";
	print "<font size=-1>that opens, because the program will not allow you to use it unless you come from ";
	print "<font size=-1>this page first</b>.<p>\n";
	print "<img src=\"https://surflocal.net/bullet-logo.gif\"> <a href=https://www.surflocal.net/cgi-bin/surflocal/RawUpload.cgi target=_blank><font color=000000>Click here to begin uploading your photos.</a>\n";
	print "<p><img src=\"https://surflocal.net/bullet-logo.gif\"> <a href=$newform><font color=000000>Or click here to continue editing your page.</font></a>\n";
	exit;
}

####### PICK PRODUCT PAGES
sub PickProductPages {
	
	#Lets user change how many product pages they want.
	&OpenMyDatabase;
	$TheNumber = $MyData{NumberOfProductPages};
        print "<link href=\"/style-page.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
	print "<font size=+1><center><font color=000000>Number of Add-On Pages</font></center>\n";
	print "<font color=000000></center>Below, the number of add-on pages you have appears. You can reduce or increase that number here to add or subtract pages.  Be sure when you subtract pages, that you remember that you will subtract from the last page you created. <p>For example, if you nave 4 pages, and you want to subtract 2 pages, the <u>last two pages</u> you created will disappear when you change the number to 2.<br><br>\n";
	print "If you decide to subtract pages, be sure to backup the pages you are deleting, in case you change your mind later.</font><br>\n";
        print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ModifyProductPagesNumber><br>\n";
	print "<font size=-1><font color=800000><b>Number of add-on pages:</b> <input type=text name=NewNumber value=\"$TheNumber\"><br>\n";
	print "<p><center><input type=submit value=\"Make Change\"></form>\n";
	exit;
}

####### MODIFY PRODUCT PAGES NUMBER
sub ModifyProductPagesNumber {
	#
	# Writes the new number of product pages to the database, calls GetDecision sub.
	#
	$NewNumber = $in{NewNumber} if $in{NewNumber};
	if (! $NewNumber) {
		&Error("You must select a number of product pages, even if it's 0");
	}
	if (length($NewNumber) > 2) {
		&Error("You cannot select more than 99 product pages");
	}
	if (length($NewNumber) > 1) {
		if ($NewNumber !~ /\d\d/) {
			&Error("You must enter numbers only.");
		}
	} elsif ($NewNumber !~ /\d/) {
		&Error("You must enter numbers only.");
	}
	&OpenMyDatabase;
	$MyData{NumberOfProductPages} = $NewNumber;
	&CloseMyDatabase;
	&GetDecision("Edit made");
}
####### EDIT PRODUCT PAGES
sub EditProductPages
{
	&OpenMyDatabase;
	$TheNumber = $MyData{NumberOfProductPages};
	#MyData{Product_$i_Name} is the name of the product number.
	#MyData{Product_$i_Description} is the description of the product
	#MyData{ProductImage_$i} is the url to the image (if blank, no image).
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
	#print "<h2><font color=000000>Edit your Multimedia Ad</h2></center></center>\n";
	print "</center></center></center></center><p><font size=+1><b>To Edit Your Pages: </b>Simply click on the name of the page you want to edit. <p>To view your update you have to finalize your changes. <p>If you want to add pages, go to \"Add or Subtract Ad-On Pages\" in the main editing menu.</font><br><ul>\n";
	$MyBase = $baseurl . $CityState . "/" . $BizName . "/";
	for ($i=1; $i <= $TheNumber; $i++)
	{
		$TheKey = "Product_" . $i . "_Name";
		$TheName=$MyData{$TheKey};
		if (! $TheName) {
			print "<img src=\"https://surflocal.net/images/glbutn.gif\"> <font color=000000>Edit this page:  <a href=$newform\?action=ProductPage\&Page=$i><font color=000000><u>Create additional page here</u><br></font></a> ";
		} else {
			print "<img src=\"https://surflocal.net/images/glbutn.gif\"><font color=000000> Edit this page:  <a href=$newform\?action=ProductPage\&Page=$i><font color=000000><u>$TheName</u></font></a> ";
			$Htmer = $MyBase . $TheName . ".html";
			#print "<font size=-2> (<a href=\"$Htmer\" target=\"_new\">Display this page in a new window</a>)</font><br>\n";
		}
	}
	print "</ul>\n";
	&CloseMyDatabase;
	print "<p><center><form action=$newform method=POST><input type=submit value=\"Back to Editing Tools\"></form></center>\n";
}

####### PRODUCT PAGE
sub ProductPage
{
	&Error("You must provide a page to edit.") unless ($in{Page});
	$ThePage=$in{Page};
	&OpenMyDatabase;
	$TheKey = "Product_" . $ThePage . "_Name";
	$TheName = $MyData{$TheKey};
	$TheKey = "Product_" . $ThePage . "_Description";
	$TheDescription = $MyData{$TheKey};
	$TheKey = "ProductImage_" . $ThePage;
	$TheImage=$MyData{$TheKey};
	&CloseMyDatabase;
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=735>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<font size=+1><center><font color=000000><b>Edit Add-On page for <font color=800000>$BizName</b>\n";
	print "<p><font color=000000><font size=+1>In this section, edit one item at a time by choosing the appropriate radio button. <br><img src=\"https://surflocal.net/images/glbutn.gif\"><a href=\"https://www.surflocal.net/information/coding.html\" target=_blank><font color=000000><u>Click Here </u></a> for Basic HTML help for your pages.  <br>This page will open in a new window so you can continue working.</font></a></center><br>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=ExecuteEdit>\n";
	print "<table border=1>\n";
	#if ($TheImage ne "")
	#{
		print "<tr><td WIDTH=40%><font color=000000><font size=-1>(1) <b>EDIT OR ADD AN IMAGE</b> for this page:  (NOTE: For your photos to properly present use .jpg or .gif format images at 300 pixels width.)</font></td><td>";
		$TheText="ProductImage_" . $ThePage;
		print "<input type=radio name=EditItem value=$TheText> <font color=000000><b><font size=-1>EDIT YOUR IMAGE FILE.</b> To add additional photos to your page,  Go to \"Upload Additional Images \" in your Editing Tools  Main Menu and follow the directions.</font></td></tr>\n";
	#}
	print "<tr><td align=left><font color=000000><font size=-1>(2) <b>PAGE NAME:</b>(This will be the title of the link to this section of your website. For instance:<b> \'MY PAGE\')</b></font></td>\n";
	$TheText="Product_" . $ThePage . "_Name";
	print "<td><input type=radio name=EditItem value=$TheText><input type=text name=$TheText value=\"$TheName\"></td></tr>\n";
	print "<tr><td align=left valign=top><font color=000000><font size=-1>(3)<b> DESCRIPTION</b>: This is the body of your page.   <br><br><B>Basic html for your pages:</B> <BR><BR>For <b>BOLD</b> text, type:<br> \&lt\;b\&gt\;The text to be bolded\&lt\;\/b\&gt\; </b> <br><br>
        For <i>ITALIC</i> text, type<BR> \&lt\;i\&gt\;The text to be italicized\&lt\;\/i\&gt\; <br><BR>
        For PARAGRAPHS, type<br> \&lt\;p\&gt\; To begin a new a paragraph, <BR>OR type \&lt\;br\&gt\; to put in a linebreak.<br><br>
        To make 'BULLET LISTS', simply follow the example below<p>
        Example:<br>
The title of your listing [ul]<br>
[li]First item<br>
[li]Next item<br>
[li]next item<br>
[li]nest item<br>
[li]last item<br>
[/ul]<p>
To make a link, do this: <br>\&lt\;a href=\"https://mygreatsite.com\" target=\"new\"\&gt\;Visit this webpage\&lt\;/a\&gt\;<p></FONT></a><br></td>\n";
	$TheText="Product_" . $ThePage . "_Description";
	print "<td valign=top><input type=radio name=EditItem value=$TheText CHECKED><textarea name=\"$TheText\" cols=\"50\" rows=\"25\" wrap=\"VIRTUAL\">";
	print "$TheDescription</textarea></td></tr>\n";
	print "<tr><td colspan=2 align=left><input type=submit value=\"Change the Selected Item\"></form></td></tr></table>\n";
	exit;
}


####### EDIT FONT COLOR
sub EditFontColor
{
	$TheFile="PageEditFontColor";
	print "Select A New TEXT COLOR For Your Multimedia Ad:<p>\n";
	&ReadTemplateFile;
}

####### EDIT FONT FACE
sub EditFontFace
{
	$TheFile="PageEditFontFace";
	print "Select A New TEXT STYLE For Your Multimedia Ad:<p>\n";
	&ReadTemplateFile;
}

####### EDIT BACKGROUND IMAGE
sub EditBackgroundImage
{
	&OpenMyDatabase;
	$TheTemplate = $MyData{PageTemplate};
	if ($TheTemplate ne "2") 
         
	{
		$TheFile="PageEditBackgroundImage";
	}
	else
	{
		$TheFile = "PageEditBackgroundImage2";
	}
	print "Select A New Background Image For Your Multimedia Ad:<br>Mouse Over \"View\" to test the backgrounds<p>\n";
	&ReadTemplateFile;
}

####### EDIT TEMPLATE
sub EditTemplate
{
	$TheFile="PageEditTemplate";
	#print "Select a DESIGN LAYOUT for your Multimedia Ad:<p>\n";
	&ReadTemplateFile;
}
	

####### READ TEMPLATE FILE
sub ReadTemplateFile
{
	$ThisFile = $basedir . "Templates" . "/" . $TheFile;
	$Thedir = $baseurl . "images" . "/";
	open(THETEMP,"$ThisFile") || &Error("Can't open $ThisFile. Reason: $!");
	@Tempy=<THETEMP>;
	close(THETEMP);
	foreach (@Tempy)
	{
		$_ =~ s/\%\%ImgsDir\%\%/$Thedir/gi;
		print "$_";
	}
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
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";	
        print "<BR><font color=000000><font size=+1><b>Edit Made <font color=800000>$BizName! <p></b></font><font size=-1><font color=000000>Choose another item to update or click<b> \"POST UPDATE\" </b>to finalize your changes.</font></center>\n";
	}
	else
	{
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\">\n";	
        print "<br><font size=+1><font color=000000>Editing Tools Main Menu for <font color=800000>$BizName:</center>\n";
	}
	print "<br><form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=SelectEditItem>\n";
	print "<blockquote><input type=radio name=EditItem value=Template>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000><font size=+1>Multimedia Ad Layout<br>\n";
	print "<input type=radio name=EditItem value=BackgroundImage>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Background Image<br>\n";
	print "<input type=radio name=EditItem value=FontFace>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Text Style<br>\n";
	print "<input type=radio name=EditItem value=FontColor>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Text Color<br>\n";
	print "<input type=radio name=EditItem value=PageItems CHECKED>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Front Page Items<br>\n";
        print "<p><b><font color=000000>Administrator Menu</b><br>\n";
	print "<input type=radio name=EditItem value=PickProductPages>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Add or Subtract Ad-On Pages<br>\n";
	print "<input type=radio name=EditItem value=ProductPages>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Edit Add-On pages<br>\n";
	print "<input type=radio name=EditItem value=RawUpload>&nbsp;&nbsp;&nbsp;<img src=\"https://surflocal.net/images/edit-text2.jpg\"><font color=000000>Upload Additional Images  </b></b></b></b><font size=-1><p>MUST BE .JPG or .GIF FILES ONLY. If you can not upload with this program, contact <a href=\"mailto:trinity\@surflocal.net\">The Administrator </a>.  We will upload them for you.<br>\n";
        print "<p><input type=submit value=\"START UPDATE\"></form>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=Preview><input type=submit value=\"PREVIEW FRONT PAGE\"></form>\n";
	print "<form action=FinalizeEdit.cgi method=POST><input type=submit value=\"POST UPDATE\"></form></center></td>\n";
	exit;
}

####### EDIT PAGE ITEMS    
sub EditPageItems   
{
	&OpenMyDatabase;
    	$BackgroundImage=$MyData{PageBackgroundImage};
    	$TheFont=$MyData{PageFont};
    	$FontColor=$MyData{PageFontColor};
    	$Template = $MyData{PageTemplate};
    	$TheTemplate = $basedir . "Templates" . "/" . $Template;
    	open(PAG,"$TheTemplate") || &Error("Can't open $TheTemplate for reading in WritePageOptions routine. Reason: $!");
    	@Pag=<PAG>;
    	close(PAG);
   
    	$count = 0;
    	foreach (@Pag)
    	{
    		$TheBGDir = $ImagesDir . $BackgroundImage;
    		$_ =~ s/\<\!-- BodyStuff --\>/<body background=\"$BackgroundImage\">/gi;
		$_ =~ s/\%\%BackgroundImage\%\%/$BackgroundImage/gi;
		$_ =~ s/\<\!-- Font stuff --\>/<font face=\"$TheFont\" color=\"$FontColor\">/gi;
		$_ =~ s/\%\%FontColor\%\%/$FontColor/gi;
		$_ =~ s/\%\%CityState\%\%/$CityState/gi;
                 $_ =~ s/\%\%TitleTag\%\%/$TitleTag/gi;	
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;
		if ($_ =~ /<!--(\w*)-->/)
		{
			$TheKey = $1;
			$TheThingy=$MyData{$TheKey};
			$TheThingy =~ s/\[/</gi;
			$TheThingy =~ s/\]/>/gi;
			$_ =~ s/<!--$TheKey-->/$TheThingy/gi;
			$_ .= "\n<form action=$newform method=POST>\n";
			$_ .= "<input type=hidden name=action value=EditSelection>\n";
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
}#end DisplayPage sub

####### EDIT SELECTION
sub EditSelection
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
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550><tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";	
    	print "<p><font size=+1><b><font color=800000><img src=\"https://surflocal.net/images/edit-text.jpg\">Change $TheItem</font></center>\n";
    	print "<form action=$newform method=POST>\n";
    	print "<input type=hidden name=action value=MakeEdit>\n";
    	print "<input type=hidden name=TheItem value=$TheItem>\n";
    	print "</center><blockquote><blockquote><blockquote><blockquote><font color=000000></b>You can code basic html into this form if you need formatting, use the key below:<br>\n";
        print "<br><b>Edit $TheItem below:<br>\n";
    	print "<textarea rows=20 cols=70 name=EditThis>";
    	print "$MyData{$TheItem}";
    	print "</textarea>\n";
    	print "<br><input type=submit value=\"Change $TheItem\"><input type=Reset></form>\n";    	
        print "<iframe name=\"inlineframe\" src=\"https://www.surflocal.net/information/coding.html\" frameborder=\"0\" scrolling=\"yes\" width=\"800\" height=\"800\" marginwidth=\"1\" marginheight=\"1\" ></iframe>\n";
    	&CloseMyDatabase;
    	exit;
}

####### PREPARE UPLOAD
sub PrepareUpload
{
	#&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\"><br><br>\n";
	print "<font size=+2><font color=800000>Upload image</font></FONT>\n";
	print "<form action=PageEditUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=TheItem value=\"$TheItem\">\n";
	print "<font color=000000>Select an image to upload:<input type=\"FILE\" name=\"file-to-upload-1\"><br>\n";
	print "<p><input type=submit value=\"Upload this image\"><br><font color=000000>Press the button ONLY ONCE. The image upload may take a few moments.</form></td></tr></table>\n";
	exit;
}


####### MAKE EDIT
sub MakeEdit
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
	&Header;
	&PHed;
	&EditPageItems;
}

#######
#PREVIEW
sub Preview
{
	&Header;
	&OpenMyDatabase;
    	$BackgroundImage=$MyData{PageBackgroundImage};
    	$TheFont=$MyData{PageFont};
    	$FontColor=$MyData{PageFontColor};
    	$Template = $MyData{PageTemplate};
    	$TheTemplate = $basedir . "Templates" . "/" . $Template;
    	open(PAG,"$TheTemplate") || &Error("Can't open $TheTemplate for reading in WritePageOptions routine. Reason: $!");
    	@Pag=<PAG>;
    	close(PAG);
   
    	$count = 0;
    	foreach (@Pag)
    	{
    		$TheBGDir = $ImagesDir . $BackgroundImage;
    		$_ =~ s/\<\!-- BodyStuff --\>/<body background=\"$BackgroundImage\">/gi;
		$_ =~ s/\%\%BackgroundImage\%\%/$BackgroundImage/gi;
		$_ =~ s/\<\!-- Font stuff --\>/<font face=\"$TheFont\" color=\"$FontColor\">/gi;
		$_ =~ s/\%\%FontColor\%\%/$FontColor/gi;
		$_ =~ s/\%\%CityState\%\%/$CityState/gi;	
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;
		if ($_ =~ /<!--(\w*)-->/)
		{
			$TheKey = $1;
			$TheThingy=$MyData{$TheKey};
			$TheThingy =~ s/\[/</gi;
			$TheThingy =~ s/\]/>/gi;
			if ($TheKey eq "EmailAddress")
			{
				$_ =~ s/<!--$TheKey-->/<a href=\"mailto:$TheThingy\">/gi;
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
    print "<table border=0><tr><td bgcolor=white>---------- NOTHING BELOW THIS LINE WILL BE ON YOUR FINAL PAGE ---------<br>\n";
    print "</td></tr></table>\n";
    print "<form action=$newform method=POST>";
    print "<input type=submit value=\"Click here to continue making changes\">\n";
    print "</form>\n";
    exit;
}

####### PRINT FINISH CHANCE
sub PrintFinishChance
{
    print "<form action=$newform method=POST>\n";
    print "<input type=submit value=\"Click here to go back to the main editing menu\">\n";
    print "</form>\n";
}
