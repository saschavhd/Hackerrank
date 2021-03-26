function getMaxLessThanK(n, k) {
    let maxV = 0
    for (let i = 1; i < n; i++) {
        for (let j = i+1; j < n+1; j++) {
            if ((i & j) > maxV && (i & j) < k) {
                maxV = i & j;
            }
        }
    }
    return maxV
}
