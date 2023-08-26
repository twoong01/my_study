function solution(arr) {
    var answer = 0;
    var gcd = function (a, b) {
        if(b === 0) return a;
        return gcd(b, a % b);
    }
    
    var lcm = function (a, b) {
        return a * b / gcd(a, b);
    }
    while(arr.length > 1) {
        let a = arr.pop(), b = arr.pop();
        let tmp = lcm(a, b);
        arr.push(tmp);
    }
    answer = arr[0]
    return answer;
}