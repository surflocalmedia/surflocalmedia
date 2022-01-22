#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2019
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####	 variables    ######
$newform = "/cgi-bin/surflocal/Page.cgi";
#$ImageWidth=200;
$Hed{T} = "Building Your Multimedia Ad  ";
###### PROGRAM CONDITIONALS, SUNDRIES #######
&Parse;
&GetCookieValues;
#     This gives me $BizName and $CityState
$ImagesDir = $baseurl . "/" . "images/";
&Error("You must first go through the registration process.") if (($BizName eq "") || ($CityState eq ""));
$Action = $in{action} if ($in{action} ne "");
&SelectATemplate unless $Action;
if ($Action eq "ChooseOptions") {&ChooseOptions;}
if ($Action eq "WritePageOptions") {&WritePageOptions;}
if ($Action eq "SelectATemplate") {&SelectATemplate;}
if ($Action eq "DisplayPage"){&DisplayPage;}
if ($Action eq "MakeEdit"){&MakeEdit;}
if ($Action eq "EditSelection") {&EditSelection;}
if ($Action eq "FinishEditing") {&FinishEditing;}
if ($Action eq "PreviewPage") {&PreviewPage;}
if ($Action eq "SelectProductPages") {&SelectProductPages;}
if ($Action eq "InputProductPages") {&InputProductPages;}
if ($Action eq "ProductPagesImages") {&ProductPagesImages;}
if ($Action eq "PrepareUpload") {&PrepareUpload;}
if ($Action eq "CheckForUploads") {&CheckForUploads;}
if ($Action eq "RecordProductPage") {&RecordProductPage;}
#############################


####### WRITE PAGE OPTIONS
sub WritePageOptions
{
	#Writes the options for page, like background image, etc.
    	&Error("You must select a background image") unless ($in{BackgroundImage});
    	&Error("You must select a font face") unless ($in{font});
    	&Error("You must select a font color") unless ($in{FontColor});
    	#getting BackgroundImage, font, FontColor
    
    	#######
    	#Here, open PageMasterData.text. Parse each line, making a key/value pair. 
    	#Dump those values into the MyDatabase. That way, when the page is opened, those
    	#values will be put in there, and when they are changed, they'll of course be changed.
    	#
    	#Have to use something like "if (exists (keys xyz)) then...
    	$MasterKeys=$basedir . "/" . "Templates" . "/" . "PageMasterData.txt";
    	open(PAGEMASTER,"$MasterKeys") || &Error("Can't open $MasterKeys for reading. Reason: $!");
    	@PageMasterKeys=<PAGEMASTER>;
    	close(PAGEMASTER);
    	&OpenMyDatabase;
    	foreach (@PageMasterKeys)
    	{
    		($thKey,$thValue)=split(/\|/,$_);
    		$MyData{$thKey}=$thValue;
    	}
    	$MyData{PageBackgroundImage}=$in{BackgroundImage};
    	$MyData{PageFont}=$in{font};
    	$MyData{PageFontColor}=$in{FontColor};
    	&CloseMyDatabase;
    	&DisplayPage;
}

####### DISPLAYPAGE    
sub DisplayPage   
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
                $_ =~ s/\%\%TitleTag\%\%/$TitleTag/gi;
                $_ =~ s/\%\%PhoneNumber\%\%/$PhoneNumber/gi;
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
	#Get user's information to populate the individual database.
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table border=0 width=800><tr><td background=\"https://www.surflocal.net/images/white_table.jpg\">\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\">\n";
    	print "<font size=+2><font color=800000><center><img src=\"https://surflocal.net/images/edit-text.jpg\"><b><font size=-1>Change $TheItem</font></center>\n";
    	print "<form action=$newform method=POST>\n";
    	print "<input type=hidden name=action value=MakeEdit>\n";
    	print "<input type=hidden name=TheItem value=$TheItem>\n";
    	print "<center><font color=000000><font size=-1><b>You can type html into this form or use the key below the text box:<br><ul>\n";
    	print "<b>Edit $TheItem below:<br>\n";
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
	&Header;
	&PHed;
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table border=0 width=550><tr><td background=\"https://www.surflocal.net/images/white_table.jpg\">\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG3.gif\">\n";	
	print "<p><font size=+2><font color=800000><img src=\"https://surflocal.net/images/edit-image.jpg\">Upload Your Image</font></center></font> \n";  
	print "<form action=PageUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=TheItem value=\"$TheItem\">\n";
	print "<font size=+1><b>Select an image to upload: <input type=\"FILE\" name=\"file-to-upload-1\"><br>\n";
	print "<p><input type=submit value=\"Upload this image\"><p><font color=000000></b>Press the button ONLY ONCE.</b> The image upload may take a few moments.</form>\n";
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
	&DisplayPage;
}


####### CHOOSE OPTIONS
sub ChooseOptions
{
	&Error("You must choose a template") unless ($in{"template"} ne "");
	$TheTemplate = $in{"template"};
	&OpenMyDatabase;
	$MyData{PageTemplate}=$TheTemplate;
	&CloseMyDatabase;
	if ($TheTemplate eq "2")
	{
		$PageOptionsPage = $TemplatesDir . "PageOptions2.html";
	}
	else
	{
		$PageOptionsPage = "$TemplatesDir" . "PageOptions.html";
	}
	&Header;
	&PHed;
	open(PAGETMP, "$PageOptionsPage") || &Error("Can't open $PageOptionsPage in ChooseOptions sub. Reason: $!");
	@Lines=<PAGETMP>;
	close(PAGETMP);
	foreach (@Lines)
	{
		$_ =~ s/\%\%ImgsDir\%\%/$ImagesDir/gi;
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;
		print "$_";	
	}	
	exit;
}

####### SELECT A TEMPLATE
sub SelectATemplate
{
    &Header;
    &PHed;
    $PageTemplatesPage = "$TemplatesDir" . "PageTemplates.html";
    open(PAGETMP, "$PageTemplatesPage") || &Error("Couldn\'t open $PageTemplatesPage in SelectATemplate sub. Reason: $!");
    @Lines = <PAGETMP>;
    close (PAGETMP);
    foreach (@Lines)
    {
	$_ =~ s/\%\%ImgsDir\%\%/$ImagesDir/gi;
	print "$_";
    }
    exit;
}


####### FINISH EDITING
sub FinishEditing
{
	&Header;
	&PHed;	
	#Get user's information to populate his individual database.
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG3.gif\">\n";
	print "<font size=+1><b><font color=000000><center><img src=\"https://surflocal.net/images/edit-text.jpg\">Finish Editing Front Page</b></font><br>\n";
	print "<font color=000000>You have two choices at this point. </center><p>You can <b><font color=800000>Preview</b> <font color=000000>your finished Front Page,";
	print " <br><font color=000000>or <font color=800000><b>SKIP preview </b><font color=000000> and proceed to the next step.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "</center><input type=radio name=action value=\"PreviewPage\" CHECKED> <font color=000000>Preview Your Front Page<br><br>\n";
	print "<input type=radio name=action value=\"SelectProductPages\"> <font color=000000>Skip the Preview and Proceed to the Next Step<br></b>\n";
	print "<br><input type=submit value=\"Continue to the Next Step\"></form>\n";
	exit;
}

#######
#PREVIEW
sub PreviewPage
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
                $_ =~ s/\%\%TitleTag\%\%/$TitleTag/gi;
                $_ =~ s/\%\%PhoneNumber\%\%/$PhoneNumber/gi;
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
    print "<center><table border=0><tr><td bgcolor=white><center>---------- NOTHING BELOW THIS LINE WILL BE ON YOUR FINAL PAGE ---------<br>\n";
    print "</td></tr></table>\n";
    print "<form action=$newform method=POST>";
    print "<input type=hidden name=action value=DisplayPage>\n";
    print "<input type=submit value=\"Click here to continue making changes\"><br><br>\n";
    print "</form>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=\"SelectProductPages\">\n";
    print "<input type=submit value=\"Click here to accept this page and proceed to the next step.\"></form>\n";
    exit;
}


####### SELECT PRODUCT PAGES
sub SelectProductPages
{
	&Header;
	&PHed;	
	#Get user's information to populate his individual database.
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
<tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG.jpg\">\n";
	print "<b><center><font color=000000><font size=+1><img src=\"https://surflocal.net/images/edit-text.jpg\"> Your Add-On Pages</b><p></font></center>\n";
	print "<font color=000000>You can create up to 20 pages for your new Multimedia Ad.";
	print "</center><font color=000000> <b><p><font color=800000><i>QUICK START WEB BUILDING : <p></b></i><font color=000000> <li>Choose \"0\" pages then click \"Continue\" <li>You can add additional pages to your Multimedia Ad later in your Editing Tools. </font>.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=InputProductPages>\n";
	print "<select name=TheNumber>";
	for ($str=0; $str<21;$str++)
	{
		print "<option value=$str>$str</option>";
	}
	print "</select><input type=submit value=\"Continue\"></form></center></td></tr></table>\n";
	exit;
}


####### INPUT PRODUCT PAGES
sub InputProductPages
{
	
	&OpenMyDatabase;
	$MyData{NumberOfProductPages}=$in{TheNumber};
	&CloseMyDatabase;
	$TheNumber=$in{TheNumber};
	
	
	$Hed{T} = "Individual product pages";
	&Header;
	&PHed;		
	#Get user's information to populate his individual database.
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        # print "<center><table border=0 width=800><tr><td background=\"https://www.surflocal.net/images/white_table.jpg\">\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG3.gif\">\n";
	print "<center><b><font color=000000><blockquote><font size=+2>QUICK START SUCCESSFUL:<font color=800000> $BizName </b></font>\n";
	#print "<font color=000000>--This will be the additional pages in your web site, with information and a photo that you will upload from your computer. NOTE:  If you chose \"0\" pages, you can simply click on the button below to continue.</font><br>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=\"CheckForUploads\">\n";
	print "<input type=hidden name=TheNumber value=$TheNumber>\n";
	for ($i = 1; $i <= $TheNumber; $i++)
	{
		&ProductInputInfo($i);
		print "\n<p>\n";
	}
	print "<p><input type=submit value=\"Continue\"><p>";
	print "</body></html>\n";
	exit;
}
####### PRODUCT INPUT INFO
sub ProductInputInfo
{
	$myNumber = join(//,@_);
	print "<table width=800 border=1>\n";
	print "<tr><td colspan=2 BGCOLOR=FFFFFF><center><b><font size=+1>Page Number $myNumber</b></font> <br></center></td></tr>\n";
	print "<tr><td background=\"https://www.surflocal.net/images/white_table.jpg\"><font size=-1>Is there a <b>Photo or Logo</b> for Page $myNumber?  <b>NOTE:</b> For your photos to properly present on your page, use .jpg or .gif format images at 300 pixels in width.</font></td><td background=\"https://www.surflocal.net/images/white_table.jpg\">";
	print "<select name=ImageExists_$myNumber><option value=\"Yes\">Yes</option>\n";
	print "<option value=\"No\">No</option></select></td></tr>\n";
	print "<tr><td align=left BGCOLOR=ffffff><b><font size=-1>Title for Page $myNumber:</b> This will be the title of the link to this section of your Multimedia Ad. For instance:<b> \'OUR HISTORY\'</b></font></td><td background=\"https://www.surflocal.net/images/white_table.jpg\"><input type=text name=ProductName_$myNumber></td></tr>\n";
	print "<tr><td align=left valign=top BGCOLOR=ffffff><b><font size=-1>Description of your product or service:</b> Use as much information here as you want.  
<br><br><B>HOW TO FORMAT YOUR PAGES:</B> <p>For <b>BOLD</b> text, type: \&lt\;b\&gt\;The text to be bolded\&lt\;\/b\&gt\; </b> <br>
For <i>ITALIC</i> text, type \&lt\;i\&gt\;The text to be italicized\&lt\;\/i\&gt\; <br>
<p>For PARAGRAPHS, type \&lt\;p\&gt\; To begin a new a paragraph, <BR>OR type \&lt\;br\&gt\; to put in a linebreak.<br><br>
To make 'BULLET LISTS', simply follow the example below<p>
Example:<br>
The title of your listing \&lt\;ul\&gt\;<br>
&lt\;li\&gt\;First item<br>
&lt\;li\&gt\;Next item<br>
&lt\;li\&gt\;next item<br>
&lt\;li\&gt\;nest item<br>
&lt\;li\&gt\;last item<br>
&lt\;/ul\&gt\;<p>
To make a link, do this: <br>\&lt\;a href=\"https://mygreatsite.com\" target=\"new\"\&gt\;Visit this webpage\&lt\;/a\&gt\;<p></FONT></a><br></td>\n";
	print "<td background=\"https://www.surflocal.net/images/white_table.jpg\"><textarea name=\"Description_$myNumber\" cols=\"50\" rows=\"25\" wrap=\"VIRTUAL\"></textarea></td></tr></table>\n";	
}

#######CHECK FOR UPLOADS
sub CheckForUploads
{
	$TheNumber=$in{TheNumber};
	&OpenMyDatabase;
	for ($i=1; $i <= $TheNumber; $i++)
	{
		$TheKey="Product_" . $i . "_Name";
		$TheIn="ProductName_" . $i;
		$MyData{$TheKey}=$in{$TheIn} if ($in{$TheIn});
		$TheKey="Product_" . $i . "_Description";
		$TheIn="Description_" . $i;
		$MyData{$TheKey}=$in{$TheIn} if ($in{$TheIn});
		$TheKey="ProductImage_" . $i;
		$TheIn="ImageExists_" . $i;
		$MyData{$TheKey}=$in{$TheIn} if ($in{$TheIn});
	}
	for ($i=1; $i <= $TheNumber; $i++)
	{
		$ThePhrase="ProductImage_" . $i;
		if ($MyData{$ThePhrase} eq "Yes")
		{
			$ImageExists="true";
		}
	}
	&CloseMyDatabase;
	if ($ImageExists eq "true")
	{
		&MakeProductUploadPage;
	}
	else
	{
		&RecordProductPage;
	}
}

####### MAKE PRODUCT UPLOAD PAGE
sub MakeProductUploadPage
{
	#The Upload script will be recording a url in $MyData{ProductImage_n}. Therefore,
	#by checking to see if it equals "Yes", we'll hopefully only generate an upload page
	#for values that do not yet have images associated with them.
	&OpenMyDatabase;
	$TheNumber=$MyData{NumberOfProductPages};
	for ($i=1; $i <= $TheNumber; $i++)
	{
		$ThePhrase = "ProductImage_" . $i;
		if (($MyData{$ThePhrase} eq "Yes") && ($FirstBlankImage eq ""))
		{
			$FirstBlankImage=$i
		}
	}
	
	if ($FirstBlankImage ne "")
	{
		&Header;
		&PHed;	
		$ProductName="Product_" . $FirstBlankImage . "_Name";
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";		
	#Get user's information to populate his individual database.
        # print "<center><table border=0 width=800><tr><td background=\"https://www.surflocal.net/images/white_table.jpg\">\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG3.gif
\"><br><br></center>\n";
		#print "<center><font color=000000><font size=+1><b><img src=\"https://surflocal.net/images/edit-image.jpg\">Upload image for $MyData{$ProductName}</font>\n";
		print "<form action=PPUpload.cgi method=POST ENCTYPE=\"multipart/form-data\">\n";
		print "<input type=hidden name=ProductNumber value=$FirstBlankImage>\n";
		print "<center>Image file for $in{ProductName}: <input type=\"FILE\" name=\"file-to-upload-1\"><br>\n";
		print "<p><input type=submit value=\"Upload this image\"><p><font color=000000>Press the button ONLY ONCE. The image upload may take a few moments.</form></center>\n";
		exit;
		&CloseMyDatabase;
	}
	else
	{
		&CloseMyDatabase;
		&RecordProductPage;
	}
}


####### RECORD PRODUCT PAGE
sub RecordProductPage
{
	&OpenMyDatabase;
    	$BackgroundImage=$MyData{PageBackgroundImage};
    	$TheFont=$MyData{PageFont};
    	$FontColor=$MyData{PageFontColor};
    	$Email=$MyData{Email};
    	$TheNumber=$MyData{NumberOfProductPages};    	
    	$ThisDirectory = $baseurl . $CityState . "/" . $BizName . "/";
    	###########
    	# Start mukking.
    	#&Header;
    	for ($i=1; $i <=$TheNumber; $i++)
    	{
    		$MyPhrase = "Product_" . $i . "_Name";
    		$ThisFileName = $MyData{$MyPhrase};
    		$TheLinkage = $ThisDirectory . $ThisFileName . ".html";
    		
    		$TheLinkage =~ s/ /\%20/gi;
    		#print "TheLinkage is : $TheLinkage for $MyPhrase<bR>\n";
    		if ($TheProductLinks){$TheProductLinks .= " \ <a href=\"$TheLinkage\">$ThisFileName</a>";}
    		else{$TheProductLinks = "<a href=\"$TheLinkage\">$ThisFileName</a>";}
    	}    	
    	
    	####END
    	$MyData{ProductLinks}=$TheProductLinks;
	for ($i=1; $i <= $TheNumber; $i++)
	{
		#Product_n_Name is the title
		#Product_n_Description is the Description
		#ProductImage_n is the image
		#     if it equals "No" then there's no image.
		$ThePhrase = "Product_" . $i . "_Name";
		$TheTitle=$MyData{$ThePhrase};
		$ThePhrase= "Product_" .$i . "_Description";
		$TheDescription = $MyData{$ThePhrase};
		$ThePhrase = "ProductImage_" . $i;
		$TheImage = $MyData{$ThePhrase};		
		if ($TheImage eq "No"){$TemplFile = "$basedir" . "Templates" . "/" . "ProductPageTemplate.html";}
		else{$TemplFile = "$basedir" . "Templates" . "/" . "ProductPagesImgTemplate.html";}		
		open(TEMPL,"$TemplFile") || &Error("Can't open $TemplFile in ProductPagesImages sub. Reason: $!");
		@Tempor=<TEMPL>;
		close(TEMPL);
		$PermFile = $basedir . $CityState . "/" . $BizName . "/" . $TheTitle . ".html";
		open(PERM,">$PermFile") || &Error("Can't open $PermFile. Reason: $!");
		foreach (@Tempor)
    		{
    			$TheBGDir = $ImagesDir . $BackgroundImage;
    			$_ =~ s/\<\!-- BodyStuff --\>/<body background=\"$BackgroundImage\">/gi;
			$_ =~ s/\%\%BackgroundImage\%\%/$BackgroundImage/gi;
			$_ =~ s/\<\!-- Font stuff --\>/<font face=\"$TheFont\" color=\"$FontColor\">/gi;
			$_ =~ s/\%\%FontColor\%\%/$FontColor/gi;
			$_ =~ s/\%\%CityState\%\%/$CityState/gi;	
			$_ =~ s/\%\%BizName\%\%/$BizName/gi;
			$_ =~ s/\%\%email\%\%/$Email/gi;
			$_ =~ s/\<\!--ProductTitle--\>/$TheTitle/gi;
			$_ =~ s/\<\!--ProductDescription--\>/$TheDescription/gi;
			$_ =~ s/\<\!--ProductImage--\>/$TheImage/gi;
			$_ =~ s/\<\!-- ProductLinks --\>/$TheProductLinks/gi;
                        $_ =~ s/\%\%PhoneNumber\%\%/$PhoneNumber/gi;
			if ($_ =~ /<!--(\w*)-->/)
			{
				$TheKey = $1;
				$TheThingy=$MyData{$TheKey};
				$TheThingy =~ s/\[/</gi;
				$TheThingy =~ s/\]/>/gi;
				if ($TheKey eq "EmailAddress"){$_ =~ s/<!--$TheKey-->/<a href=\"mailto:$TheThingy\">/gi;}
				else{$_ =~ s/<!--$TheKey-->/$TheThingy/gi;}
			}
			print  PERM "$_";
    		}
	}
	close(PERM);
	&FinalizeWebPage;
}

####### FINALIZE WEB PAGE
sub FinalizeWebPage
{
	#Database should still be open
    	$BackgroundImage=$MyData{PageBackgroundImage};
    	$TheFont=$MyData{PageFont};
    	$FontColor=$MyData{PageFontColor};
    	$Template = $MyData{PageTemplate};
    	$TheTemplate = $basedir . "Templates" . "/" . $Template;
    	open(PAG,"$TheTemplate") || &Error("Can't open $TheTemplate for reading in WritePageOptions routine. Reason: $!");
    	@Pag=<PAG>;
    	close(PAG);
    	
    	$PermPage = $basedir . $CityState . "/" . $BizName . "/" . "index.html";
    	open (PERMY,">$PermPage") || &Error("Can't create $PermPage. Hmm. $!");
    	$count = 0;
    	foreach (@Pag)
    	{
    		$TheBGDir = $ImagesDir . $BackgroundImage;
    		$_ =~ s/\<\!-- BodyStuff --\>/<body background=\"$BackgroundImage\">/gi;
    		$_ =~ s/\<\!-- ProductLinks --\>/$TheProductLinks/gi;
		$_ =~ s/\%\%BackgroundImage\%\%/$BackgroundImage/gi;
		$_ =~ s/\<\!-- Font stuff --\>/<font face=\"$TheFont\" color=\"$FontColor\">/gi;
		$_ =~ s/\%\%FontColor\%\%/$FontColor/gi;
		$_ =~ s/\%\%CityState\%\%/$CityState/gi;	
		$_ =~ s/\%\%BizName\%\%/$BizName/gi;
                $_ =~ s/\%\%TitleTag\%\%/$TitleTag/gi;
                $_ =~ s/\%\%PhoneNumber\%\%/$PhoneNumber/gi;
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
		print PERMY "$_";
   	 }#end foreach loop
   	 close(PERMY);
   	 &CloseMyDatabase;
   	 &FinalStep;
}

####### FINAL STEP
sub FinalStep
{
	&Header;
	&PHed;	
	#Get user's information to populate his individual database.
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
<tr><td>\n";
        print "<center><img src=\"https://surflocal.net/\sm_banner_MKTG3.gif\">\n";
	print "<font color=800000><font size=+2><center><img src=\"https://surflocal.net/images/success.jpg\">Success! GO LIVE to: <p>\n";
	print "</center></center><font color=000000><font size=+1>1- Post your web site online <p></center></font>\n";
	print "<font color=000000><font size=+1>2- Get your Surflocal Editing Tools account information sent to your email ";
	print "<font color=000000><font size=+1>so you can update your new web site.<Br>\n";
	print "<center><form action=Finalize.cgi method=POST><input type=submit value=\"GO LIVE\"></form></td></tr></table>\n";
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
