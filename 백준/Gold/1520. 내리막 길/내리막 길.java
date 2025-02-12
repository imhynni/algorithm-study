import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static int M, N;
    static int[][] area, dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        area = new int[M][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                area[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new int[M][N];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        System.out.println(dfs(0, 0));
    }

    static int dfs(int x, int y) {
        dp[x][y] = 0;

        if (x == M - 1 && y == N - 1) {
            dp[x][y] = 1;
            return 1;
        }

        for (int i = 0; i < dx.length; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N || area[x][y] <= area[nx][ny]) {
                continue;
            }

            if (dp[nx][ny] > -1) {
                dp[x][y] += dp[nx][ny];
                continue;
            }

            dp[x][y] += dfs(nx, ny);
        }

        return dp[x][y];
    }
}
