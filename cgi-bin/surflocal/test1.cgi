#!/usr/local/bin/perl5.22
# This script converts DBM database into a json flatfile database.
# I've commented it extensively because I haven't coded Perl since Methusaleh was a boy.


#server directory of the site
$basedir = "/usr/home/starting2014/public_html/surflocal.net/";
#allows reading/writing to dbm files
use DB_File;
#location of the dbm file to read
$database = $basedir . "TestTownTX/Leif/Database.db";
#read the file, tie it to a hash
dbmopen(%MyData,$database,0666)|| print "Content-type: text/html\n\n ERROR $!";
#start the json string
$string = "\{";
#process the dbm hash and add each key/value pair to the json string
while (($key,$value) = each(%MyData)) {
	#get rid of newlines
	chomp($value);
	#escape quotation marks
	$value =~ s/\"//gi;
	#change left brackets to their ascii equivalent. Comment this out for production
	$value =~ s/</\&lt\;/gi;
	$string .= "\"" . $key . "\":\"" . $value . "\",";
}
#get rid of trailing comma
chop($string);
#close the json string
$string .= "\}";
#create a scalar for the new json database
$file = $basedir . "TestTownTX/Leif/database.json";
#open the json file
open FILE, ">" , $file or die $!;
#print the json string to it
print FILE $string;
close FILE;

#echo the json string to the browser
print "Content-type: text/html\n\n ";
print $string;

#untie the dbm database from the mydata hash
dbmclose %MyData;


#http://www.surflocal.net//cgi-bin/surflocal/Edit.cgi?TestTownTX&Leif