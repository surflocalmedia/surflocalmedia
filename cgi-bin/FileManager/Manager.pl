#!/usr/local/bin/perl5.22
use CGI::Carp qw(fatalsToBrowser);
($script=$0) =~s!^.*[/\\]!!;

##########################################################################
################## iDC File Manager Version 1.4.04 #######################
############################OEM VERSION###################################
##########################################################################

##########################################################################
# i Dot Communications ? 2004-2007 Copyright Mark Roberts / Alexandre Golovkine

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

##########################################################################

##########################################################################
# For Instructions / Questions / Comments etc... Please visit:
# Help Forum:   https://www.idotcommunications.co.uk/OnlineSupportArea/Forum/
##########################################################################

####File Manager - Version:###############################################
my $Version= "1.4.04e OEM";
##########################################################################

##########################################################################
##########################################################################
##########################################################################
############Modify The Following Sections Only!###########################

####File Manager - Registered Owner:######################################

my $RegisteredOwner= "Surflocal.Net";
#Change the "File Manager - Registered Owner:" to the name of your website or company etc...

##########################################################################

####Administrator Username And Password###################################

my $AdminLogin = {
        "trinityprescott" =>"tpadmin",
        "davidprescott" =>"dpadmin",
        "agent" =>"office",
};

#You may specify up to 4 Admin accounts.
#E.g. "Mark" =>"12345",

#PLEASE NOTE: THE USER NAME AND PASSWORDS YOU ENTER IN THE MANAGER.PL SCRIPT
#MUST BE THE SAME AS THE ONES YOU SPECIFY IN THE CLIENTMANAGER.PL SCRIPT.

####Main File Manager Title###############################################

my $Filemanagertitle = "Surflocal.Net- Agent Office";
#Change the "File Manager Title" to the name of your website or company etc...

##########################################################################

####Main Clients Directory################################################

my $rootHomeDir = "/usr/home/starting2014/public_html/surflocal.net/Clients/";

#Change the path to the "Main Clients Directory" to your servers path to the Main Root Directory + The sub-folderof the File Manager folder which will hold all your Clients folders.
#For example:
#e.g. Main Clients Directory ("/home/mysite/public_html/") +  Main File Manager Directory (FileManager) + "Clients"

##########################################################################

####File Manager Language#################################################
my $language = "en"; # default
#aliases - run as script.pl?language=en
my %languageFile = (
        "en" => "English.ini",
        "fr" => "French.ini",
        "de" => "German.ini",
        "nl" => "Dutch.ini",
        "it" => "Italian.ini",
        "es" => "Spanish.ini",
        "dk" => "Dansk.ini",
        "sw" => "Swedish.ini",
        "nr" => "Norsk.ini",
        "fi" => "Finnish.ini",
        "po" => "Portuguese (BR).ini",
        "ru" => "Russian.ini"
);

# Specify the File Manager language pack
##########################################################################

####Main Client Manager Script:###########################################

my $ClientScript = "ClientManager.pl";
#Do not modify the Main Client Manager Script name unless told to do so by iDC Support.

##########################################################################

####Main Login Script:####################################################

my $LoginScript = "Login.pl";
#Do not modify the Main Login Script name unless told to do so by iDC Support.

##########################################################################

####User Database#########################################################

my $userTable ="users.txt";
#Do not modify the User Database settings unless told to do so by iDC Support.

##########################################################################

####Notes File############################################################

my $notesFile = "/usr/home/starting2014/public_html/surflocal.net/FileManagerData/notes.txt";
#my $notesFile = "c:/www/filemanager/notes.txt";
#Change the path to the "Notes File" to your servers path to the Main Root Directory + the FileManagerData directory.
##########################################################################

####Hotlink URL############################################################

my $hotlinkurl = "http://www.surflocal.net/Clients";
#Change the url to the "Hotlink URL" to the url of your servers Client Folder

####File Manager Description##############################################

my $fileDescriptionOn = 1; #0 to off
# save description in a flatfile database "Description.ion"

##########################################################################

####File Manager Date Stamp###############################################

my $USdateFormat = 0;
# Change the USdateFormat to "1" to date stamp all files using the American Date format.

##########################################################################

####Hide Files############################################################

@notShowFiles = ('ion','htaccess','gacl','ade','adp','app','asa','asp','bas','bat','cdx','cer','chm','class','cmd','com','cpl','crt','csh','dll','exe','fxp','hlp','hta','htr','htw','ida','idc','idq','ins','isp','its','jse','ksh','lnk','mad','maf','mag','mam','maq','mar','mas','mat','mau','mav','maw','mda','mdb','mde','mdt','mdw','mdz','msc','msi','msp','mst','ops','pcd','pif','prf','prg','printer','pst','reg','scf','scr','sct','shb','shs','shtm','shtml','stm','url','vb','vbe','vbs','wsc','wsf','wsh','js','cgi','pl','php','zip','rar');
# Specify file extensions you do not want to be shown and they will
# be automatically hidden from view.

##########################################################################

#####Session Timeout######################################################

my $timeOut = "";
#You may configure (if required) the session timeout period.
#If no mouse or keyboard activity is detected in the specified time frame the user will be logged out.

##########################################################################

#####Auto Transfer Mode###################################################

my @autoTextMode = ('txt', 'htm', 'html', 'cgi', 'pl', 'pm');
#Please enter the file extension you wish to automatically upload in ASCII format.
#Those not specified will be uploaded in Binary.

##########################################################################

####Main Header Logo #####################################################

my $CustomerFrameUrl = 'http://www.surflocal.net/header.html';
my $CustomerFrameHeight = 0; # in px
#Change the "CustomerFrameUrl" to the URL (Domain name) of your companies logo or similar.
#You may also specify a webpage to appear in this frame.
#Change the "$CustomerFrameHeight" to the height (in pixels) of the frame you require.

##########################################################################

####Upload Settings ######################################################

####HTTP And HTTPS Upload Settings####

my $upload_prog_on = 1;  #Change to "1" to enable Upload Progress bar (Linux servers only)

####Flash Upload Settings####

my $secretWord = "fTf4m#G56sGH!";  #Do not modify the $secretWord unless told to do so by iDC Support.

my $sslUri ="https://www.mysite.com:443/cgi-bin/FileManager/Manager.pl";
# If you plan to use the Flash upload system under SSL (HTTPS) you must enter the url of the File Manager
#Script but include ":443" (without the speech marks) after your domain extension
#e.g. https://www.mysite.com:443/cgi-bin/FileManager/Manager.pl

my $Uploadflashfile = "http://www.surflocal.net/FileManagerData/";

#Change the url to the "$Uploadflashfile" to your servers url to the File Manager Image Directory
#For example:
#e.g. Main Main Image Directory ("http://www.surflocal.net/FileManagerData")

my $sslOn = 0; # Change the $sslOn to "1" to use the Flash upload system under SSL (HTTPS)

##########################################################################

####Miscellaneous Configuration Settings##################################

my $ResizePreviewOn = 1; #Change to "0" to disable Preview Window Resize

##########################################################################

####HTML Editor Configuration Settings####################################

####Default HTML Editor####

my $useWysiwig=1; #Change to "1" to enable the default HTML editor
my $editorSrc="/FileManagerData/wysiwyg.js"; #Enter the path to the HTML Editor wysiwyg.js file.

###########################

####Default HTML Editor####

#If you have uploaded the "tinymce" wysiwyg html editor directory to your server you
#can enable the editor below:

my $ResizeEditorOn = 0;  #Change to "1" to enable Editor Window Resize
my $editorpluginSrc="/tinymce/jscripts/tiny_mce/tiny_mce.js"; #Enter the path to the Tinymce HTML Editor tiny_mce.js file.
my $editorplugin = ""; #Change my $editorplugin =""; to my $editorplugin ="enable";

##########################################################################

####Analysis And Log Files ###############################################

####Activity Log####

my $LogActivity = 0;               #Change to "0" to disable User Activity Log
my $log = 'UserActivityLog.txt';   #Do not modify the $log settings unless told to do so by iDC Support.

####Error Log####

my $ErrorLog = 0;                  #Change to "0" to disable Error Log
my $elog = 'ErrorLog.txt';         #Do not modify the $log settings unless told to do so by iDC Support.

##########################################################################

####Email Configuration###################################################

#Configure the email settings so that the File Manager can send account signup details
#and notify you when new files have been uploaded

my $fromAdmin = 'trinity@surflocal.net';       #From Email Address
my $toAdmin   = 'trinity@surflocal.net';            #Email Adress you want to receive upload confirmations
my $mailprog  = '/usr/lib/sendmail';       #SendMail Path
my $subjecttitle   = 'Has Uploaded New Files';#Email Subject Title
my $msg_foot  = '';                           #Email Footer / Signature (Left Blank if using HTMl Emails)
my $send_as_html = 1;                         #Change to "1" to send an html formatted email
my $msg_body_file = "UploadEmail.shtml";      #Specify the html upload email template
my $sendConfirmUpload  = 0;#Change to "1" to receive file upload confirmations
my $sendConfirmFlashUpload  = 0;              #Change to "1" to receive flash upload confirmations
my $msg_body_file_download = "DownloadEmail.shtml";      #Specify the html download email template
my $sendConfirmDownload  = 0;#Change to "1" to receive file upload confirmations
##########################################################################

####Advanced Email Configuration##########################################

#SMTP email, uncomment next line to use it
#use Net::SMTP;
my $send_via_SMTP            = 0;
my $mailhost                 = 'smtp.com';

##########################################################################

#####Toolbar Links Configuration##########################################

my $contactus = "http://www.idotcommunications.co.uk/site.php?page=ContactUs";
my $tutorialslink = "https://www.idotcommunications.co.uk/OnlineSupportArea/Faq/";
my $forumlink = "https://www.idotcommunications.co.uk/OnlineSupportArea/Forum/";
#You may configure (if required) the above url's to link to your sites:
#contact page  / tutorials page / forum

##########################################################################

####Main Image Directory##################################################

my $htmlDataFolder = "http://www.surflocal.net/FileManagerData";
#Change the url to the "Main Image Directory" to your servers url to the File Manager Image Directory
#For example:
#e.g. Main Main Image Directory ("http://www.surflocal.net/FileManagerData")

##########################################################################

#Change the following image paths to mirror the folder structure or your File manager.
#As per point 4 you should have specified a folder in which to run your File Manager from.
#When the folder was created you should have created a sub-folder called "FileManagerData" where all the File Manager images will be stored, #therefore the path to the image folder would look like this for example:
#my $img_folder="$htmlDataFolder/folder.gif";

####File Association Images###############################################

my $fileTypeImgDir= $htmlDataFolder;
#file types
%FileType = (
        html  => 'html.gif',
        htm   => 'html.gif',
        shtml => 'html.gif',
        doc   => 'doc.gif',
        rtf   => 'doc.gif',
        exe   => 'exe.gif',
        pdf   => 'pdf.gif',
        bmp   => 'bmp.gif',
        swf   => 'swf.gif',
        gif   => 'gif.gif',
        jpeg  => 'gif.gif',
        jpg   => 'gif.gif',
        jpe   => 'gif.gif',
        png   => 'gif.gif',
        txt   => 'txt.gif',
        csv   => 'txt.gif',
        ion   => 'ion.gif',
        xls   => 'excel.gif',
        csv   => 'excel.gif',
        mp3   => 'music.gif',
        wmv   => 'music.gif',
        wma   => 'music.gif',
        mpeg  => 'music.gif',
        mpg   => 'music.gif',
        wav   => 'music.gif',
        mov  => 'music.gif',
        tif   => 'tif.gif',
        tiff   => 'tif.gif',
        zip   => 'compress.gif'
);
#Do not modify the File Association Images settings unless told to do so by iDC Support.

##########################################################################

####Toolbar Icons#########################################################

my $Download = "$htmlDataFolder/Download.gif";
my $Upload   = "$htmlDataFolder/Upload.gif";
my $BatchDownload   = "$htmlDataFolder/BatchDownload.gif";
my $hotlink  = "$htmlDataFolder/Hotlink.gif";
my $Pack     = "$htmlDataFolder/Pack.gif";
my $Unpack   = "$htmlDataFolder/Unpack.gif";
my $CHMOD    = "$htmlDataFolder/CHMOD.gif";
my $Preview  = "$htmlDataFolder/Preview.gif";
my $Copy     = "$htmlDataFolder/Copylg.gif";
my $Rename   = "$htmlDataFolder/Rename.gif";
my $Editor   = "$htmlDataFolder/Editor.gif";
my $Move     = "$htmlDataFolder/Move.gif";
my $Notes   = "$htmlDataFolder/Notes.gif";
my $MkDir    = "$htmlDataFolder/MkDir.gif";
my $Delete   = "$htmlDataFolder/Delete.gif";
my $Logoff   = "$htmlDataFolder/Logoff.gif";

####Main Toolbar Baground Images##########################################

my $toolsLine        = "$htmlDataFolder/toolsLine.png";
my $headLine         = "$htmlDataFolder/headLine.png";
my $background       = "$htmlDataFolder/background.png";

##########################################################################

####Control Panel Images##################################################

my $controlpanellogo = "$htmlDataFolder/ClientManagerLogo.png";
my $controlpanelmainheader = "$htmlDataFolder/controlpanelheader.png";
my $controlpanelsidebar = "$htmlDataFolder/controlsidebar.png";
my $controlpanelheaderwedge = "$htmlDataFolder/headerwedge.png";
my $controlpanelcontolbaricon = "$htmlDataFolder/contolbaricon.png";

##########################################################################

####Folder Image##########################################################
my $img_folder="<img src=$htmlDataFolder/folder.gif border=0>";
####File Image############################################################
my $img_file="<img src=$htmlDataFolder/file.gif border=0>";
####Up A Level Image######################################################
my $img_up="<img src=$htmlDataFolder/up.gif border=0>";
####Pack "GZ" Image#######################################################
my $img_gz="<img src=$htmlDataFolder/gz.gif border=0>";
####Arrow Up##############################################################
my $arrow_up="<img src=$htmlDataFolder/arrow_up.gif border=0  align=texttop>&nbsp;";
####Arrow Down Image ##################################################
my $arrow_down="<img src=$htmlDataFolder/arrow_down.gif border=0  align=texttop>&nbsp;";
####Note Icon##############################################################
my $img_note="<img src=$htmlDataFolder/note.gif border=0 alt=Note>";
##########################################################################
####Uploading Progress Bar################################################
my $loadImg =qq~
<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="https://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0" width="259" height="130" id="Untitled-1" align="middle">
<param name="allowScriptAccess" value="sameDomain" />
<param name="movie" value="$htmlDataFolder/Uploading.swf" /><param name="quality" value="high" /><param name="bgcolor" value="#ffffff" /><embed src="$htmlDataFolder/Uploading.swf" quality="high" bgcolor="#ffffff" width="259" height="130" name="Untitled-1" align="middle" allowScriptAccess="sameDomain" type="application/x-shockwave-flash" pluginspage="https://www.macromedia.com/go/getflashplayer" />
</object>
~;


##########################################################################

#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!


##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################

use CGI qw(:standard :cgi-lib);
#use lib "./Archive/";
#use Archive::Tar;
use Compress::Zlib;
use Cwd;
use File::Copy;
use File::Path;
use File::Find;
#use Archive::Zip;

##########################################################################
my %FORM=parse_qs();

sub parse_qs{
        my %FORM;
        (my $tmp = $ENV{'QUERY_STRING'})=~s/&amp;/&/g;
        my @pairs=split(/&/,$tmp);
        foreach (@pairs) {
                my ($name, $value) = split (/=/,$_,2);
                $value =~ tr/+/ /;
                $value =~ s/%(..)/pack("c",hex($1))/ge;
                $FORM{$name} = $value;
                }
        return %FORM;
}

flu() if $FORM{action} eq 'flu';

##########################################################################
my @params;
unless ($FORM{action} eq 'upload'){
        @params=param;
        for(@params){$FORM{$_}=join ",", param($_);}

}


        #protect html
        for ('cmd','fileDescription'){
                   $FORM{$_} =~ s/<!--(.|\n)*-->//g;
                   $FORM{$_} =~ s/<([^>]|\n)*>//g;
        }


@months = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
@weekDays = qw(Sun Mon Tue Wed Thu Fri Sat Sun);
($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = localtime();
$year = 1900 + $yearOffset;
$theHour = sprintf("%02u:%02u:%02u",$hour,$minute,$second);
$theTime = "$theHour, $weekDays[$dayOfWeek] $months[$month] $dayOfMonth, $year";

#protect for access over main root folder
$FORM{dir} =~ s/\.\.\///g;

%COOKIES = get_cookie('USER_Login');
###translate
$FORM{'language'}||= $COOKIES{language};
$FORM{'language'}||= $language;

my $charset="; charset=utf-8" if $FORM{'language'} eq 'en';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'fr';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'de';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'it';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'nl';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'dk';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'sw';
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'po';
my $charset="; charset=windows-1251" if $FORM{'language'} eq 'ru';
my $charset="; charset=UTF-8" if $FORM{'language'} eq 'enc';

%Message = get_messages($languageFile{$FORM{'language'}});
#######password protection#############
my $Rights={};
if($FORM{log_in}){
        if($AdminLogin->{$FORM{login}} && $AdminLogin->{$FORM{login}} eq  $FORM{password}){
                print "Set-Cookie: USER_Login=login&$FORM{login}&pass&$FORM{password}&language&$FORM{language}; path=/\n";
                print "Location: $script?\n\n";
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$FORM{login}|Logged in|\n" if $LogActivity;
                close(LOG);
                exit;
        }
        elsif($FORM{password}){
                my @data = read_file($userTable);
                shift @data;
                chomp;
                foreach(@data){
                      $_=~s/\r|\n//;
                      ($userId, $userLogin, $userPass, $userEmail, $userDir, $lim, $prot, $u_rights, $u_dis)=split('\|', $_);
                      if ($FORM{login} eq $userLogin && !$u_dis && $userPass eq  crypt($FORM{password},$userPass)){
                           print "Set-Cookie: USER_Login=login&$FORM{login}&pass&$FORM{password}&dir&$userDir&language&$FORM{language}; path=/\n";
                           print "Location: $script?\n\n";
                                                  open (LOG, ">>$log") or die $! if $LogActivity;
                           print LOG "$theTime|$FORM{login}|Logged in|\n" if $LogActivity;
                           close(LOG);
                           exit;
                      }
                }
                print "Location: Login.pl?error=1\n\n";
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$FORM{login}|Login error|\n" if $LogActivity;
                close(LOG);
                exit;
        }
        else{print "Location: Login.pl?error=1\n\n"; exit;}
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$FORM{login}|Login error|\n" if $LogActivity;
        close(LOG);
}
elsif(!$COOKIES{login}){print "Location: Login.pl\n\n"; exit;}
elsif($COOKIES{dir}){
        my $found;
        my @data = read_file($userTable);
        shift @data;
        chomp;
        foreach(@data){
                chomp;
                ($userId, $userLogin, $userPass, $userEmail, $userDir,  $discQuota,  $disabledFiles, $rights, $disabled)=split('\|', $_);
                if ($COOKIES{login} eq $userLogin && $userPass eq  crypt($COOKIES{pass},$userPass) && !$disabled){
                        $found=1;
                        for(split(',',$rights)){$Rights->{$_} = '1' if $_;}
                        last;
                }
        }
        unless ($found){print "Location: Login.pl\n\n"; exit;}
        $home = "$rootHomeDir/$userDir";
}
elsif($AdminLogin->{$COOKIES{login}} eq   $COOKIES{pass}){$home=$rootHomeDir; $myAdmin=1; @$Rights{("w","c","m","d","r","u","p","n","l","a")} = (1,1,1,1,1,1,1,1,1,1);}
else{print "Location: Login.pl\n\n"; exit;}

$secretWord.= $myAdmin==1? $AdminLogin->{$COOKIES{login}}:$userPass;

#######password protection end#######################
#disabled Files
my %disabledFiles;
$disabledFiles=~s/ //g;
for(split(',',$disabledFiles)){$disabledFiles{$_}=1;}

#######################################
if ($FORM{action} eq 'upload'){
        $upload_prog_on? upload() : upload2();
}
######################################################


head() if $FORM{type} eq "head";
foot() if $FORM{type} eq "foot";
logout()  if $FORM{action} eq 'logout';

%SUB = (
        download  => \&download,
        upload    => $upload_prog_on? \&upload : \&upload2,
        userarea  => \&userarea,
        findfile  => \&findfile,
        about     => \&about,
        view      => \&view,
        chmod     => \&chmod_f,
        logout    => \&logout,
        delete    => \&delete,
        mkdir     => \&mkdir,
        view      => \&view,
        rename    => \&rename,
        copy      => \&copy_f,
        pack      => \&pack,
        unpack    => \&unpack,
        move      => \&move,
        edit      => \&edit,
        tree          => \&tree,
        notes     => \&notes,
        get_css   => \&get_css,
        batch_download => \&batch_download,
        hotlink   => \&hotlink,
        fw_menu   => \&fw_menu,
        uploadfl =>  \&uploadfl,
        flu          => \&flu,
                editenable => \&editenable,
);



$dir = $FORM{dir};
$FORM{opt} ||="name";



frameText() unless $FORM{type} or $FORM{action};


unless($myAdmin){
        for (@notShowFiles){
                $notShowFiles{$_}=1;
        }
}

#######################################
##read disc space
if ($discQuota){
        find(\&discQuota, "$home/$dir");
        $overQuota = 1 if $discQuota<= $discSize /(1024*1024);
        if($discSize>(1024*1024)){
                $discSize /= 1024*1024;
                $discSizeTxt = "".sprintf("%.2f",$discSize)." $Message{Mb}";
                $discSizeTxt .= " <font color=red>$Message{over_quota}</font>" if $overQuota;
                                $userText = qq~<a href="javascript:show('$script?action=userarea', 200, 350)">$Message{control_panel}</a>~;
        }
        elsif ($discSize>1024){
                $discSize /= 1024;
                $discSizeTxt = "".sprintf("%.2f",$discSize)." $Message{Kb}";
                $discSizeTxt .= " <font color=red>$Message{over_quota}</font>" if $overQuota;
                                $userText = qq~<a href="javascript:show('$script?action=userarea', 200, 350)">$Message{control_panel}</a>~;
        }
        else{
                $discSize/=1;
                $discSizeTxt = "$discSize $Message{Bytes}";
                                $userText = qq~<a href="javascript:show('$script?action=userarea', 200, 350)">$Message{control_panel}</a>~;
        }
}
#######################################

$SUB{$FORM{action}}->() if $FORM{action} && $SUB{$FORM{action}};
print "Content-type: text/html$charset\n\n";
my $content=1;
my $has_descr = is_notes();

if($FORM{gzfile}){
  $tar = Archive::Tar->new("$home/$dir/$FORM{gzfile}",1);
  @files = $tar->list_files();
  my $i=0;
  for(@files){
        $stat{$tar->{'_data'}->[$i]->{name}}->{mode}= sprintf("%04o",$tar->{'_data'}->[$i]->{mode} & 0777);
        $stat{$tar->{'_data'}->[$i]->{name}}->{date}= $tar->{'_data'}->[$i]->{mtime};
        if ($tar->{'_data'}->[$i]->{typeflag}==5){
                my $opt=$FORM{opt};
                $opt='name' if $FORM{opt} eq 'ext' or $FORM{opt} eq 'size';
                $stat{$tar->{'_data'}->[$i]->{name}}->{name} = lc $tar->{'_data'}->[$i]->{name};
                $dsort{$tar->{'_data'}->[$i]->{name}} = $stat{$tar->{'_data'}->[$i]->{name}}->{$opt};
        }
        else{
                $stat{$tar->{'_data'}->[$i]->{name}}->{name} = lc $tar->{'_data'}->[$i]->{name};
                $stat{$tar->{'_data'}->[$i]->{name}}->{size}= $tar->{'_data'}->[$i]->{size};
                $tar->{'_data'}->[$i]->{name}=~m/\.([^\.\\\/]+)\Z/;
                $stat{$tar->{'_data'}->[$i]->{name}}->{ext} = $1;
                $sort{$tar->{'_data'}->[$i]->{name}} = $stat{$tar->{'_data'}->[$i]->{name}}->{$FORM{opt}};
                $stat{$tar->{'_data'}->[$i]->{name}}->{size}=~s/(\d)(\d{3})\Z/$1,$2/;
        }
        @time = localtime $tar->{'_data'}->[$i]->{mtime};
        $stat{$tar->{'_data'}->[$i]->{name}}->{date}= sprintf ("%02d/%02d/%04d %02d:%02d:%02d" ,$time[3],$time[4]+1,$time[5]+1900,$time[2],$time[1],$time[0] );


          $i++;
  }
   $qs = "&gzfile=$FORM{gzfile}";
}
elsif($FORM{search} && $FORM{inNotes}){
        find_in_notes();
        $qs .="&search=$FORM{search}&inNotes=1";
}
elsif($FORM{search}){
        find(\&search, "$home/$dir");
        $qs .="&search=$FORM{search}";
}
else{
        opendir(DIR, "$home/$dir") or error($Message{err_open_dir});
        while(defined($file = readdir DIR)){
                my @sb=stat("$home/$dir/$file");
                $stat{$file}->{mode}= sprintf("%04o",$sb[2] & 0777);
                $stat{$file}->{date}= $sb[10];
                if (-d "$home/$dir/$file"){
                        my $opt=$FORM{opt};
                        $opt='name' if $FORM{opt} eq 'ext' or $FORM{opt} eq 'size';
                        $stat{$file}->{name} = lc $file;
                        $dsort{$file} = $stat{$file}->{$opt} unless $file eq '.' or  $file eq '..';
                }
                else{
                        $file=~m/\.([^\.]+)\Z/;
                        next if !$myAdmin && $notShowFiles{lc $1};
                        $stat{$file}->{ext} = $1;
                        $stat{$file}->{name} = lc $file;
                        $stat{$file}->{size}= $sb[7];


                        $sort{$file} = $stat{$file}->{$FORM{opt}};
                        $stat{$file}->{size}=~s/(\d)(\d{3})\Z/$1,$2/;
                }

                @time = localtime $sb[10];
                if($USdateFormat){$stat{$file}->{date}= sprintf ("%04d-%02d-%02d %02d:%02d:%02d" ,$time[5]+1900,$time[4]+1,$time[3],$time[2],$time[1],$time[0] );}
                else{$stat{$file}->{date}= sprintf ("%02d/%02d/%04d %02d:%02d:%02d" ,$time[3],$time[4]+1,$time[5]+1900,$time[2],$time[1],$time[0] );}
        }
        close DIR;


}


if($FORM{opt} eq 'ext' or $FORM{opt} eq 'name' or $FORM{opt} eq 'mode'){
        @skeys = sort {$sort{$a} cmp $sort{$b}} keys %sort;
        @dkeys = sort {$dsort{$a} cmp $dsort{$b}} keys %dsort;
}
elsif($FORM{opt} eq 'date'){
        @skeys = sort {$sort{$b} <=> $sort{$a}} keys %sort;
        @dkeys = sort {$dsort{$b} <=> $dsort{$a}} keys %dsort;
}
elsif($FORM{opt} eq 'size'){
        @skeys = sort {$sort{$a} <=> $sort{$b}} keys %sort;
        @dkeys = sort {$dsort{$a} cmp $dsort{$b}} keys %dsort;
}
else{
        @skeys = sort {$sort{$a} <=> $sort{$b}} keys %sort;
        @dkeys = sort {$dsort{$a} <=> $dsort{$b}} keys %dsort;
}
$opt_r = $FORM{r};
$opt_{$FORM{opt}}="&r=1" unless $FORM{r};

if($FORM{r}){$arrow{$FORM{opt}} = $arrow_up;}
else{$arrow{$FORM{opt}} = $arrow_down;}


@skeys = reverse @skeys if $opt_r;
@dkeys = reverse @dkeys if $opt_r && ($FORM{opt} ne 'ext' and $FORM{opt} ne 'size');
$alert = "alert(\"$Message{not_support}\"); return;" if $FORM{gzfile};
my $selectedB = "selected" if $FORM{mode} eq 'b';
my $selectedT = "selected"  if $FORM{mode} eq 't';
my $selectedA  = "selected" unless $FORM{mode};

my $hWind = 340;
my $nameRow=56;
my $nameW=380;
if ($fileDescriptionOn){
        $hWind = 590;
        $nameRow-=30;
        $nameW-=196;
}


my $timeScript =qq~
        <script>
          var timerId ;
          function ResetIdle()
          {
                  clearTimeout(timerId) ;
                  timerId = window.setTimeout("PageTimeout()", $timeOut) ;
          }

          function PageTimeout()
          {
                  clearTimeout(timerId) ;
                  parent.location.href="$script?action=logout";
          }
        </script>
~ if $timeOut;

my $enableTime=qq~onMouseMove="ResetIdle()" onKeyPress="ResetIdle();"  onLoad=" ResetIdle();"~  if $timeOut;
my $matchCase=" checked" if $FORM{matchCase};
print qq~
<html>
        <head>
        <title>$Filemanagertitle</title>
        <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
        $timeScript
        <script>
                function sh(obj){if (obj.className!="selected") obj.className="of";}
                function shh(obj){if (obj.className!="selected") obj.className="off";}
                function test(ifFile){
                        var m=0;
                        var fileName;
                        var itDir;
                        for(i=0; i<document.files.dir.length; i++){
                                if (document.files.dir[i].checked) {fileName = document.files.dir[i].value;m++; itDir=1;}
                        }
                        for(i=0; i<document.files.file.length; i++){
                                if (document.files.file[i].checked) {fileName = document.files.file[i].value;m++}
                        }
                        if (!fileName) {alert("$Message{select_file}"); return;}
                        if (m>1){alert("$Message{only_one_file}"); return;}
                        if(itDir && ifFile){alert("$Message{no_selection}"); return;}
                        return fileName;
                }
                function testA(){
                        var m=0;
                        var Line ="";
                        filesSelected=0; itDir = 0;
                        for(i=0; i<document.files.dir.length-1; i++){
                                if (document.files.dir[i].checked) {
                                        Line += "&file="+escape(document.files.dir[i].value);
                                        itDir = 1;
                                        filesSelected++;
                                        }
                        }
                        for(i=0; i<document.files.file.length-1; i++){
                                if (document.files.file[i].checked) {
                                        Line += "&file="+escape(document.files.file[i].value);
                                        filesSelected++;
                                        }
                        }
                        return Line;
                }
                function selectAll(flag){
                        if (flag){
                                for(i=0; i<document.files.dir.length; i++){document.files.dir[i].checked = true;}
                                for(i=0; i<document.files.file.length; i++){document.files.file[i].checked = true;}
                        }
                        else{
                                for(i=0; i<document.files.dir.length; i++){document.files.dir[i].checked = false;}
                                for(i=0; i<document.files.file.length; i++){document.files.file[i].checked = false;}
                        }
                }
        </script>
        </head>
        <body $enableTime topmargin=0 leftmargin=0>
        <table border=0 width=100% cellspacing=2  cellpadding=1 ALIGN=left >
        <form name=files id=files>
        ~;
my $addQs = "&opt=$FORM{opt}" if $FORM{opt};
$addQs .= "&opt_=$FORM{opt_}" if $FORM{opt_};


if($FORM{search} && !(@dkeys || @skeys)){
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|Search performed - no results found|\n" if $LogActivity;
        close(LOG);
        print "<tr><th><br><br><br><br><br>No Results Found</th></tr>";
        print "</table></form></body></html>";
        exit;
}



($up=$dir)=~s![/\\][^/\\]*\Z!! if $dir=~m/[\/\\]/;
$up=$dir if $FORM{gzfile};
if ($dir or $FORM{gzfile} or $FORM{search}){
        for(".."){
                print "<tr class=off onmouseover=sh(this) onmouseout=shh(this)>
                <td>&nbsp;</td>
                <td><a href='$script?dir=$up$addQs' target=_top>$img_up</a> <a href='$script?dir=$up$addQs' target=_top>[$_]</td>
                <td>&nbsp;</td><td>&lt;DIR&gt;</td>";
                print "<td>&nbsp;</td>" if $fileDescriptionOn;
                print "<td>$stat{$_}->{date}</td><td>$stat{$_}->{mode}</td>";
                print "        </tr>";
        }
}


        $shDir =$dir;
        $shDir &&="$dir/";
        use Data::Dumper;

for(@dkeys){
        (my $tmpDir="$_")=~s/\&/%26/g; $tmpDir=~s/#/%23/g;
        print qq~<tr class=off onmouseover=sh(this) onmouseout=shh(this)>
                <td><input type=checkbox name=dir value="$shDir$tmpDir"></td><td>~;
        print "<a href='$script?dir=$shDir$tmpDir$addQs' target=_top>" unless $FORM{gzfile};
        print "$img_folder";
        (my $fileN=$home."/".$dir."/".$_)=~s/\/+/\//g;
        $fileN=~s/\/\/+/\//g;
        print "<a href=\"javascript:parent.head.notesview('$shDir$_')\"    >$img_note" if $has_descr->{$fileN};
        print "</a>" unless $FORM{gzfile};
        print " <a href='$script?dir=$shDir$tmpDir$addQs' target=_top>[$_]<a></td><td>&nbsp;</td><td>&lt;DIR&gt;</td>";

        my $desc;
        if ($has_descr->{$fileN}){
                $desc =$has_descr->{$fileN}->[0]->[2];
                $desc = substr($desc,0,30);
                $desc =~s!<br>.*$! !gi;
                $desc=~s!\r|\n! !g;
        }

        print "<td>&nbsp;<a href=\"javascript:parent.head.notesview('$shDir$_')\"    >$desc</td>" if $fileDescriptionOn;
        print "<td>$stat{$_}->{date}</td><td>$stat{$_}->{mode}</td>";
        print "        </tr>";
}
for(@skeys){
        my $desc;
        my $icon = qq~<img src="$fileTypeImgDir/$FileType{lc $stat{$_}->{ext}}" border=0>~ if $FileType{lc $stat{$_}->{ext}};
        $icon ||=$img_file;
        print qq~<tr class=off onmouseover=sh(this) onmouseout=shh(this)>\n<td><input type=checkbox name=file value="$shDir$_"></td><td>~;
        if ($_=~m/(gz)|(tar)\Z/i){
                (my $tmpFile="$_")=~s/\&/%26/g;
                $tmpFile=~s/#/%23/g;
                print "<a href='$script?opt=name&dir=$dir&r=$FORM{r}&gzfile=$tmpFile' target=_top>$img_gz</a> $_\n";
        }
        else{
                my $fileN=$home."/".$dir."/".$_;
                $fileN=~s/\/\/+/\//g;
                (my $fl = "$shDir$_")=~s/'/\\'/g;
                print "<a href=\"javascript:parent.head.fview('$fl')\"    >$icon".($has_descr->{$fileN}? "<a href=\"javascript:parent.head.notesview('$fl')\">$img_note":'')." <a href=\"javascript:parent.head.fview('$fl')\"    >$_</a>\n";
                if ($has_descr->{$fileN}){
                        $desc =$has_descr->{$fileN}->[0]->[2];
                        $desc = substr($desc,0,30);
                        $desc =~s!<br>.*$! !gi;
                        $desc=~s!\r|\n! !g;
                }

        }
        if(length($stat{$_}->{size})>7){
                $stat{$_}->{size}=~s/,//;
                $stat{$_}->{size} = sprintf("%.2f",$stat{$_}->{size}/(1024*1024))." Mb.";
        }
        print "</td><td>$stat{$_}->{ext}</td><td align=right>$stat{$_}->{size}</td>";


        print "<td>&nbsp;<a href=\"javascript:parent.head.notesview('$shDir$_')\"    >$desc</td>" if $fileDescriptionOn;
        print "<td>$stat{$_}->{date}</td><td>$stat{$_}->{mode}</td>";
        print "</tr>\n";
}

print qq~<tr>
          <td width=2%><img src="$fileTypeImgDir/spacer.gif"  border=0 width=20 height=1></td>
          <td width=$nameRow%><img src="$fileTypeImgDir/spacer.gif" border=0 width=$nameW height=1></td>
          <td width=5%><img src="$fileTypeImgDir/spacer.gif"  border=0 width=35 height=1></td>
          <td width=11%><img src="$fileTypeImgDir/spacer.gif" border=0 width=70 height=1></td>\n~;
print qq~ <td width=27%><img src="$fileTypeImgDir/spacer.gif" border=0 width=180 height=1></td>\n~ if $fileDescriptionOn;
print qq~ <td widht=19%><img src="$fileTypeImgDir/spacer.gif" border=0 width=150 height=1></td>
          <td width=6%><img src="$fileTypeImgDir/spacer.gif"  border=0 width=50 height=1></td>
         </tr>~;
print "</table><input type=hidden name=file><input type=hidden name=dir></form></body></html>";
exit;

###################################################
sub find_in_notes{
        #my $notes = is_notes();
        for my $key (keys %$has_descr){
                next unless $key=~m!$home!;
                my $found =0;
                if ($FORM{matchCase}){
                        for (@{$has_descr->{$key}}){
                           if ($_->[2]=~/$FORM{search}/i){$found=1; last;}
                        }
                }
                else{
                        $FORM{search}=~s/\s+/ /g;
                        my @words = split ' ', $FORM{search};
                        for my $note (@{$has_descr->{$key}}){
                                last if $found;
                                for my $word(@words){
                                        if ($note->[2]=~/$word/i){$found=1; last;}
                                }

                        }
                }
                next unless $found;


                my @sb=stat($key);
                (my $file=$key)=~s/$home\///;
                $stat{$file}->{mode}= sprintf("%04o",$sb[2] & 0777);
                $stat{$file}->{date}= $sb[10];
                if (-d "$key"){
                        my $opt=$FORM{opt};
                        $opt='name' if $FORM{opt} eq 'ext' or $FORM{opt} eq 'size';
                        $stat{$file}->{name} = lc $file;
                        $dsort{$file} = $stat{$file}->{$opt};
                }
                else{
                        $stat{$file}->{name} = lc $file;
                        $stat{$file}->{size}= $sb[7];
                        $file=~m/\.([^\.]+)\Z/;
                        $stat{$file}->{ext} = $1;

                        $sort{$file} = $stat{$file}->{$FORM{opt}};
                        $stat{$file}->{size}=~s/(\d)(\d{3})\Z/$1,$2/;
                }
                @time = localtime $sb[10];
                $stat{$file}->{date}= sprintf ("%02d/%02d/%04d %02d:%02d:%02d" ,$time[3],$time[4]+1,$time[5]+1900,$time[2],$time[1],$time[0] );
        }
 }







sub search {
        $file=$File::Find::name;
        return if $file eq $rootHomeDir;
        unless($myAdmin){
                $file=~m/\.([^\.]+)\Z/;
                return if $notShowFiles{$1};
        }
        if($FORM{search}=~m/\*/){
                if($FORM{search}=~m/(.*)\.(.*)/){
                        if($FORM{matchCase}){
                                if($1 ne '*') {return if $file!~m/$1\./;}
                                elsif($2 ne '*') {return if $file!~m/\.$2/;}

                        }
                        else{
                                if($1 ne '*') {return if $file!~m/$1\./i;}
                                elsif($2 ne '*') {return if $file!~m/\.$2/i;}
                        }
                }
        }
        else{
                if($FORM{matchCase}){return if $file!~m/$FORM{search}/;}
                else{return if $file!~m/$FORM{search}/i;}

        }

                my @sb=stat("$file");
                $file=~s/$home\///;
                $stat{$file}->{mode}= sprintf("%04o",$sb[2] & 0777);
                $stat{$file}->{date}= $sb[10];
                if (-d "$home/$dir/$file"){
                        my $opt=$FORM{opt};
                        $opt='name' if $FORM{opt} eq 'ext' or $FORM{opt} eq 'size';
                        $stat{$file}->{name} = lc $file;
                        $dsort{$file} = $stat{$file}->{$opt} unless $file eq '.' or  $file eq '..';
                }
                else{
                        $stat{$file}->{name} = lc $file;
                        $stat{$file}->{size}= $sb[7];
                        $file=~m/\.([^\.]+)\Z/;
                        $stat{$file}->{ext} = $1;

                        $sort{$file} = $stat{$file}->{$FORM{opt}};
                        $stat{$file}->{size}=~s/(\d)(\d{3})\Z/$1,$2/;
                }
                @time = localtime $sb[10];
                $stat{$file}->{date}= sprintf ("%02d/%02d/%04d %02d:%02d:%02d" ,$time[3],$time[4]+1,$time[5]+1900,$time[2],$time[1],$time[0] );

}

sub logout{
        print "Set-Cookie: USER_Login=; path=/\n";
        print "Location: $script\n\n";
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|Logged out|\n" if $LogActivity;
        close(LOG);
        exit;
}
sub promt{
        print "Content-type: text/html$charset\n\n";
        my $txt= qq|<head>
<script>
location.replace("$LoginScript")
</script>
</body>
</html>
|; print $txt;
        exit;
}
sub get_cookie{
my %COOK;
        @cookies=split('; ',$ENV{HTTP_COOKIE});
        foreach $line (@cookies){
                ($c_name, $c_value) = split(/=/,$line,2);
                if ($c_name eq $_[0]){
                        @cook=split(/&/,$c_value);
                        for($a=0; $a<@cook; $a+=2){
                                $cook[$a+1] =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                                $COOK{$cook[$a]}=$cook[$a+1];
                        }
                }
        }
        return %COOK;
}
sub read_file{
        my $file=shift;
        open(F, $file) || error("$Message{err_open_file} $file!");
        my @data = <F>;
        close F;
        return @data;
}
sub pack{
        error_right('p') unless $Rights->{'p'};
        @files=param('file');
        if($FORM{cmd} ){
                        $tar = Archive::Tar->new();
                        chdir "$home/$dir";
                        for(@files){
                                $_=~m/\.([^\.])+\Z/;
                                next if $disabledFiles{lc $1};
                                $_=~s/$dir\/?//;
                                $t.=$tar->add_files($_);
                                if (-d $_){
                                        @listF = ();
                                        find(\&toTar, $_);
                                        shift @listF;
                                        $tar->add_files(@listF);
                                }
                        }
                        (@path) = split(/\//,$FORM{cmd});
                        $file = pop @path;
                        $file =~s/\.tar//;
                        $file =~s/\.gz//;
                        foreach (@path) {
                            if (-e $_ && ! -d $_) {
                                warn "$_ $Message{err_not_dir}\n";
                                next;
                            }
                            mkdir $_,0777 unless -d $_;
                            chdir $_;
                        }
                        chdir "$home/$dir";
                        $tar->write("$file.tar") or error("$Message{err_create} $file.tar");
                        binmode ("$file.tar.gz"); # gzopen only sets it on the fd
                        my $gz = gzopen("$file.tar.gz", "wb") or error( "$Message{err_open_std}: $gzerrno\n") ;
                        open (F,"$file.tar")  or error("$Message{err_open} $file.tar");
                        binmode F;
                        while(<F>){$gz->gzwrite($_)  or error( "$Message{err_write}: $gzerrno\n") ;}
                        close (F);
                        $gz->gzclose;
                        unlink "$file.tar";
                  html(1,1);
        }
        (my $filename=$FORM{file})=~s!^.*[/\\]!!;
        foreach(@files) {$hidden.=qq~<input type=hidden name=file value="$_">~;}
        my $arch = "$dir/$filename.tar.gz";
        my $text = qq~<table width=100%><tr><td>$Message{pack_to}:</td></tr><tr><td>$hidden<input name=cmd size=45 value="$arch"></td></tr><tr><td align=right><input type=submit value="$Message{ok}"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button></table>~;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|Archive File '$filename.tar.gz' created|\n" if $LogActivity;
        close(LOG);
        html($text,0, "pack", $dir,"$Message{pack_file}");

}
sub toTar{
        push @listF, $File::Find::name;
        return;
}
sub unpack{
        error_right('p') unless $Rights->{'p'};
        my $text;
        if($FORM{cmd}){
                $_=~m/\.([^\.])+\Z/;
                next if $disabledFiles{lc $1};
                $FORM{cmd}=~s!/\*\.\*\Z!!;
                $FORM{cmd}=~s!\A/!!;
                $tar = Archive::Tar->new("$home/$FORM{file}",1);
                  @files = $tar->list_files();
                  chdir "$home/$FORM{cmd}";
                $tar->extract(@files);
                html(1,1);
        }
        elsif($FORM{file}!~m/\.tar/ && $FORM{file}!~m/\.gz/){$text = qq~<table width=100%><tr><td align=center><font color=red><b>$FORM{file}</b> $Message{not_archive}</font></td></tr><tr><td align=right><input type=button value=$Message{cancel} onclick="window.close()" class=button></td></tr></table>~;}
        else{
                $slash='/' if $dir;
                $text = qq~<table width="100%"><tr><td>$Message{unpack_files_from}:</td></tr><tr><td><input type=hidden name=file value="$FORM{file}"><input name=cmd size=30 value="$slash$dir/*.*"></td></tr><tr><td align=right><input type=submit value="OK"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button></td></tr></table>~;}
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|File '$FORM{file}' unpacked|\n" if $LogActivity;
        close(LOG);
        html($text,0, "unpack", $dir,"$Message{unpack_files}");
}

sub chmod_f{
        error_right('c') unless $Rights->{'c'};
        my ($text, $mode);
        chdir $home;
        $FORM{cmd}=eval("$FORM{cmd}") & 0777;
        for(param('file')){
                $_=~m/\.([^\.])+\Z/;
                next if $disabledFiles{lc $1};
                if ($FORM{cmd}){ chmod $FORM{cmd}, $_; }
                else{
                        $text .="<input type=hidden name=file value=\"$_\" >"  if $_ ;
                        my @sb=stat("$home/$dir/$_");
                        $mode= sprintf("%04o",$sb[2] & 0777);
                }
        }
        $mode ||= "0644";
        my $R;
        my ($n,$u,$g,$o) = split("",$mode);
        if ($u>=4){$u-=4; $R->{u}->{r}="checked"}
        if ($u>=2){$u-=2; $R->{u}->{w}="checked"}
        if ($u>=1){$u-=1; $R->{u}->{e}="checked"}

        if ($g>=4){$g-=4; $R->{g}->{r}="checked"}
        if ($g>=2){$g-=2; $R->{g}->{w}="checked"}
        if ($g>=1){$g-=1; $R->{g}->{e}="checked"}

        if ($o>=4){$o-=4; $R->{o}->{r}="checked"}
        if ($o>=2){$o-=2; $R->{o}->{w}="checked"}
        if ($o>=1){$o-=1; $R->{o}->{e}="checked"}

$text .= qq~
<script>
        function SetMod(){
        var U = 0; var G = 0; var O =0;
                for(a=0;a<3;a++){
                        if (document.wndForm.U[a].checked) U += 1*document.wndForm.U[a].value;
                        if (document.wndForm.G[a].checked) G += 1*document.wndForm.G[a].value;
                        if (document.wndForm.O[a].checked) O += 1*document.wndForm.O[a].value;
                }
                document.wndForm.cmd.value= "0"+U+G+O;
        }
</script>
<input type=hidden name=file value="$FORM{file}">
<center><b>$Message{chmod}</b></center>
<table align=center class="border">
<tr><td>Mode</td><td>User</td><td>Group</td><td>World</td></tr>
<tr><td>Read</td>
<td><input type=checkbox name="U" onclick="SetMod(this)" value="4" $R->{u}->{r}></td>
<td><input type=checkbox name="G" onclick="SetMod(this)" value="4" $R->{g}->{r}></td>
<td><input type=checkbox name="O" onclick="SetMod(this)" value="4" $R->{o}->{r}></td>
</tr>
<tr><td>Write</td>
<td><input type=checkbox name="U" onclick="SetMod(this)" value="2" $R->{u}->{w}></td>
<td><input type=checkbox name="G" onclick="SetMod(this)" value="2" $R->{g}->{w}></td>
<td><input type=checkbox name="O" onclick="SetMod(this)" value="2" $R->{o}->{w}></td>
</tr>
<tr><td>Execute</td>
<td><input type=checkbox name="U" onclick="SetMod(this)" value="1" $R->{u}->{e}></td>
<td><input type=checkbox name="G" onclick="SetMod(this)" value="1" $R->{g}->{e}></td>
<td><input type=checkbox name="O" onclick="SetMod(this)" value="1" $R->{o}->{e}></td>
</tr>
<tr><td>Permission</td><td colspan=3><input type=text name="cmd" size="4" value="$mode"></td></tr>
<tr><td colspan="4" align="center">
        <input type=submit value="$Message{chmod}">
        <input type=button  value=$Message{cancel} onclick="window.close()"></td></tr>
</table>
~;
        html(1,1) if $FORM{cmd};
        html($text,0,"chmod", $dir,"$Message{chmod}");
}
sub delete{
        error_right('d') unless $Rights->{'d'};
        for(param('file')){
                $_=~m/\.([^\.])+\Z/;
                next if $disabledFiles{lc $1};
                if ($_ and -e "$home/$_"){
                        if (-d "$home/$_"){rmtree("$home/$_");}
                        else{unlink "$home/$_";}
                }
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$COOKIES{login}|$_ deleted|\n" if $LogActivity;
                close(LOG);

        }
        print "Location: $script?dir=$dir&r=$FORM{r}\n\n";
}
sub hotlink{
        error_right('r') unless $Rights->{'r'};
        my $filename=$FORM{file};
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|File '$filename' hotlinked|\n" if $LogActivity;
        close(LOG);

my $text = qq~<table width=100%>
<script language="javascript" type="text/javascript">
function copy_clip(txt)
{
 if (window.clipboardData)
   {
 window.clipboardData.setData("Text", txt);
  }
  }
function replaceCharacters() {
  var origString = document.wndForm.inTB.value;
  var inChar = document.wndForm.inC.value;
  var outChar = document.wndForm.outC.value;
  var newString = origString.split(inChar);
  newString = newString.join(outChar);
  document.wndForm.link.value = newString;
}
function sendmail()
{
location.href = "mailto:?Subject=" + "RE: $Message{hotlink}"
+ "&Body=" + escape(document.wndForm.link.value);
}
function writeText (form) {
    wndForm.inTB.value = "$hotlinkurl/$userDir/$filename"
}
</script>
<BODY onLoad="writeText(this.form); replaceCharacters();">

<tr><td>$Message{hotlink}:</td></tr>
<tr><td nowrap>
<form>
<input name="inTB" type="hidden" id="inTB" value="">
<input name="link" size=43 id = "txt" value="">
<input name="inC" type="hidden" id="inC" value=" ">
<input name="outC" type="hidden" id="outC" value="%20">
<input type="button" class=button value="->" onclick="window.open ('$hotlinkurl/$userDir/$filename')" /></td></tr>
<tr><tr>
<td align=right>
<input type = "button" class=button value = "$Message{select_all}" onclick = "copy_clip(document.getElementById('txt').value); javascript:this.form.link.focus();this.form.link.select();" >
<input type="button" class=button value="Email $Message{hotlink}" onClick="sendmail();">
</form>
</table>
~;
html($text,0, "hotlink", "$dir","$Message{hotlink}");
}

sub rename{
        error_right('m') unless $Rights->{'a'};
        if($FORM{cmd}){
                $FORM{cmd}=~m/\.([^\.]+)\Z/;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|'$FORM{old_cmd}' renamed to '$FORM{cmd}'|\n" if $LogActivity;
        close(LOG);
                error("$Message{err_rename_disabled}") if $disabledFiles{lc $1};
                $FORM{old_cmd}=~m/\.([^\.]+)\Z/;
                error("$Message{err_rename_disabled}") if $disabledFiles{lc $1};

                chdir "$home/$dir";
                rename  "$FORM{old_cmd}", "$FORM{cmd}" or error("$Message{err_rename_file}");
                update_notes("$home/$dir/$FORM{old_cmd}","$home/$dir/$FORM{cmd}");
                html(1,1);
        }
        (my $filename=$FORM{file})=~s!^.*[/\\]!!;


        my $text = qq~<table width=100%><tr><td><input type=hidden name=old_cmd value="$filename"><input name=cmd size=30 value="$filename"></td></tr><tr><td align=right><input type=submit value="$Message{ok}"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button></table>~;
        html($text,0, "rename", "$dir","$Message{rename_file}");
}
sub copy_f{
        error_right('m') unless $Rights->{'m'};
        if($FORM{cmd}){
                my @old = param('old_cmd');
                 my $fname=0;
                       if ($FORM{cmd}=~s/(\/|\*\.\*)$/\//){
                               $fname =0;
                       }
                elsif(@old==1){
                        $fname = 1;
                        $FORM{cmd}=~m/\.([^\.]+)\Z/;
                        error("$Message{err_copy_disabled}") if $disabledFiles{lc $1};
                }
                  for(@old){
                        $_=~m/\.([^\.]+)\Z/;
                        error("$Message{err_copy_disabled}") if $disabledFiles{lc $1};
                        (my $filename=$_)=~s!^.*[/\\]!!;
                        if(-d "$home/$_"){
                                $DIR="$FORM{cmd}/$filename";
                                mkpath("$home/$FORM{cmd}", 0, 0755);
                                chdir "$home";
                                find(\&wanted, "$_");
                        }
                        elsif($fname){copy("$home/$_", "$home/$FORM{cmd}");}
                        else{
                                (my $newname=$_)=~s!^.*[/\\]!!;
                                copy("$home/$_", "$home/$FORM{cmd}/$newname");
                        }
                }
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|'$FORM{old_cmd}' copied to '$FORM{cmd}'|\n" if $LogActivity;
        close(LOG);
                html(1,1);
        }
        my @files = param('file');
        (my $filenames = $FORM{file})=~s/,/, /g;
        if (scalar @files < 2){my $filename=$FORM{file} ;}
        else{$filename="*.*";}

        my $text = qq~
                <script type="text/javascript">
                        function show( url,height, width){
                                newWnd=window.open(url, '_tree', "height="+height+", width="+width+", top="+200+", left="+200+", status=none, scrollbars='yes', location=none");
                                newWnd.focus();
                        }
                        function setPath2(path){
                                var rest = document.getElementById('cmd').value;
                                   if (document.getElementById('cmd').value.lastIndexOf('\/')>=0) rest = rest.substr(document.getElementById('cmd').value.lastIndexOf('\/')+1);
                                document.getElementById('cmd').value=path+"/"+ rest;
                        }
                </script>

        <table width=100%>
                <tr><td>$Message{copy} <b>$filenames</b> $Message{to}:</td></tr>
                <tr><td nowrap>~;
         for(@files){
                $text .= "<input type=hidden name=old_cmd value=\"$_\">";
         }

        $text .= qq~<input name="cmd" id="cmd" size="50" style="width:260" value="$filename">
                <input type=submit value="$Message{ok}"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button></td></tr>
                </table>
                <iframe  style="width:340; border-style:none; height:160"   src="$script?action=tree">~;
        html($text,0, "copy", $dir,"$Message{copy_file}");
}



sub move{

        error_right('m') unless $Rights->{'m'};
        #read definition for path from cookies
        my @paths = split ',', {get_cookie('USER_paths')}->{'paths'};
        my %paths;
        for (@paths){$paths{$_}++};
        $DIR ='';
        if ($FORM{cmd}){
                $FORM{cmd}=~s/(\/|\/\*\.\*)$/\//;

                error("Your target directory is not correct!") unless -d "$home/$FORM{cmd}";
                (my $dir = $FORM{cmd} )=~s/\/([^\/]+)$//;
                for my $d (param('old_cmd')){
                        next unless $d;
                        $d=~m/\.([^\.]+)\Z/;
                        error("$Message{err_move_disabled}") if $disabledFiles{lc $1};
                        (my $filename=$d)=~s!^.*[/\\]!!;
                        if(-d "$home/$d"){
                                next if "$home/$d" =~m/$home\/$FORM{cmd}\/$filename/;
                                #copy folder
                                $DIR="$FORM{cmd}/$filename";
                                unless ( -d "$home/$FORM{cmd}/$filename" ){mkpath("$home/$FORM{cmd}/$filename", 0, 0755)  or error("can't move folder $_ - $!") ;}
                                chdir "$home";

                                find(\&wanted, "$d");
                                if ($FORM{cmd} !~m/$d/){
                                        #die "%$d% %$FORM{cmd}%". $FORM{cmd} =~m/$d/;
                                        rmtree("$home/$d") or die $!
                                }
                        }
                        else{        #TODO messages!
                                my $op=copy("$home/$d", "$home/$FORM{cmd}/$filename");
                                error("can't move file $d to $home/$FORM{cmd}/$filename $!") unless $op;
                                unlink "$home/$d" if $d ne $FORM{cmd};
                                update_notes("$home/$d","$home/$FORM{cmd}/$filename");
                        }
                }
                html(1,1);
        }
        my @files = param('file');
        (my $filenames = $FORM{file})=~s/,/, /g;
        my $filename="/";
        my $ftomove=join ", ",@files;

        $_ = "<option>$_</option>" for @paths;
        my $pathSelect;# = "<tr><td><select name=\"path\" id=\"path\"  onChange=\"setPath();\" style=\"width:320\"><option value=\"\">&nbsp;</option>".(join ("\n",@paths))."</select></td></tr>" if @paths;
        my $text = qq~
                <script type="text/javascript">
                        function show( url,height, width){
                                newWnd=window.open(url, '_tree', "height="+height+", width="+width+", top="+200+", left="+200+", status=none, scrollbars='yes', location=none");
                                newWnd.focus();
                        }
                        function setPath2(path){
                                var rest = document.getElementById('cmd').value;
                                   if (document.getElementById('cmd').value.lastIndexOf('\/')>=0) rest = rest.substr(document.getElementById('cmd').value.lastIndexOf('\/')+1);
                                document.getElementById('cmd').value=path+"/"+ rest;
                        }
                </script>
                <table width=100%>
                <tr><td>$Message{move} <b>$ftomove</b> $Message{to}:</td></tr>~;
         for(@files){
                $text .= "<input type=hidden name=old_cmd value=\"$_\">";
         }

                $text .= qq~<tr><td nowrap><input name="cmd" id="cmd" size="30" style="width:240" value="$filename">
                <input type=submit value="$Message{ok}"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button>
                </td></tr>
                <tr><td align=right></td></tr>
                </table>
                <iframe  style="width:340; border-style:none; height:160"   src="$script?action=tree">

                ~;
        html($text,0, "move", $dir,"$Message{move_file}");
}


my $Tree={};
sub tree{
        $home=~s/\/$//;
        find(\&build_tree, "$home");
        my $text=qq~
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<title>File list</title>



<style type="text/css">
html, body {border:none;}
#tree { white-space:nowrap; *overflow-y:scroll; background-color:#eeeeee;}
#tree img      {vertical-align:middle;height:16px;width:16px;margin:2px 0;margin-left:0px;}
#tree div      {margin-left:20px;display:none;}
#tree div.blk  {display:block;}
#tree div.blki {margin:0;display:inline;}
#tree span { border: solid 1px #eeeeee; padding:2px; display:inline; top:-2px; font-size:10px; cursor:pointer; *cursor:hand; line-height:20px; margin-left:32px; argin-left:16px;}
#tree span.h { background-color:#eeeeee}
#tree span.fld {font-family: Verdana, Arial; font-size:8pt;background:url($htmlDataFolder/folder.gif) no-repeat bottom left; padding-left:16px; eight:17px; vertical-align:middle; margin-left:2px;}
</style>

<script type="text/javascript">
var frm, file, btn;
function pageLoad(){
 tre  = document.getElementById('tree');
}
function tMove(e, over){
 var e = e || window.event;
 e = e.target || e.srcElement;
 if (e.tagName!='SPAN') return;
 if (over)
  e.className+=' h';
 else
  e.className = e.className.substring(0, e.className.length-2);
}
function tClick(e){
 var e = e || window.event;
 e = e.target || e.srcElement;
 var i, d, clickAtImg;
 if (e.tagName=='IMG') {
  i = e;
  e = e.nextSibling;
  clickAtImg = 1;
 }
 if (e.tagName=='SPAN')
  i = e.previousSibling;
 else {
  return;
 }
 d = e.nextSibling.nextSibling;
 if (d && d.tagName=='DIV' && (clickAtImg)) {
  d.className = (d.className=='')? 'blk' : '' ;
  i.src = '$htmlDataFolder/' +
((d.className=='blk')?'e.gif':'c.gif');

 }
 if (!clickAtImg){
  parent.setPath2(e.id.substring(1));
  // window.close();
  }
}
</script>
</head>
<body onload="pageLoad();" bgcolor="#eeeeee">
<div  id="tree"  onmouseover="tMove(event, 1)"  onmouseout ="tMove(event)"  onclick="tClick(event)">~;
for my $cat (@{$Tree->{''}}){
        my $tmp =  treeline($cat->{id}, $Tree);
        my $coll= $tmp? 'c':'l';
        $text.=qq~<img src='$htmlDataFolder/$coll.gif'><span class="fld" id="A$cat->{id}">$cat->{Title}</span><br>~;
        $text.=qq~<div>$tmp</div>~ if $tmp;
}
$text.="<div>\n</body>\n</html>\n";
        print "Content-type: text/html\n\n";
        print $text;
        exit;
}
sub build_tree{
             my $name= $File::Find::name;
             return if $name eq $home or !-d $name or $name=~/\.thumb/;
             $name=~s/\Q$home\E//g;
             $name=~s/^\///g;
             if ($name!~m/\//){push @{$Tree->{''}}, {id=>$name,Title=>$name};}
              else{
                      $name=~m/(.*)\/([^\/]+)/;
                      push @{$Tree->{$1}},{id=>$1."/".$2, Title=>$2};
              }
}

sub treeline{
        my $cat_id = shift;
        my $Tree = shift;
        return unless $cat_id;
        my $content = '';
        for my $subcat (@{$Tree->{$cat_id}}){
           my $tmp = treeline($subcat->{id}, $Tree);
           my $coll = $tmp? "c":"l";
           $content .= qq~<img src='$htmlDataFolder/$coll.gif'><span class="fld" id="A$subcat->{id}">$subcat->{Title}</span><br>~;
           $content .= $tmp ? "<div>\n$tmp</div>":"";
       }
       return $content;
    }


sub is_notes{
        open (F, "$notesFile");
        my @notes = <F>;
        close F;
        my $note = {};
        for (@notes){
                $_=~s/\n|\r//g;
                my ($file, @tmp) = split('##', $_);
                push @{$note->{$file}}, \@tmp;
        }
        return $note;
}


sub note_list{
        open (F, "$notesFile");
        my @notes = <F>;
        close F;
        my $note = {};
        for (@notes){
                $_=~s/\n|\r//g;
                my ($file, @tmp) = split('##', $_);
                $tmp[2]=~s/['"]//g;
                $tmp[1]=~s/['"]//g;
                $note->{$file}.="<b>$tmp[0]</b> ($tmp[1])<br>$tmp[2]<br>";
        }
        return $note;
}

sub update_notes{
        my $name=shift;
        my $new_name=shift;
        $name=~s!/+!/!g;
        $new_name=~s!/+!/!g;

        open (F, "+<$notesFile") or die "Can't open file $notesFile $!";
        flock (F, LOCK_EX);
        my @notes = <F>;
        for(@notes){
                my (@tmp) = split('##', $_);
                if ($tmp[0] eq $name){
                        $tmp[0] = $new_name;
                        $_ = join "##", @tmp;
                }
        }
        seek (F,0,0);
        print F join "", @notes;
        truncate F, tell F;
        close F;
}

sub add_note{
        (my $file = shift)=~s/\/+/\//g;
        my $note = shift;

        open (F, ">>$notesFile") or die "Can't open notes file";
        $note=~s/\r//g;
        $note=~s/\n/<br>/g;
        $note=~s/##+/#/g;
        my $date = localtime;
        print F "$file##$COOKIES{login}##$date##$note\n";
        close F;
}


sub notes{
        error_right('l') unless $Rights->{'l'};
        my $fileN =$home."/".$FORM{file};
        $fileN=~s/\/\/+/\//g;
        if($FORM{del} || $FORM{edit}){
                open (F, "+<$notesFile");
                flock (F, LOCK_EX);
                my @notes = <F>;

                my $notes; my $id =0;
                my $x;
                for (@notes){
                        #$_=~s/\n|\r//g;
                        my ($file, $user, $time, $note) = split('##', $_);

                        if ($file eq $fileN){
                                $id++;
                                if ($id eq $FORM{edit}){
                                        $FORM{note}=~s/\r//g;
                                        $FORM{note}=~s/\n/<br>/g;
                                        $FORM{note}=~s/##+/#/g;
                                        $_=  "$file##$user##$time##$FORM{note}\n";
                                        last;
                                }
                                elsif ($id eq $FORM{del}) {$notes[$x]=undef; last;}
                        }
                        $x++;
                }
                seek (F,0,0);
                print F join "", @notes;
                truncate F, tell F;
                close F;

                print "Location: $script?action=notes&file=$FORM{file}\n\n";
                exit;
        }
        open (F, "$notesFile");
        my @notes = <F>;
        close F;
        my $notes; my $id =0;
        for (@notes){
                my ($file, $user, $time, $note) = split('##', $_);
                if ($file eq $fileN){
                        $id++;
                        $notes.="<b>$user</b> $time".($user eq $COOKIES{login}? " <a href=\"#editnote\" onclick=\"set_edit('$id')\"class=Menucss><b>$Message{edit}</b></a> <a href=\"$script?action=notes&amp;file=$FORM{file}&amp;del=$id\"  onclick=\"return confirm('$Message{sure_del_note}')\" class=Menucss><b>$Message{delete}</b></a>":'')."<br><div id=\"edit_$id\" >$note</div><hr align=\"center\" size=\"1\">\n";

                }

        }
        if($FORM{Submit} && !$FORM{edit}){
                unless ($needsave){push @notes, $FORM{file}."##".$FORM{note}."\n";}
                open (F, ">>$notesFile") or die "Can't open notes file";
                $FORM{note}=~s/\r//g;
                $FORM{note}=~s/\n/<br>/g;
                $FORM{note}=~s/##+/#/g;
                my $date = localtime;
                print F "$fileN##$COOKIES{login}##$date##$FORM{note}\n";
                close F;
                $id++;
                $notes.="<b>$COOKIES{login}</b> $date <a href=\"#editnote\" onclick=\"set_edit('$id')\"class=Menucss><b>$Message{edit}</b></a> <a href=\"$script?action=notes&amp;file=$FORM{file}&amp;del=$id\" onclick=\"return confirm('$Message{sure_del_note}')\"class=Menucss><b>$Message{delete}</b></a><br><div  id=\"edit_$id\" >$FORM{note}</div><hr align=\"center\" size=\"1\">\n";
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|Note added to '$FORM{file}'|\n" if $LogActivity;
        close(LOG);

        }


        #$note=~s/<br>/\n/gs;
        my $text = qq~<h3>/$FORM{file}</h3>
        $notes
        <br><br>
        <script type="text/javascript">
                function set_edit(id){
                        document.getElementById('edit').value=id;
                        var note = document.getElementById('edit_'+id).innerHTML;
                        myRe = /<br>/ig;
                        document.getElementById('note').value = note.replace(myRe,"\\n");
                }
        </script>
        <a name="editnote" />
        <form>
        <input type="hidden" name="file" value="$FORM{file}">
        <input type="hidden" name="edit" id="edit" value="">
        <textarea name="note" id="note" style="width:100%; height:120" onKeyUp="this.form.Submit.disabled=(this.value.length>0)?false:true;"></textarea>
        <div style="text-align: right"><input type="submit" name="Submit" value=" $Message{save} " onclick="opener.parent.location.reload();" disabled>
        <input type="button" value="$Message{cancel}" onclick="window.close();">
        </form>
        </div>~;
        html($text,0, "notes", $FORM{dir},"$FORM{file} :: $Message{notes}");
        exit;

}


sub wanted {
        my $name = $File::Find::name;
        $name=~s!^.*[/\\]!!;
        if (-d "$home/$File::Find::name"){
                ($path=$File::Find::name)=~s/$File::Find::dir//;
                $path = "$fileName$path";
                mkpath("$home/$FORM{cmd}$path", 0, 0755) unless -d "$home/$FORM{cmd}$path";
        }
        else{copy("$home/$File::Find::name", "$home/$FORM{cmd}$path/$name");}
                update_notes("$home/$File::Find::name","$home/$FORM{cmd}$path/$name");
}



sub mkdir{
        error_right(n) unless $Rights->{n};
        if($FORM{cmd}){
                mkdir "$home/$dir/$FORM{cmd}",0755 or error("$Message{err_create_new_dir} $!");
                if ($fileDescriptionOn && $FORM{fileDescription}){
                        add_note("$home/$dir/$FORM{cmd}",$FORM{fileDescription});
                }
                html(1,1);
        }
        my $fileDesc=qq~


<script type="text/javascript">
<!--


function chkFrm(){
var badChar = "\*|\?|\?|\<|\+|\&|\'|\$|\?|\%|\(|\)|\!|\>|\||\;|\@|\#|\~|\{|\}";
var doc = document['wndForm']['cmd'];

for (j=0;j<badChar.length;j++){
var illChar = badChar.charAt(j);
if (doc.value.indexOf(illChar,0) !=-1){
alert ("A Folder Name cannot contain any of the following illegal characters:\\n  * ? ? <> | & ! ; @ # \~ { } $ ! ? % ( )");
doc.value = doc.value.slice(illChar,-1);
}
}
}

//-->
</script>


<tr><td>$Message{description}: <input type=text name=fileDescription size="20" style="width:180pt" maxlength="32"><td></tr>
~ if $fileDescriptionOn;
        my $text = qq~<table width=100%><tr><td><input name=cmd size=50 onkeydown="javascript:chkFrm();" onkeyup="javascript:chkFrm();" /></td></tr>$fileDesc<tr><td align=right><input type=submit value="$Message{ok}"  class=button> <input type=button value=$Message{cancel} onclick="window.close()" class=button></table>~;
        html($text,0, "mkdir", $dir,"$Message{new_dir}");
}
sub download{
        error_right(r) unless $Rights->{r};
        (my $filename = $FORM{file}) =~s!^.*[/\\]!!;
        $FORM{file}=~m/\.([^\.]+)\Z/;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|File '$filename' downloaded|\n" if $LogActivity;
        close(LOG);

$FORM{RegisteredOwner}= $RegisteredOwner;
$FORM{user}= $COOKIES{login};
$FORM{files}= "$filename<br>";
$message = get_record(\%FORM, join '', read_file($msg_body_file_download));
if($sendConfirmDownload){

male($userEmail, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if $myAdmin;
male($toAdmin, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if !$myAdmin;
male($toAdmin, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if $myAdmin;
}


        error("$Message{err_downl_disabled}!") if $disabledFiles{lc $1};
        chdir $home;
        open(F, "$FORM{file}") or error($Message{err_open_file});
        print "Content-type: multipart/form-data;\n";
        print "Content-length: " .( -s $FORM{file} ). "\n";
        print "Content-Disposition: attachment;";
        print qq~filename="$filename"~;
        print "\n\n";
        binmode F;
        binmode STDOUT;
        while(<F>){print;}
        close F;
        exit;
}


sub view{
error_right('r') unless $Rights->{'r'};
        (my $filename = $FORM{file}) =~s!^.*[/\\]!!;
        $FORM{file}=~m/\.([^\.]+)\Z/;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|File '$filename' previewed|\n" if $LogActivity;
        close(LOG);
        error("Can't browse disabled file types!") if $disabledFiles{lc $1};
        if($filename=~m/\.acgi\Z|\.htm\Z|\.html\Z|\.htmls\Z|\.htx\Z|\.shtml\Z/i){
                print "Content-Type: text/html\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.bmp\Z|\.bmp\Z/i){
                print "Content-Type: image/bmp\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.jpe\Z|\.jfif\Z|\.jfif-tbnl\Z|\.jpeg\Z|\.jpg\Z/i){
                print "Content-Type: image/jpeg\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.qif\Z|\.qti\Z|\.qtif\Z/i){
                print "Content-disposition: attachment; filename=$filename\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.tif\Z/i){
                print "Content-disposition: attachment; filename=$filename\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.tiff\Z/i){
                print "Content-Type: image/tiff\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.png\Z|\.x-png\Z/i){
                print "Content-Type: image/png\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.ico\Z/i){
                print "Content-Type: image/x-icon\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.gif\Z/i){
                print "Content-Type: image/gif\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.ief\Z|\.iefs\Z/i){
                print "Content-Type: image/ief\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pbm\Z/i){
                print "Content-Type: image/x-portable-bitmap\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pgm\Z/i){
                print "Content-Type: image/x-portable-graymap\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.ras\Z|\.rast\Z/i){
                print "Content-Type: image/cmu-raster\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pict\Z|\.pic\Z/i){
                print "Content-Type: image/pict\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.dwg\Z|\.dxf\Z/i){
                print "Content-Type: image/pict\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.dxf\Z|\.dwg\Z/i){
                print "Content-Type: image/vnd.dwg\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.aif\Z|\.aifc\Z|\.aiff\Z/i){
                print "Content-Type: audio/x-aiff\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.aif\Z|\.aifc\Z|\.aiff\Z/i){
                print "Content-Type: audio/x-aiff\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.m2a\Z|\.mp2\Z|\.mpa\Z|\.wmv\Z|\.mpg\Z|\.mpga\Z/i){
                print "Content-Type: audio/mpeg\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.mp3\Z/i){
                print "Content-Type: audio/mpeg\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.kar\Z|\.mid\Z|\.midi\Z/i){
                print "Content-Type: audio/midi\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.wav\Z/i){
                print "Content-Type: audio/x-wav\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.ra\Z|\.ram\Z|\.rm\Z|\.rmm\Z|\.rmp\Z/i){
                print "Content-Type: audio/x-pn-realaudio\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.au\Z/i){
                print "Content-Type: audio/basic\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.lma\Z|\.la\Z/i){
                print "Content-Type: audio/x-nspaudio\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.avi\Z/i){
                print "Content-Type: video/x-msvideo\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.moov\Z|\.mov\Z/i){
                print "Content-Type: video/quicktime\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.m1v\Z|\.m2v\Z|\.mp2\Z|\.mpe\Z|\.mpeg\Z|\.mpg\Z|.mpa\Z/i){
                print "Content-Type: video/mpeg\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.asf\Z|\.asx\Z/i){
                print "Content-Type: video/x-ms-asf\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.css\Z/i){
                print "Content-Type: text/css\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.asp\Z/i){
                print "Content-Type: text/asp\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pm\Z/i){
                print "Content-Type: x-script.perl-module\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.py\Z/i){
                print "Content-Type: text/x-script.phyton\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.rtf\Z|\.rtx\Z/i){
                print "Content-Type: application/x-rtf\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pot\Z|\.ppa\Z|\.pps\Z|\.ppt\Z|\.pwz\Z/i){
                print "Content-disposition: attachment; filename=$filename\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.exe\Z/i){
                print "Content-disposition: attachment; filename=$filename\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.doc\Z|\.dot\Z|\.w6w\Z|\.wiz\Z|\.word\Z/i){
                print "Content-Type: application/msword\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.wpd\Z|\.wp\Z/i){
                print "Content-Type: application/wordperfect\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.pdf\Z/i){
                print "Content-Type: application/pdf\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.xls\Z|\.xlc\Z|\.xll\Z|\.xlm\Z|\.xlb\.xlw\Z/i){
                print "Content-Type: application/vnd.ms-excel\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.ai\Z|\.eps\Z|\.ps\Z/i){
                print "Content-Type: application/postscript\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.exe\Z/i){
                print "Content-Type: application/octet-stream\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.class\Z/i){
                print "Content-Type: application/x-java-class\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.mime\Z/i){
                print "Content-Type: www/mime\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.swf\Z/i){
                print "Content-Type: application/x-shockwave-flash\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.vsd\Z|\.vst\Z|\.vsw \Z/i){
                print "Content-Type: application/x-visio\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.zip\Z/i){
                print "Content-disposition: attachment; filename=$filename\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.xml\Z/i){
                print "Content-Type: application/xml\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.tgz\Z/i){
                print "Content-Type: application/x-compressed\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.tar\Z/i){
                print "Content-Type: application/x-tar\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.wmf\Z/i){
                print "Content-Type: windows/metafile\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.help\Z/i){
                print "Content-Type: application/x-helpfile\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.help\Z/i){
                print "Content-Type: application/x-gzip\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.gz\Z/i){
                print "Content-Type: application/x-compressed\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }
        if($filename=~m/\.gtar\Z/i){
                print "Content-Type: application/x-gtar\n\n";
                open(F, "$home/$FORM{file}") or error($Message{err_open_file});
                binmode F;
                binmode STDOUT;
                while(<F>){print;}
                close F;
                exit;
        }


        print "Content-Type: text/html$charset\n\n";
        print "\n\n";
        print "<html>\n<head>\n<title>$Message{preview}: $FORM{file}</title>\n</head>\n<body topmargin=0 leftmargin=0><form onsubmit='return false'>
                <textarea readonly rows=25 cols=50 style=\"width:100%;height: 99%;\">";
        open(F, "$home/$FORM{file}") or error($Message{err_open_file});
        while(<F>){print;}
        close F;
        print "</textarea></form>\n</body>\n</html>";
        exit;
}


sub edit{
        error_right('w') unless $Rights->{'w'};
        $FORM{file}=~m/\.([^\.]+)\Z/;
        error("Can't edit disabled file types!") if $disabledFiles{lc $1};
        if($FORM{submitSave} or $FORM{closeSave} or $FORM{closeExit}){
                $FORM{content}=~s/\r//gs;
                open (F, ">$home/$FORM{file}") or error($Message{err_open_file});
                print F $FORM{content};
                close F;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|'$FORM{file}' edited|\n" if $LogActivity;
        close(LOG);
        }
        print "Content-Type: text/html$charset\n\n";
        print qq~<html><head><title>$FORM{file}</title>
                <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">\n~;
        if ($FORM{closeSave} or $FORM{closeExit}){
                print qq~<script>
                function go(){
                opener.parent.focus();
                window.close();
                }
                </script>
                ~;
         }
         else{
                print qq~<script>
                var isClose = 0;
                function closeWnd(){
                        if (isClose){
                                if (confirm("$Message{save_changes}")){
                                        document.myform.closeExit.value="1";
                                        document.myform.submit();
                                        isClose=null;
                                }
                                else{isClose=null; window.close();}
                        }
                        else{isClose=null; window.close();}
                }
                </script>
                ~;
         }
        print qq~<script language="JavaScript" type="text/javascript" src="$editorSrc"></script>\n~ if $useWysiwig;
        print qq~</head><body ~;
        print qq~ onload="go()"~ if $FORM{closeSave} or $FORM{closeExit};

        print qq~   background="$fileTypeImgDir/toolsLine.png"~ unless $useWysiwig;
        print qq~ topmargin=0 leftmargin=0>
                <form action=$script method=post name="myform">
                <input type=hidden name=action value="edit">
                <input type=hidden name=closeExit>
                <input type=hidden name=file value="$FORM{file}">
                <textarea id='content1' name=content rows=25 cols=50 style=width:100% onchange="javascript:isClose=1">~;
        open(F, "$home/$FORM{file}") or error($Message{err_open_file});
        while(<F>){$_=~s!<!&#60;!g; $_=~s!>!&#62;!g; print;}
        close F;
        print qq~</textarea><p align=center><input type=reset> <input type=submit name=submitSave value="$Message{save}" onclick="javascript:isClose=0"> <input type=submit name=closeSave value="$Message{save_close}"  onclick="javascript:isClose=0"> <input type=button value="$Message{cancel}" onclick="closeWnd()"></p></form>~;
        print qq~<script language="javascript1.2">
        generate_wysiwyg('content1');
        </script>~ if $useWysiwig;

        print qq~</body></html>~;
        exit;
}

sub editenable{
        error_right('w') unless $Rights->{'w'};
        $FORM{file}=~m/\.([^\.]+)\Z/;
        error("Can't edit disabled file types!") if $disabledFiles{lc $1};
        if($FORM{submitSave} or $FORM{closeSave} or $FORM{closeExit}){
                $FORM{content}=~s/\r//gs;
                open (F, ">$home/$FORM{file}") or error($Message{err_open_file});
                print F $FORM{content};
                close F;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|'$FORM{file}' edited|\n" if $LogActivity;
        close(LOG);
        }
        print "Content-Type: text/html$charset\n\n";
        print qq~<html><head><title>$FORM{file}</title><body bgcolor="#F3F3F3">
                <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">\n~;
        if ($FORM{closeSave} or $FORM{closeExit}){
                print qq~<script>
                function go(){
                opener.parent.focus();
                window.close();
                }
                </script>
                ~;
         }
         else{
                print qq~<script>
                var isClose = 0;
                function closeWnd(){
                        if (isClose){
                                if (confirm("$Message{save_changes}")){
                                        document.myform.closeExit.value="1";
                                        document.myform.submit();
                                        isClose=null;
                                }
                                else{isClose=null; window.close();}
                        }
                        else{isClose=null; window.close();}
                }
                </script>
                ~;
         }
        print qq~<script language="JavaScript" type="text/javascript" src="$editorpluginSrc"></script>\n~ if $useWysiwig;
  print qq~<script language="javascript" type="text/javascript">
 tinyMCE.init({
  mode : "textareas",
  theme : "advanced",
  plugins :
"devkit,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,fullpage",
  theme_advanced_buttons1_add_before : "newdocument,separator",
  theme_advanced_buttons1_add : "fontselect,fontsizeselect",
  theme_advanced_buttons2_add : "separator,insertdate,inserttime,preview,separator,forecolor,backcolor",
  theme_advanced_buttons2_add_before: "cut,copy,paste,pastetext,pasteword,separator,search,replace,separator",
  theme_advanced_buttons3_add_before : "tablecontrols,separator",
  theme_advanced_buttons3_add : "emotions,iespell,flash,advhr,separator,print,separator,ltr,rtl,separator,fullpage",
  theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops",
  theme_advanced_toolbar_location : "top",
  theme_advanced_toolbar_align : "left",
  theme_advanced_path_location : "bottom",
  content_css : "/tinymce/examples/example_full.css",
     plugin_insertdate_dateFormat : "%Y-%m-%d",
     plugin_insertdate_timeFormat : "%H:%M:%S",
  extended_valid_elements : "hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
  external_link_list_url : "/tinymce/examples/example_link_list.js",
  external_image_list_url : "/tinymce/examples/example_image_list.js",
  flash_external_list_url : "/tinymce/examples/example_flash_list.js",
  theme_advanced_resize_horizontal : false,
  theme_advanced_resizing : true,
   relative_urls : false,
    remember_last_path : false,
document_base_url : "$hotlinkurl",
nonbreaking_force_tab : true,
apply_source_formatting : true
 });
</script>\n~ if $useWysiwig;
        print qq~</head><body ~;
        print qq~ onload="go()"~ if $FORM{closeSave} or $FORM{closeExit};

        print qq~   background="$fileTypeImgDir/toolsLine.png"~ unless $useWysiwig;
        print qq~ topmargin=0 leftmargin=0>
                <form action=$script method=post name="myform">
                <input type=hidden name=action value="edit">
                <input type=hidden name=closeExit>
                <input type=hidden name=file value="$FORM{file}">
                <textarea id='content1' name=content rows=25 cols=50 style=width:100% onchange="javascript:isClose=1">~;
        open(F, "$home/$FORM{file}") or error($Message{err_open_file});
        while(<F>){$_=~s!<!&#60;!g; $_=~s!>!&#62;!g; print;}
        close F;
        print qq~</textarea><p align=center><input type=reset> <input type=submit name=submitSave value="$Message{save}" onclick="javascript:isClose=0"> <input type=submit name=closeSave value="$Message{save_close}"  onclick="javascript:isClose=0"> <input type=button value="$Message{cancel}" onclick="closeWnd()"></p></form>~;
        print qq~<script language="javascript1.2">
  </script>~ if $useWysiwig;
  print qq~</body></html>~;
        exit;
}



sub userarea{
        my $txt ="";
        if($FORM{pw} eq 'change'){
                my $error ='';
                chomp $FORM{newpw};
                chomp $FORM{newpw2};
                $error .="<li><b class=error>$Message{err_old_pw}</b></li>" if !$FORM{oldpw} ;
                $error .="<li><b class=error>$Message{err_blank_pw}</b></li>" unless $FORM{newpw};
                $error .="<li><b class=error>$Message{err_new_pw}</b></li>" if $FORM{newpw} ne $FORM{newpw2};
                unless ($error){
                        my @data = read_file($userTable);
                        my $headLine=shift @data;
                        foreach(@data){
                                my ($userId, $userLogin, $userPass,$userEmail, $userDir, $discQuota, $disabledFiles, $rights, $disabled)=split('\|', $_);
                                if ($COOKIES{login} eq $userLogin && $userPass eq  crypt($FORM{oldpw},$userPass)){
                                        my $newPass = createPass($FORM{newpw});
                                        $_ = "$userId|$userLogin|$newPass|$userEmail|$userDir|$discQuota|$disabledFiles|$rights|$disabled";
                                        open(F, ">$userTable") or error("Can't open users file");
                                        print F $headLine;
                                        print F join('', @data);
                                        close F;
                                        print "Set-Cookie: USER_Login=login&$COOKIES{login}&pass&$FORM{newpw}&dir&$userDir&language&$COOKIES{language}; path=/\nLocation: $script?action=userarea&msg=pw_changed\n\n";
                                        exit;

                                }

                        }
                }
                $error ="<li><b class=error>$Message{err_old_pw}</b></li>" unless $error;
                $txt = $error."<br><br><center><a href=javascript:history.back()>Back</a>";
        }
        elsif ($FORM{pw} eq 'new'){
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$COOKIES{login}|Changed password|\n" if $LogActivity;
                close(LOG);
                $txt = qq~<form action=$script method=post>
                <input type=hidden name=action value=userarea><input type=hidden name=pw value=change>
                <td class=headline width=100% align=center colspan=2>$Message{change_password}</td></tr>
                <tr>
                <td width=50%>$Message{old_password}:</td>
                <td width=50%><input type=password name=oldpw></td>
                <tr>
                <td>$Message{new_password}:</td>
                <td><input type=password name=newpw></td>
                <tr>
                <td>$Message{retype_password}:</td>
                <td><input type=password name=newpw2></td>
                <tr><td colspan=2 align=right><input type=submit> <input type=button onclick="window.close()" value="$Message{cancel}"></td></tr>
                </form>

                ~;

        }
        elsif($FORM{email} eq 'change'){
                my @data = read_file($userTable);
                my $headLine=shift @data;
                foreach(@data){
                        my ($userId, $userLogin, $userPass,$userEmail, $userDir, $discQuota, $disabledFiles, $rights, $disabled)=split('\|', $_);
                        if ($COOKIES{login} eq $userLogin){
                                $_ = "$userId|$userLogin|$userPass|$FORM{userEmail}|$userDir|$discQuota|$disabledFiles|$rights|$disabled";
                                open(F, ">$userTable") or error("Can't open users file");
                                print F $headLine;
                                print F join('', @data);
                                close F;
                                print "Location: $script?action=userarea&msg=email_changed\n\n";
                                open (LOG, ">>$log") or die $! if $LogActivity;
                                print LOG "$theTime|$COOKIES{login}|Changed email address|\n" if $LogActivity;
                                close(LOG);
                                $message = "Client: $userLogin ID#$userId\nOld Email: $userEmail\nNew email: $FORM{userEmail}\n";
                                male($toAdmin, $fromAdmin, "Client has changed Email", $message) if $sendConfirmChEmail;
                                exit;
                        }
                }
        }
        elsif($FORM{email} eq 'new'){
                $txt = qq~<form action=$script method=post>
                <input type=hidden name=action value=userarea><input type=hidden name=email value=change>
                <td class=headline width=100% align=center colspan=2>$Message{ch_eml}</td></tr>
                <tr>
                <td width=50%>$Message{new_eml}:</td>
                <td width=50%><input type=text name=userEmail></td>
                <tr><td colspan=2 align=right><input type=submit> <input type=button onclick="window.close()" value="$Message{cancel}"></td></tr>
                </form>

                ~;
        }

        else{
                $txt =qq~
        <b>$Message{$FORM{msg}}</b>
        <td class=headline width=100% align=center colspan=2>$Message{client_details}</td></tr>
        <tr>
        <td width=50%>$Message{client_username}:</td>
        <td width=50%>$userLogin</td>
        <tr>
        <td>$Message{client_password}:</td>
        <td>******* &nbsp; <a href=$script?action=userarea&pw=new>$Message{change}</a></td>
        <tr>
        <td>$Message{client_email}:</td>
        <td>$userEmail  &nbsp; <a href=$script?action=userarea&email=new>$Message{change}</a></td>
        <tr>
        <td>$Message{disc_quota}:</td>
        <td>$discQuota Mb.</td>
        <tr>
        <td>$Message{used_spase}:</td>
        <td>$discSizeTxt</td>
        <tr>
        <td>$Message{disabled_files}:</td>
        <td>$disabledFiles</td>
        </tr>
        <tr><td colspan=2 align=right><input type=button onclick="window.close()" value="$Message{cancel}"></td></tr>
        ~;


        }


        print "Content-type: text/html$charset\n\n";
        print qq~
<html>
        <head>
        <title>User Details</title>
        <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
        </head>
        <body bgcolor=#eeeeee>
        <table width=100%>
        $txt
        </table>
</body></html>
        ~;



exit;
}

my @archive =();
sub batch_download{
        error_right('p') unless $Rights->{'p'};
         my $zip = Archive::Zip->new();
$FORM{RegisteredOwner}= $RegisteredOwner;
$FORM{user}= $COOKIES{login};
$FORM{files}= "$FORM{'zipname'}.zip<br>";
$message = get_record(\%FORM, join '', read_file($msg_body_file_download));
if($sendConfirmDownload){
male($userEmail, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if $myAdmin;
male($toAdmin, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if !$myAdmin;
male($toAdmin, $fromAdmin, "$FORM{user} has downloaded the following file(s):", $message) if $myAdmin;
}
chdir $home."/".$dir;

         $FORM{'zipname'} .=".zip" if $FORM{'zipname'}!~m/\.zip$/i;
        for(param('file')){
                $_=~m/\.([^\.])+\Z/;
                next if $disabledFiles{lc $1};
                $_=~s/\/$//;
                $_=~s/.*\///g;
                if (-d "$home/$dir/$_"){
                        find(\&ops, "$home/$dir/$_");
                        for (@archive){
                                (my $name=$_)=~s/$home//;
                                $name=~s/$dir//;
                                if(-d $_){$zip->addDirectory( "$_", $name );}
                                else{$zip->addFile( "$_",$name );}
                        }
                }
                else{my $member = $zip->addFile( "$_" );}
        }
        print STDOUT "Content-type: application/zip\n";
        print STDOUT "Content-Disposition: inline; filename=\"$FORM{'zipname'}\"\n";
        print STDOUT "\n";
        binmode STDOUT;
        $zip->writeToFileHandle( STDOUT, 0 );
        exit;
}

sub ops{
        my $name=$File::Find::name;
        return if $name=~m/\/\./;
        push @archive,$name;
}


sub findfile{
        print "Content-type: text/html$charset\n\n";
        print qq~

<html>
<head><head><title>$Message{search}</title>
<link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
<script type="text/javascript">
        function _Search(){
        opener.document.mode.search.value=document.mode.search.value;
        if (document.mode.matchCase.checked) opener.document.mode.matchCase.checked=true;
        else opener.document.mode.matchCase.checked=false;

        if (document.mode.inNotes.checked) opener.document.mode.inNotes.checked=true;
        else opener.document.mode.inNotes.checked=false;

        opener.document.mode.dir.value = "";
        opener.document.mode.submit();
        window.close();
        return false;
        }
</script>
</head>

<body bgcolor="#F3F3F3" topmargin=0 leftmargin=0>
<br><center>
<form name=mode onsubmit="return _Search()">
<p><b>$Message{search}:
<input type=text name=search size=20 value="$FORM{search}">
<input type=submit value=go> <br>
<input type=checkbox name=matchCase value=1 matchCase> $Message{match_case}
<input type=checkbox name=inNotes value=1 ~. ($FORM{inNotes}? 'checked':'') .qq~> $Message{notes}
</b></p>
~;
exit;
}

sub about{
print "Content-type: text/html;\n\n";

print qq~

<HTML>
<head>
<title>About File Manager</title>
<meta http-equiv="imagetoolbar" content="false">
<style type="text/css">
.fsx01 {font-size: 11px;}
.txdec {text-decoration: none;}
.dfltt {font-family:Times New Roman;font-size:14px;font-weight:normal;text-decoration:none;text-align:left;}
body {margin:0;height:100%;width:100%;}
</style>
</head>
<body bgcolor="#ffffff" alink="#ff0000" link="#0000ff" vlink="#800080" >
<div id="Oobj18" style="position:absolute;z-index:1;visibility:visible; left:1px;top:0px;width:384px;height:321px;font-size:1px;">
<img name="Ggeo30" Align=Top SRC="$htmlDataFolder/aboutfilemanager.png" alt="" border=0 width="384" height="321"></div>

<div id="Oobj29" style="position:absolute;z-index:2;visibility:visible; left:212px;top:178px;width:170px;height:18px;">
<div id="Grtf29" class="dfltt">
<font face="Arial" class="fsx01" color="#808080"><B>$RegisteredOwner<br>
</B></font></div>
</div>
<div id="Oobj31" style="position:absolute;z-index:3;visibility:visible; left:304px;top:80px;width:64px;height:19px;">
<div id="Grtf31" class="dfltt">
<font face="Arial" class="fsx01" color="#727272"><B>$Version<br></B></font></div>
</div>
</body>
</html>
~;

open (LOG, ">>$log") or die $! if $LogActivity;
print LOG "$theTime|$COOKIES{login}|About window openend|\n" if $LogActivity;
close(LOG);
exit;
}

sub upload2{
        if (!$myAdmin && $ENV{CONTENT_LENGTH} /(1024*1024)>$discQuota){error ("Cannot Upload Files - You Have Exceeded Your Quota");}
        print "Content-type: text/html;\n\n";
        $FORM{dir} =~ s/\.\.\///g;
        my $dir = $FORM{dir};
        $content=1;
        $j_script = "<script>
                function go(){
                opener.parent.location.reload();
                window.close();
                }
        </script>";


        my $s =0;
        my @fDesc = param('fileDescription') if $fileDescriptionOn;
        #protect html
        for (@fDesc){
                   $_ =~ s/<!--(.|\n)*-->//g;
                   $_ =~ s/<([^>]|\n)*>//g;
        }


        my ($descriptionString,$uploadInfo);
        my $ind=0;
       for(param('file')){
          error("A File Name $_ or Description cannot contain any of the following illegal characters:  *  ? ? <> | ; @ # ~ { }", 2)
          if $_=~m/[\*\?\|\;;\{\}<>\@\#~\?]/;
       }
        my $time = localtime;
        for(param('file')){
                $_=~m/\.([^\.]+)\Z/;
                next if $disabledFiles{lc $1};
                my $tmp;
                $s+=save_file($_, "$dir", $FORM{mode}) if $_;
                #create description string
                ($tmp=$_) =~s!^.*[/\\]!!;
                (my $file = "$home/$dir/$tmp")=~s/\/+/\//g;
                $fDesc[$ind]=~s/##+/#/g;
                $descriptionString.="$file##$COOKIES{login}##$time##$fDesc[$ind]\n" if $_ && $fDesc[$ind];
                $uploadInfo .= "$dir/$tmp &nbsp;&nbsp;&nbsp;&nbsp;$fDesc[$ind]<br>" if $_;
                $uploadfilelog .= "$tmp" if $_;
                $uploaddirlog .= "$dir/" if $_;
                $ind++;
        }
        if($ind && $sendConfirmUpload){
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$COOKIES{login}|File '$uploadfilelog' uploaded to '$uploaddirlog'|\n" if $LogActivity;
                close(LOG);
                if($send_as_html){
                      my %FORM;
                      $FORM{RegisteredOwner}= $RegisteredOwner;
                      $FORM{user}= $COOKIES{login};
                      $FORM{files}= $uploadInfo;
                      $message = get_record(\%FORM, join '',read_file($msg_body_file));
                }
                else{$message=$descriptionString}
                male($toAdmin, $fromAdmin, "$COOKIES{login} $subjecttitle", $message);
        }



        if ($fileDescriptionOn){
                open (DESC, ">>$notesFile") or error($Message{err_open_desc}." $!");
                print DESC $descriptionString;
                close DESC;
        }

        if(%disabledFiles){
                $bannedFile = "bannedFile =new Array(";
                for(keys %disabledFiles){$bannedFile.="\"$_\","}
                chop $bannedFile;
                $bannedFile .= ");";
        }

        print qq~<html><head><title>$Message{upload_file_to} $home/$dir</title>
        <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
                    <style>
                    td, th {font-family: Verdana, Arial; font-size:8pt}
                    input,select {font-family: Verdana, Arial; font-size:8pt}
                .titel  {font-family: Verdana, Arial; font-size:10pt; font-weight:bolder; color: #999999}
                .of {border-style:solid; border-width: 1; border-color : #7c96af; background-color:#dddddd; font-size:8pt}
                .off {border-style:none;background-color:#f3f3f3}
                .error {color: #ff0000; text-align: center;  font-size:12pt;}
        </style>~;
my $regExp = '\*|\?|\?|\<|\+|\&|\'|\$|\?|\%|\!|\>|\||\;|\@|\#|\~|\{|\}';
        print qq~<script>
                $bannedFile
                function checkFile(fileform){
         ~;
        print qq~
                        for(var a=0; a<bannedFile.length; a++){
                                if(fileform.value.indexOf("."+bannedFile[a])>=0) {
                                        alert("$Message{err_banned_format}");
                                        fileform.focus();
                                        return;
                                }
                        }
                        ~  if !$myAdmin && $bannedFile;
        print qq~       var re5digit=/$regExp/; //regular expression
                        if (re5digit.test(fileform.value)){
                                alert ("A File Name cannot contain any of the following illegal characters:\\n * ? ? < +  ! & ' > ; ! ? % @ # { }");
                                fileform.focus();
                                                                document.forms[0].reset();
                                                                return;
                        }
                }
        </script> ~ ;
        my $onchange=qq~ onchange="checkFile(this)"~;
        print qq~</head>
        <body bgcolor=#eeeeee~;

        if($s){        my $text ="$s file";
                $text ="s" if $s>1;
                $text =" saved in $dir\n$j_script";

                print " onload=go()>",$text;
        print "</body></html>";
        exit;
        }
        my $fileDesc=qq~<tr><td>$Message{description}:</td><td><input type=text name=fileDescription size="34" style="width:250pt" maxlength="32"><td></tr>~ if $fileDescriptionOn;
        print qq~>
<div style="position:absolute;z-index:1;visibility:visible; left:0px;top:0px;width:443px;height:41px;">
<img Align=Top src="$htmlDataFolder/tabbg.png" border="0" width="443px"  height="41px"></div>
<div id="navigation" style="position:absolute;z-index:2;visibility:visible; left:14px;top:15px;width:300px;height:154px;">
<ul>
<li><a href="$script?action=upload&amp;dir=$dir"><span>$Message{upload}</span></a></li>
<li><a href="$script?action=uploadfl&amp;dir=$dir"><span>Flash $Message{upload}</span></a></li>
</ul>
</div>
<div id="loadI" name="loadI" style="position:absolute;z-index:4;; top:176; left:100; display:none;">$loadImg</div>
                <script>
                        function load(){document.all.loadI.style.display="";}
                </script>
<div style="position:absolute;z-index:3;visibility:visible; left:10px;top:32px;width:403px;height:41px;">
                <form method=post action=$script  ENCTYPE=\"multipart/form-data\" onsubmit="load();">
                <input type=hidden name=mode value=$FORM{mode}>
                <input type=hidden name=action value=upload>
                <input type=hidden name=dir value="$dir">
                <table>
                                <tr><td>&nbsp;<td></tr>
                                <tr><td>&nbsp;<td></tr>
                                <tr><td>&nbsp;<td></tr>
                                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td colspan=2 align=center><input type=submit value="$Message{upload_files}"> <input type=reset onclick=window.close() value=$Message{cancel}>
</td></tr></table></form></div>~;

        print "</body></html>";
        exit;
}


sub upload{
        error_right('u') unless $Rights->{'u'};
        print "Content-type: text/html$charset\n\n";
        my $session=$FORM{session};
        my $dir = $FORM{dir};

        if ($FORM{session}){
                ###############################################################################
                ###Status Bar
                use Fcntl qw(:DEFAULT :flock);

                my ($bufferSize, $buffer, $bytesRead) = (1024*8,0,0);
                my $tmpDir = "./status";
                mkdir "$tmpDir",0755  unless -d $tmpDir or die "Can't create tmp folder $tmpDir $!!";
                my $startTime=time;
                ###################
                unless (-f "$tmpDir/$FORM{session}"){
                        open (ST , ">$tmpDir/$FORM{session}") or error("Can't open status file $!");
                        flock(ST, LOCK_EX);
                        print ST "$ENV{'CONTENT_LENGTH'} 0 $startTime\n";
                        close ST;
                }
                ##################
                #create template file for content
                open (TMP , ">$tmpDir/$FORM{session}.tmp") or error("Can't open tmp session file $!", '1', $session);
                binmode TMP;
                flock(TMP, LOCK_EX);
                while (read(STDIN,$buffer,$bufferSize) && $bRead < $ENV{'CONTENT_LENGTH'}){
                        $bytesRead+=length $buffer;
                        print TMP $buffer;

                        ############################
                        $proz = int($bytesRead/$ENV{'CONTENT_LENGTH'} *100);
                        $proz = 99 if $proz>=100;
                        open (ST , ">$tmpDir/$FORM{session}");
                        flock(ST, LOCK_EX);
                        print ST "$ENV{'CONTENT_LENGTH'} $proz $startTime\n";
                        close ST;
                        ############################
                        select(undef, undef, undef, 0.03);
                }
                close TMP;

                #upload finished
                        open (ST , ">$tmpDir/$FORM{session}");
                        flock(ST, LOCK_EX);
                        print ST "$ENV{'CONTENT_LENGTH'} 100 $startTime\n";
                        close ST;
                open(STDIN,"$tmpDir/$FORM{session}.tmp") or error("can't open temp file $FORM{session}.tmp $!", '1', $session);
                ################################################################################
                @params=param;
                for(@params){$FORM{$_}=join ",", param($_);}
                #protect from access over main root folder
                $FORM{dir} =~ s/\.\.\///g;
                $dir = $FORM{dir};
                ####
                $content = 1;

                my $s =0;
                my @fDesc = param('fileDescription') if $fileDescriptionOn;
                #protect html
                for (@fDesc){
                           $_ =~ s/<!--(.|\n)*-->//g;
                           $_ =~ s/<([^>]|\n)*>//g;
                }

                my $descriptionString;
                my $ind=0;

                for(param('file')){
                        error("A File Name $_ or Description cannot contain any of the following illegal characters:  *  ? ? <> | ; @ # ~ { }", 2)
                        if $_=~m/[\*\?\|\;;\{\}<>\@\#~\?]/;
                }
                my $time=localtime;
                my $uploadInfo = '';
                my @uplError;
                for(param('file')){
                        next unless $_;
                        $_=~m/\.([^\.]+)\Z/;
                        next if $disabledFiles{lc $1};
                        my $tmp;
                        (my $filename = $_) =~s!^.*[/\\]!!;

                        if (!$FORM{overwrite} && -e "$home/$dir/$filename"){
                                push @uplError, "$Message{uploadfail}! \\n$filename $Message{already_exists}!";
                                next;
                        }

                        my $tt=save_file($_, "$dir", $FORM{mode}) if $_;
                        $s+=$tt;
                        #create description string
                        ($tmp=$_) =~s!^.*[/\\]!!;
                        (my $file = "$home/$dir/$tmp")=~s/\/+/\//g;
                        $fDesc[$ind]=~s/##+/#/g;
                        $descriptionString.="$file##$COOKIES{login}##$time##$fDesc[$ind]\n" if $_ && $fDesc[$ind];
                        $uploadInfo .= "$dir/$tmp &nbsp;&nbsp;&nbsp;&nbsp;$fDesc[$ind]<br>" if $_;
                        $uploadfilelog .= "$tmp" if $_;
                        $uploaddirlog .= "$dir/" if $_;
                        $ind++;
                }
                if($ind && $sendConfirmUpload){
                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$COOKIES{login}|File '$uploadfilelog' uploaded to '$uploaddirlog'|\n" if $LogActivity;
                close(LOG);
                        if($send_as_html){
                                 my %FORM;
                                $FORM{RegisteredOwner}= $RegisteredOwner;
                                $FORM{user}= $COOKIES{login};
                                $FORM{files}= $uploadInfo;
                                $message = get_record(\%FORM, join '',read_file($msg_body_file));
                        }
                        else{$message=$descriptionString}
                        male($toAdmin, $fromAdmin, "$COOKIES{login} $subjecttitle", $message);
                }
                close STDIN;
                unlink "$tmpDir/$FORM{session}.tmp" or die $!;
                if ($fileDescriptionOn){
                        open (DESC, ">>$notesFile") or error($Message{err_open_desc}, 2);
                        print DESC $descriptionString;
                        close DESC;
                }

                my $err;
        if (@uplError){
                $err= "alert('".(join("\n",@uplError))."');";

        }

        print qq~
                <html><body onload=\"$err parent.CloseUpload($FORM{session});\">
                <b>Upload Proceess finished!</b>
                </body></html>
        ~;


        unlink "$tmpDir/$FORM{session}.tmp";
        #unlink "$tmpDir/$FORM{session}";
        exit;
        }
                if(%disabledFiles){
                        $bannedFile = "bannedFile =new Array(";
                        for(keys %disabledFiles){$bannedFile.="\"$_\","}
                        chop $bannedFile;
                        $bannedFile .= ");";
                }

        print qq~<html><head><title>$Message{upload_file_to} $home/$dir</title>
                    <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">\n~;
        print qq~
        <script>
                $bannedFile
                function checkFile(fileform){
                        for(var a=0; a<bannedFile.length; a++){
                                if(fileform.value.indexOf("."+bannedFile[a])>=0) {
                                        alert("$Message{err_banned_format}");
                                        fileform.focus();
                                        return;
                                }
                        }

                }
        </script> ~ if !$myAdmin && $bannedFile;

my $regExp = '\*|\?|\?|\<|\+|\&|\'|\$|\?|\%|\!|\>|\||\;|\@|\#|\~|\{|\}';


        print <<EOF;

<script language ="Javascript">
        var maxGet = 200;
        function loadHTML(sURL)
        {
          if (!maxGet) return;
          var request=null;
          // MSXML 2
          if(!request) try {
                request=new ActiveXObject('Msxml2.XMLHTTP');
          } catch (e){}

          // MSXML 1
          if(!request) try {
                request=new ActiveXObject('Microsoft.XMLHTTP');
          } catch (e){}

          // Mozilla
          if(!request) try {
                request=new XMLHttpRequest();
          } catch (e){}

          if(!request)
                // can't create request
                return "";

          // request
          request.open('GET', sURL, false);
          request.send(null);
          return request.responseText;
        }
        var Status = parseInt(100000000000000000*Math.random())+"";
        function startUp()
        {
                //check filenames

                var re5digit=/$regExp/; //regular expression
                for (i=0; i<document.myform.file.length; i++){
                        if (re5digit.test(document.myform.file[i].value)){
                                alert ("A File Name cannot contain any of the following illegal characters:\\n * ? ? < + & ' > ; ! ? % @ # ~ { } $ !");
                                document.myform.file[i].focus();
                                                                document.forms[0].reset();
                                return;
                        }
                }

                document.myform.btnSubmit.disabled='true';
                document.myform.action= document.myform.action+"&session="+Status ;
                document.getElementById('statusWnd').style.display="block";
                window.setTimeout("test2()", 400);
                return true;
        }
        function test()
        {
                window.setTimeout("test2()", 400);
        }

        function CloseUpload(Status){
               var content = loadHTML("status.pl?type=clear&session="+Status);
               opener.parent.location.reload();
               javascript:top.window.close();


        }
        ResponseData = new Array;
        StatusData = new Array;
        function test2(){
                var content = loadHTML("status.pl?session="+Status);
                if (content) ResponseData = content.split("\\n");
           //alert(content);
                if(1*ResponseData[0]!=1*Status)
                {
                        document.getElementById('statusInfo').innerHTML=ResponseData[0]+"--<B>Status Bar Unable To Detect Server Response!</B>";
                        return;
                }
                StatusData = ResponseData[1].split(" ");
                if(!StatusData[1])
                {
                        while(maxGet)
                        {
                                maxGet--;
                                // document.getElementById('statusInfo').innerHTML=maxGet;
                                test();
                                return;
                        }
                }
                if(maxGet<=0)
                {
                        document.getElementById('statusInfo').innerHTML="<B>Status Bar Unable To Detect Server Response!</B>";
                        return;
                }
                var e =document.getElementById('statusBar');
                e.style.width = StatusData[1]+"%";
                if(parseInt(StatusData[0])==0) {StatusData[0] = 'unknown '; maxGet--;}
                document.getElementById('statusInfo').innerHTML=StatusData[1]+"% of "+StatusData[0]+"Kb ("+StatusData[2]+"Kbps)";
                if (StatusData[1]<100){test()}
                else
                {
                        document.getElementById('statusInfo').innerHTML=StatusData[0]+"Kb ("+StatusData[2]+" Kbps)<br>$Message{uploadcomplete}!";
                               var duration = 500;
                               setTimeout("CloseUpload(Status)",duration);

                }
        }

        function showControl(fin){
                      window.setTimeout("replaceBody("+fin+")", 1000);
        }
        function replaceBody(fin){
                maxGet = 0;
                if (fin)
                {
                        opener.parent.location.reload();
                }
                document.body.innerHTML = contrFrame.document.body.innerHTML;
        }

</script>

EOF


        my $onchange=qq~ onchange="checkFile(this)"~  if !$myAdmin && $bannedFile;
        print qq~</head>
     <body bgcolor=#eeeeee>
        <div id="statusWnd" name="statusWnd" style="position:absolute;z-index:4; width:259; height:130; top:176; left:100; display:none; border-style: solid; border-width:1; border-color:#686868; background-image:url($htmlDataFolder/uploadbg.png)">
        <center>
        <div id="statusLine" name="statusLine" style="position:relative; width:200; height:20; top:20; border-style: solid; border-width:1; border-color:#686868; background-color:#FFFFFF">
        <div id="statusBar" name="statusBar" style="float: left; position:relative; width:0%; height:20; top:0; border-style: none; border-width:1; border-color:#333333; background-image:url($htmlDataFolder/progressbar.png)"></div>
        </div>
        <div id="statusInfo" name="statusInfo" style="position:relative; width:200; top:50">
        </div>
        </center>
                </div>
        <iframe style="width:0px; height:0px; overflow:hidden;  border:0" src="secure.shtml" name="contrFrame" name="contrFrame"></iframe>
        ~;
my $fileDesc=qq~<tr><td>$Message{description}:</td><td><input type=text name=fileDescription size="34" style="width:250pt" maxlength="32"><td></tr>~ if $fileDescriptionOn;
        print qq~
<div style="position:absolute;z-index:1;visibility:visible; left:0px;top:0px;width:413px;height:41px;">
<img Align=Top src="$htmlDataFolder/tabbg.png" border="0" width="443px"  height="41px"></div>
<div id="navigation" style="position:absolute;z-index:2;visibility:visible; left:14px;top:15px;width:300px;height:154px;">
<ul>
<li><a href="$script?action=upload&amp;dir=$dir"><span>$Message{upload}</span></a></li>
<li><a href="$script?action=uploadfl&amp;dir=$dir"><span>Flash $Message{upload}</span></a></li>
</ul>
</div>
<div style="position:absolute;z-index:3;visibility:visible; left:10px;top:32px;width:403px;height:41px;">
<form onsubmit="return startUp();"  target="contrFrame" name="myform" method=post action=$script?action=upload  ENCTYPE=\"multipart/form-data\">
                <input type=hidden name=mode value=$FORM{mode}>
                <input type=hidden name=shared value=$FORM{shared}>
                <input type=hidden name=dir value="$dir">
                <table>
                                <tr><td>&nbsp;<td></tr>
                                <tr><td>&nbsp;<td></tr>
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td>$Message{file}:</td><td><input type=file name=file size="34" $onchange><td></tr>$fileDesc
                <tr><td colspan="2"><input type="checkbox" name="overwrite" value="1" checked> Overwrite existing files</td></tr>
                <tr><td colspan=2 align=center><input type=submit value="$Message{upload_files}" name="btnSubmit"> <input type=reset onclick=window.close() value=$Message{cancel}>
</td></tr></table></form>~;
print qq~
</body></html>~;
        exit;
}

sub uploadfl{
        print "Content-type: text/html\n\n";
        use Digest::MD5;
        my $url = $sslOn? $sslUri : $ENV{SCRIPT_NAME};
        $userLogin||=$COOKIES{login};
        my $md5 = Digest::MD5::md5_hex($userLogin.$secretWord);
        print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
        <title>Upload Files</title>
        <script type="text/javascript" src="$htmlDataFolder/FlashObject.js"></script>
        </head>
        <body bgcolor="#eeeeee">
<div style="position:absolute;z-index:1;visibility:visible; left:0px;top:0px;width:443px;height:41px;">
<img Align=Top src="$htmlDataFolder/tabbg.png" border="0" width="443px"  height="41px"></div>
<div id="navigation" style="position:absolute;z-index:2;visibility:visible; left:14px;top:15px;width:300px;height:154px;">
<ul>
<li><a href="$script?action=upload&amp;dir=$dir"><span>$Message{upload}</span></a></li>
<li><a href="$script?action=uploadfl&amp;dir=$dir"><span>Flash $Message{upload}</span></a></li>
</ul>
</div>
<div  id="flashcontent" style="position:absolute;z-index:2;visibility:visible; left:0px;top:46px;width:420px;height:560px;">
                        You will need <a href="http://www.macromedia.com/software/flashplayer/public_beta/" title="Flash Player 8">Flash Player 8</a>. <br />
                        Currently set to 204800kb MAX filesize for each file that can be uploaded!<br />
</div>

<script>
<!--
                                var flashObj = new FlashObject("$Uploadflashfile/fileUpload.swf", "uploadFile", "100%", "100%", "8.0.5", "#eeeeee", true);
                                flashObj.addVariable ("uploadUrl", "$url");
                                flashObj.addVariable ("maxFileSize", "204800");
                                flashObj.addVariable ("folderName", "$dir");
                                flashObj.addVariable ("uploadMode", "$FORM{mode}");
                                flashObj.addVariable ("userLogin", "$userLogin");
                                flashObj.addVariable ("uploadButtonlabel", "$Message{upload}");
                                flashObj.addVariable ("clearButtonlabel", "$Message{cancel}");
                                flashObj.addVariable ("clearButtonlabel", "$Message{cancel}");
                                                                flashObj.addVariable ("browseLabeltext", "  $Message{selectfiletoupload}");
                                                            flashObj.addVariable ("no_right", "$Message{no_right}");
                                                            flashObj.addVariable ("over_quota", "$Message{over_quota}");
                                                            flashObj.addVariable ("err_banned_format", "$Message{err_banned_format}");
                                                                   flashObj.addVariable ("uploadcomplete", "$Message{uploadcomplete}");
                                                                flashObj.addVariable ("md5", "$md5");
                                flashObj.write("flashcontent");
                        // -->
                </script>

        </body>
        </html>
        ~;
        exit;
}


sub flu{

       # open (LG, ">log.txt");
       # use Data::Dumper;
       # print LG Dumper(\%FORM). " = ".join ', ', param();
       # print LG "\n user: ".$FORM{user}."\n";


        #check access
        die "user not found" unless $FORM{user};

        my $found;
        if ($FORM{user} && $AdminLogin->{$FORM{user}}){
                if ($FORM{cip} eq  Digest::MD5::md5_hex($FORM{user}.$secretWord.$AdminLogin->{$FORM{user}})){
                $home=$rootHomeDir;
                $myAdmin=1;
                $found=1;
                @$Rights{("w","c","m","d","r","u","p","n","l","a","h","i")} = (1,1,1,1,1,1,1,1,1,1,1,1);}


        }
        else{
                my @data = read_file($userTable);
                shift @data;
                chomp;
                foreach(@data){
                        chomp;
                        ($userId, $userLogin, $userPass, $userEmail, $userDir, $discQuota, $disabledFiles, $rights)=split('\|', $_);
                        # print LG "user: ".$FORM{cip}." ". Digest::MD5::md5_hex($userLogin.$secretWord.$userPass)."\n";
                        if ($FORM{user} && $FORM{user} eq $userLogin && $FORM{cip} eq  Digest::MD5::md5_hex($userLogin.$secretWord.$userPass)){
                                $found=1;
                                for(split(',',$rights)){$Rights->{$_} = '1' if $_;}
                                $home = "$rootHomeDir/$userDir";
                                last;
                        }
                }
        }
        unless ($found || $Rights->{'u'}) {
                print "Status: 501\n\n";
                exit;
        }
        #disabled Files
        my %disabledFiles;
        $disabledFiles=~s/ //g;
        for(split(',',$disabledFiles)){$disabledFiles{$_}=1;}
        my $file=param('Filedata');
        $file=~m/\.([^\.]+)\Z/;
        if ($disabledFiles{lc $1}){
                print "Status: 502\n\n";
                exit;
        }

        #disk quota
        if (!$myAdmin && $ENV{CONTENT_LENGTH} /(1024*1024)>$discQuota){
                #die ("Cannot Upload Files - You Have Exceeded Your Quota");
                print "Status: 503\n\n";
                exit;
        }
        # print LG "\n  ".$ENV{CONTENT_LENGTH} /(1024*1024)." $discQuota\n";
        #file name illegal chars (* ? " <> | ; @ # \~ { })
               #die "A File Name $_ or Description cannot contain any of the following illegal characters:  *  ? ? <> | ; @ # ~ { }" if $file=~m/[\*\?\|\;;\{\}<>\@\#~\?]/;
        if ($file=~m/[\*\?\+\&\'\!\?\%\(\)\|\;;\{\}<>\@\#~\?]/){
                print "Status: 504\n\n";
                exit;
        }

        print "Content-type: text/html\n\n";
        print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
        <html>
        <head>
        <title> Upload Page </title>
        </head>

        <body>
                <h3>Upload Successful</h3>
        </body>
        </html>
        ~;

        save_file($file, $FORM{dir}, $FORM{mode}) if $file;

                open (LOG, ">>$log") or die $! if $LogActivity;
                print LOG "$theTime|$COOKIES{login}|File '$file' uploaded to '$FORM{dir}'|\n" if $LogActivity;
                close(LOG);

        #message to admin
                        if($send_as_html){
                                my %FORM;
                                $FORM{RegisteredOwner}= $RegisteredOwner;
                                $FORM{files}= "$FORM{dir}/$file &nbsp;&nbsp;&nbsp;&nbsp;Flash Upload<br>";
                               $message = get_record(\%FORM, join '', read_file($msg_body_file));
                        }
                        else{$message="$FORM{dir}/$file     Flash Upload\n\n";}

                        male($toAdmin, $fromAdmin, "$FORM{user} $subjecttitle", $message) if $sendConfirmFlashUpload;
        #open (LG, ">>log.txt");
        #print LG "[ $file ]";
        #print LG "$toAdmin, $fromAdmin, $FORM{user} Has Uploaded New Files, $message"."\n";
        #close LG;

        exit;
}




sub html{
        print "Content-type: text/html$charset\n\n";
        $j_script = "<script>
                function go(){
                opener.parent.location.reload();
                opener.parent.focus();
                window.close();
                }
        </script>";
        print qq~<html><head><title>$_[4]</title>
        <link rel="STYLESHEET" type="text/css" href="$script?action=get_css">\n~;
        print $j_script if $_[1];
        print qq~</head>
        <body bgcolor=#eeeeee ~;
        if($_[1]){
                print " onload=go()>",$text;
                print "</body></html>";
                exit;
        }

        print qq~>
                <form method="post" name="wndForm" action="$script">
                <input type=hidden name=action value="$_[2]">
                <input type=hidden name=dir value="$_[3]">
                $_[0]
                </form>~;

        print "</body></html>";
        exit;
}

####
sub save_file{
        my $file=shift;
        my $dir=shift;
        my $mode = shift;
        my %modeFiles;
        unless ($mode){
                for(@autoTextMode){$modeFiles{$_}++}
        }

        (my $filename = $file) =~s!^.*[/\\]!!;
        $filename =~m!\.(\w*?)$!;
        my $ext = $1;
        open(FILE,">$home/$dir/$filename") || error("$Message{err_save_file} $home/$dir/$filename! $!", 2, 1);
        binmode FILE if $mode==1 || (!$mode && !$modeFiles{$ext});

        while (read($file,$buffer,1024)) {
                #hack for clear \r
                $buffer=~s/\r//gs unless ($mode==1 || (!$mode && !$modeFiles{$ext}));
                print FILE $buffer;
        }
        close(FILE);
        return 1;
}



sub error{
        print "Content-Type: text/html$charset\n\n" unless $content;
        my $func = qq~ onload=\"if(parent) parent.showControl();\"~ if $_[1]==2;
        print qq~<html><head><title>FileManager::Error</title><link rel="STYLESHEET" type="text/css" href="$script?action=get_css"></head>
        <body$func>~;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|$_[0]|\n" if $LogActivity;
        close(LOG);
        open (eLOG, ">>$elog") or die $! if $ErrorLog;
        print eLOG "$theTime|$COOKIES{login}|$_[0]|\n" if $ErrorLog;
        close(eLOG);
        print "<table align=center height=100%><tr><td align=center><b class=error>$_[0]</b></td></tr></table>";
        print "</body></html>";
        exit;

}

sub discQuota{
        if (-f "$File::Find::name"){
                $discSize +=(stat($File::Find::name))[7];

        }
}

sub get_messages{
        my %Mess;
        open (MESS, $_[0]) or error("Error: Cannot Open Lanaguage File (Check CHMOD Settings)");
        my @data=<MESS>;
        close MESS;

        for (@data){
                chomp;
                $_=~s/\r//gs;
                my ($key,$value) = split("==",$_);
                $Mess{$key}=$value;
        }
        return %Mess;
}



sub frameText{
        $FORM{dir}   =~s/\&/%26/g; $FORM{dir}   =~s/#/%23/g;
        $FORM{search}=~s/\&/%26/g; $FORM{search}=~s/#/%23/g;
        $FORM{gzfile}=~s/\&/%26/g; $FORM{gzfile}=~s/#/%23/g;

        my $opt = "&opt=$FORM{opt}" if $FORM{opt};
        $opt .= "&r=1" if $FORM{r};
        $opt .= "&dir=$FORM{dir}" if $FORM{dir};
        $opt .= "&search=$FORM{search}" if $FORM{search};
        $opt .= "&matchCase=$FORM{matchCase}" if $FORM{matchCase};
        $opt .= "&inNotes=$FORM{inNotes}" if $FORM{inNotes};
        $opt .= "&gzfile=$FORM{gzfile}" if $FORM{gzfile};
        print "Content-Type: text/html$charset\n\n";
 my $headFrame;
if($CustomerFrameHeight){
$headFrame =qq~<frameset rows="$CustomerFrameHeight,116,*,126" FRAMEBORDER="0">
  <frame src="$CustomerFrameUrl" name="_customer" FRAMEBORDER="0" NORESIZE SCROLLING="no">~;
}
else{
$headFrame =qq~<frameset rows="116,*,126" FRAMEBORDER="0">
  ~;

}

        print qq~
<html>
   <head>
<meta http-equiv="content-type" content="text/html$charset">
   <meta name="resource-type" content="document">
   <meta name="revisit-after" content="15">
   <meta name="language" content="">
   <meta name="doc-type" content="Web Page">
   <meta name="doc-class" content="Completed">
   <meta name="doc-rights" content="Copywritten Work">
   <title>$Filemanagertitle</title>
   </head>
$headFrame
  <frame src="$script?type=head$opt" name="head" FRAMEBORDER="0" NORESIZE SCROLLING="no">
  <frame src="$script?type=content$opt" name="content" FRAMEBORDER="0" NORESIZE SCROLLING="yes">
  <frame src="$script?type=foot" name="foot" FRAMEBORDER="0" NORESIZE SCROLLING="no">
</frameset>
<body>Your browser not support frames!</body>
</html>
        ~;
        exit;

}

sub head{
        ##############it is head frame#############
        print "Content-type: text/html$charset\n\n";
        $opt_r = $FORM{r};
        $opt_{$FORM{opt}}="&r=1" unless $FORM{r};
        $dir=$FORM{dir};
        $dirTitle ="/$dir" if $dir;
        $dirTitle .="/$FORM{gzfile}" if $FORM{gzfile};


        $arrow{$FORM{opt}} = $FORM{r} ? $arrow_up : $arrow_down;
        my ($hWind, $colspan, $nameRow) = (340,6,54);
        if ($fileDescriptionOn){
                ($hWind, $colspan, $nameRow) = (590,7,24);
                $descrTitle="<td class=head_line width=25%><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>&nbsp;$Message{description}</FONT></B></td>";
        }

        my $admin_item = qq~fw_menu_0.addMenuItem("$Message{control_panel}","window.open('$ClientScript?action=users','_blank')")~ if $myAdmin;

        #read disc space
        if ($discQuota){
                find(\&discQuota, "$home/$dir");
                $overQuota = 1 if $discQuota<= $discSize /(1024*1024);
                if($discSize>(1024*1024)){
                        $discSize /= 1024*1024;
                        $discSizeTxt = "$Message{used_spase}: ".sprintf("%.2f",$discSize)." $Message{Mb}";
                        $discSizeTxt .= " <font color=red>$Message{over_quota}</font>" if $overQuota;
                }
                elsif ($discSize>1024){
                        $discSize /= 1024;
                        $discSizeTxt = "$Message{used_spase}: ".sprintf("%.2f",$discSize)." $Message{Kb}";
                        $discSizeTxt .= " <font color=red>$Message{over_quota}</font>" if $overQuota;
                }
                else{
                        $discSize/=1;
                        $discSizeTxt = "$Message{used_spase}: $discSize $Message{Bytes}";

                }
        }

        $admin_item ||= qq~fw_menu_0.addMenuItem("$Message{control_panel}","show('$script?action=userarea', 200, 350)")~;


        print qq~
<html>
<head>
<link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
<script type="text/javascript">

                var overQuota = "$overQuota";
                function sh(obj){if (obj.className!="selected") obj.className="of";}
                function shh(obj){if (obj.className!="selected") obj.className="off";}
                var filesSelected=0;
                var itDir = 0;
                function selectAll(){
                        if (document.mode.all_file.checked){parent.content.selectAll(1);}
                        else{parent.content.selectAll(0);}
                }
                function selectFile(ifFile){
                        var fileName=parent.content.test(ifFile);
                        return escape(fileName);
                }

                function selectFiles(){
                        return parent.content.testA();
                }
                function select(obj, file){
                        if (obj.className!="selected") { obj.className="selected";}
                        else  { obj.className="of";}

                }
                function download(){
                        $alert
                        var myFile = selectFile(1);
                        if (!myFile || myFile == 'undefined') return;
                        window.location.href="$script?action=download&file="+myFile;
                }
                function editor(){
                        $alert
                        var myFile = selectFile(1);
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=edit$editorplugin&file="+myFile
                                                if($ResizeEditorOn)
                                                {
                                                   showresize(page, 468,700, 'no', 'editor');
                                                }
                                                else
                                                {
                                                   show(page, 468,700, 'no', 'editor');
                                }
                                }
                                                function view(){
                        $alert
                        var myFile = selectFile(1);
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=view&file="+myFile;
                                                if($ResizePreviewOn)
                                                {
                                                   showresize(page, 408,600, 'no');
                                                }
                                                else
                                                {
                                                   show(page, 408,600, 'no');
                                }
                                }
                                                function fview(file){
                        var page="$script?action=view&file="+file;
                        if($ResizePreviewOn)
                        {
                        showresize(page, 468,700, 'no');
                        }
                        else
                        {
                        show(page, 468,700, 'no');
                        }
                }
                function chmod(){
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine || fileLine == 'undefined') {alert("$Message{select_file}"); return;}
                        var page="$script?action=chmod"+fileLine;
                        show(page, 200, 280, 'no');
                }
                function rename(){
                        $alert
                        var myFile = selectFile();
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=rename&dir=$dir&file="+myFile;
                        show(page, 40,260, 'no');
                }
                function copy(){
                        if(overQuota){
                                alert("overQuota");
                                return;
                        }
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine || fileLine == 'undefined') {alert("$Message{select_file}"); return;}

                        var page="$script?action=copy&dir=$dir"+fileLine;
                        show(page, 280,380, 'no');
                }
                function notes(){
                        $alert
                        var myFile = selectFile();
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=notes&dir=$dir&file="+myFile;
                        show(page, 540, 500, 'yes');
                }
                function notesview(file){
                                var page="$script?action=notes&dir=$dir&file="+file;
                show(page, 540, 500, 'yes');
                }
                function batch_download(){
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine) {alert("$Message{select_file}"); return;}
                        var tsd = '$Message{del_file}';
                        if (filesSelected>1) tsd = '$Message{file_directories}';
                        if(itDir==1) {alert(); return;}
                        var Check = prompt("Enter zip file name:",'');
                        if (!Check) return;
                        top.location.href="$script?action=batch_download&zipname="+Check+"&dir=$dir"+fileLine;
                }
                function move(){
                        if(overQuota){
                                alert("$Message{over_quota}");
                                return;
                        }
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine || fileLine == 'undefined') {alert("$Message{select_file}"); return;}
                        var page="$script?action=move&dir=$dir"+fileLine;
                        show(page, 280,380, 'no');
                }
                function pack(){
                        if(overQuota){
                                alert("$Message{over_quota}");
                                return;
                        }
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine) {alert("$Message{select_file}"); return;}
                        var page="$script?action=pack&dir=$dir&"+fileLine;
                        show(page, 80,350,'no');
                }
                function unpack(){
                        if(overQuota){
                                alert("$Message{over_quota}");
                                return;
                        }
                        $alert
                        var myFile = selectFile();
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=unpack&dir=$dir&file="+myFile;
                        show(page, 80,350, 'no');
                }
                function delete_f(){
                        $alert
                        var fileLine = selectFiles();
                        if (!fileLine) {alert("$Message{select_file}"); return;}
                        var tsd = '$Message{del_file}';
                        if (filesSelected>1) tsd = '$Message{file_directories}';
                        else if(itDir==1) tsd = '$Message{del_directory}';
                        if(confirm("$Message{confirm_delete} "+tsd+"?")){
                                top.location.href="$script?action=delete&dir=$dir&r=$FORM{r}"+fileLine+"&shared=$FORM{shared}";
                        }
                        else return;
                }
                function hotlink(){
                        $alert
                        var myFile = selectFile();
                        if (!myFile || myFile == 'undefined') return;
                        var page="$script?action=hotlink&dir=$dir&file="+myFile;
                        show(page, 40,365, 'no');
                }
                function mkdir(){
                        $alert
                        var page="$script?action=mkdir&dir=$dir";
                        show(page, 110,380);
                }
                function findfile(){
                        $alert
                        var page="$script?action=findfile&dir=$dir";
                        show(page, 10,370);
                }
                function about(){
                        var page="$script?action=about&dir=$dir";
                        shownoscroll(page, 321,385);
                }
                function upload(){
                        if (window.newWnd && !newWnd.closed){
                                if (newWnd.location.href.indexOf("action=upload")>=0) {newWnd.focus();}
                                else newWnd.close();
                                return;
                        }
                        if(overQuota){
                                alert("$Message{over_quota}");
                                return;
                        }
                        $alert
                        var mode=0;
                        if(document.mode.transfer.value=='b') mode=1;
                        if(document.mode.transfer.value=='t') mode=2;
                        var hWind = $hWind;
                        show("$script?action=upload&dir=$dir&mode="+mode, 660, 460);
                }


                function show(url,height, width, scroll){
                        if(!scroll) scroll = "yes";
                        newWnd=window.open(url, '_show', "height="+height+", width="+width+", top=100, left=100, status=none, scrollbars="+scroll+", location=none");
                        newWnd.focus();
                }
                function shownoscroll(url,height, width, scroll){
                        if(!scroll) scroll = "yes";
                        newWnd=window.open(url, 'show', "height="+height+", width="+width+", top=100, left=100, status=none, scrollbars=none, location=none");
                        newWnd.focus();
                }
                function showresize(url,height, width, scroll, name){
                        if(!scroll) name='show';
                        if(!scroll) scroll = "yes";
                        newWnd=window.open(url, name, "height="+height+", width="+width+", top=100, left=100, status=none, resizable=yes, scrollbars=yes, location=none");
                        newWnd.focus();
                }
                function logout(){
                        if(opener) window.close();
                        else top.location.href="$script?action=logout";
                }
        </script>
        <script language="JavaScript1.2" src="$script?action=fw_menu"></script>
        ~;

my $Action = {};
my $notRight = qq~"alert('$Message{no_right}')"~;
$Action->{copy}        = $Rights->{m} ? "\"javascript:copy();\"" : $notRight;
$Action->{rename}= $Rights->{a} ? "\"javascript:rename();\"" : $notRight;
$Action->{delete}= $Rights->{d} ? "\"javascript:delete_f();\"" : $notRight;
$Action->{move}        = $Rights->{m} ? "\"javascript:move();\"" : $notRight;
$Action->{chmod}        = $Rights->{c} ? "\"javascript:chmod();\"" : $notRight;
$Action->{upload}= $Rights->{u} ? "\"javascript:upload();\"" : $notRight;
$Action->{download}= $Rights->{r} ? "\"javascript:download();\"" : $notRight;
$Action->{preview}= $Rights->{r} ? "\"javascript:view();\"" : $notRight;
$Action->{pack}        = $Rights->{p} ? "\"javascript:pack();\"" : $notRight;
$Action->{unpack}= $Rights->{p} ? "\"javascript:unpack();\"" : $notRight;
$Action->{editor}= $Rights->{w} ? "\"javascript:editor();\"" : $notRight;
$Action->{notes}= $Rights->{l} ? "\"javascript:parent.head.notes();\"" : $notRight;
$Action->{batch_download}= $Rights->{p} ? "\"javascript:parent.head.batch_download();\"" : $notRight;
$Action->{hotlink}= $Rights->{r} ? "\"javascript:hotlink();\"" : $notRight;

my $autoTxtType=join(',',@autoTextMode);


        print qq~
        <script language="JavaScript">
        <!--
        function fwLoadMenus() {
          if (window.fw_menu_0) return;
          window.fw_menu_0 = new Menu("root",120,13,"Verdana, Arial, Helvetica, sans-serif;",9,"#000000","#ffffff","#F3F3F3","#2A4D88");
          $admin_item
          fw_menu_0.addMenuItem("$Message{exit}","logout()");
          fw_menu_0.hideOnMouseOut=true;
          window.fw_menu_1 = new Menu("root",120,13,"Verdana",9,"#000000","#ffffff","#F3F3F3","#2A4D88");
          fw_menu_1.addMenuItem("$Message{copy}",$Action->{copy});

          fw_menu_1.addMenuItem("$Message{rename}",$Action->{rename});
          fw_menu_1.addMenuItem("$Message{delete}",$Action->{delete});
          fw_menu_1.addMenuItem("$Message{move}",$Action->{move});
          fw_menu_1.addMenuItem("$Message{chmod}",$Action->{chmod});
          fw_menu_1.addMenuItem("$Message{search}","javascript:findfile();");
          fw_menu_1.addMenuItem("$Message{select_all}","parent.content.selectAll(1); document.mode.all_file.checked=true;");
                  fw_menu_1.hideOnMouseOut=true;


          window.fw_menu_2 = new Menu("root",120,13,"Verdana, Arial, Helvetica, sans-serif",9,"#000000","#ffffff","#F3F3F3","#2A4D88");
          fw_menu_2.addMenuItem("$Message{upload}",$Action->{upload});
          fw_menu_2.addMenuItem("$Message{download}",$Action->{download});
          fw_menu_2.addMenuItem("$Message{preview}",$Action->{preview});
          fw_menu_2.addMenuItem("$Message{pack}",$Action->{pack});
          fw_menu_2.addMenuItem("$Message{unpack}",$Action->{unpack});
          fw_menu_2.addMenuItem("$Message{editor}",$Action->{editor});
          fw_menu_2.hideOnMouseOut=true;

          window.fw_menu_3 = new Menu("root",120,13,"Verdana, Arial, Helvetica, sans-serif",9,"#000000","#ffffff","#F3F3F3","#2A4D88");
          fw_menu_3.addMenuItem("$Message{contact_us}","window.open('$contactus','_blank');");
          fw_menu_3.addMenuItem("$Message{tutorials}","window.open('$tutorialslink','_blank');");
          fw_menu_3.addMenuItem("$Message{support_forums}","window.open('$forumlink','_blank');");
          fw_menu_3.addMenuItem("$Message{about}","javascript:about();");
          fw_menu_3.hideOnMouseOut=true;

           fw_menu_3.writeMenus();
        }

        //-->
        </script>

<font size=-1>
<img src="/Agent-Office/link.gif">  <a href="http://www.surflocal.net/office/video-library/nktppt.html" target="_blank">Surflocal Marketing Powerpoint Videos </a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="/Agent-Office/link.gif">  <a href="/office/video-library/" target="_blank">Audio Visual Creation Videos</a> &nbsp;&nbsp;&nbsp;<img src="/Agent-Office/link.gif">  <a href="/office/video-library/slmv.html" target="_blank">Visual Build and Edit Tutorials</a> &nbsp;&nbsp;&nbsp;<img src="/Agent-Office/link.gif">  <a href="/Agent-Office/top300headings-rank.pdf" target="_blank">Top Ranked Headings </a>&nbsp;&nbsp;&nbsp;<img src="/Agent-Office/link.gif">  <a href="/Agent-Office/postcards" target="_blank">Send Postcards to Clients</a> &nbsp;&nbsp;&nbsp;&nbsp;




        <body topmargin=0 leftmargin=0 background="$background" bgcolor="#F3F3F3">
<script language="JavaScript1.2">fwLoadMenus();</script>
<table border=0  width=100% ALIGN=center cellpadding=1 class=head_frame>
<tr><td colspan=$colspan>
        <table border=0  width=99% cellpadding=0>
        <tr><td  width=$Message{file_position}><a href="#" onMouseOut="FW_startTimeout();"  onMouseOver="window.FW_showMenu($Message{file_coordinates});" class="Menucss">$Message{file}</a>&nbsp;</td>
        <td width=$Message{edit_position}><a href="#" onMouseOut="FW_startTimeout();"  onMouseOver="window.FW_showMenu($Message{edit_coordinates});" class="Menucss">$Message{edit}</a>&nbsp;</td>
        <td width=$Message{tools_position}><a href="#" onMouseOut="FW_startTimeout();"  onMouseOver="window.FW_showMenu($Message{tools_coordinates});" class="Menucss">$Message{tools}</a>&nbsp;</td>
        <td width=$Message{help_position}><a href="#" onMouseOut="FW_startTimeout();"  onMouseOver="window.FW_showMenu($Message{help_coordinates});" class="Menucss">$Message{help}</a>&nbsp;</td>
        </td><td align=right class="misc_header">$Message{login_as}: <B><FONT COLOR='#2A4D88' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$COOKIES{login}</FONT></B></td></tr>
</td></tr>
        </table>
<tr><td  height=5 colspan=$colspan>
<tr><td  colspan=$colspan><img src="$fileTypeImgDir/spacer.gif" border=0 width=700 height=1></td></tr>
<tr><td  colspan=$colspan align="left"></td></tr>
<tr><td  colspan=$colspan>
        <table  width=100% >
        <form name=mode target=_top><input type=hidden name=dir value="$FORM{dir}">
        <tr><td class="misc_header">$Message{search}: <input type=text name=search size=20 value="$FORM{search}">
        <input type=submit value=go>
        <input type=checkbox name=matchCase value=1 ~. ($FORM{matchCase}? 'checked':'') .qq~> $Message{match_case}
        <input type=checkbox name=inNotes value=1 ~. ($FORM{inNotes}? 'checked':'') .qq~> $Message{notes}
        </td><td align=right class="misc_header">$Message{transfer_mode}: <select name=transfer><option $selectedA value="">Auto [$autoTxtType]</option><option $selectedT value="t">Text [plain text, html, etc.]</option><option $selectedB value="b">Binary [archives, doc, etc.]</option></select></td></tr>
        </table>
</td></tr>
                <tr class=misc_header height=18><td colspan=$colspan class=on>&nbsp;&nbsp;<b>$dirTitle/*.*</b></td></tr>
                <tr>
                <tr><td  height=27 colspan=$colspan>
                <table width=100% border=0 cellpadding=0 cellspacing=0>
                    <td class=head_line width=2%><input type=checkbox name=all_file onclick=selectAll()></td>
                    <td class=head_line width=$nameRow% height=18>&nbsp;$arrow{name}<a href="$script?opt=name&dir=$dir$opt_{name}$qs" style="text-decoration:none" target=_top><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$Message{name}</FONT></B></a></td>
                    <td class=head_line width=5%>&nbsp;$arrow{ext}<a href="$script?opt=ext&dir=$dir$opt_{ext}$qs" style="text-decoration:none" target=_top><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$Message{ext}</FONT></B></a></td>
                    <td class=head_line width=11%>&nbsp;$arrow{size}<a href="$script?opt=size&dir=$dir$opt_{size}$qs" style="text-decoration:none" target=_top><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$Message{size}</FONT></B></a></td>
                     $descrTitle
                    <td class=head_line width=20%>&nbsp;$arrow{date}<a href="$script?opt=date&dir=$dir$opt_{date}$qs" style="text-decoration:none" target=_top><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$Message{date}</FONT></B></a></td>
                    <td class=head_line width=8%>&nbsp;$arrow{mode}<a href="$script?opt=mode&dir=$dir$opt_{mode}$qs" style="text-decoration:none" target=_top><B><FONT COLOR='#000000' SIZE=1 FACE='Verdana,Arial,Helvetica,Sans Serif'>$Message{attr}</FONT></B></a></td>
                </table>
                </td>
                </tr></form>
   </table>
   </body>
   </html>
    ~;

        exit;
}



sub foot{
        ##########it is foot frame##################
        print "Content-type: text/html$charset\n\n";

        my @data = read_file($userTable);
        shift @data;
        foreach(@data){
                chomp;
                ($userId, $userLogin, $userPass, $userEmail, $userDir, $discQuota, $disabledFiles, $rights)=split('\|', $_);
                if ($COOKIES{login} eq $userLogin && $userPass eq  crypt($COOKIES{pass},$userPass)){
                        for(split(',',$rights)){$Rights->{$_} = '1' if $_;}
                        last;
                }
        }



        print qq~
<html>
<head>
<style type="text/css">
        body {background-color: #F3F3F3; margin:0; padding:0; background: url("$toolsLine") repeat; }
        #tools {border:none; margin:20px auto 0 auto;}
        #tools th {padding:0px;}
        #tools th a img {border:none;}
        #tools td{text-align:center; padding:0px;}
        #tools td a {font: bold 10px verdana, arial, helvetica, sans-serif;  color:#808080;  text-decoration:none;}
        .dis {font: bold 10px verdana, arial, helvetica, sans-serif;  color:#a0a0a0; }
</style>
</head>
<body bgcolor="#F3F3F3">
<table id="tools" cellspacing="5" align="center">
     <tr>~;

print qq~          <th><a href="javascript:parent.head.download()"><img src="$Download" alt="$Message{download}" onMouseOver="window.status='$Message{download}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{r};
print qq~          <th><a href="javascript:parent.head.upload()"  ><img src="$Upload"   alt="$Message{upload}" onMouseOver="window.status='$Message{upload}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{u};
print qq~          <th><a href="javascript:parent.head.batch_download()"  ><img src="$BatchDownload"   alt="$Message{batch_download_zip}" onMouseOver="window.status='$Message{batch_download_zip}'; return true;" onMouseOut="window.status=''; return true;"></a></th>~ if $Rights->{p};
print qq~          <th><a href="javascript:parent.head.pack()"    ><img src="$Pack"     alt="$Message{pack}" onMouseOver="window.status='$Message{pack}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{p};
print qq~          <th><a href="javascript:parent.head.unpack()"  ><img src="$Unpack"   alt="$Message{unpack}" onMouseOver="window.status='$Message{unpack}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{p};
#print qq~          <th><a href="javascript:parent.head.chmod()"   ><img src="$CHMOD"    alt="$Message{chmod}" onMouseOver="window.status='$Message{chmod}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{c};
print qq~          <th><a href="javascript:parent.head.view()"    ><img src="$Preview"  alt="$Message{preview}" onMouseOver="window.status='$Message{preview}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{r};
#print qq~          <th><a href="javascript:parent.head.hotlink()"    ><img src="$hotlink"  alt="$Message{hotlink}" onMouseOver="window.status='$Message{hotlink}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{r};
print qq~          <th><a href="javascript:parent.head.notes()"   ><img src="$Notes"    alt="$Message{notes}" onMouseOver="window.status='$Message{notes}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{l};
print qq~          <th><a href="javascript:parent.head.copy()"    ><img src="$Copy"     alt="$Message{copy}" onMouseOver="window.status='$Message{copy}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{m};
#print qq~          <th><a href="javascript:parent.head.rename()"  ><img src="$Rename"   alt="$Message{rename}" onMouseOver="window.status='$Message{rename}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{a};
#print qq~          <th><a href="javascript:parent.head.editor()"  ><img src="$Editor"   alt="$Message{editor}" onMouseOver="window.status='$Message{editor}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{w};
#print qq~          <th><a href="javascript:parent.head.move()"    ><img src="$Move"     alt="$Message{move}" onMouseOver="window.status='$Message{move}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{m};
#print qq~          <th><a href="javascript:parent.head.mkdir()"   ><img src="$MkDir"    alt="$Message{mkdir}" onMouseOver="window.status='$Message{mkdir}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{n};
#print qq~          <th><a href="javascript:parent.head.delete_f()"><img src="$Delete"   alt="$Message{delete}" onMouseOver="window.status='$Message{delete}'; return true;" onMouseOut="window.status=''; return true;"></th>~ if $Rights->{d};
print qq~          <th><a href="javascript:parent.head.logout()"  ><img src="$Logoff"   alt="$Message{exit}" onMouseOver="window.status='$Message{exit}'; return true;" onMouseOut="window.status=''; return true;"></th> ~;
print "     </tr>
     <tr>";
print qq~         <td><a href="javascript:parent.head.download()" onMouseOver="window.status='$Message{download}'; return true;" onMouseOut="window.status=''; return true;">$Message{download}</a></td>~ if $Rights->{r};
print qq~         <td><a href="javascript:parent.head.upload()" onMouseOver="window.status='$Message{upload}'; return true;" onMouseOut="window.status=''; return true;">$Message{upload}</a></td>~ if $Rights->{u};
print qq~         <td><a href="javascript:parent.head.batch_download()" onMouseOver="window.status='$Message{batch_download_zip}'; return true;" onMouseOut="window.status=''; return true;">$Message{batch_download_zip}</a></td>~ if $Rights->{p};
print qq~         <td><a href="javascript:parent.head.pack()" onMouseOver="window.status='$Message{pack}'; return true;" onMouseOut="window.status=''; return true;">$Message{pack}</a></td>~ if $Rights->{p};
print qq~         <td><a href="javascript:parent.head.unpack()" onMouseOver="window.status='$Message{unpack}'; return true;" onMouseOut="window.status=''; return true;">$Message{unpack}</a></td>~ if $Rights->{p};
#print qq~         <td><a href="javascript:parent.head.chmod()" onMouseOver="window.status='$Message{chmod}'; return true;" onMouseOut="window.status=''; return true;">$Message{chmod}</a></td>~ if $Rights->{c};
print qq~         <td><a href="javascript:parent.head.view()" onMouseOver="window.status='$Message{preview}'; return true;" onMouseOut="window.status=''; return true;">$Message{preview}</a></td>~ if $Rights->{r};
#print qq~         <td><a href="javascript:parent.head.hotlink()" onMouseOver="window.status='$Message{hotlink}'; return true;" onMouseOut="window.status=''; return true;">$Message{hotlink}</a></td>~ if $Rights->{r};
print qq~         <td><a href="javascript:parent.head.notes()"  onMouseOver="window.status='$Message{notes}'; return true;" onMouseOut="window.status=''; return true;">$Message{notes}</a></td>~ if $Rights->{l};
print qq~         <td><a href="javascript:parent.head.copy()" onMouseOver="window.status='$Message{copy}'; return true;" onMouseOut="window.status=''; return true;">$Message{copy}</a></td>~  if $Rights->{m};
#print qq~         <td><a href="javascript:parent.head.rename()" onMouseOver="window.status='$Message{rename}'; return true;" onMouseOut="window.status=''; return true;">$Message{rename}</a></td>~  if $Rights->{a};
#print qq~         <td><a href="javascript:parent.head.editor()" onMouseOver="window.status='$Message{editor}'; return true;" onMouseOut="window.status=''; return true;">$Message{editor}</a></td>~  if $Rights->{w};
#print qq~         <td><a href="javascript:parent.head.move()" onMouseOver="window.status='$Message{move}'; return true;" onMouseOut="window.status=''; return true;">$Message{move}</a></td>~  if $Rights->{m};
#print qq~         <td><a href="javascript:parent.head.mkdir()" onMouseOver="window.status='$Message{mkdir}'; return true;" onMouseOut="window.status=''; return true;">$Message{mkdir}</a></td>~  if $Rights->{n};
#print qq~         <td><a href="javascript:parent.head.delete_f()" onMouseOver="window.status='$Message{delete}'; return true;" onMouseOut="window.status=''; return true;">$Message{delete}</a></td>~  if $Rights->{d};
print qq~         <td><a href="javascript:parent.head.logout()" onMouseOver="window.status='$Message{exit}'; return true;" onMouseOut="window.status=''; return true;">$Message{exit}</a></td> ~;

 print qq~    </tr>
</table>
</body>
</html>~;
        exit;
}


sub error_right{
        #my $mess = shift;
        error ($Message{"no_right"}) ;
        open (LOG, ">>$log") or die $! if $LogActivity;
        print LOG "$theTime|$COOKIES{login}|Message{no_right}|\n" if $LogActivity;
        close(LOG);
        open (eLOG, ">>$elog") or die $! if $ErrorLog;
        print eLOG "$theTime|$COOKIES{login}|$_[0]|\n" if $ErrorLog;
        close(eLOG);

}



sub get_record{
        my %INSERT = %{shift()};
        my $text = shift;
        $text =~ s{\[\[(.*?)\]\]}{exists($INSERT{$1}) ? $INSERT{$1} : ""}gsex;
        return $text;
}

sub createPass{
        my $password = shift;
        my $string = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM";
        my @chars=split(//,$string);
        my $crypt = $chars[int(rand(@chars-1))].$chars[int(rand(@chars-1))];
        return crypt($password,$crypt);
}



sub male{
        error("Incorrect email!")  if $_[1]=~m/:/is or $_[0]=~m/:/is;
        error("Incorrect email!")  if $_[1]=~m/Content-type/is or $_[0]=~m/Content-type/is;
        error("Incorrect email!")  if $_[1]=~m/\n/is or $_[0]=~m/\n/is ;
        $_[1] =~ s/<([^>]|\n)*>//g;
        $_[0] =~ s/<([^>]|\n)*>//g;
        $_[1]=~s/\n|\r//g;
        $_[0]=~s/\n|\r//g;

        if($send_via_SMTP){
            $smtp = Net::SMTP->new($mailhost);

            $smtp->mail($_[1]);
            $smtp->to($_[0]);

            $smtp->data();
            $smtp->datasend("To: $_[0]\n");
            $smtp->datasend("Content-type: text/html\n") if $send_as_html;
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
                print MAIL "Content-type: text/html\n" if $send_as_html;
                print MAIL "Subject: $_[2]\n\n";
                print MAIL "$_[3]\n";
                close(MAIL);
                #print "To: $_[0]<br>";
        }

}




sub fw_menu{
        print "Content-type: application/x-javascript\n\n";
        print   q~/**
 * fw_menu 24OCT2000 Version 4.0
 * John Ahlquist, October 2000
 * Copyright (c) 2000 Macromedia, Inc.
 *
 * based on menu.js
 * by gary smith, July 1997
 * Copyright (c) 1997-1999 Netscape Communications Corp.
 *
 * Netscape grants you a royalty free license to use or modify this
 * software provided that this copyright notice appears on all copies.
 * This software is provided "AS IS," without a warranty of any kind.
 */
function Menu(label, mw, mh, fnt, fs, fclr, fhclr, bg, bgh) {
        this.version = "990702 [Menu; menu.js]";
        this.type = "Menu";
        this.menuWidth = mw;
        this.menuItemHeight = mh;
        this.fontSize = fs||7.5;
        this.fontFamily = fnt||"arial, helv, sans-serif";
        this.fontColor = fclr||"#000000";
        this.fontColorHilite = fhclr||"#FF3401";
        this.menuBorder = 1;
        this.menuItemBorder = 0;
        this.menuItemBgColor = bg||"#AAAAAA";
        this.menuLiteBgColor = "#F3F3F3";
        this.menuBorderBgColor = "#AAAAAA";
        this.menuHiliteBgColor = bgh||"#000084";
        this.childMenuIcon = "arrows.gif";
        this.items = new Array();
        this.actions = new Array();
        this.childMenus = new Array();
        this.disabled = new Array();

        this.hideOnMouseOut = true;

        this.addMenuItem = addMenuItem;
        this.addMenuSeparator = addMenuSeparator;
        this.writeMenus = writeMenus;
        this.FW_showMenu = FW_showMenu;
        this.onMenuItemOver = onMenuItemOver;
        this.onMenuItemAction = onMenuItemAction;
        this.hideMenu = hideMenu;
        this.hideChildMenu = hideChildMenu;

        if (!window.menus) window.menus = new Array();
        this.label = label || "menuLabel" + window.menus.length;
        window.menus[this.label] = this;
        window.menus[window.menus.length] = this;
        if (!window.activeMenus) window.activeMenus = new Array();
}

function addMenuItem(label, action, disable) {
        this.items[this.items.length] = label;
        this.actions[this.actions.length] = action;
        this.disabled[this.disabled.length] = disable;
}

function addMenuSeparator() {
        this.items[this.items.length] = "separator";
        this.actions[this.actions.length] = "";
        this.menuItemBorder = 0;
}

// For NS6.
function FIND(item) {
        if (document.all) return(document.all[item]);
        if (document.getElementById) return(document.getElementById(item));
        return(false);
}

function writeMenus(container) {
        if (window.triedToWriteMenus) return;

        if (!container && document.layers) {
                window.delayWriteMenus = this.writeMenus;
                var timer = setTimeout('delayWriteMenus()', 250);
                container = new Layer(100);
                clearTimeout(timer);
        } else if (document.all || document.hasChildNodes) {
                document.writeln('<SPAN ID="menuContainer"></SPAN>');
                container = FIND("menuContainer");
        }

        window.fwHideMenuTimer = null;
        if (!container) return;
        window.triedToWriteMenus = true;
        container.isContainer = true;
        container.menus = new Array();
        for (var i=0; i<window.menus.length; i++)
                container.menus[i] = window.menus[i];
        window.menus.length = 0;
        var countMenus = 0;
        var countItems = 0;
        var top = 0;
        var content = '';
        var lrs = false;
        var theStat = "";
        var tsc = 0;
        if (document.layers) lrs = true;
        for (var i=0; i<container.menus.length; i++, countMenus++) {
                var menu = container.menus[i];
                if (menu.bgImageUp) {
                        menu.menuBorder = 0;
                        menu.menuItemBorder = 0;
                }
                if (lrs) {
                        var menuLayer = new Layer(100, container);
                        var lite = new Layer(100, menuLayer);
                        lite.top = menu.menuBorder;
                        lite.left = menu.menuBorder;
                        var body = new Layer(100, lite);
                        body.top = menu.menuBorder;
                        body.left = menu.menuBorder;
                } else {
                        content += ''+
                        '<DIV ID="menuLayer'+ countMenus +'" STYLE="cursor:pointer; position:absolute;z-index:1;left:10;top:'+ (i * 100) +';visibility:hidden;">\n'+
                        '  <DIV ID="menuLite'+ countMenus +'" STYLE="cursor:pointer; position:absolute;z-index:1;left:'+ menu.menuBorder +';top:'+ menu.menuBorder +';visibility:hide;" onMouseOut="mouseoutMenu();">\n'+
                        '         <DIV ID="menuFg'+ countMenus +'" STYLE="cursor:pointer; position:absolute;left:'+ menu.menuBorder +';top:'+ menu.menuBorder +';visibility:hide;">\n'+
                        '';
                }
                var x=i;
                for (var i=0; i<menu.items.length; i++) {
                        var item = menu.items[i];
                        var childMenu = false;
                        var defaultHeight = menu.fontSize+6;
                        var defaultIndent = menu.fontSize;
                        if (item.label) {
                                item = item.label;
                                childMenu = true;
                        }

                        menu.menuItemHeight = menu.menuItemHeight || defaultHeight;
                        menu.menuItemIndent = menu.menuItemIndent || defaultIndent;
                        var itemProps = 'font-family:' + menu.fontFamily +';font-weight:' + menu.fontWeight + ';fontSize:' + menu.fontSize + ';';
                        if (menu.fontStyle) itemProps += 'font-style:' + menu.fontStyle + ';';
                        if (document.all) {
                                if(menu.disabled[i]) {itemProps += 'font-size:' + menu.fontSize + ';" onMouseOver="onMenuItemOver(null,this);" onClick="onMenuItemAction(null,this);';
                                }
                                else{
                                itemProps += 'font-size:' + menu.fontSize + ';" onMouseOver="onMenuItemOver(null,this);" onClick="onMenuItemAction(null,this);';
                                }
                        }
                        else if (!document.layers) {
                                itemProps += 'font-size:' + menu.fontSize + 'px;'; // zilla wants 12px.
                        }
                        var l;
                        if (lrs) {
                                l = new Layer(800,body);
                        }
                        var dTag        = '<DIV ID="menuItem'+ countItems +'" STYLE="position:absolute;left:0;top:'+ (i * menu.menuItemHeight) +';'+ itemProps +'">';
                        var dClose = '</DIV>'
                        if (menu.bgImageUp) {
                                menu.menuBorder = 0;
                                menu.menuItemBorder = 0;
                                dTag        = '<DIV ID="menuItem'+ countItems +'" STYLE="background:url('+menu.bgImageUp+');position:absolute;left:0;top:'+ (i * menu.menuItemHeight) +';'+ itemProps +'">';
                                if (document.layers) {
                                        dTag = '<LAYER BACKGROUND="'+menu.bgImageUp+'" ID="menuItem'+ countItems +'" TOP="'+ (i * menu.menuItemHeight) +'" style="' + itemProps +'">';
                                        dClose = '</LAYER>';
                                }
                        }
                        var textProps = 'position:absolute;left:' + menu.menuItemIndent + ';top:1;';
                        if (lrs) {
                                textProps +=itemProps;
                                dTag = "";
                                dClose = "";
                        }
                        var dText= '<DIV ID="menuItemText'+ countItems +'" STYLE="' + textProps + 'color:'+ menu.fontColor +';">'+ item +' &nbsp</DIV>\n<DIV ID="menuItemHilite'+ countItems +'" STYLE="' + textProps + 'top:1;color:'+ menu.fontColorHilite +';visibility:hidden;">'+ item +'&nbsp</DIV>';

                        if (item == "separator") {
                                content += ( dTag + '<DIV ID="menuSeparator'+ countItems +'" STYLE="position:absolute;left:1;top:2;"></DIV>\n<DIV ID="menuSeparatorLite'+ countItems +'" STYLE="position:absolute;left:1;top:2;"></DIV>\n' + dClose);
                        } else if (childMenu) {
                                content += ( dTag + dText + '<DIV ID="childMenu'+ countItems +'" STYLE="position:absolute;left:0;top:3;"><IMG SRC="'+ menu.childMenuIcon +'"></DIV>\n' + dClose);
                        } else {
                                content += ( dTag + dText + dClose);
                        }
                        if (lrs) {
                                l.document.open("text/html");
                                l.document.writeln(content);
                                l.document.close();
                                content = '';
                                theStat += "-";
                                tsc++;
                                if (tsc > 50) {
                                        tsc = 0;
                                        theStat = "";
                                }
                                status = theStat;
                        }
                        countItems++;
                }
                if (lrs) {
                        // focus layer
                        var focusItem = new Layer(100, body);
                        focusItem.visiblity="hidden";
                        focusItem.document.open("text/html");
                        focusItem.document.writeln("&nbsp;");
                        focusItem.document.close();
                } else {
                  content += '          <DIV ID="focusItem'+ countMenus +'" STYLE="position:absolute;left:0;top:0;visibility:hide;" onClick="onMenuItemAction(null,this);">&nbsp;</DIV>\n';
                  content += '   </DIV>\n  </DIV>\n</DIV>\n';
                }
                i=x;
        }
        if (document.layers) {
                container.clip.width = window.innerWidth;
                container.clip.height = window.innerHeight;
                container.onmouseout = mouseoutMenu;
                container.menuContainerBgColor = this.menuContainerBgColor;
                for (var i=0; i<container.document.layers.length; i++) {
                        proto = container.menus[i];
                        var menu = container.document.layers[i];
                        container.menus[i].menuLayer = menu;
                        container.menus[i].menuLayer.Menu = container.menus[i];
                        container.menus[i].menuLayer.Menu.container = container;
                        var body = menu.document.layers[0].document.layers[0];
                        body.clip.width = proto.menuWidth || body.clip.width;
                        body.clip.height = proto.menuHeight || body.clip.height;
                        for (var n=0; n<body.document.layers.length-1; n++) {
                                var l = body.document.layers[n];
                                l.Menu = container.menus[i];
                                l.menuHiliteBgColor = proto.menuHiliteBgColor;
                                l.document.bgColor = proto.menuItemBgColor;
                                l.saveColor = proto.menuItemBgColor;
                                l.onmouseover = proto.onMenuItemOver;
                                l.onclick = proto.onMenuItemAction;
                                l.action = container.menus[i].actions[n];
                                l.focusItem = body.document.layers[body.document.layers.length-1];
                                l.clip.width = proto.menuWidth || body.clip.width + proto.menuItemIndent;
                                l.clip.height = proto.menuItemHeight || l.clip.height;
                                if (n>0) l.top = body.document.layers[n-1].top + body.document.layers[n-1].clip.height + proto.menuItemBorder;
                                l.hilite = l.document.layers[1];
                                if (proto.bgImageUp) l.background.src = proto.bgImageUp;
                                l.document.layers[1].isHilite = true;
                                if (l.document.layers[0].id.indexOf("menuSeparator") != -1) {
                                        l.hilite = null;
                                        l.clip.height -= l.clip.height / 2;
                                        l.document.layers[0].document.bgColor = proto.bgColor;
                                        l.document.layers[0].clip.width = l.clip.width -2;
                                        l.document.layers[0].clip.height = 1;
                                        l.document.layers[1].document.bgColor = proto.menuLiteBgColor;
                                        l.document.layers[1].clip.width = l.clip.width -2;
                                        l.document.layers[1].clip.height = 1;
                                        l.document.layers[1].top = l.document.layers[0].top + 1;
                                } else if (l.document.layers.length > 2) {
                                        l.childMenu = container.menus[i].items[n].menuLayer;
                                        l.document.layers[2].left = l.clip.width -13;
                                        l.document.layers[2].top = (l.clip.height / 2) -4;
                                        l.document.layers[2].clip.left += 3;
                                        l.Menu.childMenus[l.Menu.childMenus.length] = l.childMenu;
                                }
                        }
                        body.document.bgColor = proto.bgColor;
                        body.clip.width  = l.clip.width +proto.menuBorder;
                        body.clip.height = l.top + l.clip.height +proto.menuBorder;
                        var focusItem = body.document.layers[n];
                        focusItem.clip.width = body.clip.width;
                        focusItem.Menu = l.Menu;
                        focusItem.top = -30;
            focusItem.captureEvents(Event.MOUSEDOWN);
            focusItem.onmousedown = onMenuItemDown;
                        menu.document.bgColor = proto.menuBorderBgColor;
                        var lite = menu.document.layers[0];
                        lite.document.bgColor = proto.menuLiteBgColor;
                        lite.clip.width = body.clip.width +1;
                        lite.clip.height = body.clip.height +1;
                        menu.clip.width = body.clip.width + (proto.menuBorder * 3) ;
                        menu.clip.height = body.clip.height + (proto.menuBorder * 3);
                }
        } else {
                if ((!document.all) && (container.hasChildNodes)) {
                        container.innerHTML=content;
                } else {
                        container.document.open("text/html");
                        container.document.writeln(content);
                        container.document.close();
                }
                if (!FIND("menuLayer0")) return;
                var menuCount = 0;
                for (var x=0; x<container.menus.length; x++) {
                        var menuLayer = FIND("menuLayer" + x);
                        container.menus[x].menuLayer = "menuLayer" + x;
                        menuLayer.Menu = container.menus[x];
                        menuLayer.Menu.container = "menuLayer" + x;
                        menuLayer.style.zIndex = 1;
                    var s = menuLayer.style;
                        s.top = s.pixelTop = -300;
                        s.left = s.pixelLeft = -300;

                        var menu = container.menus[x];
                        menu.menuItemWidth = menu.menuWidth || menu.menuIEWidth || 140;
                        menuLayer.style.backgroundColor = menu.menuBorderBgColor;
                        var top = 0;
                        for (var i=0; i<container.menus[x].items.length; i++) {
                                var l = FIND("menuItem" + menuCount);
                                l.Menu = container.menus[x];
                                if (l.addEventListener) { // ns6
                                        l.style.width = menu.menuItemWidth;
                                        l.style.height = menu.menuItemHeight;
                                        l.style.top = top;
                                        l.addEventListener("mouseover", onMenuItemOver, false);
                                        l.addEventListener("click", onMenuItemAction, false);
                                        l.addEventListener("mouseout", mouseoutMenu, false);
                                } else { //ie
                                        l.style.pixelWidth = menu.menuItemWidth;
                                        l.style.pixelHeight = menu.menuItemHeight;
                                        l.style.pixelTop = top;
                                }
                                top = top + menu.menuItemHeight+menu.menuItemBorder;
                                l.style.fontSize = menu.fontSize;
                                l.style.backgroundColor = menu.menuItemBgColor;
                                l.style.visibility = "inherit";
                                l.saveColor = menu.menuItemBgColor;
                                l.menuHiliteBgColor = menu.menuHiliteBgColor;
                                l.action = container.menus[x].actions[i];
                                l.hilite = FIND("menuItemHilite" + menuCount);
                                l.focusItem = FIND("focusItem" + x);
                                l.focusItem.style.pixelTop = l.focusItem.style.top = -30;
                                var childItem = FIND("childMenu" + menuCount);
                                if (childItem) {
                                        l.childMenu = container.menus[x].items[i].menuLayer;
                                        childItem.style.pixelLeft = childItem.style.left = menu.menuItemWidth -11;
                                        childItem.style.pixelTop = childItem.style.top =(menu.menuItemHeight /2) -4;
                                        //childItem.style.pixelWidth = 30 || 7;
                                        //childItem.style.clip = "rect(0 7 7 3)";
                                        l.Menu.childMenus[l.Menu.childMenus.length] = l.childMenu;
                                }
                                var sep = FIND("menuSeparator" + menuCount);
                                if (sep) {
                                        sep.style.clip = "rect(0 " + (menu.menuItemWidth - 3) + " 1 0)";
                                        sep.style.width = sep.style.pixelWidth = menu.menuItemWidth;
                                        sep.style.backgroundColor = menu.bgColor;
                                        sep = FIND("menuSeparatorLite" + menuCount);
                                        sep.style.clip = "rect(1 " + (menu.menuItemWidth - 3) + " 2 0)";
                                        sep.style.width = sep.style.pixelWidth = menu.menuItemWidth;
                                        sep.style.backgroundColor = menu.menuLiteBgColor;
                                        l.style.height = l.style.pixelHeight = menu.menuItemHeight/2;
                                        l.isSeparator = true
                                        top -= (menu.menuItemHeight - l.style.pixelHeight)
                                } else {
                                        l.style.cursor = "hand"
                                }
                                menuCount++;
                        }
                        menu.menuHeight = top-1;
                        var lite = FIND("menuLite" + x);
                        var s = lite.style;
                        s.height = s.pixelHeight = menu.menuHeight +(menu.menuBorder * 2);
                        s.width = s.pixelWidth = menu.menuItemWidth + (menu.menuBorder * 2);
                        s.backgroundColor = menu.menuLiteBgColor;

                        var body = FIND("menuFg" + x);
                        s = body.style;
                        s.height = s.pixelHeight = menu.menuHeight + menu.menuBorder;
                        s.width = s.pixelWidth = menu.menuItemWidth + menu.menuBorder;
                        s.backgroundColor = menu.bgColor;

                        s = menuLayer.style;
                        s.width = s.pixelWidth  = menu.menuItemWidth + (menu.menuBorder * 4);
                        s.height = s.pixelHeight  = menu.menuHeight+(menu.menuBorder*4);
                }
        }
        if (document.captureEvents) {
                document.captureEvents(Event.MOUSEUP);
        }
        if (document.addEventListener) {
                document.addEventListener("mouseup", onMenuItemOver, false);
        }
        if (document.layers && window.innerWidth) {
                window.onresize = NS4resize;
                window.NS4sIW = window.innerWidth;
                window.NS4sIH = window.innerHeight;
        }
        document.onmouseup = mouseupMenu;
        window.fwWroteMenu = true;
        status = "";
}

function NS4resize() {
        if (NS4sIW < window.innerWidth ||
                NS4sIW > window.innerWidth ||
                NS4sIH > window.innerHeight ||
                NS4sIH < window.innerHeight )
        {
                window.location.reload();
        }
}

function onMenuItemOver(e, l) {
        FW_clearTimeout();
        l = l || this;
        a = window.ActiveMenuItem;
        if (document.layers) {
                if (a) {
                        a.document.bgColor = a.saveColor;
                        if (a.hilite) a.hilite.visibility = "hidden";
                        if (a.Menu.bgImageOver) {
                                a.background.src = a.Menu.bgImageUp;
                        }
                        a.focusItem.top = -100;
                        a.clicked = false;
                }
                if (l.hilite) {
                        l.document.bgColor = l.menuHiliteBgColor;
                        l.zIndex = 1;
                        l.hilite.visibility = "inherit";
                        l.hilite.zIndex = 2;
                        l.document.layers[1].zIndex = 1;
                        l.focusItem.zIndex = this.zIndex +2;
                }
                if (l.Menu.bgImageOver) {
                        l.background.src = l.Menu.bgImageOver;
                }
                l.focusItem.top = this.top;
                l.Menu.hideChildMenu(l);
        } else if (l.style && l.Menu) {
                if (a) {
                        a.style.backgroundColor = a.saveColor;
                        if (a.hilite) a.hilite.style.visibility = "hidden";
                        if (a.Menu.bgImageUp) {
                                a.style.background = "url(" + a.Menu.bgImageUp +")";;
                        }
                }
                if (l.isSeparator) return;
                l.style.backgroundColor = l.menuHiliteBgColor;
                l.zIndex = 1;  // magic IE 4.5 mac happy doohicky.        jba
                if (l.Menu.bgImageOver) {
                        l.style.background = "url(" + l.Menu.bgImageOver +")";
                }
                if (l.hilite) {
                        l.style.backgroundColor = l.menuHiliteBgColor;
                        l.hilite.style.visibility = "inherit";
                }
                l.focusItem.style.top = l.focusItem.style.pixelTop = l.style.pixelTop;
                l.focusItem.style.zIndex = l.zIndex +1;
                l.Menu.hideChildMenu(l);
        } else {
                return; // not a menu - magic IE 4.5 mac happy doohicky.  jba
        }
        window.ActiveMenuItem = l;
}

function onMenuItemAction(e, l) {
        l = window.ActiveMenuItem;
        if (!l) return;
        hideActiveMenus();
        if (l.action) {
                eval("" + l.action);
        }
        window.ActiveMenuItem = 0;
}

function FW_clearTimeout()
{
        if (fwHideMenuTimer) clearTimeout(fwHideMenuTimer);
        fwHideMenuTimer = null;
        fwDHFlag = false;
}
function FW_startTimeout()
{
        fwStart = new Date();
        fwDHFlag = true;
        fwHideMenuTimer = setTimeout("fwDoHide()", 100);
}

function fwDoHide()
{
        if (!fwDHFlag) return;
        var elapsed = new Date() - fwStart;
        if (elapsed < 200) {
                fwHideMenuTimer = setTimeout("fwDoHide()", 1100-elapsed);
                return;
        }
        fwDHFlag = false;
        hideActiveMenus();
        window.ActiveMenuItem = 0;
}

function FW_showMenu(menu, x, y, child) {
        if (!window.fwWroteMenu) return;
        FW_clearTimeout();
        if (document.layers) {
                if (menu) {
                        var l = menu.menuLayer || menu;
                        l.left = 1;
                        l.top = 1;
                        hideActiveMenus();
                        if (this.visibility) l = this;
                        window.ActiveMenu = l;
                } else {
                        var l = child;
                }
                if (!l) return;
                for (var i=0; i<l.layers.length; i++) {
                        if (!l.layers[i].isHilite)
                                l.layers[i].visibility = "inherit";
                        if (l.layers[i].document.layers.length > 0)
                                FW_showMenu(null, "relative", "relative", l.layers[i]);
                }
                if (l.parentLayer) {
                        if (x != "relative")
                                l.parentLayer.left = x || window.pageX || 0;
                        if (l.parentLayer.left + l.clip.width > window.innerWidth)
                                l.parentLayer.left -= (l.parentLayer.left + l.clip.width - window.innerWidth);
                        if (y != "relative")
                                l.parentLayer.top = y || window.pageY || 0;
                        if (l.parentLayer.isContainer) {
                                l.Menu.xOffset = window.pageXOffset;
                                l.Menu.yOffset = window.pageYOffset;
                                l.parentLayer.clip.width = window.ActiveMenu.clip.width +2;
                                l.parentLayer.clip.height = window.ActiveMenu.clip.height +2;
                                if (l.parentLayer.menuContainerBgColor) l.parentLayer.document.bgColor = l.parentLayer.menuContainerBgColor;
                        }
                }
                l.visibility = "inherit";
                if (l.Menu) l.Menu.container.visibility = "inherit";
        } else if (FIND("menuItem0")) {
                var l = menu.menuLayer || menu;
                hideActiveMenus();
                if (typeof(l) == "string") {
                        l = FIND(l);
                }
                window.ActiveMenu = l;
                var s = l.style;
                s.visibility = "inherit";
                if (x != "relative")
                        s.left = s.pixelLeft = x || (window.pageX + document.body.scrollLeft) || 0;
                if (y != "relative")
                        s.top = s.pixelTop = y || (window.pageY + document.body.scrollTop) || 0;
                l.Menu.xOffset = document.body.scrollLeft;
                l.Menu.yOffset = document.body.scrollTop;
        }
        if (menu) {
                window.activeMenus[window.activeMenus.length] = l;
        }
}

function onMenuItemDown(e, l) {
        var a = window.ActiveMenuItem;
        if (document.layers) {
                if (a) {
                        a.eX = e.pageX;
                        a.eY = e.pageY;
                        a.clicked = true;
                }
    }
}

function mouseupMenu(e)
{
        hideMenu(true, e);
        hideActiveMenus();
        return true;
}

function mouseoutMenu()
{
        hideMenu(false, false);
        return true;
}


function hideMenu(mouseup, e) {
        var a = window.ActiveMenuItem;
        if (a && document.layers) {
                a.document.bgColor = a.saveColor;
                a.focusItem.top = -30;
                if (a.hilite) a.hilite.visibility = "hidden";
                if (mouseup && a.action && a.clicked && window.ActiveMenu) {
                         if (a.eX <= e.pageX+15 && a.eX >= e.pageX-15 && a.eY <= e.pageY+10 && a.eY >= e.pageY-10) {
                                setTimeout('window.ActiveMenu.Menu.onMenuItemAction();', 2);
                        }
                }
                a.clicked = false;
                if (a.Menu.bgImageOver) {
                        a.background.src = a.Menu.bgImageUp;
                }
        } else if (window.ActiveMenu && FIND("menuItem0")) {
                if (a) {
                        a.style.backgroundColor = a.saveColor;
                        if (a.hilite) a.hilite.style.visibility = "hidden";
                        if (a.Menu.bgImageUp) {
                                a.style.background = "url(" + a.Menu.bgImageUp +")";;
                        }
                }
        }
        if (!mouseup && window.ActiveMenu) {
                if (window.ActiveMenu.Menu) {
                        if (window.ActiveMenu.Menu.hideOnMouseOut) {
                                FW_startTimeout();
                        }
                        return(true);
                }
        }
        return(true);
}

function PxToNum(pxStr)
{ // pxStr == 27px, we want 27.
        if (pxStr.length > 2) {
                n = Number(pxStr.substr(0, pxStr.length-2));
                return(n);
        }
        return(0);
}

function hideChildMenu(hcmLayer) {
        FW_clearTimeout();
        var l = hcmLayer;
        for (var i=0; i < l.Menu.childMenus.length; i++) {
                var theLayer = l.Menu.childMenus[i];
                if (document.layers) {
                        theLayer.visibility = "hidden";
                } else {
                        theLayer = FIND(theLayer);
                        theLayer.style.visibility = "hidden";
                }
                theLayer.Menu.hideChildMenu(theLayer);
        }

        if (l.childMenu) {
                var childMenu = l.childMenu;
                if (document.layers) {
                        l.Menu.FW_showMenu(null,null,null,childMenu.layers[0]);
                        childMenu.zIndex = l.parentLayer.zIndex +1;
                        childMenu.top = l.top + l.parentLayer.top + l.Menu.menuLayer.top + l.Menu.menuItemHeight/3;
                        if (childMenu.left + childMenu.clip.width > window.innerWidth) {
                                childMenu.left = l.parentLayer.left - childMenu.clip.width + l.Menu.menuLayer.left + 15;
                                l.Menu.container.clip.left -= childMenu.clip.width;
                        } else {
                                childMenu.left = l.parentLayer.left + l.parentLayer.clip.width  + l.Menu.menuLayer.left -5;
                        }
                        var w = childMenu.clip.width+childMenu.left-l.Menu.container.clip.left;
                        if (w > l.Menu.container.clip.width)
                                l.Menu.container.clip.width = w;
                        var h = childMenu.clip.height+childMenu.top-l.Menu.container.clip.top;
                        if (h > l.Menu.container.clip.height) l.Menu.container.clip.height = h;
                        l.document.layers[1].zIndex = 0;
                        childMenu.visibility = "inherit";
                } else if (FIND("menuItem0")) {
                        childMenu = FIND(l.childMenu);
                        var menuLayer = FIND(l.Menu.menuLayer);
                        var s = childMenu.style;
                        s.zIndex = menuLayer.style.zIndex+1;
                        if (document.all) { // ie case.
                                s.pixelTop = l.style.pixelTop + menuLayer.style.pixelTop + l.Menu.menuItemHeight/3;
                                s.left = s.pixelLeft = (menuLayer.style.pixelWidth) + menuLayer.style.pixelLeft -5;
                        } else { // zilla case
                                var top = PxToNum(l.style.top) + PxToNum(menuLayer.style.top) + l.Menu.menuItemHeight/3;
                                var left = (PxToNum(menuLayer.style.width)) + PxToNum(menuLayer.style.left) -5;
                                s.top = top;
                                s.left = left;
                        }
                        childMenu.style.visibility = "inherit";
                } else {
                        return;
                }
                window.activeMenus[window.activeMenus.length] = childMenu;
        }
}

function hideActiveMenus() {
        if (!window.activeMenus) return;
        for (var i=0; i < window.activeMenus.length; i++) {
                if (!activeMenus[i]) continue;
                if (activeMenus[i].visibility && activeMenus[i].Menu) {
                        activeMenus[i].visibility = "hidden";
                        activeMenus[i].Menu.container.visibility = "hidden";
                        activeMenus[i].Menu.container.clip.left = 0;
                } else if (activeMenus[i].style) {
                        var s = activeMenus[i].style;
                        s.visibility = "hidden";
                        s.left = -200;
                        s.top = -200;
                }
        }
        if (window.ActiveMenuItem) {
                hideMenu(false, false);
        }
        window.activeMenus.length = 0;
}

        ~;
        exit;


}




sub get_css{
        print "Content-type: text/css\n\n";
        print   qq~

a:link    {
  text-decoration:  none;
  font-weight: normal;
  color:            black;
  font: normal 8pt Verdana, Arial, Helvetica, sans-serif;
  }
a:visited {
  text-decoration:  none;
  font-weight: normal;
  color:            black;
  font: normal 8pt Verdana, Arial, Helvetica, sans-serif;
  }
a:hover   {
  text-decoration:  none;
  font-weight: normal;
  color:            black;
  font: normal 8pt Verdana, Arial, Helvetica, sans-serif;
  }
a:active  {
  text-decoration:  none;
  font-weight:      normal;
  color: black;
  text-decoration: none;
  font: normal 8pt Verdana, Arial, Helvetica, sans-serif;
  }

a.Menucss:link    {
  text-decoration:  none;
  font-weight: bold;
  color:            black;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
a.Menucss:visited {
  text-decoration:  none;
  font-weight: bold;
  color:            black;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
#navigation {
text-align: center;
float: left;
}
#navigation ul {
        font-family: Verdana;
        font-size: 12px;
        font-weight: bold;
        text-decoration: none;
        margin: 0;
        padding: 0;
        list-style:none;
}
#navigation li {
        display: inline;
        background: url($htmlDataFolder/tbbg.png) repeat-x center top;
        text-align: center;
        padding: 0;
        margin-right: 4px;
        float: left;
}
#navigation a {
        color: Black;
        background: url($htmlDataFolder/tbleft.png) no-repeat left top;
        float: left;
        margin:        0;
        padding-left:7px;
        text-decoration: none;
}
#navigation a span {
        background: url($htmlDataFolder/tbright.png) no-repeat right top;
        display: block;
        padding:7px 13px 4px 5px;
}
#navigation a span {
        float: none;
}

td, th, body {font-family: Verdana, Arial; font-size:8pt;}
            input, select {font-family: Verdana, Arial; font-size:8pt;}
            .button {font-size:7pt;width:''}
        .titel  {font-family: Verdana, Arial; font-size:10pt; font-weight:bolder; color: #999999}
        .of {border-style:solid; border-width: 1; background-color:#dddddd; border-color : #7c96af; font-size:8pt}
        .off {border-style:none;background-color:#f3f3f3}
        .border {border-style:solid; border-width: 1; border-color: #7c96af;}
        .selected {border-style:none;background-color:#ff6666}
        .error {color: #ff0000; text-align: center;  font-size:12pt;}
.headline {border-style:solid; border-width: 1; border-color : #7C96AF; background-color:#dddddd;}
.controlpanel {border-style:solid; border-width: 1; border-color : #DDDDDD; background-color:#EEEEEE;}
.misc_header {font-family: Verdana, Arial; font-size:7.5pt; font-weight:bolder;}
.test {border-style:solid; border-width: 1; border-color : #000000; background-color:#EEEEEE;}
.head_line {padding-bottom: 13;}
 ~;
 exit;

}
