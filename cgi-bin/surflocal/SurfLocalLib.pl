$basedir = "/usr/home/starting2014/public_html/surflocalmedia.com/";
$baseurl = "https://www.surflocalmedia.com/";
$TemplatesDir = "$basedir" . "Templates" . "/";
$admin = "david\@surflocalmedia.com";
$ButtonScript = "/cgi-bin/surflocal/Button.cgi";
$CouponScript = "/cgi-bin/surflocal/Coupon.cgi";
$TextScript = "/cgi-bin/surflocal/Text.cgi";
$PageScript = "/cgi-bin/surflocal/page.cgi";
$CouponDisplay = "/cgi-bin/surflocal/CouponDisplay.cgi";
$FinalizeScript = "/cgi-bin/surflocal/Finalize.cgi";
$mailprog = "/usr/sbin/sendmail";

@StateAbs=("AD","MU","AL","NH","AK","AR","AZ","CA","CO","CT","DC","DE",
	   "FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","ME",
	   "MD","MI","MN","MO","MS","MT","NC","ND","NE",
	   "NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC",
	   "SD","TN","TX","UT","VA","VT","WA","WI","WV","WY",
           "VI","US","SL","BC","MX","JP","BS","BM","DO","VG","AB", "PG",
           "MB","NB","NF","NT","NS","ON","PE","QC","SK","YT","AG",
           "DO","BB","BZ","CR","CU","DM","SV","GD","GT","HT","HN","JM","SL",
           "NI","KN","LC","VC","FC","TT"); 
	   
	   

%States = ("AK" => "Alaska",
           "SL" => "Media",
           "US" => "USA",
           "AD" =>"Ad",
           "MU" =>"Music",
           "SA" =>"SA",
           "WW" =>"WorldWide",  
           "FC" =>"Fort-Collins", 
           "PG" =>"Page", 
           "AZ" => "Arizona",
           "MI" =>"Michigan",
           "US" =>"USA",
           "VI" =>"Virgin Islands",
	   "WA" => "Washington",
           "NH" => "New-Hampshire",
	   "OR" => "Oregon",
	   "CA" => "California",
	   "AK" => "Alaska",
	   "ID" => "Idaho",
	   "NV" => "Nevada",
	   "MT" => "Montana",
	   "WY" => "Wyoming",
	   "UT" => "Utah",
	   "CO" => "Colorado",
	   "NM" => "New-Mexico",
	   "ND" => "North-Dakota",
	   "SD" => "South-Dakota",
	   "NE" => "Nebraska",
	   "KS" => "Kansas",
	   "OK" => "Oklahoma",
	   "TX" => "Texas",
	   "MN" => "Minnesota",
	   "IA" => "Iowa",
	   "MO" => "Missouri",
	   "AR" => "Arkansas",
	   "LA" => "Louisiana",
	   "WI" => "Wisconsin",
	   "IL" => "Illinois",
           "IN" => "Indiana",
	   "KY" => "Kentucky",
	   "TN" => "Tennessee",
	   "MS" => "Mississippi",
	   "OH" => "Ohio",
	   "AL" => "Alabama",
	   "WV" => "West-Virginia",
	   "GA" => "Georgia",
	   "FL" => "Florida",
	   "ME" => "Maine",
	   "VT" => "Vermont",
	   "NY" => "New-York",
	   "MA" => "Massachusetts",
	   "RI" => "Rhode-Island",
	   "CT" => "Connecticut",
	   "NJ" => "New-Jersey",
	   "DE" => "Delaware",
	   "DC" => "DC",
	   "MD" => "Maryland",
	   "VA" => "Virginia",
	   "NC" => "North-Carolina",
	   "SC" => "South-Carolina",
	   "HI" => "Hawaii",
	   "PA" => "Pennsylvania");

%Abbrevs = ("Alaska" => "AK",
            "Music"=>"MU",
            "Media" => "SL",
            "Ad"=>"AD",
            "SA"=>"SA",
            "USA" => "US",
            "Page"=>"PG",
            "Fort-Collins"=>"FC",
            "WorldWide"=>"WW",               
            "Arizona" => "AZ",
           "Michigan"=>"MI",
           "USA"=>"US",
           "Virgin Islands"=>"VI",
	   "Washington" => "WA",
           "New-Hampshire" => "NH",
	   "Oregon" => "OR",
	   "California" => "CA",
	   "Alaska" => "AK",
	   "Idaho" => "ID",
	   "Nevada" => "NV",
	   "Montana" => "MT",
	   "Wyoming" => "WY",
	   "Utah" => "UT",
	   "Colorado" => "CO",
	   "New-Mexico" => "NM",
	   "North-Dakota" => "ND",
	   "South-Dakota" => "SD",
	   "Nebraska" => "NE",
	   "Kansas" => "KS",
	   "Oklahoma" => "OK",
	   "Texas" => "TX",
	   "Minnesota" => "MN",
	   "Iowa" => "IA",
	   "Missouri" => "MO",
	   "Arkansas" => "AR",
	   "Louisiana" => "LA",
	   "Wisconsin" => "WI",
	   "Illinois" => "IL",
           "Indiana" => "IN",
	   "Kentucky" => "KY",
	   "Tennessee" => "TN",
	   "Mississippi" => "MS",
	   "Ohio" => "OH",
	   "Alabama" => "AL",
	   "West-Virginia" => "WV",
	   "Georgia" => "GA",
	   "Florida" => "FL",
	   "Maine" => "ME",
	   "Vermont" => "VT",
	   "New-York" => "NY",
	   "Massachusetts" => "MA",
	   "Rhode-Island" => "RI",
	   "Connecticut" => "CT",
	   "New-Jersey" => "NJ",
	   "Delaware" => "DE",
	   "DC" => "DC",
	   "Maryland" => "MD",
	   "Virginia" => "VA",
	   "North-Carolina" => "NC",
	   "South-Carolina" => "SC",
	   "Hawaii" => "HI",
	   "Pennsylvania" => "PA");

sub CookieHeader
{
	print "Content-type: text/html\n";
}
sub CookieFooter
{
	print "\n";
}
sub GetCookieValues
{
	&GetCookies("User");
	$TheCookie=$Cookies{"User"};
	($BizName,$CityState) = split(/\|/,$TheCookie);
	$dirname = $basedir . $CityState . "/" . $BizName;
}
sub GetSubsequentCookie
{
	&GetCookies("Subsequent");
	$ThisCookie=$Cookies{"Subsequent"};
	$AdType=$ThisCookie;
}
sub OpenCityDatabase
{
	use DB_File;
	#This database "CityData" will be in each city's directory.
	$citydatabase = $basedir . $CityState . "/" . "MainData.db";

	dbmopen(%CityData,$citydatabase,0640) || &Error("Can't open the city database $citydatabase. Reason: $!");
}
sub CloseCityDatabase
{
	dbmclose %CityData;
}
sub OpenMyDatabase
{
	use DB_File;
	$MyDatabase = $dirname . "/" . "Database.db";
	dbmopen(%MyData,$MyDatabase,0666) || &Error("Can't open the personal database file at $MyDatabase. $!");
}
sub CloseMyDatabase
{
	dbmclose %MyData;
}
sub PHed
{
    $PHedLocation = "$TemplatesDir" . "Header";
    
    open (THEHED,"$PHedLocation") || &Error("Can't open $PHedLocation in PHed sub. Reason: $!");
    @Phed=<THEHED>;
    close(THEHED);
    foreach $hhd (@Phed)
    {
        print "$hhd";
    }
}

####### SUBSTITUTE VALUES
sub SubstituteValues
{
    $_ =~ s/\%\%City\%\%/$City/gi;
    $_ =~ s/\%\%State\%\%/$State/gi;
    $_ =~ s/\%\%BizName\%\%/$BizName/gi;
    $_ =~ s/\%\%TitleTag\%\%/$TitleTag/gi;
    $_ =~ s/\%\%Email\%\%/$Email/gi;
    $_ =~ s/\%\%Category\%\%/$Category/gi;
    $_ =~ s/\%\%AdType\%\%/$AdType/gi;
    $_ =~ s/\%\%PhoneNumber\%\%/$PhoneNumber/gi;
}


####### SHORTEN VALUES
sub ShortenValues
{
    $Action = "$in{action}";
    $BizName = "$in{BizName}";
    $TitleTag = "$in{TitleTag}";
    $Email = "$in{Email}";
    $PhoneNumber = "$in{PhoneNumber}";
    $State = "$in{State}";
    $City = "$in{City}";
    $AdType = "$in{AdType}";
    $Category = "$in{Category}";
}

####### PRINT HIDDEN VALUES
sub PrintHiddenValues
{
    print "<input type=hidden name=BizName value=\"$BizName\">\n" if ($BizName ne "");
    print "<input type=hidden name=TitleTag value=\"$TitleTag\">\n" if ($TitleTag ne "");
    print "<input type=hidden name=State value=\"$State\">\n";
    print "<input type=hidden name=City value=\"$City\">\n";
    print "<input type=hidden name=AdType value=\"$AdType\">\n" if ($AdType ne "");
    print "<input type=hidden name=Email value=\"$Email\">\n" if ($Email ne "");
    print "<input type=hidden name=PhoneNumber value=\"$PhoneNumber\">\n" if ($PhoneNumber ne "");
    print "<input type=hidden name=Category value=\"$Category\">\n" if ($Category ne "");
}


1;
