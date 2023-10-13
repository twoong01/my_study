function solution(begin, target, words) {
    var answer = 0;
    const visited = [];
    const q = [];
    if(!words.includes(target)){
        return 0;
    }
    q.push([begin, answer]);
    while(q){
        let [v, cnt] = q.shift();
        if(v === target){
            return cnt;
        }
        words.forEach((word) => {
            let notEqual = 0;
            
            if(visited.includes(word)) return;
            
            for(let i = 0; i < word.length; i++){
                if(word[i] !== v[i]) notEqual ++;
            }
            
            if(notEqual === 1){
                q.push([word, ++cnt]);
                visited.push(word);
            }
        })
    }
    return answer;
}