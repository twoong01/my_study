function solution(n, m) {
    var answer = [];
    let getgcd = (num1, num2) => (num2 > 0 ? getgcd(num2, num1 % num2) : num1);
    const gcd = getgcd(n, m);
    answer = [gcd, (n * m) / gcd]
    return answer;
}