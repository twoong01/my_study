function solution(n, k) {
    var answer = 0;
    const toStringKnum = n.toString(k).split('0').map(str=>Number(str)).filter(num => num !== 1 && num !== 0)
    toStringKnum.forEach((value, idx) => {
        let isDivide = false;
        for(let i=2;i<=Math.sqrt(value);i++){
            if(value % i === 0){
                isDivide = true
                break
            }
        }
        answer += (isDivide ? 0 : 1)
    })
    return answer;
}