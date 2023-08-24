function solution(s) {
    var answer = 0;
    if(s.slice(0, 1) === '-'){
        answer = Number(s.slice(1, s.length)) * (-1)
    } else {
        answer = Number(s)
    }
    return answer;
}