import java.io.*;
import java.util.StringTokenizer;

public class P3584 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] parent = new int[N+1];
            for(int i = 0; i < N-1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int p = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                parent[c] = p;
            }
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            boolean[] visited = new boolean[N+1];
            for(int i = v1; i > 0; i = parent[i]) visited[i] = true;
            for(int i = v2; i > 0; i = parent[i]) {
                if(visited[i]) {
                    bw.write(String.valueOf(i));
                    bw.newLine();
                    break;
                }
            }
        }
        bw.flush();
    }
}
