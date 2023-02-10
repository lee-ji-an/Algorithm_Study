import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P12869 {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] hp = new int[N];
        for(int i = 0; i < N; i++) hp[i] = Integer.parseInt(st.nextToken());
        System.out.println(game(hp));
    }

    static int[][] d = {{9, 3, 1}, {9, 1, 3}, {3, 1, 9}, {3, 9, 1}, {1, 3, 9}, {1, 9, 3}};
    static int game(int[] hp) {
        Queue<Attack> pq = new LinkedList<>();
        Set<Attack> visited = new HashSet<>();
        Attack s = new Attack(hp, 0);
        pq.add(s);
        visited.add(s);
        while (!pq.isEmpty()) {
            Attack a = pq.remove();
            for(int k = 0; k < 6; k++) {
                int[] nhp = new int[N];
                boolean go = true;
                for(int i = 0; i < N; i++) {
                    nhp[i] = a.hp[i] - d[k][i];
                    if(nhp[i] < 0) go = false;
                }
                Attack na = new Attack(nhp, a.cnt+1);
                if(na.done()) return na.cnt;
                if(visited.contains(na)) continue;
                if(go) {
                    pq.add(na));
                    visited.add(na);
                }
            }
        }
        return -1;
    }

    static class Attack implements Comparable<Attack> {
        int[] hp;
        int cnt;

        public Attack(int[] hp, int cnt) {
            this.hp = hp;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Attack o) {
            return Integer.compare(this.cnt, o.cnt);
        }

        public boolean done() {
            for(int i = 0; i < N; i++) {
                if(this.hp[i] > 0) return false;
            }
            return true;
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(this.hp);
        }

        @Override
        public boolean equals(Object obj) {
            Attack attack = (Attack) obj;
            for(int i = 0; i < N; i++) {
                if(this.hp[i] != attack.hp[i]) return false;
            }
            return true;
        }
    }
}
