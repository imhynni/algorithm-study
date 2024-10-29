const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

const n = parseInt(input[0]);
const lines = [];
for (let i = 1; i <= n; i++) {
  lines.push(input[i].split(' ').map((v) => parseInt(v)));
}

lines.sort((a, b) => a[0] - b[0]);
const nums = lines.map((line) => line[1]);

const dp = Array(n).fill(1);
let maxCount = 0;

for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (nums[j] >= nums[i]) continue;
    dp[i] = Math.max(dp[i], dp[j] + 1);
    maxCount = Math.max(maxCount, dp[i]);
  }
}

console.log(n - maxCount);