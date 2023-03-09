import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P9205 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            Pos home = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            List<Pos> list = new LinkedList<>();
            for(int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                list.add(new Pos(Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken())));
            }
            st = new StringTokenizer(br.readLine());
            Pos festival = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            list.add(festival);

            go(home, list, festival);
        }
    }

    static void go(Pos home, List<Pos> list, Pos festival) {
        Queue<Pos> q = new LinkedList<>();
        q.add(home);
        boolean[] visited = new boolean[list.size()];
        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(p == festival) {
                System.out.println("happy");
                return;
            }
            for(int i = 0; i < list.size(); i++) {
                Pos np = list.get(i);
                if(visited[i]) continue;
                if(available(p, np)) {
                    q.add(np);
                    visited[i] = true;
                }
            }
        }

        System.out.println("sad");
    }

    static boolean available(Pos p1, Pos p2) {
        return Math.abs(p1.i-p2.i) + Math.abs(p1.j-p2.j) <= 1000;
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
