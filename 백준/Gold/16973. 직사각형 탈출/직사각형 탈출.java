import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {-1, 1, 0, 0};

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] area = new int[N][M];
        boolean[][] visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                area[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int[] start = new int[2];
        int[] finish = new int[2];
        start[0] = Integer.parseInt(st.nextToken()) - 1;
        start[1] = Integer.parseInt(st.nextToken()) - 1;
        finish[0] = Integer.parseInt(st.nextToken()) - 1;
        finish[1] = Integer.parseInt(st.nextToken()) - 1;

        ArrayDeque<Point> q = new ArrayDeque<>();
        q.add(new Point(start[0], start[1]));
        visited[start[0]][start[1]] = true;

        int level = 0;

        while (!q.isEmpty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                Point curr = q.poll();

                if (curr.x == finish[0] && curr.y == finish[1]) {
                    System.out.println(level);
                    return;
                }

                Outer: for (int d = 0; d < 4; d++) {
                    int nx = curr.x + dx[d];
                    int ny = curr.y + dy[d];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) {
                        continue;
                    }

                    if (dx[d] == 0) {
                        int nc = dy[d] == -1 ? ny : curr.y + W;

                        if (nc < 0 || nc >= M) {
                            continue Outer;
                        }

                        for (int r = 0; r < H; r++) {
                            if (area[nx + r][nc] == 1) {
                                continue Outer;
                            }
                        }
                    } else {
                        int nr = dx[d] == -1 ? nx : curr.x + H;

                        if (nr < 0 || nr >= N) {
                            continue Outer;
                        }

                        for (int c = 0; c < W; c++) {
                            if (area[nr][ny + c] == 1) {
                                continue Outer;
                            }
                        }
                    }

                    q.add(new Point(nx, ny));
                    visited[nx][ny] = true;
                }
            }

            level++;
        }

        System.out.println(-1);
    }
}
