function solution(elements) {
    var answer = [];
    const arr = [...elements, ...elements];
    elements.forEach((element, idx) => {
        for(let i = 0; i < elements.length;i++){
            const slice = arr.slice(i, i + 1 + idx);
            answer.push(slice.reduce((acc, cur) => acc + cur, 0));
        }
    })
    const set = new Set(answer);
    return [...set].length;
}