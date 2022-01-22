#!/usr/local/bin/perl5.22
use CGI::Carp qw(fatalsToBrowser);
($script=$0) =~s!^.*[/\\]!!;

##########################################################################
# i Dot Communications © 2005-2007 Copyright Mark Roberts / Alexandre Golovkine

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
# http://www.idotcommunications.co.uk/site.php?page=TechnicalSupport
##########################################################################

####Administrator Username And Password############################

#Admin Username / Password Account Number 1

my $AdminLogin = {
        "trinityprescott" =>"tpadmin",
        "davidprescott" =>"dpadmin",
        "agent" =>"office",
};

#You may specify up to 3 Admin accounts.
#E.g. "Mark" =>"12345",

#PLEASE NOTE: THE USER NAME AND PASSWORDS YOU ENTER IN THE MANAGER.PL SCRIPT
#MUST BE THE SAME AS THE ONES YOU SPECIFY IN THE MANAGER.PL SCRIPT.

###################################################################

####Main Client Manager Script:####################################

my $parentScript = "Manager.pl";
#Do not modify the Main Client Manager Script name unless told to do so by iDC Support.

###################################################################

####Main Login Script:#############################################

my $LoginScript = "Login.pl";
#Do not modify the Main Login Script name unless told to do so by iDC Support.

###################################################################

####Main Clients Directory################################################

my $rootHomeDir = "/usr/home/starting2014/public_html/surflocal.net/Clients/";
#Change the path to the "Main Clients Directory" to your servers path to the Main Root Directory + The sub-folderof the File Manager folder which will hold all your Clients folders.
#For example:
#e.g. Main Clients Directory ("/home/mysite/public_html/") +  Main File Manager Directory (FileManager) + "Clients"

##########################################################################

####Email Configuration############################################

#Configure the email settings so that the File Manager can send account signup details
#and notify you when new files have been uploaded

my $fromAdmin = 'trinity@surflocal.net';     #From Email Address
my $toAdmin   = 'trinity@surflocal.net';    #Email Adress you want to receive upload confirmations
my $mailprog  = '/usr/lib/sendmail';     #SendMail Path
my $subject   = 'Your Account Details';     #Email Subject Title
my $msg_foot  = '';                         #Email Footer / Signature (Left Blank if using HTMl Emails)
my $send_as_html = 1;                       #Change to "1" to send an html formatted email
my $msg_body_file = "SignupEmail.shtml";    #Specify the html upload email template

my $sendConfirmAccount = "0";  #Change to "1" to send automatic account details

####Advanced Email Configuration###################################
#SMTP email, uncomment next line to use it
# use Net::SMTP;
my $send_via_SMTP            = 0;
my $mailhost                 = 'smtp.com';
###################################################################

####User Database##################################################
my $userTable ="users.txt"; #format id|login|password|email|dir|quote|disabled_files|rights
#Do not modify the User Database settings unless told to do so by iDC Support.
###################################################################

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

#####Control Panel Links Configuration#############################
my $NameLink1 = "Link 1";
my $Link1 = "http://www.yoursite.com/link1.html";
my $NameLink2 = "Link 2";
my $Link2 = "http://www.yoursite.com/link2.html";
my $NameLink3 = "Link 3";
my $Link3 = "http://www.yoursite.com/link3.html";
my $NameLink4 = "Link 4";
my $Link4 = "http://www.yoursite.com/link4.html";
my $NameLink5 = "Link 5";
my $Link5 = "http://www.yoursite.com/link5.html";
###################################################################

#####Session Timeout###############################################
my $timeOut = "";
#You may configure (if required) the session timeout period.
#If no mouse or keyboard activity is detected in the specified time frame the user will be logged out.
###################################################################

####Main Image Directory###########################################
my $htmlDataFolder = "http://www.surflocal.net/FileManagerData";
#Change the url to the "Main Image Directory" to your servers url to the File Manager Image Directory
#For example:
#e.g. Main Main Image Directory ("http://www.yoursite.com/FileManagerData")
###################################################################


####Control Panel Images###########################################
my $controlpanellogo = "$htmlDataFolder/ClientManagerLogo.png";
my $controlpanelmainheader = "$htmlDataFolder/controlpanelheader.png";
my $controlpanelheaderwedge = "$htmlDataFolder/headerwedge.png";
my $controlpanelcontolbaricon = "$htmlDataFolder/contolbaricon.png";
####################################################################

####Arrow Up#######################################################
my $arrow_up="<img src=$htmlDataFolder/arrow_up.gif border=0  align=texttop>";
####Arrow Down Image ##############################################
my $arrow_down="<img src=$htmlDataFolder/arrow_down.gif border=0  align=texttop>";
###################################################################


#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!
#DO NOT MODIFY BELOW THIS LINE!!!!!!


###################################################################
use File::Path;
use CGI qw(:standard :cgi-lib);
my @params=param;
my %FORM;
for(@params){$FORM{$_}=join ",", param($_);}
my $useFileManagerLogin = 1;
my $cookName = $useFileManagerLogin ? "USER_Login" : "File_USER_Login";
%COOKIES = get_cookie($cookName);
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
my $charset="; charset=ISO-8859-1" if $FORM{'language'} eq 'nr';
my $charset="; charset=ISO-8859-7" if $FORM{'language'} eq 'gr';
my $charset="; charset=windows-1251" if $FORM{'language'} eq 'ru';

%Message = get_messages($languageFile{$FORM{'language'}});

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


$FORM{action} ||= 'users';

#######password protection#############
my $Rights={};
if($FORM{log_in}){
        if($AdminLogin->{$FORM{login}} && $AdminLogin->{$FORM{login}} eq  $FORM{password}){
                print "Set-Cookie: $cookName=login&$FORM{login}&pass&$FORM{password}&language&$FORM{language}; path=/\n";
                print "Location: $script?\n\n";
                exit;
        }
        else{error("$Message{incorrect_login}");}
}
elsif(!$COOKIES{login}){promt();}
elsif($AdminLogin->{$COOKIES{login}} eq   $COOKIES{pass}){$home=$rootHomeDir; $myAdmin=1; @$Rights{("w","c","m","d","r","u","p","n")} = (1,1,1,1,1,1,1,1);}
else{promt();}
#######password protection#############

logout()  if $FORM{action} eq 'logout';
$FORM{option} ||="name";

%SUB = (
        userarea  => \&userarea,
        users     => \&users,
        get_css   => \&get_css,
);

$SUB{$FORM{action}}->() if $FORM{action} && $SUB{$FORM{action}};


print "Cache-control: no-cache\n";
print "Pragma: no-cache\n";
print "Content-type: text/html$charset\n\n";
my $content=1;


###################################################
sub createPass{
        my $password = shift;
        my $string = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM";
        my @chars=split(//,$string);
        my $crypt = $chars[int(rand(@chars-1))].$chars[int(rand(@chars-1))];
        return crypt($password,$crypt);
}


sub closeWnd {
print "Content-type: text/html$charset\n\n";
                print "<html>
                <script>
                function go(){
                        opener.location.reload();
                        window.close();
                }
                </script>
                <body onload=go()></body></html>";
                exit;
}

sub users{
        return unless $myAdmin;
        my $text;
        my @data = read_file($userTable);
        my $headLine=shift @data;
        if($FORM{item} eq 'save'){
                $ID =1; my $found = 0; my $uLogin=0;
                my %id; my @id=param('id');
                for(@id){$id{$_}=1;}
                foreach(@data){
                        my $line = $_;
                        chomp $line;
                        ($userId, $userLogin, $userPass, $userEmail, $userDir, $disabledFiles, $rights)=split('\|', $line);
                        if ($id{$userId}){
                                my $cryptuserPass = $FORM{userPassword} ? createPass($FORM{userPassword}) : $userPass;
                                if(@id>1){$FORM{userLogin}=$userLogin; $FORM{userEmail}=$userEmail;}
                                elsif($userLogin eq $FORM{userLogin}){$uLogin++;}
                                $_ = "$userId|$FORM{userLogin}|$cryptuserPass|$FORM{userEmail}|$FORM{userDir}|$FORM{discQuota}|$FORM{disabledFiles}|$FORM{rights}|$FORM{disabled}\n";
                                $found=1;
                        }
                        $ID = $userId if $ID<$userId;
                }
                error("Login &lt;$FORM{userLogin}&gt; already exist!", 1) if $uLogin>1;
                if($found){
                        open(F, ">$userTable") or error("Can't open users file");
                        mkpath("$home/$FORM{userDir}", 0, 0755) unless -d "$home/$FORM{userDir}";
                        print F $headLine;
                        print F join('', @data);
                        close F;
                        closeWnd();
                }

                error("record not found",1) if $FORM{id};
                $ID++;

                error("Please Set Password!",1) unless $FORM{userPassword};
                foreach(@data){
                        my $line = $_;
                        chomp $line;
                        ($userId, $userLogin, $userPass, $userEmail, $userDir, $disabledFiles, $rights)=split('\|', $line);
                        if ($FORM{userLogin} eq $userLogin){
                                error("Login &lt;$FORM{userLogin}&gt; already exist!", 1);
                        }

                }




                $userPass = $FORM{userPassword};
                $FORM{userPassword} = createPass($FORM{userPassword});
                open(F, ">>$userTable") or error($Message{err_open_file});
                mkpath("$home/$FORM{userDir}", 0, 0755) unless -d "$home/$FORM{userDir}";
                print F "$ID|$FORM{userLogin}|$FORM{userPassword}|$FORM{userEmail}|$FORM{userDir}|$FORM{discQuota}|$FORM{disabledFiles}|$FORM{rights}|$FORM{disabled}\n";
                close F;

                #####rights
                @$uR{split(',',$FORM{rights})} = split(',',$FORM{rights});
                my $userRights = " $Message{upload} [";
                $userRights.= $uR->{'u'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= " $Message{move} / $Message{copy} [";
                $userRights.= $uR->{'m'} ? 'yes' : 'no';
                $userRights.= "]\n";
                                $userRights.= "  $Message{download} / $Message{preview} / $Message{hotlink} [";
                $userRights.= $uR->{'r'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{rename} [";
                $userRights.= $uR->{'a'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{pack} / $Message{unpack} / $Message{batch_download_zip} [";
                $userRights.= $uR->{'p'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{editor} [";
                $userRights.= $uR->{'w'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{chmod} [";
                $userRights.= $uR->{'c'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{mkdir}  [";
                $userRights.= $uR->{'n'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{notes}  [";
                $userRights.= $uR->{'l'} ? 'yes' : 'no';
                $userRights.= "]\n";
                $userRights.= "  $Message{delete}  [";
                $userRights.= $uR->{'d'} ? 'yes' : 'no';
                $userRights.= "]\n";
                ########

                $message = "Client Login: $FORM{userLogin}\nClient Password: $userPass\nDisk Quota: $FORM{discQuota}Mb.\nDisabled Files: $FORM{disabledFiles}\nRights:\n$userRights \n\n";

                if($send_as_html){
                        $FORM{password}= $userPass;
                        $FORM{userPassword}= $userPass;
                        $FORM{ID}=$ID;
                        $FORM{rights}=$userRights;
                        $message = get_record(\%FORM, join '',read_file($msg_body_file));
                }
                male($FORM{userEmail}, $fromAdmin, $subject, $message.$msg_foot) if $FORM{userEmail} && $sendConfirmAccount;
                 closeWnd();
        }
        if($FORM{item} eq 'delete'){#print "Content-type: text/html$charset\n\n";
                my %id;
                for(param('id')){$id{$_}=1;}
                foreach(@data){
                        ($userId, $userLogin, $userPass, $userEmail, $userDir)=split('\|', $_);
                        $_ = '' if $id{$userId};
                }
                open(F, ">$userTable") or error($Message{err_open_file});
                print F $headLine;
                print F join('',@data);
                close F;

                print "Location: $script?action=users\n\n";
                exit;

        }

        if($FORM{item} eq 'add'){
                my $title="$Message{new_client}";
                my %id; my @id=param('id');
                for(@id){$id{$_}=1;}

                if ($FORM{id}){
                        foreach(@data){
                                chomp;
                                my @row=split('\|', $_);
                                if($id{$row[0]}){
                                        ($userId, $userLogin, $userPass, $userEmail, $userDir, $discQuota, $disabledFiles, $rights, $isDisabled)=@row;
                                        $text.="<input type=hidden name=id value=$userId>";
                                        $id{$userId} = $userLogin;

                                }
                        }
                        $userPass = "<br><small>($Message{leave_blank}.)</small>";
                        $title ="$Message{edit_client}";

                }

                my $Rights={};
                for(split(',',$rights)){$Rights->{$_} = 'checked' if $_;}

                my $noEdit = "";
                if (@id>1){
                        $noEdit = " disabled";
                        $userLogin = join (', ', values (%id));
                        $userEmail = '';
                }


                $text.=qq~<br><br><br><input type=hidden name=item value=save><table width=80% align=center>
                <tr><td class=headline align=center colspan=2><b>$title</b></td></tr>
                <tr><td>$Message{login}:</td><td><input type=text name=userLogin value="$userLogin" $noEdit></td></tr>
                <tr><td valign=top>$Message{password}:</td><td><input type=text name=userPassword $noEdit> $userPass</td></tr>
                <tr><td>$Message{email}:</td><td><input type=text name=userEmail value="$userEmail" $noEdit></td></tr>
                <tr><td>$Message{directory}:</td><td><b>/</b><input type=text name=userDir style=width:180pt value="$userDir"></td></tr>
                <tr><td>$Message{disc_quota}:</td><td><input type=text name=discQuota style=width:40pt value="$discQuota"> Mb.</td></tr>
                <tr><td valign=top>$Message{disabled_files}:</td><td><input type=text name=disabledFiles style=width:180pt value="$disabledFiles"><br><small>(eg: exe,pl,cgi)</small></td></tr>
                <tr><td colspan=2>
                Rights: <br>
                <table border=0 cellpadding=0 width=100%><tr>
                <tr>
                <td><input type=checkbox name=rights value=u $Rights->{'u'}>$Message{upload}</td>
                <td><input type=checkbox name=rights value=m $Rights->{'m'}>$Message{move} / $Message{copy}</td>
                </tr>
                <tr>
                <td><input type=checkbox name=rights value=r $Rights->{'r'}>$Message{download} / $Message{preview} / $Message{hotlink}</td>
                <td><input type=checkbox name=rights value=a $Rights->{'a'}>$Message{rename}</td>
                </tr>
                <tr>
                <td><input type=checkbox name=rights value=p $Rights->{'p'}>$Message{pack} / $Message{unpack} / $Message{batch_download_zip}</td>
                <td><input type=checkbox name=rights value=w $Rights->{'w'}>$Message{editor}</td>
                </tr>
                <tr>
                <td><input type=checkbox name=rights value=c $Rights->{'c'}>$Message{chmod}</td>
                <td><input type=checkbox name=rights value=n $Rights->{'n'}>MkDir</td>
                </tr>
                <tr>
                <td><input type=checkbox name=rights value=l $Rights->{'l'}>$Message{notes}</td>
                <td><input type=checkbox name=rights value=d $Rights->{'d'}>$Message{delete}</td>
                <tr>
                <td><input type=checkbox name=disabled value=1 ~.($isDisabled? 'checked':'').qq~>$Message{disabled}</td>
                <td></td>
                <tr>
                </tr></table>


                ~;

                $text .= "<tr><td colspan=2 align=right><input type=submit value='$Message{add_client}'> <input type=button value=$Message{cancel} onclick='window.close()'></td></tr></table>\n";
                html($text,0, "users",  $dir,"$Message{new_client}");
        }



        $opt_r = $FORM{r};
        $opt_{$FORM{option}}="&r=1" unless $FORM{r};
        $arrow{$FORM{option}} = $FORM{r} ? $arrow_up : $arrow_down;



        #order @data

        @data = orderData(\@data,$headLine, $FORM{option},$FORM{r});


        $text = qq~

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<head>
<link rel="STYLESHEET" type="text/css" href="$script?action=get_css">
$timeScript
<style>
body
{
background: url($htmlDataFolder/CMBG.png) repeat-y;
}
</style>


<script type="text/javascript"><!--


function selectAll(){
     if (document.forms[0].all_file.checked){
         for(i=0; i<document.forms[0].user.length; i++) {document.forms[0].user[i].checked = true;}
     }
     else{
         for(i=0; i<document.forms[0].user.length; i++) {document.forms[0].user[i].checked = false;}
     }
}

        function sh(obj){if (obj.className!="selected") obj.className="of";}
        function shh(obj){if (obj.className!="selected") obj.className="off";}

function expandcontent(cid,pic){

document.getElementById(cid).style.display=(document.getElementById(cid).style.display!="none")? "none" : "block"
document.getElementById(pic).src = (document.getElementById(cid).style.display!="block")? "$controlpanelcontolbaricon" : "$controlpanelcontolbaricon"
}

function show(url,height, width, scroll){
       if(!scroll) scroll = "yes";
       newWnd=window.open(url, 'show', "height="+height+", width="+width+", top=100, left=100, status=none, scrollbars="+scroll+", location=none");
       newWnd.focus();
}
function Delete(){
         var filesSelected=0;
         var qs = ""; var users = "";
        for(i=0; i<document.myform.user.length; i++){
               if (document.myform.user[i].checked) {
                             qs += "&id="+escape(document.myform.user[i].value);
                      filesSelected++;
                      if(document.myform.user[i].value){
                              var login = "login_"+document.myform.user[i].value;
                              if (users) users += ", ";
                              users += document.getElementById(login).value;
                      }
               }
        }
        if (filesSelected<1) alert("Please select user");
        if (!confirm("Delete user(s) " + users + "?")) return;
        document.location.href="$script?action=users&item=delete"+qs;

}
function Edit(){
         var filesSelected=0;
         var qs = "";
        for(i=0; i<document.myform.user.length; i++){
               if (document.myform.user[i].checked) {
                             qs += "&id="+escape(document.myform.user[i].value);
                      filesSelected++;
               }
        }
        if (filesSelected<1) {alert("Please select user");}
        else show("$script?action=users&item=add"+qs ,450,680)

}

var url = location.href;
// -->
</script>

</head>

<body bgcolor="#ffffff" alink="#ff0000" link="#0000ff" vlink="#800080" $enableTime>

<div id="Oobj19" style="position:absolute;z-index:1;visibility:visible; left:0px;top:0px;width:100%;height:105px;font-size:1px;">
<img name="Ggeo19" Align=Top SRC="$controlpanelmainheader" alt="" border=0 width="100%" height="105px"></div>

<div id="Oobj21" style="position:absolute;z-index:2;visibility:visible; left:0px;top:80px;width:216px;height:25px;font-size:1px;">
<img name="Ggeo21" Align=Top SRC="$controlpanelheaderwedge" alt="" border=0 width="216px" height="25px"></div>

<div id="Oobj23" style="position:absolute;z-index:3;visibility:visible; left:4px;top:1px;width:220px;height:79px;font-size:1px;">
<img name="Ggeo23" Align=Top SRC="$controlpanellogo" alt="" border=0 width="220px" height="79px"></div>

<div id="Oobj26" style="position:absolute;z-index:5;visibility:visible; left:16px;top:86px;width:201px;height:17px;">
<span id="Grtf26" class="dfltt">
<font face="Verdana" class="fsx01" color="#808080"><B>$Message{controlpanel_title}<br></B></font></span>
</div>

<div id="Oobj27" style="position:absolute;z-index:6;visibility:visible; left:12px;top:116px;width:201px;height:401px;">
<span id="Gcode27" class="dfltt">


<div id="MainMenu">
        <!-- begin submenu --><span>
        <div style="WIDTH: 180px">
            <table class="Menu_Head" cellspacing="0" cellpadding="1">
                <tbody>
                    <tr>
                        <td width="90%" onClick="expandcontent('AccountInfo','image1')" style = "cursor:hand">
                            &nbsp;$Message{accountinfo_title}</td>
                        <td>
                            <img src="$controlpanelcontolbaricon" border="0" id = "image1" onClick="expandcontent('AccountInfo','image1')" />&nbsp;</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="Menu_Items">
            <div id = "AccountInfo">
                <div><a>$Message{domainname_title}: </a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a href="/" target="_blank"><script>document.write (url.substr(11, url.substr(11, url.length).indexOf('/')))</script></a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a>$Message{client_username}: $COOKIES{login}</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a>$Message{usergroup_title}</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
<div><a href="$script?action=logout">$Message{exit}</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
        </span>
        <!-- end sub menu -->
        <br />
        <!-- begin submenu --><span>
        <div style="WIDTH: 180px">
            <table class="Menu_Head" cellspacing="0" cellpadding="1">
                <tbody>
                    <tr>
                        <td width="90%" onClick="expandcontent('AccountManager','image2')" style = "cursor:hand">
                            &nbsp;$Message{usermanager_title}</td>
                        <td>
                            <img src="$controlpanelcontolbaricon" id = "image2" border="0" onClick="expandcontent('AccountManager','image2')" />&nbsp;</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="Menu_Items">
            <div id = "AccountManager">
                        <div><a href="javascript:show('$script?action=users&item=add', 450,680)">$Message{createnew_account}</a>
                        <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a href="javascript:Edit()">$Message{edit_account}</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a href="javascript:Delete()">$Message{remove_account}</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </span>
        <!-- end sub menu -->
        <br />
        <!-- begin submenu --><span>
        <div style="WIDTH: 180px">
            <table class="Menu_Head" cellspacing="0" cellpadding="1">
                <tbody>
                    <tr>
                        <td width="90%" onClick="expandcontent('links','image3')" style = "cursor:hand">
                            &nbsp;$Message{yourlinks_title}</td>
                        <td>
                            <img src="$controlpanelcontolbaricon" id = "image3" border="0"onClick="expandcontent('links','image3')" />&nbsp;</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="Menu_Items">
            <div id = "links">
                <div><a href="$Link1" target="_blank">$NameLink1</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a href="$Link2" target="_blank">$NameLink2</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
                <div><a href="$Link3" target="_blank">$NameLink3</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
<div><a href="$Link4" target="_blank">$NameLink4</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
<div><a href="$Link5" target="_blank">$NameLink5</a>
                    <div class="Description">
                        <div class="DescTitle">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </span>
        <!-- end sub menu -->
    </div>

<div id="Oobj29" style="position:absolute;z-index:7;visibility:visible; left:230px;top:4px;width:229px;height:56px;">
<span id="Gcode29" class="dfltt">

</div>

<div id="Oobj30" style="position:absolute;z-index:8;visibility:visible; left:217px;top:83px;width:79%;height:401px;">
<span id="Gcode30" class="dfltt">
<form name="myform" method="post">

<table width=100% border=0 cellspacing=1  cellpadding=0>
        <tr>
               <td class=head_line width=5%>&nbsp;&nbsp;<input type=checkbox  onclick=selectAll() name="all_file"></td>
               <td class=head_line width=15% height=18 align=center><nobr>&nbsp;$arrow{login}<a href=$script_name?option=login$opt_{login}>$Message{client_username}</a></nobr></td>
               <td class=head_line width=20% height=18 align=center><nobr>&nbsp;$arrow{email}<a href=$script_name?option=email$opt_{email} class=head>$Message{email}</a></nobr></td>
               <td class=head_line width=20% height=18 align=center><nobr>&nbsp;$arrow{dir}<a href=$script_name?option=dir$opt_{dir}>$Message{directory}</a></nobr></td>
               <td class=head_line width=15% height=18 align=center><nobr>&nbsp;$arrow{quote}<a href=$script_name?option=quote$opt_{quote}>$Message{disc_quota}</a></nobr></td>
               <td class=head_line width=15% height=18 align=center><nobr>&nbsp;$arrow{disabled_files}<a href=$script_name?option=disabled_files$opt_{disabled_files}>$Message{disabled_files}</a></nobr></td>
               <td class=head_line width=15% height=18 align=center><nobr>&nbsp;$arrow{disabled_files}<a href=$script_name?option=disabled$opt_{disabled}>$Message{disabled}</a></nobr></td>
       </tr>\n~;

       #print user table
       foreach(@data){
                chomp;
                $_=~s/\r|\n//g;
                ($userId, $userLogin, $userPass, $userEmail, $userDir, $discQuota, $disabledFiles, $uRights, $isDisabled)=split('\|', $_);
                $isDisabled &&="Yes";
                $discQuota .= "$Message{Mb}&nbsp;" if $discQuota;
                $userEmail &&="<a href=\"mailto:$userEmail\">$userEmail</a>";
                $text .= qq~<tr class=off onmouseover="sh(this)" onmouseout="shh(this)"><td align=center><input type="checkbox" name="user" value ="$userId"></td>
                <td align=center>
                <input type=hidden name="login_$userId" value="$userLogin" id="login_$userId">
                $userLogin</td>
                <td align=center>$userEmail</td>
                <td align=center>$userDir</td>
                <td align=center>$discQuota</td>
                <td align=center>$disabledFiles</td>
                <td align=center>$isDisabled</td>
                </tr>\n

        ~;
        }

$text .= "</table><input type=hidden name=user></form></span></div></body></html>\n";

print "Content-type: text/html$charset\n\n";
print $text;
exit;
       # html($text,0, "users",  $dir,"$Message{client_manager}");

}



sub  orderData{
        my @data = @{shift()};
        my $head = shift;
        my $order_by = shift;
        my $r = shift;
        chomp $head;
        my @head = split ('\|',$head);
        my ($pos,$it) = (-1,0);
        for(@head){
                $pos = $i if $_ eq $order_by;
                $i++;
        }
        return @data if $pos<0;
        my %sort; my $data;
        for (@data){
                my @row = split ('\|',$_);
                $sort{$row[0]}=$row[$pos];
                $data->{$row[0]}=$_;
        }
        if ($order_by eq 'id' or $order_by eq 'quote'){@skeys = sort {$sort{$a} <=> $sort{$b}} keys %$data;}
        else{@skeys = sort {lc $sort{$a} cmp lc $sort{$b}} keys %$data;}


        @data=();
        for(@skeys){
                push @data, $data->{$_};
        }
        @data = reverse @data if $r;

        return @data;

}


sub logout{
        print "Set-Cookie: $cookName=; path=/\n";
        print "Location: $script\n\n";
        exit;
}

sub promt{
        print "Content-type: text/html$charset\n\n";
        my $txt= qq|<HTML>

<head>
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
                <form method=post action="$script">
                <input type=hidden name=action value="$_[2]">
                <input type=hidden name=dir value="$_[3]">
                $_[0]
                </form>~;

        print "</body></html>";
        exit;
}



sub error{

        print "Content-Type: text/html$charset\n\n" unless $content;
        print qq~<html><head><title>FileManager::Error</title><link rel="STYLESHEET" type="text/css" href="$script?action=get_css"></head><body>~;
        print "<table align=center height=60%><tr><td align=center><b class=error>$_[0]</b></td></tr>";
        print "<tr><td align=center><a href=javascript:history.back()>Back</a></td></tr>" if $_[1];
        print "</table>";

        print "</body></html>";
        exit;

}



sub get_messages{
        my %Mess;
        open (MESS, $_[0]) or error("Can't not open message-file");
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


sub get_record{
        my %INSERT = %{shift()};
        my $text = shift;
        $text =~ s{\[\[(.*?)\]\]}{exists($INSERT{$1}) ? $INSERT{$1} : ""}gsex;
        return $text;
}



sub error_right{
        #my $mess = shift;
        error ($Message{"no_right"}) ;
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


sub get_css{
        print "Content-type: text/css\n\n";
        print   qq~

.fsx01 {font-size: 11px;}
.txdec {text-decoration: none;}
.dfltt {font-family:Arial;font-size:10px;font-weight:normal;text-decoration:none;text-align:left;}
body {margin:0;height:100%;width:100%;font-size: 10px;  font-family: Arial; overflow-x: hidden; overflow:-moz-scrollbars-vertical;}

.Menu_Head {font-size: 10px;  font-family: Arial; background-color: #757575; color: white;  font-weight: bold;  cursor: pointer;  width: 100%;    }
.Menu_Items {
          filter:alpha(opacity=100);
          background-color: #DDDDDD;
          padding: 11px 0px;
          width: 180;
          display: block;
}
.DescTitle {
          background-color: #006699;
          color: white;
          font-weight: bold;
}

a:link    {
  text-decoration:  none;
  font-weight:      bold;
  color:            black;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
a:visited {
  text-decoration:  none;
  font-weight:      bold;
  color:            black;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
a:hover   {
  text-decoration:  none;
  font-weight:      bold;
  color:            black;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
a:active  {
  text-decoration:  none;
  font-weight:      bold;
  color: black;
  text-decoration: none;
  font: bold 7.5pt Verdana, Arial, Helvetica, sans-serif;
  }
a {
font-family: Verdana, Arial;
font-size:7.5pt;
font-weight:bolder;
cursor:normal;
padding-left: 5;

}

td, th {font-family: Verdana, Arial; font-size:8pt;}
            input, select {font-family: Verdana, Arial; font-size:8pt;}
            .button {font-size:7pt;width:''}
        .titel  {font-family: Verdana, Arial; font-size:10pt; font-weight:bolder; color: #999999}
        .of {border-style:solid; border-width: 1; background-color:#dddddd; border-color : #7c96af; font-size:8pt}
        .off {border-style:none;background-color:#f3f3f3}
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
