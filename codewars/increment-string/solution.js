function areThereZeros(numStr) {
    let zeros = ''
    for (let i = 0; i < numStr.length; ++i) {
        if (numStr[i] == '0') {zeros += numStr[i]}
    
    }
    return zeros
}
console.log(areThereZeros('foobar000'))
const incrementString = function(str) {
    const nums = ['0', '1', '2', '3', '4', '5','6','7','8','9']
    let result = ''
    let numberToIncrement = ''
    
    for (let i = 0; i < str.length; ++i) {
        nums.forEach(el => {
        if (el === str[i]) {
            numberToIncrement += str[i]
        } 

    })
    
    }
    
    for(let j = 0; j < str.length - numberToIncrement.length; j++) {
        result += str[j]
    }
    const temp = numberToIncrement
    if (numberToIncrement ==  0){
        zeros = ''

        for (let k =0; k < areThereZeros(numberToIncrement).length; ++k) zeros + areThereZeros(numberToIncrement)[k]
        numberToIncrement++
        return result + zeros + numberToIncrement.toString()
    }
    
    parseInt(numberToIncrement)
    numberToIncrement++
    return result + areThereZeros(temp) + numberToIncrement.toString()
}


console.log(incrementString('foobar000'))
