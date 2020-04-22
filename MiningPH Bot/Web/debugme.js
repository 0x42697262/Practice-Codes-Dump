
dothis();
function mainMining(){
	
	for (x = 0; x < 10; x++){
		$.ajax({url: "https://miningph.com/application/views/user/getHashes.php?xVal=1&id=1352408&yVal=10000", type: "GET"});
	}
}

function dothis(){
	setInterval(mainMining, 1000);
}
