import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P16928 {

    static int[] trap;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
        trap = new int[101];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            trap[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
        }
        System.out.println(bfs());
    }

    public static int bfs() {
        Queue<Pos> q = new LinkedList<>();
        boolean[] visited = new boolean[101];
        q.add(new Pos(1, 0));
        visited[1] = true;
        while(!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == 100) return p.cnt;
            for(int i = 1; i <= 6; i++) {
                int ni = p.i + i;
                if(ni > 100) continue;
                if(trap[ni] != 0) ni = trap[ni];
                if(!visited[ni]) {
                    visited[ni] = true;
                    q.add(new Pos(ni, p.cnt+1));
                }
            }
        }
        return -1;
    }

    static class Pos {
        int i;
        int cnt;
        Pos(int i, int cnt) {
            this.i = i;
            this.cnt = cnt;
        }
    }
}
