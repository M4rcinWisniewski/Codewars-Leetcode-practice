function sumPairs(arr, sum) {
    let firstIndex = -1;
    let secondIndex = -1;

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (i != j && arr[i] + arr[j] == sum) {
                if (secondIndex > j || secondIndex == -1) {
                    firstIndex = i
                    secondIndex = j
                }
            }
        }
    }
    if (firstIndex > secondIndex){
        let temp = firstIndex
        firstIndex = secondIndex
        secondIndex = temp
    }
    if (firstIndex === -1 || secondIndex === -1){
        return undefined
    }
    let result = [];
    result.push(arr[firstIndex]);
    result.push(arr[secondIndex]);
    
    let string = JSON.stringify(result);
    return string
  
}
console.log(sumPairs([1, 4, 8, 7, 3, 15], 8))