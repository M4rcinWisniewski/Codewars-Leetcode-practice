const range = function(a, b = undefined, c = undefined) {
    const rangeResult = [];

    switch(true){
        case b == undefined && c == undefined:
            for (let i = 1; i < a + 1; i++){
                rangeResult.push(i);
            }
        case c == undefined &&  b != undefined:
            for (let i = a; i < b + 1; i++) {
                rangeResult.push(i);
            }
        default:
            for (let i = a; i < c + 1; i += b){
                rangeResult.push(i);
            }
    }
    
    return rangeResult;
}

console.log(range(1,1,1))