#!/usr/local/bin/perl
#set the line above this to your perl path. Usually fine as is
# or /usr/local/bin/perl  /sbin/perl
# make certain that the first line stays the first line!
################################################################## 
#  (C)1998-2002 Bignosebird.com   cardcgi v2.1
#  This software is FREEWARE! Do with it as you wish. It is yours   
#  to share and enjoy. Modify it, improve it, and have fun with it! 
#  It is distributed strictly as a learning aid and bignosebird.com 
#  disclaims all warranties- including but not limited to:          
#  fitness for a particular purpose, merchantability, loss of       
#  business, harm to your system, etc... ALWAYS BACK UP YOUR        
#  SYSTEM BEFORE INSTALLING ANY SCRIPT OR PROGRAM FROM ANY          
#  SOURCE!                                                          

use Socket;

$|=1;

#### PROGRAM CONFIGURATION SECTION ############################
# 
# Modify each item below to meet your needs.
#
# DAYS: number of days to keep cards before purging
# SMTP_SERVER: the name of the system acting as your sendmail gateway
#   localhost should work on most systems.
# IF NOT- SET THE SEND_MAIL VARIABLE!
# BASEDIR is the unix directory that your greeting cards will
#   be stored in.
# BASEURL is the URL (http address) of the directory your cards
#   will be stored in.
# SITEURL is the home page URL for your site.
# SITENAME is the Name of your site, ie Title
# EXT is the ending name for your card files. NEVER, EVER USE shtml!!
# PROGNAME is the URL of THIS script.
# MAILLOG is a file name that you can capture e-mail addresses in
# FOR SECURITY REASONS: RENAME THIS FILE!!!!!!!!
# okaydomains are (if specified, the ONLY domains that the script
#    can be run from. If left empty, anyone could run your script,
#    but they wouldn't see any graphics!!! If your site answers to
#    both www.domain.com and domain.com, then use both!
#

@okaydomains=("http://www.surflocal.net", "http://surflocal.net");
$DAYS=11;

# USE EITHER SMTP OR SEND_MAIL DEPENDING ON YOUR SYSTEM-
# BUT NOT BOTH!

$SMTP_SERVER="localhost";
#$SEND_MAIL="/usr/sbin/sendmail";

$BASEDIR="/data/10/0/135/118/787770/user/806977/htdocs/Agent-Office/emailclients";
$BASEURL="http://www.surflocal.net/Agent-Office/emailclients";
$SITEURL="http://www.surflocal.net/Agent-Office/emailclients";
$SITENAME="Message from Surflocal Marketing Client Corespondence";
$EXT=".html";
$PROGNAME="/cgi-bin/emailclients/emailclients.cgi";
$MAILLOG="maillog";
$SUBJECT ="Surflocal.Net Local Search Placement System";

###############################################################

  &main_driver;

###############################################################
#
# Now go thru the program looking for the string "BNB SAYS!"
# to locate other changes you should make, such as wording of
# the notification e-mail and "plug" for the site.
#
# to keep things simple, the field names are hard coded in.
# you can of course modify what you wish.
###############################################################

sub thank_you
{
 if ($MAILLOG ne "")
  {
   open (ML,">>$BASEDIR/$MAILLOG");      
   print ML "$fields{'recip_email'}\n";  
   print ML "$fields{'sender_email'}\n"; 
   close(ML);
  }

print "Content-type: text/html\n\n";
print <<__STOP_OF_THANKS__;

<CENTER>
<link href="/styleC.css" rel="stylesheet" type="text/css" />

<H1><B><font color=000000>THANKS!</B></H1>
Your message notification has been sent to $fields{'recip_name'}<BR>
The URL of this card is<P>
<A HREF="$URL_NAME">$URL_NAME</A>
<P>
<B><A HREF=$fields{'parent'}>RETURN</A></B>
<P>

__STOP_OF_THANKS__
}

# BNB SAYS! 
# THIS IS WHERE YOU CAN CUSTOMIZE YOUR NOTIFICATION LETTER
# DO NOT TOUCH THE TWO LINES WITH __STOP_OF_MESSAGE__ ON
# THEM!!!!

sub setup_letter
{
$msgtext =<<__STOP_OF_MESSAGE__;

Hi $fields{'recip_name'}

It was great speaking with you about the SurfLocal Search Placement System.  
Please click on the link below.  I have prepared additional information for you about our services. 

   $URL_NAME

This information will remain on the server for a week, so
please print it out or save it as soon as you can.  I will get back with you 
in a day or two to discuss it.

I look forward to speaking with you soon,

$fields{'sender_name'} 
$fields{'sender_cell'}

__STOP_OF_MESSAGE__
}

# BNB SAYS! 
# This is what makes up the body of your card. DO NOT REMOVE OR
# MODIFY THE LINES ABOVE THE WORD $param or the $param line
# itself. Doing so will cause the script to fail.
sub make_body
{
$cardbody =<<__END_OF_CARD_BODY__;
<SCRIPT LANGUAGE="JavaScript">
<!--
if(navigator.userAgent.indexOf("MSIE") != -1)
document.writeln ('');
else
document.writeln ('<EMBED SRC="$BASEURL/$fields{'midifile'}" AUTOSTART="true" HIDDEN="true" VOLUME="80%">');
//-->
</SCRIPT>
<BGSOUND SRC="$BASEURL/$fields{'midifile'}">
<link href="/styleC.css" rel="stylesheet" type="text/css" />
<script language="javascript">

/*
Auto center window script- Eric King (http://redrival.com/eak/index.shtml)
Permission granted to Dynamic Drive to feature script in archive
For full source, usage terms, and 100's more DHTML scripts, visit http://dynamicdrive.com
*/

var win = null;
function NewWindow(mypage,myname,w,h,scroll){
LeftPosition = (screen.width) ? (screen.width-w)/2 : 0;
TopPosition = (screen.height) ? (screen.height-h)/2 : 0;
settings =
'height='+h+',width='+w+',top='+TopPosition+',left='+LeftPosition+',scrollbars='+scroll+',resizable'
win = window.open(mypage,myname,settings)
}

</script>
$params
<CENTER>
<P><CENTER>
   <FONT SIZE=+2 COLOR=$fields{'text_color'}
     FACE=ARIAL><B>$fields{'the_title'}</B></FONT>
   <HR WIDTH=200>
<TABLE WIDTH=735  BGCOLOR=$fields{'back_color'} BORDER=5 bordercolor=AB974E>
 <TR>

 <TD ALIGN=TOP VALIGN=TOP>
<TABLE WIDTH=800  BGCOLOR=$fields{'back_color'}>
 <TR>

 <TD ALIGN=TOP VALIGN=TOP>
  <TABLE WIDTH=400>
    <TR>
      <TD ALIGN=TOP VALIGN=TOP>
       <a href="http://www.surflocal.net"><IMG SRC=$BASEURL/$fields{'pic_select'} BORDER=0></a>

<P><B>Surflocal Video Library</b>

<P><img SRC="/bullet-logo.gif" WIDTH=30 HEIGHT=17>&nbsp;&nbsp;&nbsp;<a href="/office/video-library/sl-competition.html" onclick="NewWindow(this.href,'name','600','500','yes');return false"><FONT COLOR=800000><FONT SIZE=-1>Surflocal -VS- The Competition</a><br>


<img SRC="/bullet-logo.gif" WIDTH=30 HEIGHT=17>&nbsp;&nbsp;&nbsp;<a href="/office/video-library/Next-Generation.html" onclick="NewWindow(this.href,'name','600','500','yes');return false"><FONT COLOR=800000>The Next Generation Video</a><br>

<img SRC="/bullet-logo.gif" WIDTH=30 HEIGHT=17>&nbsp;&nbsp;&nbsp;<a href="/office/video-library/Surflocal-Hook-Voice.html" onclick="NewWindow(this.href,'name','600','500','yes');return false"><FONT COLOR=800000>Businesses Reducing Phonebook Advertising Video</a><br> 

<img SRC="/bullet-logo.gif" WIDTH=30 HEIGHT=17>&nbsp;&nbsp;&nbsp;<a href="/office/video-library/Surflocal-Line-Voice.html" onclick="NewWindow(this.href,'name','600','500','yes');return false"><FONT COLOR=800000>Local Search Industry Statistics Video</a> <br>

<img SRC="/bullet-logo.gif" WIDTH=30 HEIGHT=17>&nbsp;&nbsp;&nbsp;<a href="/office/video-library/Surflocal-Sinker-Voice.html" onclick="NewWindow(this.href,'name','600','500','yes');return false"><FONT COLOR=800000>Customers Respond to Online Advertising Video</a>  </CENTER></B></FONT>
      </TD>
    </TR>
  </TABLE>

 </TD>
 <TD WIDTH=380 VALIGN=TOP >
   
   <TABLE>
    <TR>
     <TD><P><BR><BR><FONT FACE=ARIAL COLOR=$fields{'text_color'}>
         $fields{'the_message'}

      <P ALIGN=CENTER>
      <I>$fields{'sig_line'}
      </I>
      </P>
      </FONT>
      </TD>
    </TR>
   </TABLE>
   </CENTER>


 </TD>
 </TR>
</TABLE>
<p>
<center> <table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=8 WIDTH="735" >
<tr>

<td WIDTH=10% HEIGHT=10  BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/local.html"><font size=-1>Local Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/state.html"><font size=-1>State Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/national.html"><font size=-1>National Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/strategies.html"><font size=-1>Coupon Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><font size=+1><a href="http://www.surflocal.net/marketing/advertisers.html"><font size=-1>Rate Card</a></center></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/Awards/"><font size=-1>About Us</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/office/"><font size=-1>Media Kit</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/"><font size=-1>Home</a></td>



</td>
</tr>
</table>
</TD>
</TR>
</TABLE>

<P><BR>
<center><table BORDER=0 COLS=1 WIDTH="90%" BGCOLOR="#FFFFFF"  bordercolor=67480F>
<tr>


<td>
<P><b><center><P><font size=+1><i>SURFLOCAL –VS- THE COMPETITION</i></b></font></center>

<p><center><font color=000000><font size=-1><i><P>Many consumers and businesses believe local search placement services are the same as search engine optimization: <br> This belief is incorrect and could be very costly.</i></center>



<p>
<center><table BORDER=0 COLS=2 WIDTH="90%" BGCOLOR="#FFFFFF">
<tr>


<td width=50%>
<P><b>Surflocal.Net</b>
<font size=-2>
<LI>	Local placement in desired physical marketplace selected by the client
<LI>	4 distinct key phrases to accurately represent the clients website to local buyers
<LI>	Opens the door for the search engines bots to explore and list your website
<LI>	Natural, Organic Search Placement Service through accurate client representation
<LI>	For 13 years Classified as a Data Pool / Data Source– our clients are deemed accurate when using our service
<LI>	Never has control of client’s web site – The Client is SAFE with Surflocal.Net
<LI>	Displays client in the World-Wide-Web just as web site reflects
<LI>	Does not ever manipulate the world wide web to make your site visible
<LI>	You will never be in danger of being banned from the world wide web when working with Surflocal.Net
<LI>	Offers creative, proven, cost effective ways to gain the attention of shoppers looking for the client’s products and services
</td>

<td width=50% VALIGN="TOP">
<P><B>The Competition – SEO Companies (Search Engine Optimization Companies)</B>
<font size=-2>
<p>
<li>SEO’s spam Google and the major search engines for better rankings putting their client in danger of permanent website removal
<li>“Over pack” the client’s website with irrelevant keywords thus making putting the client’s site in 
       jeopardy of index removal.
<li>Takes control of the client’s web site and all information, both public and private, therein attached and can sell the client’s information, both public and private, to a fellow competitor 
<li>Offers costly programs that is highly expensive
<li>Many SEO’s are newer LLC or LLP corporations          (Limiting any if not all liability)

</td></tr></table>

</center>
<blockquote>
<P><b>According to Google Webmaster’s Guidelines,</b> ‘Deciding to hire an SEO is a big decision that can potentially improve your site and save time, but you can also risk damage to your site and reputation.  Make sure to research the potential advantages as well as the damage an irresponsible SEO can do to your site.  Practices that violate our guidelines may result in a negative adjustment of your site’s presence in Google, or even the removal of your site from the index.’  This is a clear statement to site owners that if you hire a company to optimize your site, and they break the rules, there’s no playing dumb.  Whether you knew the techniques your SEO Company used violated Google’s policies or not, your site will be penalized or banned nonetheless.

<P><b>Most of these companies charge a very large amount in the beginning and a large monthly fee to market your website and only 3-6 month agreements, in order to get as much money out of you as possible.</b>  You surrender control of the administration of your website to them which gives them access to your proprietary information which often times includes your client lists.  After the 3-6 months is up, they triple charge you to remain with them or they go to your competition knowing what works in your market and which customers are seeking your services.  They promise and guarantee anything and everything to get your business. This is the first sign you are dealing with an unethical SEO. Google says, No-one can guarantee search placement.  

<P><b>Google also says if you hire an SEO that violates their guidelines this will result in a negative adjustment of your website search presence on Google.</b>  Most SEO’s use deceptive web indexing practices that violate the major search engine guidelines.  If Google catches you using an SEO that is involved in any form of deceptive practice, the owner of the website is to blame.  Google will remove your website or websites from its index list permanently and the SEO simply goes to another victim.

<P><b>One way to know if you are using a company that employs unethical tactics on the World Wide Web</b> is if the telephone directory, the lead generation, or the SEO company is using computer programs to check your rankings in the search results, and they are sending you computer generated reports on your search placement.  Such programs violate the terms of service of most search engines.  In fact, Google considers this a huge violation. This is a wide spread problem.  The larger companies view this as ‘business as usual’, knowing that many of their customers will be banned.

<P><b>Because we do not try to "cheat" the search engines by deceptive tactics</b> our data pool is trusted to present our clients in a professional manner. Surflocal has been in the business for 13 years and has strictly followed the guidelines set forth by the major search engines to provide relevant and proper classification of a business website.

<P><b>One hidden pitfall in marketing online:</b> When a business places an ad online with a company promising local search placement, they unknowingly surrendered their search placement to that company. Their local search placement is re- directed so their website can only be found online by searching another company’s directory that also lists all of their competitors. When this happens, their business’ information is no longer available directly to their local customers, decreasing the value of their web presence.

<P><b>Another unknown obstacle: </b>Businesses often pay substantial fees to market through what is known as a lead generation company. A lead generation company uses a business’ proprietary information to generate local search placement to harvest leads from the local customer base. The lead generation company then sells the leads back to all of their clients in the region, creating a bidding war. This form of marketing not only charges for both membership and each lead, but also has the effect of dramatically reducing profit margins for the winning bidder 

<P><b>Your business is very important </b> and should be treated as such with your success and safety clearly in focus.  Let Surflocal.Net help promote your company with our SAFE, PROVEN, PROPRIETARY AND COST EFFECTIVE INTERNET MARKETING SYSTEM.
  
</blockquote>
<P>

</td>



</tr>
<table>
<P>
<TABLE WIDTH=500>
  <TR>
  <TD>
  
  <BLOCKQUOTE>
  <I><font color=000000><font size=-1>
  from $fields{'sender_name'} <br>
   Help us "PROMOTE LOCAL BUSINESS with <A HREF="http://www.surflocal.net"/> Surflocal.Net</A>
</CENTER>
  </TD>
  </TR>
</TABLE>
<p>
<center> <table BORDER=0 CELLSPACING=3 CELLPADDING=0 COLS=8 WIDTH="735" >
<tr>

<td WIDTH=10% HEIGHT=10  BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/local.html"><font size=-1>Local Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/state.html"><font size=-1>State Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><center><a href="http://www.surflocal.net/national.html"><font size=-1>National Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/strategies.html"><font size=-1>Coupon Ads</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><font size=+1><a href="http://www.surflocal.net/marketing/advertisers.html"><font size=-1>Rate Card</a></center></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/Awards/"><font size=-1>About Us</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/office/"><font size=-1>Media Kit</a></td>

<td WIDTH=10% HEIGHT=10 BACKGROUND=/images/btn-menu.jpg><center><a href="http://www.surflocal.net/"><font size=-1>Home</a></td>



</td>
</tr>
</table>
</CENTER>
</BODY>
</HTML>
__END_OF_CARD_BODY__
}

sub pass_params
{
$params=<<__END_OF_PARAMS__;
<CENTER>
<TABLE WIDTH=500>
 <TR>
 <TD>
 <FONT FACE="ARIAL"><font color=000000>
 <B>To send , click on the SEND button. To return
    without sending, please press your
    browser's BACK button.
 </B>
 <P>
<CENTER>
<FORM METHOD="POST" ACTION="$PROGNAME">
<INPUT TYPE="HIDDEN" NAME="action_code" VALUE="SENDCARD">
<INPUT TYPE="HIDDEN" VALUE="$fields{'pic_select'}" NAME="pic_select">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sender_name'}" NAME="sender_name">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sender_email'}" NAME="sender_email">
<INPUT TYPE="HIDDEN" VALUE="$fields{'recip_name'}" NAME="recip_name">
<INPUT TYPE="HIDDEN" VALUE="$fields{'recip_email'}" NAME="recip_email">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sender_cell'}" NAME="sender_cell">
<INPUT TYPE="HIDDEN" VALUE="$fields{'text_color'}" NAME="text_color">
<INPUT TYPE="HIDDEN" VALUE="$fields{'back_color'}" NAME="back_color">
<INPUT TYPE="HIDDEN" VALUE="$fields{'the_title'}" NAME="the_title">
<INPUT TYPE="HIDDEN" VALUE="$fields{'the_message'}" NAME="the_message">
<INPUT TYPE="HIDDEN" VALUE="$fields{'sig_line'}" NAME="sig_line">
<INPUT TYPE="HIDDEN" VALUE="$fields{'midifile'}" NAME="midifile">
<INPUT TYPE="HIDDEN" VALUE="$fields{'background'}" NAME="background">
<INPUT TYPE="HIDDEN" VALUE="$ENV{'HTTP_REFERER'}" NAME="parent">
<INPUT TYPE="submit" VALUE="SEND">   
</FORM>
</CENTER>
 </TD>
 </TR>
</TABLE>
__END_OF_PARAMS__
}


###################################################################
###################################################################
sub sendmail  {

# error codes below for those who bother to check result codes <gr>

# 1 success
# -1 $smtphost unknown
# -2 socket() failed
# -3 connect() failed
# -4 service not available
# -5 unspecified communication error
# -6 local user $to unknown on host $smtp
# -7 transmission of message failed
# -8 argument $to empty
#
#  Sample call:
#
# &sendmail($from, $reply, $to, $smtp, $subject, $message );
#
#  Note that there are several commands for cleaning up possible bad inputs - if you
#  are hard coding things from a library file, so of those are unnecesssary
#

    my ($fromaddr, $replyaddr, $to, $smtp, $subject, $message) = @_;

    $to =~ s/[ \t]+/, /g; # pack spaces and add comma
    $fromaddr =~ s/.*<([^\s]*?)>/$1/; # get from email address
    $replyaddr =~ s/.*<([^\s]*?)>/$1/; # get reply email address
    $replyaddr =~ s/^([^\s]+).*/$1/; # use first address
    $message =~ s/^\./\.\./gm; # handle . as first character
    $message =~ s/\r\n/\n/g; # handle line ending
    $message =~ s/\n/\r\n/g;
    $smtp =~ s/^\s+//g; # remove spaces around $smtp
    $smtp =~ s/\s+$//g;

    if (!$to)
    {
	return(-8);
    }

 if ($SMTP_SERVER ne "")
  {
    my($proto) = (getprotobyname('tcp'))[2];
    my($port) = (getservbyname('smtp', 'tcp'))[2];

    my($smtpaddr) = ($smtp =~
		     /^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/)
	? pack('C4',$1,$2,$3,$4)
	    : (gethostbyname($smtp))[4];

    if (!defined($smtpaddr))
    {
	return(-1);
    }

    if (!socket(MAIL, AF_INET, SOCK_STREAM, $proto))
    {
	return(-2);
    }

    if (!connect(MAIL, pack('Sna4x8', AF_INET, $port, $smtpaddr)))
    {
	return(-3);
    }

    my($oldfh) = select(MAIL);
    $| = 1;
    select($oldfh);

    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-4);
    }

    print MAIL "helo $SMTP_SERVER\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-5);
    }

    print MAIL "mail from: <$fromaddr>\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-5);
    }

    foreach (split(/, /, $to))
    {
	print MAIL "rcpt to: <$_>\r\n";
	$_ = <MAIL>;
	if (/^[45]/)
	{
	    close(MAIL);
	    return(-6);
	}
    }

    print MAIL "data\r\n";
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close MAIL;
	return(-5);
    }

   }

  if ($SEND_MAIL ne "")
   {
     open (MAIL,"| $SEND_MAIL");
   }

    print MAIL "To: $to\n";
    print MAIL "From: $fromaddr\n";
    print MAIL "Reply-to: $replyaddr\n" if $replyaddr;
    print MAIL "X-Mailer: Perl Powered Socket Mailer\n";
    print MAIL "Subject: $subject\n\n";
    print MAIL "$message";
    print MAIL "\n.\n";

 if ($SMTP_SERVER ne "")
  {
    $_ = <MAIL>;
    if (/^[45]/)
    {
	close(MAIL);
	return(-7);
    }

    print MAIL "quit\r\n";
    $_ = <MAIL>;
  }

    close(MAIL);
    return(1);
}


sub no_email
{
print <<__STOP_OF_NOMAIL__;
Content-type: text/html

<FONT SIZE="+1">
<B>
SORRY! Your request could not be processed because of missing
e-mail address(es). Please use your browser's back button to
return to the entry page.
</B>
</FONT>
__STOP_OF_NOMAIL__
}

sub send_mail
{

&setup_letter;
$mailresult=&sendmail($fields{sender_email}, $fields{sender_email}, $fields{recip_email}, $SMTP_SERVER, $SUBJECT, $msgtext); 

}

sub card_expire
 {
  local(@items, $item);
  opendir(CARDDIR, "$BASEDIR");
  @items = grep(/[0-9]$EXT/,readdir(CARDDIR));
  closedir(CARDDIR);
  foreach $item (@items)
   {
    if (-M "$BASEDIR/$item" > $DAYS)
     {
      unlink("$BASEDIR/$item");
     }
   }
 }



##################################################################
sub valid_address 
 {
  $testmail = $fields{'recip_email'};
  if ($testmail =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||
  $testmail !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/)
   {
     return 0;
   }
   else 
    {
      return 1;
    }
}


sub bad_email
{
print <<__STOP_OF_BADMAIL__;
Content-type: text/html

<FONT SIZE="+1">
<B>
SORRY! Your request could not be processed because of an improper
recipient's e-mail address. Please use your back button to return

</B>
</FONT>
__STOP_OF_BADMAIL__
}

sub test_basedir
{
  if (not -w $BASEDIR)
   {
print <<__STOP_OF_BADBASE__;
Content-type: text/html

<FONT SIZE="+1">
<B>
The script cannot either find or write to the<BR>
$BASEDIR directory. Please check this setting if
the BASEDIR variable, and the permissions of the
directory. If you have them set to 755, please 
change them to 777.
</B>
</FONT>
__STOP_OF_BADBASE__
exit;
   }
}

##################################################################
sub valid_page
 {
 if (@okaydomains == 0) {return;}
  $DOMAIN_OK=0;                                         
  $RF=$ENV{'HTTP_REFERER'};                             
  $RF=~tr/A-Z/a-z/;                                     
  foreach $ts (@okaydomains)                            
   {                                                    
     if ($RF =~ /$ts/)                                  
      { $DOMAIN_OK=1; }
   }                                                    
   if ( $DOMAIN_OK == 0)                                
     { print "Content-type: text/html\n\n Sorry, cant run it from here....";    
      exit;
     }                                                  
}

sub decode_vars
{
#This part of the program splits up our data and gets it
#ready for formatting.
  $i=0;
  read(STDIN,$temp,$ENV{'CONTENT_LENGTH'});
  @pairs=split(/&/,$temp);
  foreach $item(@pairs)
   {
    ($key,$content)=split(/=/,$item,2);
    $content=~tr/+/ /;
    $content=~s/%(..)/pack("c",hex($1))/ge;
    $content=~s/\0//g; #strip nulls
    $content =~ s/<!--(.|\n)*-->//g;
    $fields{$key}=$content;
    $i++;
    $item{$i}=$key;
    $response{$i}=$content;
   }
}

sub get_file_name
{
   $proc=$$;
   $newnum=time;
   $newnum=substr($newnum,4,5);
   $date=localtime(time);  
   ($day, $month, $num, $time, $year) = split(/\s+/,$date); 
   $month=~tr/A-Z/a-z/;
   $PREF = "$month$num-";
   $FILE_NAME="$BASEDIR/$PREF$newnum$proc$EXT";
   $URL_NAME="$BASEURL/$PREF$newnum$proc$EXT";
}


#Write out our HTML FILE
sub create_file
{
  open(OUTFILE,">$FILE_NAME") ;
  print OUTFILE "$cardbody\n";
  close (OUTFILE);
}

#Set up our HTML Preview Form
sub do_preview
{
$fields{'the_message'} =~s/\"/\'/g;
  &pass_params;
  &make_body;
print "Content-type: text/html\n\n";
print "$cardbody\n";
}

sub main_driver
{
   &valid_page;
   &test_basedir;
   &decode_vars;

   if ($fields{'recip_email'} eq "")
     { &no_email; exit; } 
   if (&valid_address == 0)
    { &bad_email; exit; }
   if ($fields{'sender_email'} eq "")
     { &no_email; exit; }

   if ($fields{'background'} ne "")
    { $BODYTAG="<BODY BACKGROUND=\"$BASEURL/$fields{'background'}\">";}
     else { $BODYTAG="<BODY BGCOLOR=\"#FFFFFF\">"; }

   if ($fields{'action_code'} eq "NEW") 
     { &do_preview; }

   if ($fields{'action_code'} eq "SENDCARD") 
     {                             
      &make_body;
      &get_file_name;
      &create_file;
      &setup_letter;
      $mailresult=&sendmail($fields{sender_email}, $fields{sender_email}, $fields{recip_email}, $SMTP_SERVER, $SUBJECT, $msgtext); 
      &thank_you;
      if ($DAYS > 0)
       {&card_expire;}
     }

}

