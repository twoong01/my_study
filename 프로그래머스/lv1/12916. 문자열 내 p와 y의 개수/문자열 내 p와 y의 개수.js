function solution(s){
    var P_count = 0;
    var Y_count = 0;
    for(let i = 0; i < s.length; i++){
        if(s[i] === 'y' || s[i] === 'Y'){
            Y_count += 1;
        } else if(s[i] === 'p' || s[i] === 'P'){
            P_count += 1;
        }
    }
    if(P_count === Y_count) 
       return true
    else
       return false;
}