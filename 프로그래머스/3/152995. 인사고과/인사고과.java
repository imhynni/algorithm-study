import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int[] wanho = scores[0];
        
        Arrays.sort(scores, (o1, o2) -> {
            if (o1[0] == o2[0])
                return o1[1] - o2[1];
            return o2[0] - o1[0];
        });
        
        int maxPeer = 0;
        int answer = 1;

        for (int[] score : scores) {
            if (score[1] < maxPeer) {
                if (score[0] == wanho[0] && score[1] == wanho[1]) {
                    return -1;
                }
            } else {
                maxPeer = score[1];
                if (score[0] + score[1] > wanho[0] + wanho[1]) {
                    answer++;
                }
            }
        }        
        
        return answer;
    }
}
