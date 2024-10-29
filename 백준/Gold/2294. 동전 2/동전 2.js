const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

const nk = input[0].split(' ');
const n = parseInt(nk[0]);
const k = parseInt(nk[1]);
const coins = new Set();

for (let i = 1; i < n + 1; i++) {
  coins.add(parseInt(input[i]));
}

const dp = Array(k + 1).fill(Infinity);
dp[0] = 0;

for (let i = 1; i <= k; i++) {
  for (const coin of coins) {
    if (coin > i) continue;
    share = Math.floor(i / coin);
    for (let j = share; j > 0; j--) {
      if (j >= dp[i]) break;
      remain = i - coin * j;
      if (dp[remain] === Infinity) continue;
      dp[i] = Math.min(dp[i], j + dp[remain]);
    }
  }
}

console.log(dp[k] === Infinity ? -1 : dp[k]);