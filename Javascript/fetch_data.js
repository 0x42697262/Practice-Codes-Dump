url = "https://coderbyte.com/api/challenges/json/age-counting"

let count = 0;
fetch(url)
  .then(resp => resp.json())
  .then(data => {
    const items = data.data.split(', ');

    for(let i = 1; i < items.length; i += 2){
      const age = parseInt(items[i].split('=')[1], 10);
      if (age >= 50){
        count++;
      }
    }
  })
console.log(count);
