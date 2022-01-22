#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2020
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';

####### VARIABLES #######
$DocumentUri = $ENV{DOCUMENT_URI};
$RequestUri = $ENV{REQUEST_URI};
$QueryString = $ENV{QUERY_STRING};
$newform = "/cgi-bin/surflocal/IndexPage-Surflocal-Media.cgi";

$IndexTemplate = "$TemplatesDir" . "/cities/IndexTemplate-Surflocal-Media.html";
$CouponDisplay = "/cgi-bin/surflocal/CouponDisplay.cgi";
$HandleRequest = "/cgi-bin/surflocal/NewBeginAdDB.cgi";

####### CONDITIONALS ####
&AssignLocation;
&ParsePage;
exit;
#########################

####### REPLACE VALUES
sub ReplaceValues
{
    $StateCode = $Abbrevs{"$State"};
    
    $_ =~ s/\%\%City\%\%/$City/gi;
    $CityImage = lc($City);
    $_ =~ s/\%\%CityImage\%\%/$CityImage/gi;
    $_ =~ s/\%\%State\%\%/$State/gi;
    $_ =~ s/\%\%StateCode\%\%/$StateCode/gi;
    $_ =~ s/\%\%CouponScript\%\%/$CouponDisplay/gi;
}

####### PARSE PAGE
sub ParsePage
{
    open (TEMPL, "$IndexTemplate") || &Error("Can't open $IndexTemplate in ParsePage sub. Reason: $!");
    @Templ=<TEMPL>;
    close(TEMPL);
    &Header;
    foreach (@Templ)
    {
        &ReplaceValues;
	if ($_ =~ /\<\!-- CategoriesHere --\>/)
	{
	    &GenerateCategories;
	}
	if ($_ =~ /<\!--IndexArray/)
	{
		&IndexArray($_);
	}
	if ($_ =~ /\<\!--ProductAds1--\>/)
	{
	    &LocalProductAds;
	}
	if ($_ =~ /\<\!--Buttons--\>/)
	{
	    &ButtonAds;
	}
	$_ =~ s/\%\%CouponCreator\%\%/$HandleRequest\?Coupon\&$State\&$City/gi;
	
	print "$_";
    }
}



####### BUTTON ADS
sub ButtonAds
{
    $StateCodey = $Abbrevs{"$State"};
    $ButtonFile = "$basedir" . "$City" . "$StateCodey" . "/" . "Button.data";
    open(BTN,"$ButtonFile") or $NoButtons="true";
    if ($NoButtons ne "true")
    {
    	@Btn=<BTN>;
    	close(BTN);
    }
    if ($NoButtons)
    {
    	$IterationMax=5;
    	$HandleUrl = "$HandleRequest" . "\?" . "Button" . "\&" . "$State" . "\&" . "$City";
    	for ($i=0; $i <= $IterationMax; $i++)
    	{
    		print "<td align='center' width='136' height='56' background='$imgdr/2_1-out1.jpg'>";
	        print "<a href=\"$HandleUrl\">";
	        print "<font size=-1>
 USA Search Placement</a>";
	        print "</td>\n";
    	}
    }
    else
    {
    	$ButtonCount = 0;
   	foreach $Bootn (@Btn)
    	{
    	    $ButtonCount++;
    	}
    	if ($ButtonCount >= 5)
    	{
		#Divide the amount of lines by 5, because I want 5 buttons
		#per row on the page. If the divided number has a decimal,
		#kill the decimal and the stuff after it and round the number up.
       	 $ButtonRows = ($ButtonCount / 5);
       	 if ($ButtonRows =~ /\./)
		{
		    ($Bnumber,$Crapola) = split(/\./,$ButtonRows);
		    $ButtonRows++;
		}
    	}
    	else 
    	{
		$ButtonRows = 1;
    	}
    	#$BCells equals the number of four-cell rows I need to print
    	$BCells = 0;
	$imgdr = "$baseurl" . "images";
    	#Print rows until rows printed equals $Divided
    	for ($i = 0; $i <= $ButtonRows; $i++)
    	{
		print "<tr>\n";
		$ThisLoop = 0;
		until ($ThisLoop == 5)
		{
		    #If there's still less total cells printed than the amount of buttons,
		    #there must be data left in the file to print.
		    if (($BCells < $ButtonCount) && ($Btn[$i] ne "\n"))
		    {
		    	chomp($Btn[$i]);
		    	print "<!-- Btn\[$i\] is $Btn[$i] -->\n";
		    	(@CurrentButton) = split(/\|/,$Btn[$BCells]);
		    	foreach $current (@CurrentButton)
		    	{
		    		($OneKey,$OneValue) = split(/\=/,$current);
		    		$ThisButton{$OneKey} = $OneValue;
		    	}
			#$TheUserName = "$Btn";
			$Bcolor=$ThisButton{Color};
			$BGimage=$ThisButton{BackgroundImage};
			$Burl=$ThisButton{Url};
			$Bfontcolor=$ThisButton{FontColor};
			$Btext=$ThisButton{Text};
			$Bfont=$ThisButton{Font};
			print "<td align=\"center\" width=\"136\" background=\"$imgdr/$Bcolor-$BGimage.gif\" height=\"56\">\n";
			print "<a href=\"$Burl\" target=\"_top\"><font color=\"$Bfontcolor\" face=\"$Bfont\"><font size=-1>

$Btext</font></a></td>\n";
			$BCells++;
			$ThisLoop++;
	    		}
	    		#Otherwise, print the "Build Your Ad Here" stuff.
	    		else
	    		{
				$HandleUrl = "$HandleRequest" . "\?" . "Button" . "\&" . "$State" . "\&" . "$City";		
	       		 print "<td align='center' width='136' height='56' background='$imgdr/5_6-out2.jpg'>";
	       		 print "<a href=\"$HandleUrl\" target=\"_top\">";
	       		 print "<font size=-1>

$City $State <br>Press Release</a>";
	       		 print "</td>\n";
				$BCells++;
				$ThisLoop++;
		    	}	    
		}
    	}#end if from if buttons exist
	print "</tr>\n";
    }
print "</table>\n";
}



####### ASSIGN LOCATION
sub AssignLocation
{
    #/home/htdocs/surflocal/AmarilloTX/index.shtml.
    #/BorgerTX/sindex.html
    ($PreSlash,$Dir1,$indexy) = split(/\//,$DocumentUri);
    #&Header;
    #print "DocumentUri is $DocumentUri<br>\n";
    if ($State eq "")
    {
	$TheDir = $Dir1;
	($LastLetter) = chop($TheDir);
	($FirstLetter) = chop($TheDir);
	$StateCode = "$FirstLetter" . "$LastLetter";
	$State = $States{$StateCode};
	$City = $TheDir;
    }
    
    #These commented lines are in here for testing because environmental variables change as the 
    #script is moved from system to system. Don't delete them.
    #
    #&Header;
    #print "StateCode is $StateCode<br>State is $State<br>City is $City<br>PreSlash is $PreSlash<br>Scripts is $Scripts<br>Surflocal is $SurfLocal<br>Dir1 is $Dir1<br>DocumentUri is $DocumentUri.";
    #exit;
    
   # $TheDirectory = "$basedir" . "$State" . "/" . "$City";
   # opendir (CITY,"$TheDirectory") || &NoSuch;
   # closedir(CITY);
   # if ($NoSuch)
   # {
   #	mkdir("$TheDirectory", 0777) || &Error("Could not create directory $TheDirectory. Reason: $!");
   #   }
}

####### NO SUCH
sub NoSuch
{
	$NoSuch = 1;
}
