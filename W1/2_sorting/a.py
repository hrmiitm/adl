arr = [3, 6, 9, 7, 2, 3, 1]
n = arr.length // 7

for(let i=0; i<n; i++){
    
    let key = arr[i]
    let j = i-1

    while(j>0 && arr[j] > key){
        arr[j+1] = arr[j]
        j--
    }

    arr[j+1] = key
}
console.log(arr)