import java.util.*;
import java.io.*;

public class Main {
    static class Item {
        int weight, value;

        Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Item[] items = new Item[N + 1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int W = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            items[i] = new Item(W, V);
        }
        int[][] dp = new int[N + 1][K + 1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                if (items[i].weight > j) {
                    dp[i][j] = dp[i - 1][j];
                    continue;
                }
                dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - items[i].weight] + items[i].value);
            }
        }

        System.out.println(dp[N][K]);
    }
}