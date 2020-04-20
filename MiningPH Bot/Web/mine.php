<?php
$password = "Chen Zhen";
$sentKey = "";
$user_id = "1352408";
$numReqs = "100";
$URLm = "";

if(isset($_POST['submit'])){
    $sentKey = htmlspecialchars($_POST['key'], ENT_QUOTES, 'UTF-8');

    $user_id = htmlspecialchars($_POST['user_id'], ENT_QUOTES, 'UTF-8');
    $numReqs = htmlspecialchars($_POST['num_req'], ENT_QUOTES, 'UTF-8');
    

    $URLm = "https://miningph.com/application/views/user/getHashes.php?xVal=1&id=".$user_id."&yVal=10000";
    startMiner($user_id, $numReqs, $URLm);
    if($sentKey == $password){
        startMiner($user_id, $numReqs, $URLm);
    }else{
        echo("Key error...");
		
    }
}

function startMiner($id, $reqs, $link){
    echo("ID: ".$id."\nNumber of Requests: ".$reqs."\n");
    for($i = 0; $i < $reqs; $i++){
        $errors = 0;

        $options = array(
            'http' => array('method' => 'GET')
            );
        $context = stream_context_create($options);
        $result = file_get_contents($link, false, $context);
        if ($result === FALSE){$errors += 1;}

        var_dump($result);
        echo("\nErrors: " . $errors);
            
        }
        
    }
    

    
   

?> 
