#!/usr/local/bin/perl5.22
# Copyright surflocalmedia.com 2004-2022

require 'web-lib.pl';
require 'SurfLocalLib.pl';

####### VARIABLES #######
$newform = "$baseurl" . "BeginAd.cgi";
$PageScript = "$baseurl" . "page.cgi";
$IndexTemplate = "$TemplatesDir" . "IndexTemplate.html";
$HandleRequest = "$baseurl" . "BeginAd.cgi";
#########################

&Parse;
&ShortenValues;

#0 is ad type
#1 is state
#2 is city

#####################
&Disclaimer unless ($Action);
#&Header;
#print "Got past first conditional.";
&Error("You must agree or disagree to our terms to continue.") unless ($Action ne "");

if ($Action eq "Agree") {&StartAd;}
#print "<br>got past second conditional.";

if ($Action eq "Disagree") {
 #   print "<br>Entered Disagree conditional.";
    
    &Disagree;}
if ($Action eq "EnterBizName") {&EnterBizName;}
exit;

#####################

####### ENTER BIZ NAME
sub EnterBizName
{
    &Error("You must select one of the two choices on the previous page.") unless ($AdType ne "");
    if ($AdType =~ /Button/)
    {
        $NextScript = $ButtonScript;
    }
    elsif ($AdType =~ /Text/)
    {
        $NextScript = $TextScript;
    }
    elsif ($AdType =~ /Coupon/)
    {
	$NextScript = $CouponScript;
    }
    else
    {
        &Error("Can't determine what kind of ad \'$AdType\' is.");
    }
    
    &Header;
    &PHed;
    print "<h1>Step two: Enter your business name</h1>\n";
    print "Everything on SurfLocal revolves around the name of your business -- after all, ";
    print "it's what makes you unique! Enter it below to continue to the next step.<Br>\n";
    print "<form action=$NextScript method=POST>\n";
    &PrintHiddenValues;
    print "Your business name: <input type=text name=BizName><br>\n";
    print "Your e-mail address: <input type=text name=Email><br>\n";
    print "<input type=submit value=\"Click here to continue\"> ";
    print "<input type=reset value=\"Clear form and start over\"><br>\n";
    print "</form>\n";
    exit;
}

####### START AD
sub StartAd
{
    &Header;
    &PHed;
    print "<h1>Step one: Choosing the type of service you want</h1>\n";
    print "Select one of the choices below and continue.<br>\n";
    print "<form action=$newform method=POST>\n";
    print "<input type=hidden name=action value=EnterBizName>\n";
    print "<input type=hidden name=State value=\"$State\">\n";
    print "<input type=hidden name=City value=\"$City\">\n";
    if ($AdType eq "Button")
    {
	print "<input type=radio name=AdType value=ButtonOnly> Marketing link <br>\n";
	print "<input type=radio name=AdType value=ButtonPlus> Marketing link and Webpage <br>\n";
    }
    elsif ($AdType eq "TextAd")
    {
        print "<input type=radio name=AdType value=TextAdOnly> Marketing link <br>\n";
	print "<input type=radio name=AdType value=TextAdPlus> Marketing link and Webpage <br>\n";
    }
    elsif ($AdType eq "Coupon")
    {
        print "<input type=radio name=AdType value=CouponOnly> Marketing Ad <br>\n";
	print "<input type=radio name=AdType value=CouponPlus> Marketing Ad and Webpage <br>\n";
    }
    else
    {
        &Error("The ad type specified in the input, $AdType, is not a valid ad type.");
    }
    print "<input type=submit value=\"Press this button to accept your choice and move on\">\n";
    print "<input type=reset value=\"Reset this form and start over\">\n";
    print "</form>\n";
    exit;
}

####### DISAGREE
sub Disagree
{
    &Header;
    #print "Got to disagree beginning.";
    
    $SecondChance = "$newform" . "\?" . "$AdType" . "\&$State" . "\&$City";
    &PHed;
    print "<h1>Thank you</h1>\n";
    print "Thank you for your interest in SurfLocal. Unfortunately, we cannot process your ";
    print "request if you disagree with our <a href=$SecondChance>terms and conditions</a>. <br>\n";
    print "If you would like to further discuss the terms and conditions, please feel free ";
    print "to <a href=mailto:$Administrator>e-mail the administrator.</a> Thank you and God ";
    print "bless.";
    exit;
}

####### DISCLAIMER
sub Disclaimer
{
    $AdType = $in{0};
    $State = $in{'1'};
    $City = $in{'2'};
    
    &Header;
    $DisclaimerLocation = "$TemplatesDir" . "Disclaimer";
    open(DISC,"$DisclaimerLocation") || &Error("Can't open $DisclaimerLocation in Disclaimer sub. Reason: $!");
    @Disc=<DISC>;
    close(DISC);
    foreach (@Disc)
    {	
        &SubstituteValues;
        print "$_";
    }
}
