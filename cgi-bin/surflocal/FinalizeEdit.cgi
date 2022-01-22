#!/usr/local/bin/perl5.22
# Copyright Surflocal Media 2004-2022
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';
#####set variables here######
$MasterDatabase = "$basedir" . "Secure" . "/" . "MasterDatabase.txt";
$newform = "/cgi-bin/surflocal/FinalizeEdit.cgi";
$Hed{T} = "Finalize your ad";
###################
&Parse;
&GetCookieValues;
#        This gives me $BizName and $CityState

#&OpenCityDatabase;
#$AdType=$CityData{$BizName};
#&CloseCityDatabase;

&GetCookies("Edit");
$AdType=$Cookies{"Edit"};

#&Header;
#print "got past getcookies and ad type. My Biz name: $BizName. My Citystate: $CityState. My AdType: $AdType.<br>\n";


&OpenMyDatabase;
#### WRITE TO CITY'S AD TYPE DATABASE
#Essentially, I'm just dumping information to be written into the city's ad type database.
#Each ad type has its own database.
#Don't need coupon here because the coupon should already be in the city's
#database.
if ($AdType =~ /TextAd/)
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
	$MustRecord="true";
	#print "My ad type is text. I got Torecord: '$ToRecord' into the $Prefix file. MustRecord is $MustRecord.<br>\n";
	
}
elsif ($AdType=~ /Button/) 
{
	#Same thing here as Text ads.
	$Prefix = "Button";
	$ToRecord = "BackgroundImage=" . $MyData{ButtonBackgroundImage};
	$ToRecord .= "\|" . "Color=" . $MyData{ButtonColor};
	$ToRecord .= "\|" . "Font=" . $MyData{ButtonFont};
	$ToRecord .= "\|" . "BizName=" . $BizName;
	$ToRecord .= "\|" . "FontColor=" . $MyData{ButtonFontColor};
	$ToRecord .= "\|" . "Text=" . $MyData{ButtonText};
	$ToRecord .= "\|" . "Url=" . $MyData{ButtonUrl} . "\n";
	$MustRecord="true";
}

if ($MustRecord)
{
	#Set location of the ad type database, based on the "Prefix" value above
	$CityAdTypeDatabase = $basedir . $CityState . "/" . $Prefix . ".data";
	#print "I'm gonna open this database: $CityAdTypeDatabase<br>\n";
	#exit;
	open(CITYREAD,"$CityAdTypeDatabase") || &Error("Can't open $CityAdTypeDatabase to read. Reason: $!");
	@CityStuff=<CITYREAD>;
	close(CITYREAD);
	#print "OK. I've read alll the information from that database.<br>\n";
	#exit;
	open (CITYAD,">$CityAdTypeDatabase") || &Error("Can't open $CityAdTypeDatabase to overwrite. Reason: $!");
	foreach(@CityStuff)
	{
		#chomp($_);
		@CityArray=();
		%ThisHash=();
		(@CityArray)=split(/\|/,$_);
		foreach $item (@CityArray)
		{
			($TheKey,$TheValue)=split(/\=/,$item);
			$ThisHash{$TheKey}=$TheValue;
		}
		if ($ThisHash{BizName} eq $BizName)
		{
			print CITYAD "$ToRecord";
		}
		else
		{
			print CITYAD "$_";
		}
	}
	close(CITYAD);
}
#print "printed the information into that database.<br>\n";
#exit;

#Need to write the data to the Web pages
if ($AdType =~ /Page/)
{
	#Write stuff to final page. Need to overwrite existing page with new page.
	&RecordProductPage;
}
	


#Kill User, edit cookie
&CookieHeader;
&SetCookies("User","");
&SetCookies("Edit","");
&CookieFooter;
&PHed;
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=4 WIDTH=550>
        <tr><td>\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG.jpg\"><br><br>\n";
print "<font size=+1><font color=000000>Congratulations <font color=800000>$BizName! <font color=000000>You are done!</font></font></center>\n";
print "<CENTER><font color=000000><p>YOUR INFORMATION WAS SUCESSFULLY UPDATED.<br>\n";
print "<p><font color=000000>Locate Your Ad by Clicking Here: ";
print "<a href=\"$baseurl$CityState\"><font color=800000>$baseurl$CityState</font></a><br><br>\n";
#If they built a Web page, they'll want to know how to get there
if ($AdType =~ /Plus/)
{
		
$TheWeb = $basurl . $CityState . "/" . $BizName . "/" . "index.html";
	print "<br><font color=000000>Your Website is here: <a href=\"$TheWeb\"><font color=800000>$TheWeb</font></a>\n";
	print "<br><font color=000000>Copy this link for your future reference.\n";
}
#print "<br><font color=000000>In the future, if you ever want to edit your ad, you'll need this link ";
#if ($SubsequentAd ne "true")
#{
#	print "(it has also been e-mailed to $MyData{Email}) ";
#}
#print ": <a href=\"$TheLink\"><font color=800000>$TheLink</font></a><br>\n";
exit;

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
    	for ($i=1; $i <=$TheNumber; $i++)
    	{
    		$MyPhrase = "Product_" . $i . "_Name";
    		$ThisFileName = $MyData{$MyPhrase};
    		$TheLinkage = $ThisDirectory . $ThisFileName . ".html";
    		if ($TheProductLinks){$TheProductLinks .= " \| <a href=\"$TheLinkage\">$ThisFileName</a>";}
    		else{$TheProductLinks = "<a href=\"$TheLinkage\">$ThisFileName</a>";}
    	}    	
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
    	open(PAG,"$TheTemplate") || &Error("Can't open $TheTemplate for reading in Finalize Web Page routine. Reason: $!");
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
}
