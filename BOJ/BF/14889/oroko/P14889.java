import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class P14889 {

    static int minGap = Integer.MAX_VALUE;
    static int[][] capacity;

    public static void comb(int n, int start, int r, boolean[] visited) {
        if(r == 0) {
            ArrayList<Integer> startTeam = new ArrayList<>();
            ArrayList<Integer> linkTeam = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                if(visited[i]) startTeam.add(i);
                else linkTeam.add(i);
            }
            int startCapacity = 0, linkCapacity = 0;
            for(int i = 0; i < n/2; i++) {
                for(int j = i; j < n/2; j++) {
                    startCapacity += capacity[startTeam.get(i)][startTeam.get(j)] + capacity[startTeam.get(j)][startTeam.get(i)];
                    linkCapacity += capacity[linkTeam.get(i)][linkTeam.get(j)] + capacity[linkTeam.get(j)][linkTeam.get(i)];
                }
            }
            minGap = Math.min(minGap, Math.abs(startCapacity - linkCapacity));
            return;
        }

        for(int i = start; i < n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                comb(n, i+1, r-1, visited);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        capacity = new int[N][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) capacity[i][j] = Integer.parseInt(st.nextToken());
        }
        boolean[] visited = new boolean[N];
        visited[0] = true;
        comb(N, 1, N/2-1, visited);
        System.out.println(minGap);
    }
}
