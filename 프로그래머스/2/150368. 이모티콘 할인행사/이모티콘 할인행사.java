import java.util.*;

class Solution {
    static int[] rates = { 10, 20, 30, 40 };
    static int[] discount;
    static int[] answer = { 0, 0 };
    
    public int[] solution(int[][] users, int[] emoticons) {
        int N = emoticons.length;
        discount = new int[N];
        
        permutations(N, 0, users, emoticons);
        
        return answer;
    }
    
    static void permutations(int n, int depth, int[][] users, int[] emoticons) {
        if (depth == n) {
            int plus = 0;
            int sales = 0;
            
            for (int[] user : users) {
                int buy = 0;
                
                for (int i = 0; i < n; i++) {
                    if (discount[i] >= user[0]) {
                        buy += emoticons[i] * ((100 - discount[i]) / 100.0);
                    }
                }
                
                if (buy >= user[1]) {
                    plus += 1;
                } else {
                    sales += buy;
                }
            }
            
            if (answer[0] < plus) {
                answer[0] = plus;
                answer[1] = sales;
            } else if (answer[0] == plus) {
                answer[1] = Math.max(answer[1], sales);
            }
            
            return;
        }
        
        for (int r : rates) {
            discount[depth] = r;
            permutations(n, depth + 1, users, emoticons);
        }
    }
}

// 일정 비율 이상 할인하는 이모티콘 모두 구매
// 비용이 일정 가격 이상 되면 취소하고 플러스 가입
// 가입자 최대, 판매액 최대

// 40 40 40 40
// 40 40 40 30
// 40 40 30 40
// ...