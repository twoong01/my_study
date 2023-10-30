function solution(m, n, puddles) {
    const maps = [];
    for(let i = 0; i < n; i++) maps.push(Array(m).fill(0))
    maps[0][0] = 1;
    puddles.forEach(e => {
        let [ x, y ] = e;
        maps[y - 1][x - 1] = -1;
    });
    maps.forEach((arr, y) => {
        arr.forEach((e, x) => {
            if(e !== -1){
                let n = e + (x > 0 && maps[y][x-1] !== -1 ? maps[y][x-1] : 0) + (y > 0 && maps[y-1][x] !== -1 ? maps[y-1][x] : 0);
                        n = n % 1000000007;
                        maps[y][x] = n;}
        })
    })
    return maps[n - 1][m - 1] % 1000000007;
}