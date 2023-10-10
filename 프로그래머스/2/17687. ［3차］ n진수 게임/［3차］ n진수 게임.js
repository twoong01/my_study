function solution(n, t, m, p) {
    var answer = '';
    let total = []
    for(let i=0; i < t * m; i++){
        total.push(i)
    }
    let all_num = '';
    total.forEach((value) => {
        all_num += value.toString(n);
    })
    var tmp = p;
    for(let i=0; i < all_num.length; i++){
        if(answer.length === t) {
            break;
        }
        if(i === tmp - 1) {
            answer += all_num[i];
            tmp += m;
        }
    }
    answer = answer.toUpperCase()
    return answer;
}