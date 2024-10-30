const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt')
  .toString()
  .split('\n');

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  push(node) {
    if (this.isEmpty()) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }

  popLeft() {
    if (this.isEmpty()) return null;
    const node = this.head;
    this.head = this.head.next;
    if (this.head === null) this.tail === null;
    this.size--;
    return node.value;
  }
}

const T = +input[0];
let index = 1;

for (let t = 0; t < T; t++) {
  const [n, k] = input[index++].split(' ').map(Number);
  const duration = input[index++].split(' ').map(Number);
  const graph = new Map();
  const indegree = Array(n + 1).fill(0);
  for (let i = 0; i < k; i++) {
    const [x, y] = input[index++].split(' ').map(Number);
    if (!graph.has(x)) {
      graph.set(x, [y]);
    } else {
      graph.get(x).push(y);
    }
    indegree[y] += 1;
  }
  const W = +input[index++];
  const dp = Array(n + 1).fill(0);
  const queue = new Queue();
  let answer = 0;
  for (let i = 1; i <= n; i++) {
    if (indegree[i] === 0) {
      queue.push(new Node(i));
      dp[i] = duration[i - 1];
    }
  }

  while (!queue.isEmpty()) {
    const node = queue.popLeft();
    if (!graph.has(node)) continue;
    for (const child of graph.get(node)) {
      dp[child] = Math.max(dp[child], dp[node] + duration[child - 1]);
      indegree[child] -= 1;
      if (indegree[child] === 0) queue.push(new Node(child));
    }
  }

  console.log(dp[W]);
}