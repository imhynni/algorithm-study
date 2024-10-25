const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .split('\n');

const n = parseInt(input[0]);
const nums = input[1].split(' ').map((num) => parseInt(num));

const dp = Array(n).fill(1);
const linkedIndex = Array(n).fill(-1);
let count = 0;
let lastIndex = 0;

for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (nums[i] <= nums[j]) continue;
    if (dp[i] < dp[j] + 1) {
      dp[i] = dp[j] + 1;
      linkedIndex[i] = j;
    }
  }
  if (count < dp[i]) {
    count = dp[i];
    lastIndex = i;
  }
}

const answer = [];
let nextIndex = lastIndex;
while (nextIndex !== -1) {
  answer.push(nums[nextIndex]);
  nextIndex = linkedIndex[nextIndex];
}

console.log(answer.length);
console.log(answer.reverse().join(' '));
