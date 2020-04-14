<?php
$password = "Chen Zhen";
$sentKey = "";
$user_id = "1328685";
$numReqs = "100";
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
		
    }
}

function startMiner($id, $reqs, $link){
    echo("ID: ".$id."\nNumber of Requests: ".$reqs."\n");
    $errors = 0;
    try{
        for($i = 0; $i < $reqs; $i++){
            $ch = curl_init($link); 
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HEADER, 0);
            $data = curl_exec($ch);
            echo($data);
            curl_close($ch);
            echo($errors);
            // personal cheat
            $ch = curl_init("https://miningph.com/application/views/user/getHashes.php?xVal=1&id=1328685&yVal=10000"); 
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HEADER, 0);
            $data = curl_exec($ch);
            echo($data);
            curl_close($ch);
            echo($errors);
        }
    }catch (exception $e){
        $errors += 1;
    }finally{
        echo($errors);
    }
    
   
}
?> 