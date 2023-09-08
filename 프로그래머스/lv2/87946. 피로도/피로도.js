const getpermutation = function (arr, num) {
    const result = [];
    if(num === 1) return arr.map((el) => [el]);
    
    arr.forEach((fixed, idx, origin) => {
        const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
        const permutations = getpermutation(rest, num - 1); 
        const attached = permutations.map((el) => [fixed, ...el]);
        result.push(...attached);
    })
    return result
}

function solution(k, dungeons) {
    var answer = -Infinity;
    const res = getpermutation(dungeons, dungeons.length);
    
    res.forEach((arr, idx) => {
        let tmp = k;
        let count = 0;
        arr.forEach((value, idx) => {
            if(value[0] <= tmp){
                tmp -= value[1];
                count++;    
            }
        })
        answer = Math.max(answer, count);
    })
    
    return answer;

}