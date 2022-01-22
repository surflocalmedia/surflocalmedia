#!/usr/local/bin/perl5.22

##############################################################################
#                                                                            #
# File Uploader                      Version 1.4                             #
# By Paul Benn :: paul@notjustcomputers.co.uk :: www.notjustcomputers.co.uk  #
#                                                                            #
##############################################################################
#                                                                            #
# Modifications Copyright (c) 2002 Paul JJ Benn, All Rights Reserved.        #
# This version of File Uploader may be used and modified free of charge by   #
# anyone so long as this copyright notice remains intact. By using this code #
# you agree to indemnify Paul Benn and Not Just Computers of any liability   #
# arising from it's use. You also agree that this code cannot be sold to     #
# any third party without prior written consent from Paul JJ Benn            #
#                                                                            #
# Selling the code for this program without prior written consent is         #
# expressly forbidden.  In other words, please ask first before you try and  #
# make money off of my program.                                              #
#                                                                            #
# Obtain permission before redistributing this software over the Internet or #
# in any other medium. In all cases copyright and header must remain intact. #
#                                                                            #
##############################################################################

use CGI;
use DBI;

require 'SurfLocalLib.pl';
require 'cookie.lib';
require 'web-lib.pl';
require 'UploadLib.pl';


# ..:: Define Variables Start ::.. #

#### Where to Save put the files ####
# Change this for the LITERAL PATH to save the files to. Do not forget the ending / #
$upload_dir = "$basedir . $CityState . "/" . $BizName";


#### How to Save the Data ####

$storein = "1"; # 0=Txt File  1=MySQL


#### If yuo have chossen Txt File above then set the settings below ####

# Change this for the LITERAL PATH for the datafile. Do not forget the ending / #
$data_dir =   "/usr/myspace/cgi-bin/upload/";

# Set the file name to be used for saving the upload infomation in #
$datafile =   "uploaded.txt";




#### If you have chossen MySQL above then set the settings below ####

$host = "db.domain.com"; # Database host url or IP
$dbname = "myname"; # Name of MySQL Database
$table = "fupload"; # Name of table to use
$usrname = "YourUserName"; # Username to access table
$passwrd = "YourPassword"; # Password for table

#### Send notifaction email to Admin ####

$adminemailaddress = "admin\@mydomain.com"; # You must put the \ before the @
$sendadminemail = '0'; # 0 = Do not Send alert, 1 = Send Alert Message to Admin
$mailprog = '/usr/lib/sendmail -i -t'; # Path to Sendmail

#### Custom form fields change the second part to be the name of the input in your form ####
#### $f1 = "hobby"                           ####

$f1 = "field1";
$f2 = "filed2";
$f3 = "filed3";
$f4 = "field4";
$f5 = "field5";
$f6 = "field6";
$f7 = "field7";
$f8 = "field8";
$f9 = "field9";
$f10 = "field10";

########### Don't Change anything below here ###########
########## Unless you know what you are doing ##########

$version = "v1.4";
$query = new CGI;
&parse_form;



sub parse_form
{
$filename = $query->param("file");
$fileinfo = $query->param("fileinfo");
$email_address = $query->param("email_address");
$your_name = $query->param("realname");
$redirect_url = $query->param("redirect");
## Additional Form Fields for anything you like these will ##
## be posted to the database                               ##
$field1 =  $query->param($f1);
$field2 =  $query->param($f2);
$field3 =  $query->param($f3);
$field4 =  $query->param($f4);
$field5 =  $query->param($f5);
$field6 =  $query->param($f6);
$field7 =  $query->param($f7);
$field8 =  $query->param($f8);
$field9 =  $query->param($f9);
$field10 =  $query->param($f10);

##
$ipaddress = $ENV{'REMOTE_ADDR'};
$filename =~ s/(\s+|\n)?,(\s+|\n)?/,/g;

$upload_filehandle = $query->upload("file");

if ($filename eq '') {
    &error_html;
   }
&upload_file;
}

sub upload_file
{

$filepath=$filename;
if ($filepath =~ /([^\/\\]+)$/)
    {
        $filename="$1";
    }
    else
    {
        $filename="$filepath";
    }
    # if there's any space in the filename, get rid of them
    $filename =~ s/\s+//g;


open UPLOADFILE, ">$upload_dir/$filename";
while ( <$upload_filehandle> )
{
print UPLOADFILE;
}
close UPLOADFILE;
#print $query->header ( );

open(FILE, "$upload_dir/$filename") || &error("Can't get filesize $upload_dir/$filename ($!)");
        $filesizeb = -s FILE;
        close(FILE);

$filesize = sprintf("%.1f", $filesizeb/1024) ;

if ($storein=="0"){
&write_file;
}

if ($storein=="1"){
&loadmysql;
}


}


sub write_file
{
 ##### RECORD INFO

($sec,$min,$hour,$mday,$mon,$year,$wday,$ydat,$isdst) = localtime();
$mon++;
$year = 1900 + $year;
$today = $mday . "-" .  $mon . "-" . $year . " " . $hour . ":" . $min . ":" . $sec;


open (UPLO, ">> $data_dir/$datafile");

        print UPLO $your_name . "," . $email_address . "," . $filename . "," .
        $fileinfo . "," . $ipaddress . "," . $today . "," . $filesize .
        "," . $field1 . "," . $field2 . "," . $field3 . "," . $field4 . "," . $field5 .
        "," . $field6 . "," . $field7 . "," . $field8 . "," . $field9 . "," . $field10 . "\n";
close (UPLO);
$mysqlpost= "Not Used";

&sendmailalert;

}


sub loadmysql
{
# Save data to MySQL Database
#Connect to database

my $dbh = DBI->connect("DBI:mysql:$dbname:$host", $usrname, $passwrd)
or die "Can't connect to $data_source: $dbh->errstr\n";

($sec,$min,$hour,$mday,$mon,$year,$wday,$ydat,$isdst) = localtime();
$mon++;
$year = 1900 + $year;
$today = $year . "/" .  $mon . "/" . $mday;

$sql = "insert into $table (postername, posteremail, filename, fileinfo, ipaddr, datesub, filesize, id, field1,field2,field3,field4,field5,field6,field7,field8,field9,field10) VALUES('$your_name','$email_address','$filename','$fileinfo','$ipaddress','$today','$filesize Kb','0','$field1','$field2','$field3','$field4','$field5','$field6','$field7','$field8','$field9','$field10')";
my $sth = $dbh->prepare($sql);
$sth->execute();
$mysqlpost= "Updated Okay";

&sendmailalert;

}

sub myredirect
{
print "Location: $redirect_url\n\n";
}

sub sendmailalert
{
if ($sendadminemail=="1"){

open MAIL, "|$mailprog -t";
print MAIL "To: $adminemailaddress\n";
print MAIL "From: $email_address ($your_name)\n";
print MAIL "MIME-Version: 1.0\n";
print MAIL "Subject: File $filename has been Uploaded\n";
print MAIL "Content-Type: multipart/mixed; boundary=\"------------$boundary\"\n";
print MAIL "\n";
print MAIL "This is a multi-part message in MIME format.\n";
print MAIL "--------------$boundary\n";
print MAIL "Content-Type: text/html; charset=us-ascii\n";
print MAIL "Content-Transfer-Encoding: 7bit\n\n";
print MAIL "<html><font size='4pt' face='verdana'>\n";
print MAIL "<b>Dear Admin,\n\n</b><br><br>";
print MAIL "The file <b>$filename</b> has been uploaded, it is <b><i> $filesize Kb </b></i> in size.<br><br>\n";
print MAIL "The User sent the following information with the file:<br><br>\n";
print MAIL "$fileinfo<br>\n";

print MAIL "<br><br>\n";


print MAIL "<br>\n";

print MAIL "\n--------------$boundary--\n";
print MAIL "\n";
print MAIL "<html><font size='4pt' face='verdana'>\n";
close MAIL;

$mysqlpost= "Updated Okay and Admin Emailed";
}


&okay_html;
}


 sub okay_html
{
# If redirect option is used, print the redirectional location header.   #
    if ($redirect_url) {
        &myredirect;
        }
   else
   {
print $query->header ( );

print <<"(END_HTML)";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html><head>
<title></title>
<style type='text/css'>
BODY {font-family: verdana; font-size:8pt;}
TD {font-family: verdana; font-size:10pt;}
A {color: #3366cc; text-decoration: none;}
</style>
</head>
<body bgcolor='#000000'>
<table style='border: 1 solid black;border-bottom: 0;' width='100%' align='center' cellpadding='2' cellspacing='0' border='0'>
<tr bgcolor='#000000'>
<td style='padding: 5'></td>
<td valign='bottom' align='right'><font size="+2" color="Yellow"><b><i>File Uploader</i></b></font></td>
</tr>
<tr bgcolor='#2C4967'>
<td colspan=2 class='main_menu_td'>
        <table border='0' cellpadding='4' cellspacing='1'>
        <tr>
        <td><b> <font size="+1" color="White">Upload Complete</b></td>
        </tr>
        </table>
</td>
</tr>
</table>
<table style='border: 2 solid black;' width='100%' align='center' cellpadding='4' cellspacing='0' border='0'>
<tr bgcolor='#e8e8e8'>
<td valign='top'>
        <table width='100%' cellpadding='10' cellspacing='1' border='0'>
        <tr>
        <td bgcolor='#ffffff'>
<br>
<font size="+1"><b>Thanks $your_name,</b></font><br>
<br>
Your file ($filename) has been uploaded successfully.<br>
<br>
<table width='75%' cellpadding='0' cellspacing='2' border='0' align='center' bgcolor='#ffd700'>
<td colspan=2>
<font size="+1">The Following information will be kept on file:</font></td>
<tr><td width = '30%'><b>Your Name:</b> </td><td><font color="#000080"><b>$your_name<b></font><br></td></tr>
<tr><td><b>Your email address: </b></td><td><font color="#000080"><b>$email_address<b></font><br></td></tr>
<tr><td><b>Your file: </b></td><td><font color="#000080"><b>$filename<b></font><br></td></tr>
<tr><td><b>File Information: </b></td><td></b><font color="#000080"><b>$fileinfo<b></font><br></td></tr>
<tr><td><b>File Size: </b></td><td><font color="#000080"><b>$filesize Kb<b></font><br></td></tr>
<br>
<tr><td><b>Your IP Address: </b></td><td></b><font color="#000080"><b>$ipaddress<b></font><br></td></tr>
<tr><td><b>MySQL Result: </b></td><td></b><font color="#000080"><b>$mysqlpost<b></font><br></td></tr>
<tr><td><b>Var Check: </b></td><td></b><font color="#000080"><b>$upload_dir $filename<b></font><br></td></tr>
</table>
</td>
        </tr>
        </table>
        <table width='100%' cellpadding='0' cellspacing='2' border='0'>                <tr>                <td align='center'><center><font size=-1>
<a href="http://www.notjustcomputers.co.uk/cgi-scripts.html">File Uploader</a> $version &copy; 2002  Paul Benn<br>
      A Free Product of <a href="http://www.notjustcomputers.co.uk">Not Just Computers</a> </b>
</font></center></td>                </tr>        </table>        <table width='100%' cellpadding='0' cellspacing='1' border='0'>
        <tr>
        <td>
        <p align='center'>
        </td></tr>
        </table>
</td>
</tr>
</table>
</body>
</html>

(END_HTML)

exit;
}}



sub error_html
{
print $query->header ( );

print <<"(NOPE)";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html><head>
<title></title>
<style type='text/css'>
BODY {font-family: verdana; font-size:8pt;}
TD {font-family: verdana; font-size:10pt;}
A {color: #3366cc; text-decoration: none;}
</style>
</head>
<body bgcolor='#000000'>
<table style='border: 1 solid black;border-bottom: 0;' width='100%' align='center' cellpadding='2' cellspacing='0' border='0'>
<tr bgcolor='#000000'>
<td style='padding: 5'></td>
<td valign='bottom' align='right'><font size="+2" color="Yellow"><b><i>File Uploader</i></b></font></td>
</tr>
<tr bgcolor='#2C4967'>
<td colspan=2 class='main_menu_td'>
        <table border='0' cellpadding='4' cellspacing='1'>
        <tr>
        <td><b> <font size="+1" color="White">Error - No File to Upload</b></td>
        </tr>
        </table>
</td>
</tr>
</table>
<table style='border: 2 solid black;' width='100%' align='center' cellpadding='4' cellspacing='0' border='0'>
<tr bgcolor='#e8e8e8'>
<td valign='top'>
        <table width='100%' cellpadding='10' cellspacing='1' border='0'>
        <tr>
        <td bgcolor='#ffffff'>
There is no file to upload!<br>
<br>
</td>
        </tr>
        </table>
        <table width='100%' cellpadding='0' cellspacing='1' border='0'>                <tr>                <td align='center'><center><font size=-1>
<a href="http://www.notjustcomputers.co.uk/cgi-scripts.html">File Uploader</a> $version &copy; 2002  Paul Benn<br>
      A Free Product of <a href="http://www.notjustcomputers.co.uk">Not Just Computers</a> </b>
</font></center></td>                </tr>        </table>        <table width='100%' cellpadding='0' cellspacing='1' border='0'>
        <tr>
        <td>
        <p align='center'>
        </td></tr>
        </table>
</td>
</tr>
</table>
</body>
</html>
(NOPE)

exit;

}