const fs = require('fs');
const [con, inputArr] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = con.split(' ');
const trees = inputArr
  .trim()
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

function solution(arr, target) {
  let start = 0;
  let end = trees[trees.length - 1];
  let answer = Number.MIN_SAFE_INTEGER;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let _sum = 0;
    for (let x of arr) {
      if (x > mid) _sum += x - mid;
    }

    if (_sum >= target) {
      answer = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return answer;
}

console.log(solution(trees, m));
