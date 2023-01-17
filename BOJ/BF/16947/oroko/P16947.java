import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P16947 {

    static List[] g;
    static boolean[] cycle;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        g = new List[N+1];
        for(int i = 1; i <= N; i++) g[i] = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            g[v1].add(v2);
            g[v2].add(v1);
        }
        cycle = new boolean[N+1];
        for(int i = 1; i <= N; i++) {
            if(!cycle[i]) cycle[i] = isCycle(i, i, 0, new boolean[N+1], 0);
        }
        for(int i = 1; i <= N; i++) {
            if(cycle[i]) bw.write("0 ");
            else bw.write(dist(i, new boolean[N+1], 0));
        }
        bw.flush();
    }

    public static boolean isCycle(int root, int v, int prev, boolean[] visited, int len) {
        if(len >= 3 && v == root) return true;

        visited[v] = true;
        boolean ret = false;
        for(int nv : (ArrayList<Integer>) g[v]) {
            if(!visited[nv] || (nv == root && nv != prev)) {
                ret = isCycle(root, nv, v, visited, len+1);
                if(ret) break;
            }
        }
        return ret;
    }

    public static int dist(int v, boolean[] visited, int len) {
        visited[v] = true;
        int ret = 0;
        for(int nv : (ArrayList<Integer>) g[v]) {
            if(cycle[nv]) return len+1;
            if(!visited[nv]) {
                ret = dist(nv, visited, len+1);
                if(ret > 0) break;
            }
        }
        return ret;
    }
}
