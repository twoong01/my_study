function solution(s) {
    var answer = 0;
    let tmp = s;
    for(let i = 0; i < s.length; i++){
        tmp = tmp.slice(1) + tmp[0];
        answer += isCorrect(tmp);
    }
    return answer;
}

function isCorrect(s) {
    let stack = [];
    for(const char of s){
        if(char === '[' || char === '{' || char === '('){
            stack.push(char);
        } else if(char === ']' && stack[stack.length - 1] === '['){
            stack.pop()
        } else if(char === '}' && stack[stack.length - 1] === '{'){
            stack.pop()
        } else if(char === ')' && stack[stack.length - 1] === '('){
            stack.pop()
        } else {
            return 0;
        }
    }
    return stack.length === 0 ? 1 : 0
}
