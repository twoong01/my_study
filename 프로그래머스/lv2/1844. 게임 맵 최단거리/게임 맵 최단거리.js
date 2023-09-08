function solution(maps) {
    var answer = 0;
    const row = maps.length;
    const col = maps[0].length;
    let is_visited = Array.from(Array(row), () => Array(col).fill(false));
    is_visited[0][0] = true;
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const start = [0, 0, 1];
    let q = [start];
    while (q.length > 0) {
        const [x, y, count] = q.shift();
        for(let k = 0; k < 4; k++){
            let nx = x + dx[k];
            let ny = y + dy[k];
            if(nx >= 0 && nx < row && ny >= 0 && ny < col && maps[nx][ny] === 1 && !is_visited[nx][ny]){
                is_visited[nx][ny] = true;
                q.push([nx, ny, count + 1]);
                if(nx === row - 1 && ny === col - 1){
                    console.log(is_visited);
                    return count + 1;
                }
            }
        }
    }
    return -1;
}