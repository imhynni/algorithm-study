import java.io.*;
import java.util.*;

public class Main {
    static int[] dr = {0, 0, -1, 1};
    static int[] dc = {-1, 1, 0, 0};
    static int N;
    static int[][] area, visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        area = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                area[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new int[N][N];

        for (int[] row : visited) {
            Arrays.fill(row, -1);
        }

        int answer = 1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] == -1)
                    answer = Math.max(answer, dfs(i, j));
            }
        }

        System.out.println(answer);
    }

    static int dfs(int r, int c) {
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N || area[nr][nc] <= area[r][c]) {
                visited[r][c] = Math.max(visited[r][c], 1);
                continue;
            }

            if (visited[nr][nc] > -1) {
                visited[r][c] = Math.max(visited[r][c], visited[nr][nc] + 1);
                continue;
            }

            visited[r][c] = Math.max(visited[r][c], dfs(nr, nc) + 1);
        }

        return visited[r][c];
    }
}
