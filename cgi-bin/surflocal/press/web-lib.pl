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
	    print "<head><title>Can't complete requested action<\/title><\/head>\n";
	    print "<body bgcolor=ffffff><font face=Arial, Helvetica color=000000>\n";
	}
	else
	{
	    &Header;
	}
	
	$ErrorCode = join(//,@_);
print "<link href=\"/stylee.css\" rel=\"stylesheet\" type=\"text/css\" />\n";
        print "<center><h2><font color=800000><img src=\"http://surflocal.net/images/error.jpg\">THERE IS AN ERROR</font><br><br>\n";
	print "<font size=+1>AN ERROR HAS OCCURRED... <br><br>THE ERROR:  $ErrorCode \n";
        print "<p>Simply click your <i>BACK BUTTON</i> to correct your error and continue with your ad creation.</center>\n";
	exit;
}
1;
