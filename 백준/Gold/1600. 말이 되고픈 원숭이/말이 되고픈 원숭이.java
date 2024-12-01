import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {-1, 0, 1, 0, -2, -2, -1, 1, 2, 2, 1, -1};
    static int[] dy = {0, 1, 0, -1, -1, 1, 2, 2, 1, -1, -2, -2};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int[][] area = new int[H][W];
        boolean[][][] visited = new boolean[H][W][K + 1];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++)
                area[i][j] = Integer.parseInt(st.nextToken());
        }
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, K});
        visited[0][0][K] = true;
        boolean finish = false;
        int answer = 0;
        top:
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                if (curr[0] == H - 1 && curr[1] == W - 1) {
                    finish = true;
                    break top;
                }
                int len = curr[2] > 0 ? dx.length : 4;
                for (int j = 0; j < len; j++) {
                    int nx = curr[0] + dx[j];
                    int ny = curr[1] + dy[j];
                    if (nx < 0 || nx >= H || ny < 0 || ny >= W)
                        continue;
                    if (area[nx][ny] != 0) continue;
                    // 말처럼 움직이는 경우
                    if (j > 3) {
                        if (visited[nx][ny][curr[2] - 1]) continue;
                        visited[nx][ny][curr[2] - 1] = true;
                        q.add(new int[]{nx, ny, curr[2] - 1});
                        continue;
                    }
                    if (visited[nx][ny][curr[2]]) continue;
                    visited[nx][ny][curr[2]] = true;
                    q.add(new int[]{nx, ny, curr[2]});
                }
            }
            answer++;
        }
        if (!finish)
            answer = -1;
        System.out.println(answer);

    }
}