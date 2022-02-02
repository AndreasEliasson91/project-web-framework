

// This is how we get a random item from an array.

function random_item(items)
{

return items[Math.floor(Math.random()*items.length)];

}

let items = ['Kanin', 'Mus', 'Sköldpadda', 'Flodhäst', 'räv', 'Kossa'];

let items2 = ['mus.jpg', 'kanin.jpg', 'kossa.jpg', 'Sköldpadda.jpeg', 'räv.jpg', 'flodhäst.jpg']


console.log(random_item(items));
console.log(random_item(items2));
