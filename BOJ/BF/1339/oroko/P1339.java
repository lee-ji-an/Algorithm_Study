import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class P1339 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < N; i++) {
            String word = br.readLine();
            int r = 1;
            for(int j = word.length()-1; j >= 0; j--) {
                map.put(word.charAt(j), map.getOrDefault(word.charAt(j), 0) + r);
                r *= 10;
            }
        }
        Object[] values = map.values().toArray(new Integer[0]);
        Arrays.sort(values, Collections.reverseOrder());
        int sum = 0;
        int r = 9;
        for(int value : (Integer[]) values) sum += value * r--;
        System.out.println(sum);
    }

    /** 순열 풀이 - 시간 초과 */
    static int max = 0;
    static String[] words;
    static Character[] alphabets;
    public static int sum(int[] nums) {
        int sum = 0;
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) map.put(alphabets[i], nums[i]);
        for(String word : words) {
            StringBuilder num = new StringBuilder();
            for(int j = 0; j < word.length(); j++) num.append(map.get(word.charAt(j)));
            sum += Integer.parseInt(num.toString());
        }
        return sum;
    }
    public static void perm(int[] arr, int[] sub, int r, boolean[] visited) {
        if(r == 0) {
            max = Math.max(max, sum(sub));
            System.out.println(Arrays.toString(sub));
            return;
        }
        for(int i = 0; i < arr.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                sub[arr.length-r] = arr[i];
                perm(arr, sub, r-1, visited);
                visited[i] = false;
            }
        }
    }

    public static void main1(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        words = new String[N];
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < N; i++) {
            words[i] = br.readLine();
            for(int j = 0; j < words[i].length(); j++) set.add(words[i].charAt(j));
        }
        alphabets = set.toArray(new Character[0]);
        int[] nums = IntStream.range(0, alphabets.length).map(i -> 9-i).toArray();
        perm(nums, new int[nums.length], nums.length, new boolean[nums.length]);
        System.out.println(max);
    }
}
