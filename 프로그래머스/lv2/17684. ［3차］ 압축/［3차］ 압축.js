function solution(msg) {
    var answer = [];
    const dictionary = {}
    let wordIdx = 1
    for(let i=65;i<65+26;i++){
        dictionary[String.fromCharCode(i)] = wordIdx++
    }
    let msgarr = msg.split('');
    let msgIdx = 0;
    let msgString = ''
    while(msg.length !== msgIdx){
        msgString = msgString.concat(msgarr[msgIdx]);
        console.log(msgString);
        if(dictionary[msgString]){
            msgIdx ++;
        } else {
            console.log(dictionary[msgString.slice(0, msgString.length -1)])
            answer.push(dictionary[msgString.slice(0,msgString.length - 1)])
            dictionary[msgString] = wordIdx++
            msgString = ''
        }
        if(msg.length === msgIdx){
            answer.push(dictionary[msgString])
        }
    }
    return answer;
}