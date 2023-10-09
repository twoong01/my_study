function solution(num) {
    var answer = 0;
    while(true) {
        if( num === 1) {
            break;
        }
        if( answer > 500 ){
            answer = -1;
            break;
        }
        answer += 1;
        if(num % 2 === 0) {
            num = num / 2;
            if (num === 1){
                break;   
            }
        } else {
            num = num * 3 + 1;
            if (num === 1){
                break;   
            }
        }
    }
    return answer;
}