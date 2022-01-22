@badwords = ("none");
sub Header
{
	$HedTitle = join(//,@_) if @_;
	if ($HedTitle eq 'plain')
	{
		print "Content-type: text/html\n\n ";
	}
	elsif (%Hed) 
	{
		print "Content-type: text/html\n\n ";
		print "<html><head><title>$Hed{T}</title></head>\n";
		if ($Hed{Bk}){print "<body background=\"ffffff\">\n";}
		elsif ($Hed{Bg}){print "<body bgcolor=\"$Hed{Bg}\">\n";}
		else{print "<body bgcolor=white>\n";}
		if($Hed{FontFace}){print "<font face=\"$Hed{FontFace}\">\n";}
	}
	else
	{
		print "Content-type: text/html\n\n ";
	}
	$HedIs = "here";
	
}
sub Parse
{
	if ($ENV{'CONTENT_LENGTH'})
	{
		read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
	}
	$input = $ENV{'QUERY_STRING'} if $ENV{'QUERY_STRING'};
	if ($input =~ /=/g)
	{
		@pairs = split(/&/, $input);
		foreach $pair (@pairs)
		{
			($name,$value) = split(/=/, $pair);
			$value =~ tr/+/ /;
			$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
			$in{$name} = $value;
			$NVPairsExist = 1;
		}
	}
	else
	{
		$count = 0;
		(@InputString) = split(/&/, $input);
		foreach $InputString (@InputString)
		{
			$InputString =~ tr/+/ /;
			$InputString =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
			$in{$count} = $InputString;
			$count++;
		}
		$NVPairsExist = 0;
	}
}
sub Error
{
	$Hed{Bg} = "ffffff";
	$Hed{T} = "Can\'t complete requested action.";
	$Hed{FontColor} = "000000";
	if ($HedIs eq "here")
	{
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><table border=7 width=800 bordercolor=800000><tr><td background=\"https://www.surflocalmedia.com/images/white_table.jpg\">\n";
        print "<center><img src=\"https://surflocalmedia.com/\sm_banner_MKTG3.gif\">\n";	    
print "<head><title>Can't complete requested action<\/title><\/head>\n";
	    print "<body bgcolor=ffffff><font face=Arial, Helvetica color=000000>\n";
	}
	else
	{
	    &Header;
	}
	
	$ErrorCode = join(//,@_);
        print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><font size=+2><font color=800000><b>THERE IS AN ISSUE</font></b><br>\n";
	print "<P><I><font size=-1><font color=800000> $ErrorCode </I>\n";
        print "<p><font size=+1><center><font color=000000>Please email the information below to the system administrator <BR>or use your back button and change your information.</center><br><br>\n";
	exit;
}
1;
