<?php
ini_set('max_execution_time', '0');
$user_id = "1352408";
$numReqs = "10000";
$URLm = "http://miningph.com/application/views/user/getHashes.php?xVal=1&id=".$user_id."&yVal=10000";


startLoop();
function startLoop(){
	global $URLm;
	while(true){
		
		$options = array('http' => array('method' => 'GET'));
		$context = stream_context_create($options);
		$result = fopen($URLm, 'r', false, $context);
		fpassthru($result);
		fclose($result);
	}
		
}
?>
