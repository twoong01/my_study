function solution(phone_book) {
    var answer = true;
    phone_book.sort()
    for(let i = 0; i < phone_book.length - 1;i++){
        let tmp_len = phone_book[i].length;
        if(phone_book[i] === phone_book[i + 1].substr(0, tmp_len))
            {
                return false   
        }
    }
    return answer;
}