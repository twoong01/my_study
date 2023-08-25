function solution(n) {
    var answer = 0;
    answer = Number(String(n).split('').sort().reverse().join(''));
    return answer;
}