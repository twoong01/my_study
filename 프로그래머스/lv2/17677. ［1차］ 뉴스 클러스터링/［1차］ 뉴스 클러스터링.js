function solution(str1, str2) {
    var answer = 0;
    var regRex = /[`~!@#$%^&*|\\\'\";:\/?]/gi;
    if(str1.length === 0 && str2.length === 0) return 65536;
    const s1 = str1.toLowerCase();
    const s2 = str2.toLowerCase();


    const arr1 = [];
    const arr2 = [];
    for (let i = 0; i < s1.length - 1; i++) {
        if (/^[a-z]{2}$/g.test(s1[i] + s1[i + 1])) arr1.push(s1[i] + s1[i +         1])
    }
    for (let i = 0; i < s2.length - 1; i++) {
        if (/^[a-z]{2}$/g.test(s2[i] + s2[i + 1])) arr2.push(s2[i] + s2[i +         1])
    }
    const arr3 = [...arr2]
    let counter = 0;
  arr1.forEach((e, i) => {
    for (let j = 0; j < arr2.length; j++) {
      if (e === arr2[j]) {
        arr2.splice(j, 1);
        counter++
        break;
      }
    }
  })
  const g = arr1.length + arr3.length - counter
  return g ? parseInt((counter / g) * 65536) : 65536
}