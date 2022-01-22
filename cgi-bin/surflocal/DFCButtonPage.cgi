#!/usr/local/bin/perl5.22


require 'web-lib.pl';
require 'SurfLocalLib.pl';

####### VARIABLES #######
$DocumentUri = $ENV{DOCUMENT_URI};
$RequestUri = $ENV{REQUEST_URI};
$QueryString = $ENV{QUERY_STRING};
$newform = "/cgi-bin/surflocal/IndexPage.cgi";

$IndexTemplate = "$TemplatesDir" . "DFC_ButtonTemp.html";
$CouponDisplay = "/cgi-bin/surflocal/CouponDisplay.cgi";
$HandleRequest = "cgi-bin/surflocal/NewBeginAdDB.cgi";

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


####### INDEX ARRAY
sub IndexArray
{
	my $inputValue=join(//,@_);#Get subroutine input (from html tag)
	($crap,$loadedNumber)=split(/Array-/,$inputValue);#split input to get number value + -->
	($theNumber,$crap)=split(/--/,$loadedNumber);#ditch the extra crap.
	
	$theFile="$TemplatesDir" . "ia" . $theNumber . ".txt";#Set the filename to "ia" + the number, based on which menu we're processing.
	
	$LinkArrayPage = $basedir . $City . $Abbrevs{$State} . "/LinkArray.txt";#Set this city's link array data file location
	
	open (LOCARAY,"$LinkArrayPage") || print "<!--Cannot open $LinkArrayPage-->\n";#Open the link array page. No failure routine here, because many cities won't have them.
	@LocalLinks=<LOCARAY>;#Create array based on locallink's contents
	if ($LocalLinks[0] ne "")#If there's data, process it.
	{
		$count=0;
		foreach $La (@LocalLinks)
		{
			chomp($La);#whack off extra crap (specifically, the newline character)
			($LocalUrl,$LocalText,$ReplaceText)=split(/\|/,$La);#divide the line into its requisite parts
			$LocalLinkHash{$ReplaceText}=$LocalUrl . "\|" . $LocalText;#populate the hash, telling it which array item contains the information.
			$count++;
		}
	}
	close(LOCARAY);
	
	open (IAFILE,"$theFile")||&Error("Can't open $theFile for reading in IndexArray sub. Reason: $!");
	@myIndex=<IAFILE>;
	close(IAFILE);
	foreach (@myIndex)
	{
		chomp($_);
		($populatedBool,$theLink,$theText)=split(/\|/,$_);
		if ($populatedBool =~ /empty/i)
		{
			
			chomp($theText);
			print "<!--$theText is empty.-->\n";
			if ($LocalLinks[0] ne "")#if this city has local link information, we should post it here.
			{
				#print "<!--LocalLinks 0 has data-->\n";
				$LocalStuff=$LocalLinkHash{$theText};#Set scalar to array item matching this item
				if ($LocalStuff ne "")
				{
					($ThisLocalUrl,$ThisLocalText)=split(/\|/,$LocalStuff);
					print "<!-- LocalStuff is this: $LocalStuff -->\n";
					print "<a href=\"$ThisLocalUrl\">$ThisLocalText</a><br>\n";
				}else{
					#print "<!-- Looked for data for $theText, but didn't find any-->\n";
					print "<a href=\"../buy.cgi\?$State\&$City\&$theLink\">$theText</a><br>\n";
				}
			}
			else
			{
				print "<a href=\"../buy.cgi\?$State\&$City\&$theLink\">$theText</a><br>\n";
			}
		}
		else
		{
			print "<a href=\"$theLink\">$theText</a><br>\n";
		}
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
    		 print "<td align='center' width='136' height='56' background='$imgdr/3_1-out1.jpg'>";
	        print "<a href=\"$HandleUrl\">";
	        print "<font face=\"Georgia\"><strong>Discover Fort Collins</strong></a>";
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
			print "<td align=\"center\" width=\"136\" background=\"$imgdr/$Bcolor-$BGimage.jpg\" bgcolor=\"$Bcolor\" height=\"56\">\n";
			print "<a href=\"$Burl\"><font color=\"$Bfontcolor\" face=\"$Bfont\"><strong>$Btext</strong></font></a></td>\n";
			$BCells++;
			$ThisLoop++;
	    		}
	    		#Otherwise, print the "Build Your Ad Here" stuff.
	    		else
	    		{
				$HandleUrl = "$HandleRequest" . "\?" . "Button" . "\&" . "$State" . "\&" . "$City";		
	       		 print "<td align='center' width='136' height='56' background='$imgdr/5_1-out2.jpg'>";
	       		 print "<a href=\"$HandleUrl\">";
	       		 print "<font face=\"Georgia\"><strong>Discover Fort Collins</strong></a>";
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

####### LOCAL PRODUCT ADS
sub LocalProductAds
{
    $StateCodey = $Abbrevs{"$State"};
    $TextAdFile = "$bottomdir" . "$City" . "$StateCodey" . "/" . "Text.data";
    open(TXAD,"$TextAdFile") or $TextExists = "false";
    if ($TextExists ne "false")
    {
    	@TxAd=<TXAD>;
    	close(TXAD);
    	$Txs = 0;
    	foreach $Tline (@TxAd)
    	{
    	    $Txs++;
    	}
    	if ($Txs >= 4)
    	{
    	    $Trows = ($Txs / 4);
    	    if ($Trows =~ /\./)
		{
		    ($Tnumber,$Crapola) = split(/\./,$Trows);
		    $Trows++;
		}
    	}	
    	else 
    	{
		$Trows = 1;		
    	}
    	
    	#$Trows equals the number of four-cell rows I need to print
    	$Cells = 0;
	
    	#Print rows until rows printed equals $Divided
    	for ($i = 0; $i <= $Trows; $i++)
    	{
		print "<tr>\n";
		$ThisLoop = 0;
		until ($ThisLoop == 4)
		{
		    #print "Loop $ThisLoop";
		    if ($Cells < $Txs)
		    {
			$TheAd = "$TxAd[$Cells]";
			chomp($TheAd);
			(@CurrentText) = split(/\|/,$TheAd);
			foreach $texter (@CurrentText)
			{
				($TheKey,$TheValue) = split(/\=/,$texter);
				$ThisAd{$TheKey} = $TheValue;
			}
			$AdUrl = $ThisAd{Url};
			$AdText = $ThisAd{Text};
			$AdFont=$ThisAd{Font};
			$AdFontColor=$ThisAd{FontColor};
			print "<td><a href=\"$AdUrl\"><font size=\-1><b><font face=\"$AdFont\" color=$AdFontColor>$AdText</a>";
			print "</font></b></td>\n";
			$Cells++;
			$ThisLoop++;
		    }
		    else
		    {
			$AdDisp = "$HandleRequest" . "\?" . "TextAd" . "\&" . "$State" . "\&" . "$City";
			print "<td><center><font face=\"Georgia\"><b><font size=\-1>";
			print "<a href=\"$AdDisp\" class=\"roll\">Your product ad here</a>";
			print "</font></b></center></td>\n";
			$Cells++;
			$ThisLoop++;
		    }
		}
		print "</tr>\n";
    	}
    	
    	print "</table>\n";
    }
    else
    	{
    		$AdDis = "$HandleRequest" . "\?" . "TextAd" . "\&" . "$State" . "\&" . "$City";
    		print "<tr><td>\n";
		print "<a href=\"$AdDis\" class=\"roll\">There are no Product ads for $City, $State yet. Click here to be the first!</a><br>";
    		print "</td></tr>\n";
    	}
}

####### GENERATE CATEGORIES
sub GenerateCategories
{
    $StateCodey = $Abbrevs{"$State"};
    
    $CheckDir = "$bottomdir" . "$City" . "$StateCodey" . "/" . "CouponCategories.data";
    open(TOK,"$CheckDir") or $CouponCatsMissing = "true";
    if ($CouponCatsMissing)
    {
    	open(TIK,">$CheckDir");
    	close(TIK);
    }
    else
    {
    	@DirFiles =<TOK>;
    	close(TOK);
    	foreach $DirFile (@DirFiles)
    	{
    		chomp($DirFile);
    	    if ($DirFile ne "")
		{
		    push(@CatList,$DirFile);
		}
    	}
    }
    if (@CatList)
    {
	$Cats = 0;
        foreach $Cat (@CatList)
	{
	    $Cats++;
	}
	if ($Cats >= 4)
	{
	    $Divided = ($Cats / 4);
	    if ($Divided =~ /\./)
	    {
		($Dnumber,$Crapola) = split(/\./,$Divided);
		$Divided++;
	    }
	}
	else 
	{
	    $Divided = 1;
	}
	#$Divided equals the number of four-cell rows I need to print
	$PrintedCells = 0;
	
	#Print rows until rows printed equals $Divided
	for ($i = 0; $i <= $Divided; $i++)
	{
	    print "<tr>\n";
	    $ThisLoop = 0;
	    until ($ThisLoop == 4)
	    {
		if ($PrintedCells < $Cats)
		{
		    $TheCategory = "$CatList[$PrintedCells]";
		    #$TheCategory =~ s/(\w+)\.cat/$1/gi;
		    
		    $CoupDisp = "$CouponDisplay" . "\?" . "$State" . "\&" . "$City" . "\&" . "$TheCategory";
		    print "<td WIDTH=25\%><center><font face=\"Georgia\"><b><font size=-1>";
		    print "<a href=\"$CoupDisp\" class=\"roll\"><b>$TheCategory</a></b>";
		    print "</font></font></b></center></td>\n";
		    $PrintedCells++;
		    $ThisLoop++;
		}
		else
		{
		    $CoupDisp = "$HandleRequest" . "\?" . "Coupon" . "\&" . "$State" . "\&" . "$City";
		    print "<td WIDTH=25\%><center><font face=\"Georgia\"><font size=-1>";
		    print "<a href=\"$CoupDisp\" class=\"roll\">Your category here</a>";
		    print "</font></font></b></td>\n";
		    $PrintedCells++;
		    $ThisLoop++;
		}
	    }
	    print "</tr>\n";
	}
	print "</table>\n";
    }
    else
    {
        print "There are no coupon ads for this city yet. Click the link above and be the first!</center>";
    }
}

####### ASSIGN LOCATION
sub AssignLocation
{
    #/atheist/scripts/SurfLocal/MuskogeeOK/index.html.
    #/AdaOK/index.html
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
    #print "StateCode is $StateCode<br>State is $State<br>City is $City<br>PreSlash is $PreSlash<br>Atheist is $Atheist, <br>Scripts is $Scripts<br>Surflocal is $SurfLocal<br>Dir1 is $Dir1<br>DocumentUri is $DocumentUri.";
    #exit;
    
   # $TheDirectory = $bottomdir . "$State" . "/" . "$City";
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
