
const snail = arr => {
    const len = arr.length
    result = []
    let top = 0
    let bottom = len
    let right = len
    let left = 0

    if (arr[0].length === 0) {
        result.push([])
    }

    while (result.length < len ** 2) {
        // Move Right
        for (let y = left; y < right; y++) result.push(arr[top][y]);
        top++;

        // Move Down
        if (top < bottom) {
            for (let x = top; x < bottom; x++) result.push(arr[x][right - 1]);
            right--;
        }

        // Move Left
        if (left < right) {
            for (let y = right - 1; y >= left; y--) result.push(arr[bottom - 1][y]);
            bottom--;
        }

        // Move Up
        if (top < bottom) {
            for (let x = bottom - 1; x >= top; x--) result.push(arr[x][left]);
            left++;
        }
    }


    if (len % 2 == 0) return result
    result.pop()
    return result
}

const fourxfour = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
const thirdxthird = [[1,2,3],[4,5,6],[7,8,9]]
console.log(snail([[]]))