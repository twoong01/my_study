function solution(s) {
    var answer = [];
    var tuples = [];
    var arr = s.slice(2, s.length-2).split('},{').forEach((str) => {
        let newArr = str.split(',').map(tuple => Number(tuple));
        tuples.push(newArr);
    })
    tuples.sort((a, b) => a.length - b.length)
    tuples.forEach((el) => {
        el.forEach((e) => {
            if(!answer.includes(e)){
                answer.push(e)
            }
        })
    })
    return answer;
}