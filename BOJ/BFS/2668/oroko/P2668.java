import java.io.*;
import java.util.*;

public class P2668 {

    static int N;
    static int[] nums;
    static Set<Integer> pick;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N+1];
        for(int i = 1; i <= N; i++) nums[i] = Integer.parseInt(br.readLine());

        pick = new HashSet<>();
        for(int i = 1; i <= N; i++) {
            if(!pick.contains(i)) {
                dfs(i, i, new boolean[N+1]);
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(pick.size()));
        Integer[] pickArr = pick.toArray(new Integer[0]);
        Arrays.sort(pickArr);
        for(int n : pickArr) {
            bw.newLine();
            bw.write(String.valueOf(n));
        }
        bw.flush();
    }

    static void dfs(int start, int v, boolean[] visited) {
        if(v == start && visited[start]) {
            for(int i = 1; i <= N; i++) {
                if(visited[i]) pick.add(i);
            }
            return;
        }

        visited[v] = true;
        if(!visited[nums[v]] || nums[v] == start) dfs(start, nums[v], visited);
    }

}
