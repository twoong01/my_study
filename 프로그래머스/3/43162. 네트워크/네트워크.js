function solution(n, computers) {
    var answer = 0;
    let visited = Array(n).fill(false);
    for(let i = 0; i < computers.length; i++){
        if(visited[i] === false) {
            dfs(i, n, visited, computers);
            answer += 1;
        }
    }
    return answer;
}

function dfs(i, n, visited, computers) {
    visited[i] = true;
    for(let j = 0; j < n; j++){
        if(i !== j && computers[i][j] === 1) {
            if(!visited[j]){
                dfs(j, n, visited, computers)
            }
        }
    }
}