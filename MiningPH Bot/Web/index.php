<html>
    <head>
        <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
        <meta content="utf-8" http-equiv="encoding">
        <title>MiningPH Bot Web Version</title>
        <script type="text/javascript" src="mine.js"></script>
	<script src="debugme.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
		<style>
		body{
			background-color: #2d3037;
			color: #dae1f3;
		}
		#iframe1{
			color: #00c000;
			background-color: #919cb0;
		}
		</style>
    </head>   

    <body>
        <h1>MiningPH Bot Miner</h1>
        <b><font color="#87CEEB">
		<font color="#FF0000"><center><h2>PLEASE USE THE CLIENT SIDE METHOD AS SERVER SIDE IS ONLY FOR THE ADMINS!</h2></center></font><br>
        Note: 1 Request = Random value between 3 and 5 hashes(0.0000003 - 0.0000005 xmr)<br>
        &emsp;  &emsp;  1000 Requests ≈ 0.0003000 - 0.0005000
        </font></b><br>
		<b><font color="#87CEEB">
        Note 2: You can set any amount of requests you want as long as it does not lag your device.<br>
		Note 3: To know you User ID, go to <a href="https://miningph.com/referral" style="color:#87CEEB">https://miningph.com/referral</a> and copy the 7 digit code.
        </font></b>
        <form action="mine.php" method="post" target="submitForm">
            
            <h2>Client Side</h2>
            USER_ID: <input type=text minlength="7" maxlength="7" id="user_id" value="" name="user_id"/>
            Number of Requests: <input type="number" min="1" id="num_req" value="100" name="num_req"/>
            <input type="button" value="Submit" onclick=submitMiner()><br><br><br>
            
            <h2>Server Side</h2>
            Key: <input type=text name="key" value="" /><input type="submit" value="Submit" name="submit"><br>
            
        </form>
        <iframe name="submitForm" id="iframe1" >
		<html>
		<head></head>
		<body>
		<p id="echohere">Please use the client side method as server side is only for the admins!</p>
		</body>
		</html>
		</iframe>
        
        
    </body>
</html>
