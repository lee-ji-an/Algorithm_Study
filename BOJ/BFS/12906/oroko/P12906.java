import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P12906 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] towers = new String[3];
        int[] wrong = new int[3];
        for(int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            if(N == 0) {
                towers[i] = "";
                continue;
            }
            String s = st.nextToken();
            towers[i] = s;
            for(int j = 0; j < N; j++) {
                char c = s.charAt(j);
                if (c - 'A' != i) wrong[i]++;
            }
        }
        System.out.println(bfs(towers, wrong));
    }

    public static int bfs(String[] towers, int[] wrong) {
        Queue<State> q = new LinkedList<>();
        q.add(new State(towers, wrong, 0));
        Set<MyStringArray> visited = new HashSet<>();
        visited.add(new MyStringArray(towers));
        while(!q.isEmpty()) {
            State s = q.remove();
            if(s.wrong[0] == 0 && s.wrong[1] == 0 && s.wrong[2] == 0) return s.cnt;
            for(int i = 0; i < 3; i++) {    // i -> j 막대로 이동
                if(s.wrong[i] > 0 && s.towers[i].length() > 0) {
                    for(int j = 0; j < 3; j++) {
                        if(i == j) continue;
                        String[] nTowers = Arrays.copyOf(s.towers, 3);
                        int[] nWrong = Arrays.copyOf(s.wrong, 3);
                        char target = s.towers[i].charAt(s.towers[i].length()-1);
                        nTowers[i] = nTowers[i].substring(0, nTowers[i].length()-1);
                        nTowers[j] += target;
                        if(visited.contains(new MyStringArray(nTowers))) continue;
                        if(target-'A' != i) nWrong[i]--;
                        if(target-'A' != j) nWrong[j]++;
                        q.add(new State(nTowers, nWrong, s.cnt+1));
                        visited.add(new MyStringArray(nTowers));
                    }
                }
            }
        }
        return -1;
    }

    static class State {
        String[] towers;
        int[] wrong;
        int cnt;

        public State(String[] towers, int[] wrong, int cnt) {
            this.towers = towers;
            this.wrong = wrong;
            this.cnt = cnt;
        }
    }

    static class MyStringArray {
        String [] arr;

        public MyStringArray(String[] arr) {
            this.arr = arr;
        }

        @Override
        public int hashCode() {
            return Arrays.toString(arr).hashCode();
        }

        @Override
        public boolean equals(Object obj) {
            MyStringArray m = (MyStringArray) obj;
            return this.arr[0].equals(m.arr[0])
                    && arr[1].equals(m.arr[1])
                    && arr[2].equals(m.arr[2]);
        }
    }
}
