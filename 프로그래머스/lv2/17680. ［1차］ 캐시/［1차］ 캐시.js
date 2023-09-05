function solution(cacheSize, cities) {
    var answer = 0;
    const cache = new Array();
    cities.forEach((value, index) => {
        const upValue = value.toUpperCase();
        if(cache.includes(upValue)){
            answer += 1;
        } else {
            answer += 5;
        }
        
        if(cacheSize > 0){
            if(cache.includes(upValue)){
                cache.splice(cache.indexOf(upValue), 1);
                cache.push(upValue);
            } else if(cache.length === cacheSize) {
                cache.shift();
                cache.push(upValue);
            } else {
                cache.push(upValue);
            }
        }
    })
    return answer;
}