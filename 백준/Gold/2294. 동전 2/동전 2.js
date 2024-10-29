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

for (const coin of coins) {
  for (let i = coin; i <= k; i++) {
    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
  }
}

console.log(dp[k] === Infinity ? -1 : dp[k]);