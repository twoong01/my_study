function solution(want, number, discount) {
    var answer = 0;
    const isMatch = (discount) => {
        let wantMap = new Map();
        discount.map((v) => wantMap.set(v, (wantMap.get(v) || 0) + 1));
        for(let i = 0; i < want.length; i++){
            if(wantMap.get(want[i]) !== number[i]) return false;
        }
        return true;
    }
    for(let i = 0; i < discount.length; i++){
        const d = discount.slice(i, i + 10);
        if(isMatch(d)){
            answer++;
        }
    }
    
    return answer;
}