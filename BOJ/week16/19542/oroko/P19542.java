import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P19542 {

    static int D;
    static List<Integer>[] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        tree = new List[N+1];
        for(int i = 1; i <= N; i++) tree[i] = new ArrayList<>();

        for(int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            tree[v1].add(v2);
            tree[v2].add(v1);
        }

        dfs(S, -1, 0);
        System.out.println(answer*2);
    }

    static int answer = 0;

    static int dfs(int v, int pv, int depth) {
        int maxDepth = 0;
        for(int nv : tree[v]) {
            if(nv == pv) continue;
            int nDepth = dfs(nv, v, depth+1);
            if(nDepth > D) answer++;
            maxDepth = Math.max(maxDepth, nDepth);
        }

        return maxDepth+1;
    }
}
