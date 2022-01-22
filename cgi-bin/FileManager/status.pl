#!/usr/local/bin/perl5.22

##################################################################
################## iDC File Manager Version 1.4.04 ################
############################OEM VERSION############################
###################################################################

###################################################################
# i Dot Communications © 2004-2005 Copyright Mark Roberts / Alexandre Golovkine

#~~~~~~~Personal Usage ~~~~~~~
# The iDC File Manager lite version script is free for personal usage only
# You can use the scripts in any personal website you build.
# It is prohibited to sell the scripts in any format to anybody.
# The scripts may only be distributed by i Dot Communications.
# The scripts cannot be used to distribute:
# Pirated software
# Hacker programs
# Warez
# Pornography or nudity of any kind
# Copyrighted materials
# Any software that is copyrighted and not freely available for distribution without cost.
# including: ROMs, ROM Emulators and Mpeg Layer 3 files (MP3).
# The redistribution of modified versions of the scripts is prohibited.
# i Dot Communications accepts no responsibility or liability
# whatsoever for any damages however caused when using our services or scripts.
# By downloading and using this script you agree to the terms and conditions.

#~~~~~~~Commercial Usage ~~~~~~

# The iDC File Manager lite version cannot be used for commercial usage.
# You must instead upgrade to the Pro version.
# The same iDC File Manager - Pro Version script cannot be used on multiple websites.
# For every 1 copy of iDC File manager you purchase you will be provided with 1 "URL" licence.
# This means that for every subsequent website you intend to use the file manager with, you
# must purchase a new copy.
# It is prohibited to sell the scripts in any format to anybody.
# The scripts may only be distributed by i Dot Communications.
# The scripts cannot be used to distribute:
# Pirated software
# Hacker programs
# Warez
# Pornography or nudity of any kind
# Copyrighted materials
# Any software that is copyrighted and not freely available for distribution without cost,
# including: ROMs, ROM Emulators and Mpeg Layer 3 files (MP3).
# The redistribution of modified versions of the scripts is prohibited.
# i Dot Communications accepts no responsibility or liability
# whatsoever for any damages however caused when using our services or scripts.
# By downloading and using this script you agree to the terms and conditions.

###################################################################

###################################################################
# For Instructions / Questions / Comments etc... Please visit:
# Help Forum:   http://www.iDotCommunications.co.uk/forum.html
###################################################################

####Status Tempoary Folder#########################################

my $tmpDir = "./status";

#Please enter the path to the "status" folder
###################################################################



use CGI::Carp qw(fatalsToBrowser);
(my $script=$0) =~s!^.*[/\\]!!;
my %FORM = parse_cgi();

print "Cache-control: private\n";
print "Cache-control: no-cache\n";
print "Cache-control: no-store\n";
print "Cache-control: must-revalidate\n";
print "Cache-control: proxy-revalidate\n";
print "Cache-control: max-age=0\n";
print "Pragma: no-cache\n";

print "Content-type: text/html\n\n";
unless($FORM{session}){
        print "1";
        exit;
}
if ($FORM{type} eq 'clear'){
        unlink "$tmpDir/$FORM{session}";
        unlink "$tmpDir/$FORM{session}.tmp";
        print "1";
        exit;
}
unless (-f "$tmpDir/$FORM{session}"){
        print qq~$FORM{session}\n0 0 0~;
        exit;
}

local $/;
open (F, "$tmpDir/$FORM{session}") or die "Can't open file $! $tmpDir/$FORM{session}";
#flock(ST, LOCK_EX);
my $data = <F>;
close F;

my($lenght, $proz, $time)=split(' ',$data);
$lenght = sprintf("%.2f", $lenght/1024);
my $curTime=time;
my $diff = $curTime-$time;
my $speed=0;
if($diff && $lenght*$proz){$speed=sprintf("%.3f",($lenght*$proz/100)/($diff))}; #Kb/sec
if($proz<100){
        print qq~$FORM{session}\n$lenght $proz $speed~;
}
else{
        print qq~$FORM{session}\n$lenght 100 $speed~;
}
exit;

sub parse_cgi{
        my(%FORM, $buffer);
        my @pairs=split(/&/,$ENV{'QUERY_STRING'});
        foreach my $pair (@pairs) {
                my ($name, $value) = split (/=/,$pair,2);
                $value =~ tr/+/ /;
                $value =~ s/%(..)/pack("c",hex($1))/ge;
                $FORM{$name} = $value;
                }
        return %FORM;
}
