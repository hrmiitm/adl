console.log(Array.isArray('Hitesh'))
console.log(Array.from('Hitesh'))   // Create Array from String
console.log(Array.from({name: 'hites'}))   // what will happen?

console.log()

console.log(Array.of(100, 200, 300))

console.log()
const arr = [1,2,3, true, "hi"]
const arr2 = [7,8,9]

console.log([...arr, ...arr2])