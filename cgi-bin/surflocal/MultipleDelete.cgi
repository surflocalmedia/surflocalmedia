#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2005
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

#####set variables here######
$newform = "/cgi-bin/surflocal/MultipleDelete.cgi";
$ButtonTemplate = "$basedir" . "Templates" . "/" . "ButtonTemplate.html";
$ImageDir = "http://www.SurfLocal.net/images";
###################
&Parse;


##############
#
# Essentially, I need to do this:
#   * Select a city that contains the ad to be axed
#   * Select the ad from that city's ads
#   * Select an array of cities to ax the ads from (the first city should be automatically included in this list
#   * Go through each city's buttondata.txt file, compare the hash items and delete the matching ad
#
##############


####### CONDITIONALS
#&SelectCityArray unless $in{action};
&SelectCity unless $in{action};#user should select the city where the offending ad is.
$Action=$in{action};
if ($Action eq "SetCityArray") {&SetCityArray;}
if ($Action eq "SelectCityArray") {&SelectCityArray;}
if ($Action eq "SelectButton") {&SelectButton;}
if ($Action eq "DoTheDelete") {&DoTheDelete;}


#City list is MultipleUploadTemp.txt

####### DO THE DELETE
sub DoTheDelete
{
	#Button,City must be present
	$Button=$in{Button};
	#$City=$in{City};
	if ($Button eq ""){&Error("I didn't get all the inputs from the previous iteration. Button is $Button.");}
	@DoomedButton = split(/\|/,$Button);
	foreach $doomed (@DoomedButton)#make a hash of the button to kill
	{
		($KillKey,$KillValue) = split(/\=/,$doomed);
		$ToKill{$KillKey} = $KillValue;
	}
	
	open (TEMPFILE,"MultipleUploadTemp.txt") || &Error("Can't open the Temp file. Reason: $!");
	@CitiesList=<TEMPFILE>;
	close(TEMPFILE);
	foreach (@CitiesList)
	{
		if ($_ ne "")
		{
			chomp($_);
			@UploadTo=split(/\,/,$_);
			$Hit=1;
		}
	}
	if ($Hit != 1)
	{
		&Error("There was a problem with the Temporary List. It appears to be empty.");
	}
	foreach $Destination (@UploadTo)
	{
		@WriteList=();
		if ($Destination ne "")
		{
			$NewFile = $basedir . $Destination . "/" . "Button.data";
			open (DEST,"$NewFile") || &Error("Can't read $NewFile. Reason: $!");
			while (<DEST>)
			{
				chomp($_);
				(@TempArray) = split(/\|/,$_);
				foreach $temp (@TempArray)
				{
					($TempKey,$TempValue) = split(/\=/,$temp);
					$TempHash{$TempKey} = $TempValue;
				}
				if ($TempHash{BizName} eq $ToKill{BizName})
				{
					next;
				}
				else
				{
					push(@WriteList,$_);
				}
			}
			close(DEST);
			open(DEST,">$NewFile") || &Error("Can't overwrite $NewFile. Reason $!");
			foreach $toWrite (@WriteList)
			{
				print DEST "$toWrite\n";
			}
			close(DEST);
		}
	}
	&Header;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";
	print "<h1>WELL DONE...</h1>\n";
	print "CONGRATS...IT WORKED.\n";
	exit;
}
	

####### GET CITY LIST FILE
sub GetCityListFile
{
	#simply prints a select input with each city in the file.
	open(CITYLIST,"ListOfCities.txt") || &Error("Can't open City List. Reason: $!");
	@Citieses =<CITYLIST>;
	close(CITYLIST);
	foreach $City (@Citieses)
	{
		print "$City";
	}
}

####### SELECT BUTTON
sub SelectButton
{
	$ThisCity=$in{Cities};
	if ($ThisCity eq "")
	{
		&Error("You must choose a base city, dummy!");
	}
	#now I need to add this city to the temporary file (overwrite file completely)
	open (TEMPFILE,">MultipleUploadTemp.txt") || &Error("Can't open the Temp file. Reason: $!");
	print TEMPFILE "$ThisCity";
	close(TEMPFILE);
	$ButtonFile = "$basedir" . "$ThisCity" . "/" . "Button.data";#contains pipe-delimited data
	open(BTN,"$ButtonFile") or $NoButtons="true";
	
    	if ($NoButtons ne "true")#the city's directory has a button file
    	{
    		@Btn=<BTN>;#fill the array with the file's contents
    		close(BTN);
    	}
    	else#there is no button file
    	{
    		close(BTN);
    		&Error("This city does not contain a buttons file, meaning no buttons are there.");
    	}
    	$ButtonsCount=0;#clear it out and start at 0
    	foreach(@Btn)#iterate through array, increment count
    	{
    		$ButtonsCount++;
    	}
    	if ($ButtonsCount == 0)#the file was either empty or there's a problem.
    	{
    		&Error("This city doesn't have any buttons, dude. To upload a button to multiple towns, the button must first exist. Don't say I didn't tell you.");
    	}
    	else
    	{
    		&Header;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";

		print "<h1>Select a button ad to delete</h1>\n";
		print "The button ad you select below will be deleted from all the cities you select on the next step.<br>\n";
		print "<form action=$newform method=POST>\n";
		print "<input type=hidden name=action value=SelectCityArray>\n";
		print "<input type=hidden name=City value=\"$ThisCity\">\n";
		print "<table border=1 cellpadding=3>\n";
    		for ($i=0;$i<=$ButtonsCount;$i++)#iterate through array, processing each button.
    		{
    			if ($Btn[$i] ne "\n")#make sure this line isn't blank.
    			{
    				chomp($Btn[$i]);#kill the newline
    				(@CurrentButton) = split(/\|/,$Btn[$i]);#put this line's data into an array
    				foreach $current (@CurrentButton)#make a hash with the data
    				{
    					($OneKey,$OneValue) = split(/\=/,$current);
    					$ThisButton{$OneKey} = $OneValue;
    				}
    				$Bcolor=$ThisButton{Color};
				$BGimage=$ThisButton{BackgroundImage};
				$Burl=$ThisButton{Url};
				$Bfontcolor=$ThisButton{FontColor};
				$Btext=$ThisButton{Text};
				$Bfont=$ThisButton{Font};
				#print the button and the form input
				#each input is based on this button's position in the file
				print "<tr><td><input type=radio name=Button value=$i></td><td>\n";
				print "<table><tr>\n";
				print "<td align=\"center\" width=\"136\" background=\"$imgdr/$Bcolor-$BGimage.jpg\" bgcolor=\"E3EEE3\" height=\"56\">\n";
				print "<a href=\"$Burl\"><font color=\"$Bfontcolor\" face=\"$Bfont\"><strong>$Btext</strong></font></a></td>\n";
				print "</tr></table>\n";
				print "</td></tr>\n";
    			}
    		}#End for loop
    		print "</table><br>\n";
    		print "<input type=submit value=\"Go to select cities to delete this button from\">\n";
    		print "</form>\n";
    		exit;
    	}
}


####### SELECT CITY
sub SelectCity
{
	&Header;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";
	print "<h1>Select the city that contains the button you want to delete</h1>\n";
	print "Find the city where the button you want to delete is. This button MUST <b>";
	print "ALREADY EXIST</b> for you to delete it. You can only select <b>ONE ";
	print "CITY</b> from the list below. After you've selected a city, you'll be able ";
	print "to select the button from a list of all the buttons in that city.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=SelectButton>\n";
	&GetCityListFile;
	print "</select>\n";
	print "<br><input type=submit value=\"Select a button from the selected city\">\n";
	exit;
}

####### SELECT CITY ARRAY
sub SelectCityArray
{
	$Button=$in{Button};
	$City=$in{City};
	if (($Button eq "") || ($City eq ""))
	{
		&Error("I didn't get all the inputs from the previous iteration. Button is $Button City is $City.");
	}
	&GetThisButton;
	&Header;
	open(CHOOSE,"$basedir" . "Templates" . "/" . "ChooseCities2.html") || &Error("Can't open the cities file. Reason: $!");
	while(<CHOOSE>)
	{
		if ($_ =~ /\%\%ListOfCities\%\%/)
		{
			&GetCityListFile;
		}
		
		else
		{
			$_ =~ s/\%\%City\%\%/$City/gi;
			$_ =~ s/\%\%Button\%\%/$ThisButton/gi;
			print "$_";
		}
	}
	print "<!-Button is $Button. ThisButton is $ThisButton-->\n";
	close(CHOOSE);
	exit;
}

####### GET THIS BUTTON
sub GetThisButton
{
	$ButFile = $basedir. $City . "/" . "Button.data";
	open (BUTTS,"$ButFile") || &Error("Can't open $ButFile. Reason: $!");
	@ButtHole=<BUTTS>;
	close(BUTTS);
	#&Header;
	#foreach (@ButtHole)
	#{
	#	print "<!--$_-->\n";
	#}
	$ThisButton = $ButtHole[$Button];
	if ($ThisButton eq "")
	{
		&Error("Button number $Button is empty.");
	}
	chomp($ThisButton);
}

####### SET CITY ARRAY
sub SetCityArray
{
	$Cities = $in{Cities};
	$Button = $in{Button};
	if ($Cities eq ""){&Error("You must first choose at least one city");}
	if ($Button eq ""){&Error("There's a problem. I forgot which button you want. Duh.");}
	open (TMP,">>MultipleUploadTemp.txt") || &Error("Can't open temporary cities file.");
	print TMP "$Cities";
	close(TMP);
	&Header;
	&PHed;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
	print "<h1>I have saved your city selections</h1>\n";
	print "David, the list of cities you have chosen is saved. You must now complete the ";
	print "multiple upload process. If you wish to upload different cities, you must go back ";
	print "to the beginning.\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=DoTheDelete>\n";
	print "<input type=hidden name=Button value=\"$Button\">\n";
	print "<br><input type=submit value=\"Delete the button from all the selected cities\"></form>\n";
	exit;
}
