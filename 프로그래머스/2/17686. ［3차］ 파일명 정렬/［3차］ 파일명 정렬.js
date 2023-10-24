function solution(files) {
    var answer = [];
    const fileSet = [];
    for(let i = 0; i < files.length; i++){
        const head = [];
        const number = [];
        const tail = [];
        for(let j = 0; j < files[i].length; j++){
            if(files[i][j].trim() === '' && number.length === 0){
                head.push(files[i][j]);
                continue;
            }
            if(!Number.isNaN(Number(files[i][j])) && number.length < 5){
                number.push(files[i][j]);
            }else {
                if(number.length == 0){
                    head.push(files[i][j]);
                } else {
                    tail.push(files[i].slice(j));
                    break;
                }
            }
        }
        fileSet.push([head.join(''), number.join(''), tail.join('')]);
    }
    fileSet.sort((a, b) => {
      const comp1 = a[0].toLowerCase().localeCompare(b[0].toLowerCase()); 
      if (comp1 !== 0) {
        return comp1;
      }

      const numA = parseInt(a[1], 10);
      const numB = parseInt(b[1], 10);
      return numA - numB;
    })
    for(let i = 0; i < fileSet.length; i++){
        answer.push(fileSet[i].join(''))
    }
    return answer;
}