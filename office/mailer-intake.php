
<meta http-equiv="Refresh" content="1; url=http://www.surflocalmedia.com">
<script src='https://www.google.com/recaptcha/api.js'></script>
    <!-- InstanceBeginEditable name="Content-Area" -->
    <div class="contenthold">
      <div class="wrapper">
        <h1><center><font color=000000>E-mail logo's and picture's to <a href="mailto:info@surflocalmedia.com"><font color=800000>info@surflocalmedia.com</a></font></font></h1>
        <p>
          <?PHP 
$to = "info@surflocalmedia.com"; 
$from = "info@surflocalmedia.com";
$headers = "From: $from \r\n";
$subject = "Intake Form";
$headers = "From: Surflocalmedia Ad Creation Form";
$forward = 0;
$location = "surflocalmedia.com";

$date = date ("l, F jS, Y"); 
$time = date ("h:i A"); 



$msg = "It was submitted on $date at $time.\n\n"; 

if ($_SERVER['REQUEST_METHOD'] == "POST") {
	foreach ($_POST as $key => $value) { 
		$msg .= ucfirst ($key) ." : ". $value . "\n"; 
	}
}
else {
	foreach ($_GET as $key => $value) { 
		$msg .= ucfirst ($key) ." : ". $value . "\n"; 
	}
}

mail($to, $subject, $msg, $headers); 
if ($forward == 1) { 
    header ("Location:$location"); 
} 
else { 
    echo "<b><center>Thank-You!  We will contact you shortly with information.</b>"; 
} 

?>
        </p>
        <br />
      </div>
    </div>
    <!-- InstanceEndEditable -->
