function solution(n, left, right) {
    var answer = [];
    for(let i = left; i < right + 1; i++){
        answer.push(Number.parseInt(Math.max(i / n, i % n) + 1));
    }
    return answer;
}