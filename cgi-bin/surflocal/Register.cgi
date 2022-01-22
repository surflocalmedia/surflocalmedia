#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2004-2022
# See suite header in BeginAdDB script
# for copyright and usage information.

require 'web-lib.pl';
require 'SurfLocalLib.pl';

#####set variables here######
$newform = "$baseurl" . "Register.cgi";
$Hed{T} = "Making decision";
$WebPageScript = "$baseurl" . "Page.cgi";
$MasterDatabase = "$basedir" . "Secure" . "/" . "MasterDatabase.txt";
###################
&Parse;
&ShortenValues;
&Error("This script can't operate without input") unless (%in);
if ($AdType eq "CouponOnly")
{
	&CouponOnly unless ($Action);
	if ($Action eq "RecordData") 
	{
		&RecordData("Coupon");
	}
}
if ($AdType eq "CouponPlus")
{
	if ($Action eq "FinishWebPage")
	{
		&WebPage("Coupon");
	}
	elsif ($Action eq "RecordData")
	{
		&RecordData("Coupon");
	}
	else
	{
		&OnToPage("Coupon");
	}
}
if ($AdType eq "ButtonOnly")
{
	&ButtonOnly unless ($Action);
	if ($Action eq "RecordData") 
	{
		&RecordData("Button");
	}
}
if ($AdType eq "ButtonPlus") 
{
	if ($Action eq "FinishWebPage")
	{
		&WebPage("Button");
	}
	elsif ($Action eq "RecordData")
	{
		&RecordData("Button");
	}
	else
	{
		&OnToPage("Button");
	}
}
if ($AdType eq "TextAdOnly")
{
	&TextOnly unless ($Action);
	if ($Action eq "RecordData") 
	{
		&RecordData("Text");
	}
}
if ($AdType eq "TextAdPlus") 
{
	if ($Action eq "FinishWebPage")
	{
		&WebPage("TextAd");
	}
	elsif ($Action eq "RecordData")
	{
		&RecordData("Text");
	}
	else
	{
		&OnToPage("Text");
	}
}
###################

sub OnToPage
{
	&Header;
	&PHed;
	print "<h1>Next step: Building a Web Page!</h1>\n";
	print "Now that you have completed your ad, your next step is building a Web page.<p>\n";
	print "Our Web page program works very simply. The first page will present you with several dialog boxes. That page is designed";
	print " to set up the information for pages that describe up to five products you wish to advertise on their own Web pages.<p>\n";
	print "After the first page, you will be presented with a choice of Web pages, and then you will be able to edit the Web page \n";
	print "right on your screen.<p>\n";
	print "<form action=$WebPageScript method=POST>\n";
	&PrintHiddenValues;
	print "<input type=submit value=\"Click here to go on to the next step\"></form></body></html>\n";
	exit;
}


sub RecordData
{
	#if $in{Web} exists, the type is a web page. The value of that scalar is what kind of ad
	#the user has recorded.
	
	&Error("You must fill out all the required fields.") unless (($in{Address1}) && ($in{FirstName}) && ($in{LastName}) && ($in{Zip}) && ($in{Phone}) && ($in{Email}));
	if ($in{Zip} !~ /\d{5}/)
	{
		&Error("Zip code must be an actual ZIP code. Please enter a correct ZIP code.");
	}
	if ($in{Phone} !~ /\d{3}-\d{3}-\d{4}/)
	{
		&Error("Phone number MUST be formatted like 555-123-4567. You cannot include parenthesis \(\) or 1 before the number.");
	}
	if ($in{Email}	!~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/)
	{
		&Error("You must enter an actual e-mail address.");
	}
	$DataType = join(/,@_);
	$ToWrite = "$State";
	$ToWrite .= "\|$City\|$BizName\|$AdType\|$in{FirstName}\|$in{LastName}\|$in{Address1}";
	$ToWrite .= "\|$in{Address2}\|$in{Zip}\|$in{Phone}\|$in{Email}";
	open (READMASTER,"$MasterDatabase") || &Error("Can't open $MasterDatabase for reading in RecordData sub. Reason: $!");
	@ReadMaster=<READMASTER>;
	close(READMASTER);
	################
	 $howmanylines = 0;
	################
	foreach $Master (@ReadMaster)
	{
		$howmanylines++;
		($MState,$MCity,$MBiz,$Junk) = split(/\|/,$Master,4);
		if (($MState eq $State) && ($MCity eq $City) && ($MBiz eq $BizName))
		{
			&Error("The business $BizName is already registered for $MCity, $MState. Please contact the administrator for help.");
		}
	}
	
	############
	# RANDOM 9-digit number
	############
	$number=$howmanylines;
	srand();
	$time = `date +"%T"`;
	($hour,$minute,$second) = split(/:/, $time);
	$SeedNumber = "$hour" . "$second" . "$minute";
	$RandomNumber = int(rand($number)) + $SeedNumber;
	$RandomNumber = ($RandomNumber * $RandomNumber);
	###################################################
	$ItsLength = length($RandomNumber);
	if ($ItsLength > 9)
	{
		until (length($RandomNumber) == 9)
		{
			chop($RandomNumber);
		}
	}
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
	$ToWrite .= "\|$RandomNumber\n";
	#################
	# FINALLY! End the random number routine
	#################
	
	open (WRITEMASTER,">>$MasterDatabase") || &Error("Can't open $MasterDatabase for writing in RecordData sub. Reason: $!");
	print WRITEMASTER "$ToWrite";
	close(WRITEMASTER);
	if ($DataType eq "Coupon")
	{
		$StateCode = $Abbrevs{$State};
		$OldFile = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".cnp";
		$NewFile = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".coupon";
		if (rename($OldFile, $NewFile))
		{
			&RecordCategory;
			&CheckCatList;
			&ReportSuccess;
		}
		else
		{
			&Error("Could not rename $State\/$City\/$BizName. Reason: $!");
		}
		if ($in{Web})
		{
			$OldWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".inp";
			$NewWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".html";
			if (rename($OldWeb, $NewWeb))
			{
				&MailWebInfo;
			}
			else
			{
				&Error("For some reason, I could not create your Web page. Please contact the webmaster at <a href=mailto:$Admin>this link</a> and mention this error. The problematic page is $BizName. The server says this is the problem: $!");
			}
		}
	}
	if ($DataType eq "Button")
	{
		$StateCode = $Abbrevs{$State};
		$TempFile = "$basedir" . "$City" . "$StateCode" . "/" . "buttons" . ".temp";
		$PermFile = "$basedir" . "$City" . "$StateCode" . "/" . "buttons" . ".dat";
		open(TEMPFILE,"$TempFile") || &Error("Can't open $TempFile in RecordData sub. Reason: $!");
		@TempData=<TEMPFILE>;
		close(TEMPFILE);
		foreach $tempor (@TempData)
		{
			($DeBiz,$DeRest) = split(/\|/,$tempor,2);
			if ("$DeBiz" eq "$BizName")
			{
				open(PERMFILE,">>$PermFile") || &Error("Can't open $PermFile in RecordData sub. Reason: $!");
				print PERMFILE "$tempor";
				close(PERMFILE);
				$MatchFound = 1;
			}
		}
		if ($in{Web})
		{
			$StateCode = $Abbrevs{$State};
			$OldWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".inp";
			$NewWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".html";
			if (rename($OldWeb, $NewWeb))
			{
				&MailWebInfo;
			}
			else
			{
				&Error("For some reason, I could not create your Web page. Please contact the webmaster at <a href=mailto:$Admin>this link</a> and mention this error. The problematic page is $BizName. The server says this is the problem: $!");
			}
		}
		if ($MatchFound)
		{
			&ReportSuccess;
		}
		else
		{
			&Error("I couldn't find $BizName in the temporary database. Please contact the administrator.");
		}
	}
	#textads.dat
	if ($DataType eq "Text")
	{
		$StateCode = $Abbrevs{$State};
		$TempFile = "$basedir" . "$City" . "$StateCode" . "/" . "text" . ".temp";
		$PermFile = "$basedir" . "$City" . "$StateCode" . "/" . "textads" . ".dat";
		open(TEMPFILE,"$TempFile") || &Error("Can't open $TempFile in RecordData sub. Reason: $!");
		@TempData=<TEMPFILE>;
		close(TEMPFILE);
		$Catalog = "$basedir" . "Catalog" . "/" . "Catalog.dat";
		open(CATFILE,">>$Catalog") || &Error("Can't open $Catalog for writing in RecordData sub. Reason: $!");
		print CATFILE "$State\|$City\|$BizName\n";
		close(CATFILE);
		foreach $tempor (@TempData)
		{
			($DeBiz,$DeRest) = split(/\|/,$tempor,2);
			if ("$DeBiz" eq "$BizName")
			{
				open(PERMFILE,">>$PermFile") || &Error("Can't open $PermFile in RecordData sub. Reason: $!");
				print PERMFILE "$tempor";
				close(PERMFILE);
				$MatchFound = 1;
			}
		}
		if ($in{Web})
		{
			$StateCode = $Abbrevs{$State};
			$OldWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".inp";
			$NewWeb = "$basedir" . "$City" . "$StateCode" . "/" . "$BizName" . ".html";
			&Error("Can't rename $OldWeb To $NewWeb. Reason: $!") unless (rename($OldWeb, $NewWeb));
			#{
			#	&MailWebInfo;
			#}
			#else
			#{
			
			#	&Error("For some reason, I could not create your Web page. Please contact the webmaster at <a href=mailto:$Admin>this link</a> and mention this error. The problematic page is $BizName. The server says this is the problem: $!");
			#}
		}
		if ($MatchFound)
		{
			&ReportSuccess;
		}
		else
		{
			&Error("I couldn't find $BizName in the temporary database. Please contact the administrator.");
		}
	}
}

sub MailWebInfo
{
	$TheLink = "$baseurl" . "Edit.cgi" . "\?$City" . "\&" . "$State" . "\&" . "$BizName" . "\&" . "$RandomNumber";
	$EmailTo = "$in{Email}";
	$FirstName = "$in{FirstName}";
	open (MAIL, "|$mailprog -t") || &Error("Can\'t open $mailprog! Reason: $!");
	print MAIL "To: $EmailTo\n";
	print MAIL "From: $admin\n";
	print MAIL "Subject: Your new SurfLocal ad!\n\n";
	print MAIL "Dear $FirstName,\n\n";
	print MAIL "Your new SurfLocal ad is ready!\n";
	print MAIL "Below is a link you will need to use in the future to edit your ad.\n";
	print MAIL "If you need to edit your ad, use this link:\n";
	print MAIL "$TheLink";
	close (MAIL);
}

sub CheckCatList
{
	use locale;
	$MassCatList = "$basedir" . "Templates" . "/" . "CategoryList";
	open (MASSAH,"$MassCatList") || &Error("Can't open $MassCatList in CheckCatList sub. Reason: $!");
	@Massah=<MASSAH>;
	close(MASSAH);
	foreach $Mssa (@Massah)
	{
		chomp($Mssa);
		if ($Mssa eq "$Category")
		{
			$Match = "yes";
		}
	}
	if ($Match ne "yes")
	{
		open (MASSW,">>$MassCatList") || &Error("Can't open $MassCatList to write in CheckCatList sub. Reason: $!");
		print MASSW "\n";
		#ucfirst($Category);
		#$CapCat =~ s/^(\w)/$Letters{$1}/g;
		print MASSW "$Category";
		close(MASSW);
	}
}


sub MailSuccess
{
	$TheLink = "$baseurl" . "Edit.cgi" . "\?$City" . "\&" . "$State" . "\&" . "$BizName" . "\&" . "$RandomNumber";
	$EmailTo = "$in{Email}";
	$FirstName = "$in{FirstName}";
	open (MAIL, "|$mailprog -t") || &Error("Can\'t open $mailprog! Reason: $!");
	print MAIL "To: $EmailTo\n";
	print MAIL "From: Surflocal <admin\@surflocalmedia.com>\n";
	print MAIL "Subject: Your new SurfLocal ad!\n\n";
	print MAIL "Dear $FirstName,\n\n";
	print MAIL "Your new SurfLocal ad is ready!\n";
	print MAIL "Below is a link you will need to use in the future to edit your ad.\n";
	print MAIL "If you need to edit your ad, use this link:\n";
	print MAIL "$TheLink";
	close (MAIL);
	#&Header;
	#print "Got past mailsuccess.";
}

sub ReportSuccess
{
	&MailSuccess;
	&Header;
	&PHed;
	print "<h1>Success</h1>\n";
	print "Your $DataType was successfully recorded.";
	$TheUrl = "$baseurl" . "$City" . "$StateCode";
	print "<br><a href=\"$TheUrl\">Click here to go back to the $City site</a>.\n";
	exit;
}

sub RecordCategory
{
	$TheCity = "$basedir" . "$City" . "$StateCode";
	$MyCategory = "$TheCity" . "/" . "$Category" . ".cat";
	open(THECAT,">>$MyCategory") || &Error("Can't open $MyCategory in RecordCategory sub. Reason: $!");
	print THECAT "$BizName\n";
	close(THECAT);
}
		

sub PrintRevisedHiddenValues
{
	print "<input type=hidden name=BizName value=\"$BizName\">\n" if ($BizName ne "");
	print "<input type=hidden name=AdType value=\"$AdType\">\n" if ($AdType ne "");
	print "<input type=hidden name=Category value=\"$Category\">\n" if ($Category ne "");
}

sub InputArray
{
	print "<table border=1><tr><td>Your first name: </td><td><input type=text name=FirstName></td></tr>\n";
	print "<tr><td>Your last name:</td><td><input type=text name=LastName></td></tr>\n";
	print "<tr><td colspan=2><center>Billing address:</center></td></tr>\n";
	print "<tr><td>Address 1:</td><td><input type=text name=Address1></td></tr>\n";
	print "<tr><td>Address 2:</td><td><input type=text name=Address2></td></tr>\n";
	print "<tr><td>City:</td><td>$City<input type=hidden name=City value=\"$City\"></td></tr>\n";
	print "<tr><td>State:</td><td>$State<input type=hidden name=State value=\"$State\"></td></tr>\n";
	print "<tr><td>ZIP code:</td><td><input type=text name=Zip></td></tr>\n";
	print "<tr><td>Phone number with area code:</td><td><input type=text name=Phone value=\"XXX-XXX-XXXX\"></td></tr>\n";
	print "<tr><td>E-mail address:</td><td><input type=text name=Email></td></tr>\n";
}

sub WebPage
{
	my ($What) = join(/,@_);
	&Header;
	&PHed;
	print "<center>\n";
	print "<h1>Please enter the billing information for $BizName</h1>\n";
	print "All fields except for Address2 are REQUIRED.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<input type=hidden name=Web value=$What>\n";
	&PrintRevisedHiddenValues;
	&InputArray;
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	exit;
}

sub CouponOnly
{
	&Header;
	&PHed;
	print "<center>\n";
	print "<h1>Please enter the billing information for $BizName</h1>\n";
	print "All fields except for Address2 are REQUIRED.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	&PrintRevisedHiddenValues;
	&InputArray;
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	exit;
}

sub ButtonOnly
{
	&Header;
	&PHed;
	print "<center>\n";
	print "<h1>Please enter the billing information for $BizName</h1>\n";
	print "All fields except for <b>Address2</b> are REQUIRED.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	&PrintHiddenValues;
	&InputArray;
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	exit;
}

sub TextOnly
{
	&Header;
	&PHed;
	print "<center>\n";
	print "<h1>Please enter the billing information for $BizName</h1>\n";
	print "All fields except for <b>Address2</b> are REQUIRED.<p>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=RecordData>\n";
	&PrintHiddenValues;
	&InputArray;
	print "<tr><td colspan=2><center><input type=submit value=\"Record my data\"><input type=reset></form></td></tr></table>\n";
	exit;
}


