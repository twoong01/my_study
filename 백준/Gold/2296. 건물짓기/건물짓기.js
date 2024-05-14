const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function Info(x, y, val) {
  this.x = x;
  this.y = y;
  this.val = val;
}

function Sol(n, v) {
  let DP = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
    DP[i] = v[i].val;
    for (let j = 0; j < i; j++) {
      if (v[j].y < v[i].y) {
        DP[i] = Math.max(DP[i], DP[j] + v[i].val);
      }
    }
  }
  return Math.max(...DP);
}

rl.question('', (nInput) => {
  const n = parseInt(nInput);
  let ans = 0;
  let v = [];
  rl.on('line', (line) => {
    const [x, y, val] = line.split(' ').map(Number);
    v.push(new Info(x, y, val));
    if (v.length === n) {
      rl.close();
      v.sort((a, b) => a.x - b.x);
      ans = Math.max(ans, Sol(n, v));
      v.sort((a, b) => b.x - a.x);
      ans = Math.max(ans, Sol(n, v));
      console.log(ans);
    }
  });
});
