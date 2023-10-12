function solution(numbers, target) {
    var answer = 0;
    const addTarget = (tmp, sum, res) => {
        if(numbers.length === tmp) {
            if(sum === target) {
                res += 1;
            }
            answer += res;
            return;
        }
        addTarget(tmp + 1, sum + numbers[tmp], res);
        addTarget(tmp + 1, sum - numbers[tmp], res);
    }
    
    addTarget(0, 0, answer);
    return answer;
}