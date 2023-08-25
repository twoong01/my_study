function solution(n) {
    var answer = 0;
    if(Number.isInteger(n ** 0.5)){
        answer = ((n ** 0.5) + 1) ** 2;
    } else {
        answer = -1
    }
    
    return answer;
}