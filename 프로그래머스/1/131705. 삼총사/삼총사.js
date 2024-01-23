function solution(number) {
    var answer = 0;
    const getCombinations = function(arr, selectNumber) {
        const result = [];
        if(selectNumber === 1) return arr.map((value) => [value]);
        
        arr.forEach((fixed, index, origin) => {
            const rest = origin.slice(index + 1);
            const combinations = getCombinations(rest, selectNumber - 1);
            const attached = combinations.map((combination) => [fixed, ...combination]);
            result.push(...attached);
        })
        return result;
    }
    
    const com = getCombinations(number, 3);
    com.map((arr) => {
        const _sum = arr.reduce((a, b) => a + b, 0);
        if(_sum === 0){
            answer += 1;
        }
    })
    return answer;
}

