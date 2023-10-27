function solution(m, n, board) {
    var answer = 0;
    let curBoard = [...board.map(block => [...block])].concat();
    let newBoard = [...board.map(block => [...block])].concat();
    while(true){
        let count = 0;
        for(let i = 0; i < m - 1; i++){
            for(let j = 0; j < n - 1; j++){
                if(curBoard[i][j] === '')continue
                const tmp = curBoard[i][j];
                if(tmp === curBoard[i][j + 1] && tmp === curBoard[i + 1][j] && tmp === curBoard[i + 1][j + 1]) {
                    newBoard[i][j] = '';
                    newBoard[i][j + 1] = '';
                    newBoard[i + 1][j] = '';
                    newBoard[i + 1][j + 1] = '';
                    count += 1;
                }
            }
        }
        
        for (let x = 0; x < m - 1; x++) {
            for (let y = 0; y < n; y++) {
                if (newBoard[x + 1][y] === '') {
                    for (let i = x; i >= 0; i--) {
                        newBoard[i + 1][y] = newBoard[i][y];
                        newBoard[i][y] = '';
                    }
                }
            }
        }
        curBoard = [...newBoard.map(block => [...block])].concat();
        if (count === 0) break;
    }
    answer = curBoard.reduce((acc, cur) => acc.concat(cur));
    return answer.filter(block => block === '').length;
}