const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

const n = parseInt(input[0]);
const tree = new Map();
const nodes = [
  { type: null, value: null },
  { type: null, value: 0 },
];
for (let i = 2; i <= n; i++) {
  const island = input[i - 1].split(' ');
  const a = parseInt(island[1]);
  const p = parseInt(island[2]);
  nodes.push({ type: island[0], value: a });
  if (!tree.has(p)) {
    tree.set(p, [i]);
  } else {
    tree.get(p).push(i);
  }
}

function dfs(v) {
  let count = 0;
  if (tree.has(v)) {
    for (const child of tree.get(v)) {
      count += dfs(child);
    }
  }
  if (nodes[v].type === 'S') {
    count += nodes[v].value;
  } else {
    count -= nodes[v].value;
    if (count < 0) count = 0;
  }
  return count;
}

console.log(dfs(1));