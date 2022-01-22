#!/usr/local/bin/perl5.22 
# Copyright surflocalmedia.com 2004-Present
# See suite header in BeginAdDB script
# for copyright and usage information.
require 'web-lib.pl';
require 'SurfLocalLib.pl';

#####set variables here######
$newform = "/cgi-bin/surflocal/CouponDisplay.cgi";

######################################
&Parse;
&ShortenValues;
&Error("This script can't operate without input") unless (%in);
#Getting State,City,Category
$State = $in{0};
$City = $in{1};
$Category = "$in{2}";
$StateCode = $Abbrevs{$State};
#$Hed{T} = "$Category $City $StateCode Go green view to redeem in $City $StateCode";

$TheDir =  "$basedir" . "$City" . "$StateCode" . "/";

#City/Coupon.data has "Category|BizName/\n"
#Use it to find all biz names that match Category.

$TheCouponData = $TheDir . "Coupon.data";
open (COUPLIST,"$TheCouponData") || &Error("Can't open $TheCouponData. Reason: $!");       
@CoupData=<COUPLIST>;          
close(COUPLIST);
$BizCount=0;
foreach (@CoupData)
{
	chomp($_);
	if ($_ ne "")
	{
		($ListCat,$ListBiz)=split(/\|/,$_);
		if ($ListCat eq $Category)
		{
			push(@BizList,$ListBiz);
			$BizCount++;
		}
	}
}
#TheDir has the directory up to the CityState
&Header;
&PHed;
#print "<font size=-1><center><font color=000000><b>$City $State $Category.......$City $State Coupons</b><br> Go green and view to redeem our ads</font></center>\n";
#print "<center><IFRAME width=\"900\" height=\"150\" frameborder=\"no\" scrolling=\"no\" name=\"iframe\"  SRC=\"https://www.surflocalmedia.com/1/1.html\" ></IFRAME></center>\n";
if (@BizList)
{
	for ($i=0; $i <= $BizCount; $i++)
	{
		$BizName = $BizList[$i];
		$dirname=$TheDir . $BizName;
		&OpenMyDatabase;
		$Template=$MyData{CouponTemplate};
		$TheInterim =$Template;
		if ($TheInterim ne "")
		{

print "<center><table BORDER=0 CELLSPACING=3 CELLPADDING=0  WIDTH=800>
        <tr><td>\n";
#print "<center><p><b><FONT FACE=\"areal\"><font color=000000><font size=-1>Community Marketing Ads in $City $State -  Go green and view to redeem</font></font></font></font><br><br>";
			$TheTemplate= $TemplatesDir . $Template . ".ctemp";
			open (PAG,"$TheTemplate") || &Error("Can't open $TheTemplate. Reason: $!");
			@Pag=<PAG>;
			close(PAG);
			foreach (@Pag)
			{
                                
				$_ =~ s/\%\%City\%\%/$City/gi;
                                $_ =~ s/\%\%StateCode\%\%/$StateCode/gi;
                                $_ =~ s/\%\%BizName\%\%/$BizName/gi;
				if ($_ =~ /<!--(\w*)-->/)
				{
					$TheKey = $1;
					$TheThingy=$MyData{$TheKey};
					$TheThingy =~ s/\[/</gi;
					$TheThingy =~ s/\]/>/gi;
					if ($TheKey eq "CouponEmailAddress")
					{
						$_ =~ s/<!--$TheKey-->/<a href=\"mailto:$TheThingy\">/gi;
					}
					elsif ($TheKey eq "CouponBusinessLink")
					{
						$_ =~ s/<!--$TheKey-->/<a href=\"$TheThingy\">/gi;
					}
					else
					{
						$_ =~ s/<!--$TheKey-->/$TheThingy/gi;
					}


				}#end if tag loop
				print "$_";
   			 }#end foreach loop
		}
    		&CloseMyDatabase;
	}
}
else
{
	print "There aren't any coupons for the category you selected.";
}
exit;
		
