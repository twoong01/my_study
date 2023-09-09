function solution(info, edges) {
    var answer = 0;
    let edge_map = Array.from({length: info.length}, () => []);
    edges.forEach((edge, idx) => {
        edge_map[edge[0]].push(edge[1]);
    });
    
    function dfs (cur, sheep, wolf, pos) {
        let newPos = [...pos];
        let curidx = newPos.indexOf(cur);
        
        if(info[cur]){
            wolf++
        } else {
            sheep++
        }
        
        answer = Math.max(sheep, answer);
        
        if(sheep === wolf){
            return;
        }
        
        newPos.push(...edge_map[cur]);
        newPos.splice(curidx, 1);
        
        for(const next of newPos){
            dfs(next, sheep, wolf, newPos);
        }
    }
    
    dfs(0, 0, 0, [0]);
    return answer;
}