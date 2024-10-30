const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

const T = +input[0];
let index = 1;
let duration;
let graph;
let dp;

for (let t = 0; t < T; t++) {
  const [n, k] = input[index++].split(' ').map(Number);
  duration = input[index++].split(' ').map(Number);
  graph = new Map();
  dp = Array(n + 1).fill(-1);
  for (let i = 0; i < k; i++) {
    const [x, y] = input[index++].split(' ').map(Number);
    if (!graph.has(y)) {
      graph.set(y, [x]);
    } else {
      graph.get(y).push(x);
    }
  }
  const W = +input[index++];

  console.log(dfs(W));
}

function dfs(v) {
  if (dp[v] !== -1) return dp[v];

  let result = 0;
  if (graph.has(v)) {
    for (const parent of graph.get(v)) {
      result = Math.max(result, dfs(parent));
    }
  }
  dp[v] = result + duration[v - 1];
  return dp[v];
}