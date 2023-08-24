function solution(x, n) {
    var answer = [];
    var tmp = x;
    for(let i = 0;i <  n; i++){
        answer.push(tmp);
        tmp += x;
    }
    
    return answer;
}