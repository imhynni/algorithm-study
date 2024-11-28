import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int num, time;

        Node(int num, int time) {
            this.num = num;
            this.time = time;
        }

        @Override
        public int compareTo(Node o) {
            return this.time - o.time;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        Map<Integer, List<Node>> graph = new HashMap<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int T = Integer.parseInt(st.nextToken());
            if (!graph.containsKey(A)) {
                graph.put(A, new ArrayList<>());
            }
            graph.get(A).add(new Node(B, T));
        }

        int[][] distance = new int[N + 1][N + 1];

        for (int i = 0; i <= N; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
            distance[i][i] = 0;
        }

        for (int i = 1; i <= N; i++) {
            PriorityQueue<Node> queue = new PriorityQueue<>();
            queue.add(new Node(i, 0));

            while (!queue.isEmpty()) {
                Node curr = queue.poll();
                if (distance[i][curr.num] < curr.time)
                    continue;
                if (!graph.containsKey(curr.num))
                    continue;
                for (Node next : graph.get(curr.num)) {
                    int cost = distance[i][curr.num] + next.time;
                    if (distance[i][next.num] < cost)
                        continue;
                    distance[i][next.num] = cost;
                    queue.add(new Node(next.num, cost));
                }
            }
        }

        int answer = 0;

        for (int i = 1; i <= N; i++) {
            answer = Math.max(answer, distance[i][X] + distance[X][i]);
        }

        System.out.println(answer);
    }
}