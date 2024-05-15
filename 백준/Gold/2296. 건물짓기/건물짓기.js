const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = parseInt(input[0]);
const Buildings = input.slice(1).map((str) => str.split(' ').map(Number));

function max_profit(n, buildings) {
  buildings.sort((a, b) => a[0] - b[0]);

  let dp = buildings.map(([x, y, c]) => [c, c]);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (buildings[j][1] < buildings[i][1]) {
        dp[i][0] = Math.max(dp[i][0], dp[j][0] + buildings[i][2]);
      }
      if (buildings[j][1] > buildings[i][1]) {
        dp[i][1] = Math.max(dp[i][1], dp[j][1] + buildings[i][2]);
      }
    }
  }
  let answer = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < dp.length; i++) {
    answer = Math.max(answer, dp[i][0], dp[i][1]);
  }
  return answer;
}

console.log(max_profit(N, Buildings));
