<!DOCTYPE html>
<html>
	<head>
		<script src="//code.jquery.com/jquery-latest.js"></script>
		<script>
			var pageId = "<? echo $_GET['p']?>";
			$(document).ready(function(){
				if (pageId) {//viewer is looking for a user's webpage.
					$.ajax({
						url:"http://surflocal.net/assets/php/webpage_display.php",
						data:{p:pageId},
						type:'post',
						success:function(text) {
							$('#container').html(text);
						}
					});
				}
			});
		</script>
	</head>
	<body>
		<div id=container></div>
	</body>
</html>