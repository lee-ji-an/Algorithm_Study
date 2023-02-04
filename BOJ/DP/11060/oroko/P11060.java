import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P11060 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] maze = new int[N+1];
        Arrays.fill(maze, Integer.MAX_VALUE);
        maze[1] = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            int jump = Integer.parseInt(st.nextToken());
            if(maze[i] == Integer.MAX_VALUE) continue;
            for(int j = i+1; j <= i + jump && j <= N; j++) maze[j] = Math.min(maze[j], maze[i] + 1);
        }
        System.out.println(maze[N] == Integer.MAX_VALUE ? -1 : maze[N]);
    }
}
