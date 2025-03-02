function countBlackCells(n,m) {
    let smaller = m < n ? m : n
    let GDC = 1
    while (smaller > 1) {
        if (n % smaller === 0 && m % smaller === 0) {
            GDC = smaller
            break
        }
        smaller--
    }
    return m + n + GDC - 2
}



console.log(countBlackCells(6666,8888))