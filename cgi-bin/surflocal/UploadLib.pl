sub SetMyVars
{
	$MAXIMUM_UPLOAD = 0;
	$ALLOW_INDEX = 0;
	$SUCCESS_LOCATION = ""
}

sub MainUploadRoutine
{
	my $basedir = "/usr/home/starting2014/public_html/surflocalmedia.com/";
	my $baseurl = "https://www.surflocalmedia.com/";
	$SAVE_DIRECTORY = $basedir . $CityState . "/" . $BizName . "/";
	chop $SAVE_DIRECTORY if ($SAVE_DIRECTORY =~ /\/$/);
	if ( (!(-e $SAVE_DIRECTORY)) || (!(-W $SAVE_DIRECTORY)) || (!(-d $SAVE_DIRECTORY)) ) 
	{
		&Error("Bad directory! The directory you specified either doesn't exist, isn't writeable, or it's not a directory.");
	}
	foreach $key (sort {$a <=> $b} $query->param()) 
	{
		next if ($key =~ /^\s*$/);
		next if ($query->param($key) =~ /^\s*$/);
		next if ($key !~ /^file-to-upload-(\d+)$/);
		$Number = $1;
		
		if ($query->param($key) =~ /([^\/\\]+)$/) 
		{
			#$Filename = $1;
			$Filename =~ s/^\.+//;
			$File_Handle = $query->param($key);
			
			if (!$ALLOW_INDEX && $Filename =~ /^index/i) 
			{
				&Error("Filename problem! You attempted to upload a file that contains the word 'index', which is a no-no.");
			}
		} 
		else 
		{
			$FILENAME_IN_QUESTION = $query->param($key);
			&Error("Slashes in filename! Filenames can't contain slashes or other metacharacters.");
		}
		
        	if (!open(OUTFILE, ">$SAVE_DIRECTORY\/$Filename")) 
        	{
        	    $stringy = "The directory, $SAVE_DIRECTORY has problems.";
        	    $stringy .= " Specifically, I can't write to the file $Filename there.";
        	    $stringy .= "Be sure the directory is chmodded to 755 and the file ";
        	    $stringy .= "is 755 or better. Contact $admin. Error message: $!";
        	    &Error("$stringy");
        	}

			undef $BytesRead;
			undef $Buffer;
		
       	 while ($Bytes = read($File_Handle,$Buffer,1024)) 
       	 {
       	 	$BytesRead += $Bytes;
       	 	print OUTFILE $Buffer;
       	 }
		
		push(@Files_Written, "$SAVE_DIRECTORY\/$Filename");
		$TOTAL_BYTES += $BytesRead;
		$Confirmation{$File_Handle} = $BytesRead;
		close($File_Handle);
		close(OUTFILE);
		chmod (0755, "$SAVE_DIRECTORY\/$Filename");
    	}

	$FILES_UPLOADED = scalar(keys(%Confirmation));

	
	if ($TOTAL_BYTES > $MAXIMUM_UPLOAD && $MAXIMUM_UPLOAD > 0) 
	{
		foreach $File (@Files_Written) 
		{
			unlink $File;
		}
		$stringy = "You have reached your upload limit. ";
		$stringy .= "Please upload a smaller file, because the limit ";
		$stringy .= " is $MAXIMUM_UPLOAD. None of your files were ";
		$stringy .= "successfully uploaded.";
		&Error("$stringy");
	}
}
1;
