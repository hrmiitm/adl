// Literal syntax
const mysym = Symbol("k1")
const user = { name: "John", age: 25, [mysym]: 'v1' };

// Constructor
const obj = new Object({ city: "Mumbai" });

console.log(user)
console.log(user[mysym]) // frequentrly asked question

/* Output
{ name: 'John', age: 25, [Symbol(k1)]: 'v1' }
v1
*/

console.log(Object.keys(user)) // [ 'name', 'age' ]
console.log(Object.values(user)) // [ 'John', 25 ]
console.log(Object.entries(user)) // [ [ 'name', 'John' ], [ 'age', 25 ] ]

// Note symbols are not included, they are hidden