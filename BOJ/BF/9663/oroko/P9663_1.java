import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9663 {

    static int N, cnt = 0;
    static int[] queens;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        queens = new int[N];
        queens(0);

        System.out.println(cnt);
    }

    static void queens(int r) {
        boolean[] visited = new boolean[N];
        for(int q = 0; q < r; q++) {
            int d = r-q;
            visited[queens[q]] = true;
            if(queens[q]-d >= 0) visited[queens[q]-d] = true;
            if(queens[q]+d < N) visited[queens[q]+d] = true;
        }

        for(int j = 0; j < N; j++) {
            if(!visited[j]) {
                queens[r] = j;
                if(r+1 == N) cnt++;
                else queens(r+1);
            }
        }
    }
}
