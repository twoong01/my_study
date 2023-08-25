function solution(x) {
    var answer = true;
    let total = 0;
    const str_x = String(x);
    for(let i = 0; i < str_x.length;i++){
        total += Number(str_x[i]);
    }
    if(x % total === 0){
        return true;
    } else {
        return false
    }
}