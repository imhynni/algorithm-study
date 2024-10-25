const input = require('fs')
  .readFileSync(
    process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  )
  .toString()
  .split('\n');

const n = parseInt(input[0]);
const nums = input[1].split(' ').map((num) => parseInt(num));
const left = Array(n).fill(1);
const right = Array(n).fill(1);

for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (nums[j] >= nums[i]) continue;
    left[i] = Math.max(left[i], left[j] + 1);
  }
}

for (let i = n - 2; i > -1; i--) {
  for (let j = n - 1; j > i; j--) {
    if (nums[j] >= nums[i]) continue;
    right[i] = Math.max(right[i], right[j] + 1);
  }
}

let answer = 0;
for (let i = 0; i < n; i++) {
  answer = Math.max(answer, left[i] + right[i] - 1);
}

console.log(answer);