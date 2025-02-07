class Solution {
    public int solution(String arr[]) {
        int answer = -1;
        int n = arr.length;
        int[][] dpMin = new int[n][n];
        int[][] dpMax = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dpMin[i][j] = Integer.MAX_VALUE;
                dpMax[i][j] = Integer.MIN_VALUE;
            }
        }
        
        for (int i = 0; i < n; i += 2) {
            dpMin[i][i] = Integer.parseInt(arr[i]);
            dpMax[i][i] = Integer.parseInt(arr[i]);
        }

        for (int i = 2; i < n; i += 2) {
            for (int j = 0; j + i < n; j += 2) {
                for (int k = j + 1; k < j + i; k += 2) {
                    if (arr[k].equals("+")) {
                        dpMin[j][j + i] = Math.min(dpMin[j][j + i], dpMin[j][k - 1] + dpMin[k + 1][j + i]);
                        dpMax[j][j + i] = Math.max(dpMax[j][j + i], dpMax[j][k - 1] + dpMax[k + 1][j + i]);
                    } else {
                        dpMin[j][j + i] = Math.min(dpMin[j][j + i], dpMin[j][k - 1] - dpMax[k + 1][j + i]);
                        dpMax[j][j + i] = Math.max(dpMax[j][j + i], dpMax[j][k - 1] - dpMin[k + 1][j + i]);
                    }
                }
            }
        }
        
        return dpMax[0][n - 1];
    }
}
