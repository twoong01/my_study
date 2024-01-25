function solution(n) {
    const t_n = n.toString(3);
    const re_t_n = [...t_n].reverse().join("")
    const answer = parseInt(re_t_n, 3);
    return answer;
}