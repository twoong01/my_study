function solution(n) {
    var answer = 0;
    
    let newArr = [1, 1];
    for(let i = 2; i < n + 1; i++){
        newArr.push((newArr[i - 1] + newArr[i - 2]) % 1234567);
    }
    answer = newArr[n] % 1234567
    return answer
}

