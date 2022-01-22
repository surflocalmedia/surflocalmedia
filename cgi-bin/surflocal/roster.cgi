#!/usr/local/bin/perl5.22
use CGI qw( :standard );
require 'web-lib.pl';

$newform = "https://surflocalmedia.com/roster.cgi";
$clubsListFile = "clubsList.txt";

@fieldsList=("First_name","Last_name","Middle_initial","Business","Business_category",
			"Joined_Rotary","Awards","E-mail_address","Web_page");

$thisClub = param("thisClub");

if (! $thisClub) {
	&RequestClubName;
} else {
	$action = param("action");
}
if ($action eq "RequestData") {
	&CheckPassword;
	&RequestData(0);
} elsif ($action eq "RecordData") {
	&CheckPassword;
	&RecordData;
} else {
	&Error("I don't understand what $action means.");
}

####### RECORD DATA
sub RecordData {
	$fileName = $thisClub . ".txt";
	$firstName = param("First_name");
	$lastName = param("Last_name");
	if ((! $firstName) || (! $lastName)) {
		&Error("You have to have both a first and last name.");
	}
	my($stringToWrite) = "";
	foreach (@fieldsList) {
		$stringToWrite .= $_ . "\=" . param($_) . "\|";
	}
	chop($stringToWrite);
	open(THEFILE,">>$theFile") || &Error("Can't open $theFile to append. $!");
	print THEFILE $stringToWrite . "\n";
	close(THEFILE);
	&RequestData(1);
}

####### CHECK PASSWORD
sub CheckPassword {
	$password = param("password");
	open(CLUBS,"$clubsListFile") || &Error("Can't open $clubsListFile $!");
	@theListOfClubs=<CLUBS>;
	close(CLUBS);
	foreach (@theListOfClubs) {
		chomp($_);
		($clubName,$clubPassword) = split(/\|/,$_);
		if ($clubName eq $thisClub) {
			if ($clubPassword ne $password) {
				&Error("Your password did not match the password we have on file for $thisClub. Please try again.");
			}
		}
	}
}

####### REQUEST DATA
sub RequestData {
	$internallyCalled = $_[0];
	&Header;
	if (! $internallyCalled) {
		print "<h3>Enter the member's information</h3>\n";
	} else {
		print "<h3>Entry for $firstName $lastName recorded. Enter another?</h3>\n";
	}
	print "<form action=$newform method=POST ENCTYPE=\"multipart/form-data\">\n";
	print "<input type=hidden name=action value=RecordData>\n";
	print "<input type=hidden name=thisClub value=\"$thisClub\">\n";
	print "<input type=hidden name=password value=\"$password\">\n";
	foreach (@fieldsList) {
		$printField = $_;
		$printField =~ s/\_/ /gi;
		$dataField = $_;
		print "$printField" . ": <input type=text name=$dataField><br>\n";
	}
	print "Choose a photo to upload: <input type=\"FILE\" name=\"picture\">";
	print "<br><input type=submit></form>\n";
	exit;
}

####### REQUEST CLUB NAME
sub RequestClubName {
	open(CLUBS,"$clubsListFile") || &Error("Can't open $clubsListFile $!");
	@theListOfClubs=<CLUBS>;
	close(CLUBS);
	&Header;
	print "<h3>Select your club and enter your password</h3>\n";
	print "<form action=$newform method=POST>\n";
	print "<input type=hidden name=action value=\"RequestData\">\n";
	print "<select name=thisClub>";
	foreach (@theListOfClubs) {
		chomp($_);
		($clubName,$password) = split(/\|/,$_);
		print "<option value=\"$clubName\">$clubName</option>\n";
	}
	print "</select><br>\n";
	print "Password: <input type=password name=password><br>\n";
	print "<input type=submit></form>\n";
	exit;
}
