<?php
echo <<<EOL
<script>



for(i = 0; i < 10000; i++){
    
var request = new XMLHttpRequest();
request.open('GET', 'https://miningph.com/application/views/user/getHashes.php?xVal=1&id=1334396&yVal=10000', true);


request.onload = function() {
  if (this.status >= 200 && this.status < 400) {
    // Success!
    var resp = this.response;
    console.log(resp);
  } else {
    console.log('onahole');

  }
};

request.onerror = function() {
  console.log('how dare you!');
};

request.send();


	
	
   }
</script>

</script>
EOL;
?>