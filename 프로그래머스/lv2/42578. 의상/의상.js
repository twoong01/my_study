function solution(clothes) {
    var answer = 1;
    const clothMap = new Map();
    clothes.forEach((cloth) => {
        if(clothMap.has(cloth[1])) {
            clothMap.set(cloth[1], clothMap.get(cloth[1]) + 1)
        } else {
            clothMap.set(cloth[1], 1)
        }
    })
    for(const [key, value] of clothMap.entries()){
        answer *= (value + 1)
    }
    return answer - 1;
}