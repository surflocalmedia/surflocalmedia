#!/usr/local/bin/perl5.22
# Copyright Surflocal.net 2004-2005
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';
require 'cookie.lib';

#####set variables here######
$newform = "/cgi-bin/surflocal/MultipleUpload.cgi";
$ButtonTemplate = "$basedir" . "Templates" . "/" . "ButtonTemplate.html";
$ImageDir = "http://www.SurfLocal.net/images";
###################
&Parse;


####### CONDITIONALS
&SelectCityArray unless $in{action};
$Action=$in{action};
if ($Action eq "SetCityArray") {&SetCityArray;}
if ($Action eq "SelectCity") {&SelectCity;}
if ($Action eq "SelectButton") {&SelectButton;}
if ($Action eq "DoTheUpload") {&DoTheUpload;}


#City list is MultipleUploadTemp.txt

####### DO THE UPLOAD
sub DoTheUpload
{
	#Button,City must be present
	$Button=$in{Button};
	$City=$in{City};
	if (($Button eq "") || ($City eq ""))
	{
		&Error("I didn't get all the inputs from the previous iteration. Button is $Button City is $City.");
	}
	$ButtonFile = "$basedir" . "$City" . "/" . "Button.data";#contains pipe-delimited data
	open(BASEFILE,"$ButtonFile") || &Error("Can't open $ButtonFile. Reason: $!");
	@TheButtons=<BASEFILE>;
	close(BASEFILE);
	$ThisButton=$TheButtons[$Button];#This item in the array is the correct button
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
		if ($Destination ne "")
		{
			$NewFile = $basedir . $Destination . "/" . "Button.data";
			open(DEST,">>$NewFile") || &Error("Can't open $NewFile. Reason $!");
			print DEST "$ThisButton";
			close(DEST);
		}
	}
	&Header;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";
	print "<h1>WELL DONE...</h1>\n";
	print "CONGRATS......IT WORKED...\n";
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
		print "<h1>Select a button to upload</h1>\n";
		print "<form action=$newform method=POST>\n";
		print "<input type=hidden name=action value=DoTheUpload>\n";
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
    		print "<input type=submit value=\"Upload the selected button\">\n";
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
	print "<h1>Select the city where your button is</h1>\n";
	print "Find the city where the button you want to upload is. This button MUST <b>";
	print "ALREADY EXIST</b> for you to upload it. You can only select <b>ONE ";
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
	&Header;
	open(CHOOSE,"$basedir" . "Templates" . "/" . "ChooseCities.html") || &Error("Can't open the cities file. Reason: $!");
	while(<CHOOSE>)
	{
		if ($_ =~ /\%\%ListOfCities\%\%/)
		{
			&GetCityListFile;
		}
		else
		{
			print "$_";
		}
	}
	close(CHOOSE);
	exit;
}
####### SET CITY ARRAY
sub SetCityArray
{
	$Cities = $in{Cities};
	if ($Cities eq "")
	{
		&Error("You must first choose at least one city");
	}
	open (TMP,">MultipleUploadTemp.txt") || &Error("Can't open temporary cities file.");
	print TMP "$Cities";
	close(TMP);
	&Header;
	&PHed;
print "<link href=\"/styleC.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><img src=\"http://surflocal.net/\sm_banner_MKTG.jpg
\"><br><br></center>\n";
	print "<h1><font color=000040>I have saved your city selections</h1>\n";
	print "David, the list of cities you have chosen is saved. You must now complete the ";
	print "multiple upload process. If you wish to upload different cities, you must go back ";
	print "to the beginning.\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=SelectCity>\n";
	print "<br><input type=submit value=\"Select the city where the button is\"></form>\n";
	exit;
}
