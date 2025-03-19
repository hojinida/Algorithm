import java.util.*;
class Solution {
    public long solution(long n) {
        String str = String.valueOf(n);
        List<Integer> arr = new ArrayList<>();
        for(int i =0 ;i<str.length();i++){
            arr.add(Integer.valueOf(str.charAt(i) - '0'));
        }
        arr.sort(Comparator.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for(int num: arr){
            sb.append(num);
        }
        str = sb.toString();
        return Long.valueOf(str);
    }
}