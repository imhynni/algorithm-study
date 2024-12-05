import java.util.*;

class Solution {
    static int SCORE_SIZE = 11;
    static int[] lion = new int[SCORE_SIZE];
    static int maxDiff = 0;
    static int[] answer = {};
    
    public int[] solution(int n, int[] info) {        
        combinations(n, 0, 0, info);
        
        if (answer.length == 0) {
            answer = new int[]{-1};
        }
        
        return answer;
    }
    
    static void combinations(int n, int depth, int start, int[] apeach) {
        if (depth == n) {
            // 점수 계산
            int lionScore = 0, apeachScore = 0;
            for (int i = 0; i < SCORE_SIZE; i++) {
                if (lion[i] == 0 && apeach[i] == 0) {
                    continue;
                }
                if (lion[i] <= apeach[i]) {
                    apeachScore += 10 - i;
                } else {
                    lionScore += 10 - i;
                }
            }
            // 라이언이 우승할 때
            if (lionScore > apeachScore) {
                int diff = lionScore - apeachScore;
                if (diff < maxDiff) {
                    return;
                }
                // 가장 낮은 점수를 더 많이 맞히는 사람이 이김
                if (diff == maxDiff) {
                    for (int i = SCORE_SIZE - 1; i > -1; i--) {
                        if (answer[i] > lion[i]) {
                            return;
                        }
                        if (answer[i] < lion[i]) {
                            answer = Arrays.copyOf(lion, lion.length);
                            return;
                        }
                    }
                    return;
                }
                maxDiff = diff;
                answer = Arrays.copyOf(lion, lion.length);
            }
            return;
        }
        
        for (int i = start; i < SCORE_SIZE; i++) {
            lion[10 - i]++;
            combinations(n, depth + 1, i, apeach);
            lion[10 - i]--;
        }
    }
}

// 라이언 저번 우승자
// 어피치랑 대결
// 어피치 n발 쏘고 라이언 n발
// 각 점수에 더 많이 맞힌 사람이 그 점수 가져감
// 동점이면 어피치 승
// info 10점부터
// 답은 가장 낮은 점수를 더 많이 맞힌 경우를 리턴
// 우승 불가면 [-1]

// 0부터 10까지 점수 11개 중에 n개 고르기 중복 조합
// 0 0 0 0 0 -> 0 5개
// 0 0 0 0 1 -> 0 4개, 1 1개
// 0 0 0 0 2 -> 0 4개, 2 1개
// 0 0 0 0 3
// 0 0 0 0 4 ...
// ..
// 0 0 0 1 1 -> 마지막은 0부터 하면 중복이니까 1부터 해야 됨

// 골라서 점수 계산
// 우승이면 현재 저장된 정답이랑 가장 낮은 점수부터 비교
