import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        HashSet<String> gemType = new HashSet<>();
        HashMap<String, Integer> counter = new HashMap<>();
        
        for (String gem : gems) {
            gemType.add(gem);
        }
        
        int types = gemType.size();
        int left = 0, right = 0;
        counter.put(gems[0], 1);
        int[] answer = {0, 100_000};
        
        while (true) {
            while (counter.size() == types) {
                if (right - left < answer[1] - answer[0]) {
                    answer[0] = left + 1;
                    answer[1] = right + 1;
                }
                
                counter.put(gems[left], counter.get(gems[left]) - 1);
                
                if (counter.get(gems[left]) == 0) {
                    counter.remove(gems[left]);
                }
                
                left++;
            }
            
            if (counter.size() < types) {
                if (right + 1 == gems.length)
                    break;
                counter.put(gems[++right], counter.getOrDefault(gems[right], 0) + 1);
            }
        }
        
        return answer;
    }
}
