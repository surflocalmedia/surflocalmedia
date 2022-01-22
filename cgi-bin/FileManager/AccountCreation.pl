#!/usr/local/bin/perl5.22
use CGI::Carp qw(fatalsToBrowser);

##########################################################################
################## iDC File Manager - Account Creation v1.00.00 ##########
##########################################################################
##########################################################################

####File Manager - Registered Owner:######################################

my $RegisteredOwner = "License Holders Name";

#Change the "File Manager - Registered Owner:" to the name of your website or company etc...

##########################################################################

####Main Clients Directory################################################

my $clientsFolder = "/usr/home/starting2014/public_html/surflocal.net/Clients/";

#Change the path to the "Main Clients Directory" to your servers path to the Main Root Directory + The sub-folderof the File Manager folder which will hold all your Clients folders.
#For example:
#e.g. Main Clients Directory ("/home/mysite/public_html/") +  Main File Manager Directory (FileManager) + "Clients"

##########################################################################

####Main Clients Records Directory########################################

my $clientsDataFolder = "/usr/home/starting2014/public_html/surflocal.net/Clients";

#Change the path to the "Main Clients Directory" to your servers path to the Main Root Directory + The sub-folderof the File Manager folder which will hold all your Clients folders.
#For example:
#e.g. Main Clients Directory ("/home/mysite/public_html/") +  Main File Manager Directory (FileManager) + "Clients"

##########################################################################

####User Database#########################################################

my $UserDatabase = 'users.txt';

#Do not modify the User Database settings unless told to do so by iDC Support.

##########################################################################

####Default Client Information Storage Template###########################

my $ClientInfoTemplate = "/usr/home/starting2014/public_html/surflocal.net/AccountCreation/ClientInfoTemplate.html";

#Change the path to the "Default Client Information Storage Template" to your servers path to the Main Root Directory +
#the sub-folder of the Account Creation which will hold all of the templates for iDC Account Creation (i.e. "AccountCreation").

#For example:
#e.g. Main Clients Directory ("/home/mysite/public_html/") + "AccountCreation"

###################################################################################

####Application Complete URL##############################################

my $ApplicationCompleteURL           = 'http://www.surflocal.net/AccountCreation/Thankyou.html';

#Change the URL of "Application Complete URL" to the URL of the Thankyou.html page located in the
#"AccountCreation" folder
#This page will be displayed after the user has submitted their details.

##########################################################################

####Default Account Creation Properties###################################

my $defLimit = 100; #Default Account Storage Quota (MB)

my $defProtection = "exe,pl,php,cgi"; #Default Account Banned Upload File Formats

my $EnableAccess = "1"; #Set to "1" To enable Admin Account Validation or set to "" to enable instant user access

my $defRights = "u,m,r,a,p,w,c,n,l,d|$EnableAccess"; #Default Account User Rights

##########################################################################

####Email Configuration###################################################

####Admin Notification Of New Account Created####
my $from                     = 'trinity@surflocal.net';                     #From Email Address
my $admin_mail               = 'trinity@surflocal.net';       #Email Address you want to receive Account Creation confirmations
my $mailprog                 = '/usr/sbin/sendmail';                     #SendMail Path
my $subject                  = 'RE: iDC File Manager Account Created';   #Email Subject Title
my $send_me_template         = 'ApplicationNotification.html';           #Enter  the Path to ApplicationNotification.html
my $send_me                  = 0;                                        #Change to "1" to receive file Account Creation confirmations

####Additional Settings####

#Do not modify the User Database settings unless told to do so by iDC Support.

my $from_field_name          = 'email';
my $email_input_error        = "No Email Address Entered";
my $only_fields_with_values  = 1;
my $send_just_data                 = 1;

####Client Notification Of Successful Account Creation####

my $auto_responder_from             = 'support@mysite.com';              #From Email Address
my $auto_responder_subject   = "RE: iDC File Manager Account Sign-up";   #Email Subject Title
my $auto_responder_message   = 'ApplicationSignup.html';                 #Enter the Path to ApplicationSignup.html
my $auto_responder              = 0;                                     #Change to "1" to send user sign-up confirmations

##########################################################################

####Advanced Email Configuration##########################################

#If you do not have SendMail installed on your server please configure the following option:
#To enable:
#Uncoment "# use Net::SMTP;" e.g. remove "#" to become "use Net::SMTP;"
#Enter "1" instead of "0" for "my $send_via_SMTP"
#Enter your servers SMTP server address, e.g. smtp.yoursite.com

#use Net::SMTP;
my $send_via_SMTP            = 0;
my $mailhost                 = 'smtp.com';
##########################################################################

####Advanced Settings#####################################################

#Do not modify the User Database settings unless told to do so by iDC Support.

my $required_fields_form     = 1;
my @required_fields          = ('password', 'FirstName', );
my @required_fields_numbers  = ();
my @required_fields_email    = ('email');
my $error_fields_require     = "Field is blank, it is required";
my $error_fields_numbers     = "Only numbers";
my $error_fields_email       = "email address is not valid";
my $error_title              = "<b>Sorry, we require more information</b>";
my $fontColor                = "black";
my $fontSize                 = 3;
my $fontFace                 = "Verdana";
my $return_message           = "Please click 'back' on your browser and try again";
my $line_break               = '<br>';
my $kill_html_tags           = 1;
my $kill_image_buttons_value = 1;
my $separator                = '|';
my $change                   = "I";
my $ID_autoincrement         = 1;
my $ID_autoincrement_name    = "id";
##########################################################################

#########################################################################


#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!


#########################################################################


my $alternativeDateFormat= 0;
use Fcntl qw(:DEFAULT :flock);
use CGI qw/:standard :cgi-lib/;
use strict;
my $r = shift;

my @date=localtime();
$date[4]++; $date[5]+=1900;
for(0..4){$date[$_]=sprintf("%02d",$date[$_]);}
my $date="$date[2]:$date[1]:$date[0] $date[5]-$date[4]-$date[3]";
if ($alternativeDateFormat){
        $date[5]=sprintf("%02d",$date[5]-2000);
         $date = "$date[5]:$date[4]:$date[3]-$date[0]:$date[1]:$date[2]";
 }



my @field;
my %field;
error("Error: Bad record separator!") if !$separator or $separator eq $change or $separator=~m /["'\.\\\/]/;
my $my_separator=$separator;
$my_separator="\\".$separator if $separator eq '|'or  $separator eq ',' or  $separator eq '.';

my %FORM;
@field = param;
foreach my $key (@field) {
        $FORM{$key} = param($key);
        $FORM{$key} =~ s/\Q$separator/$change/g;
        $FORM{$key} =~ s/"/&#34;/g;
        $FORM{$key} =~ s/'/&#39;/g;
        $FORM{$key} =~ s/<!--(.|\n)*-->//g if $kill_html_tags;
        $FORM{$key} =~ s/<([^>]|\n)*>//g if $kill_html_tags;
        $FORM{$key} =~ s/\n/$line_break/g;         # added to strip line breaks
        $FORM{$key} =~ s/\r//g;
}

push @required_fields_email, $from_field_name if $from_field_name;
test_form();


open(F, $UserDatabase) || error("Can't open file $UserDatabase!");
flock(F, LOCK_EX);
my @data = <F>;
close F;
my $userList ={};
my $maxID;
$FORM{login}=~s/\///g;


        my @data_fields=split($my_separator, $data[0]);
        error("You have bad file!") if !@data_fields;
        chomp $data_fields[@data_fields-1];

        for(1..@data-1){
                my @line=split($my_separator, $data[$_]);
                chomp $line[@line-1];
                for (0..@data_fields-1){
                        $userList->{$line[0]}->{$data_fields[$_]}=$line[$_];
                }
                $maxID=$line[$0] if $maxID<$line[$0];
        }
        $maxID++;

        #check that login is free
        for (keys %$userList){
                if ($FORM{login} eq $userList->{$_}->{login}){
                        close F;
                        error("Login: <b>$FORM{login}</b> already in use! Please click back and select a new username.");
                }
        }



#create client folder
mkdir "$clientsFolder/$FORM{login}" || error("Can't create client folder $!") unless -e "$clientsFolder/$FORM{login}";
$FORM{home}=$FORM{login};
my $password=$FORM{password};
$FORM{password}=createPass($FORM{password});
$FORM{limit}=$defLimit;
$FORM{protect}=$defProtection;
$FORM{rights}=$defRights;
$FORM{RegisteredOwner}=$RegisteredOwner;

        #use Data::Dumper;
        #die Dumper(\%FORM);

my $textT=get_record(read_file($ClientInfoTemplate),\%FORM);
open (CL, ">$clientsDataFolder/$FORM{login}/Account Details.html") or die "Can't open client data file $!";
print CL $textT;
close CL;
my $line;



my $text;
my $message;
foreach(@data_fields){
        if ($_ eq 'REMOTE_ADDR'){
                $line .="$ENV{REMOTE_ADDR}$separator";
                $field{$_}=1;
                $message.="$_: " unless $send_just_data;
                $message.="$ENV{REMOTE_ADDR}\n";
        }
        elsif ($_ eq 'https_USER_AGENT'){
                $line .="$ENV{https_USER_AGENT}$separator";
                $field{$_}=1;
                $message.="$_: " unless $send_just_data;
                $message.="$ENV{https_USER_AGENT}\n";
        }
        elsif ($_ eq 'DATE'){
                $line .="$date$separator";
                $field{$_}=1;
                $message.="$_: " unless $send_just_data;
                $message.="$date\n";
        }
        elsif ($ID_autoincrement && $_ eq $ID_autoincrement_name){
                $line .="$maxID$separator";
                $field{$_}=1;
                $message.="$_: " unless $send_just_data;
                $message.="$maxID\n";
        }
        else{   my $word;
                $line .="$FORM{$_}$separator";
                $field{$_}=1;
                if ($FORM{$_} || (!$only_fields_with_values)) {
                  $message.="$_: " unless $send_just_data;
                  $message.="$FORM{$_}\n";
                }
        }

}
chop $line;

                #####rights
                my $uR={};
                for(split(',',$defRights)){$uR->{$_}=1;}
                my $userRights = "  Edit [";
                $userRights.= $uR->{'w'} ? 'yes' : 'no';
                $userRights.= "]\n  Chmod [";
                $userRights.= $uR->{'c'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  Move/Rename [";
                $userRights.= $uR->{'m'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  Delete [";
                $userRights.= $uR->{'w'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  Download/Preview [";
                $userRights.= $uR->{'r'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  Upload [";
                $userRights.= $uR->{'u'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  Pack/Unpack [";
                $userRights.= $uR->{'p'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  MkDir  [";
                $userRights.= $uR->{'n'} ? 'yes' : 'no';
                $userRights.= "]\n";
                ########


$FORM{rights}=$defRights;
$FORM{password}=$password;






$from =  $FORM{$from_field_name} if $FORM{$from_field_name};
if($admin_mail && $send_me){male($admin_mail, $from, $subject, get_record(read_file($send_me_template),\%FORM));}
if($auto_responder && $FORM{$from_field_name}){
        male($FORM{$from_field_name},$auto_responder_from,$auto_responder_subject, get_record(read_file($auto_responder_message),\%FORM));
}

        open(F, ">>$UserDatabase") || error("Can't open file $UserDatabase!");
        flock(F, LOCK_EX);
        print F "$line\n";
        close F;



print "Location: $ApplicationCompleteURL\n\n";

exit;




sub error{
        if($r){
                $r->content_type('text/html');
        }
        else{print "Content-type: text/html\n\n";}
        print "<html><head><title>Error</title></head><body><br>";
        print "<font color=$fontColor size=$fontSize face=$fontFace>$error_title</font><br>" if $_[1];
        print "<br><font color=$fontColor size=$fontSize face=$fontFace>$_[0]</font><br>";
        print "<font color=$fontColor size=$fontSize face=$fontFace>$return_message</font>" if $_[1];
        print "</body></html>";
        exit;

}


sub male{
        error($email_input_error)  if length($_[1])>120 or length($_[0])>120;
        error($email_input_error)  if $_[1]=~m/:/is or $_[0]=~m/:/is;
        error($email_input_error)  if $_[1]=~m/Content-type/is or $_[0]=~m/Content-type/is;
        error($email_input_error)  if $_[1]=~m/\n/is or $_[0]=~m/\n/is ;
        $_[1] =~ s/<([^>]|\n)*>//g;
        $_[0] =~ s/<([^>]|\n)*>//g;
        $_[1]=~s/\n|\r//g;
        $_[0]=~s/\n|\r//g;

        if($send_via_SMTP){
            my $smtp = Net::SMTP->new($mailhost);
            $smtp->mail($_[1]);
            $smtp->to($_[0]);
            $smtp->data();
            $smtp->datasend("To: $_[0]\n");
            $smtp->datasend("From: $_[1]\n");
            $smtp->datasend("Content-Type: text/html\n\n"); 
            $smtp->datasend("Subject: $_[2]\n\n");
            $smtp->datasend("\n");
            $smtp->datasend("$_[3]\n");
            $smtp->dataend();
            $smtp->quit;

        }
        else{
                open(MAIL,"|$mailprog -t");
                print MAIL "To: $_[0]\n";
                print MAIL "From: $_[1]\n";
                print MAIL "Content-type: text/html\n";
                print MAIL "Subject: $_[2]\n\n";
                print MAIL "$_[3]\n";
                close(MAIL);
                                #print "To: $_[0]<br>";
        }
}


sub test_form{
        my $errors='';
        foreach(@required_fields){
                $errors.="ERROR FIELD &lt; $_ &gt;: $error_fields_require!<br>" if $FORM{$_} eq "";
        }
        foreach(@required_fields_numbers){
                $errors.="ERROR FIELD &lt; $_ &gt;: $error_fields_numbers!<br>" if $FORM{$_}=~m/\D/ or $FORM{$_} eq '';
        }
        foreach(@required_fields_email){
                $errors.="ERROR FIELD &lt; $_ &gt;: $error_fields_email!<br>" if $FORM{$_} !~m/\S+?\@\S+?\.\S+?/;
        }
        $errors.="ERROR: Your Password is incorrect" if $FORM{password} ne $FORM{password2};
        error("$errors",1) if $errors;
return;
}

sub createPass{
        my $password = shift;
        my $string = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM";
        my @chars=split(//,$string);
        my $crypt = $chars[int(rand(@chars-1))].$chars[int(rand(@chars-1))];
        return crypt($password,$crypt);
}
sub get_record{
        my $text = shift;
        my $INSERT = shift;
        $text =~ s{%%(.*?)%%}{exists($INSERT->{$1}) ? $INSERT->{$1} : ""}gsex;
        return $text;
}
sub read_file{
        local $/;
        open(F, $_[0]) || error("can't open file $_[0]!");
        my $data = <F>;
        close F;
        return $data;
}
