import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P12946 {

    static int N;
    static char[][] map;
    static int[][] color;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new char[N][N];
        for(int i = 0; i < N; i++) map[i] = br.readLine().toCharArray();
        color = new int[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(map[i][j] == 'X' && color[i][j] == 0) dfs(i, j, 1);  // 색칠 해야 하는 곳인데 안돼있으면 색칠하기
            }
        }
        System.out.println(answer);
    }

    static int[] dr = {-1, -1, 0, 1, 1, 0};
    static int[] dc = {0, 1, 1, 0, -1, -1};

    public static void dfs(int i, int j, int c) {
        color[i][j] = c;
        answer = Math.max(answer, 1);   // 일단 색칠을 했기 때문에 적어도 1
        for(int k = 0; k < 6; k++) {
            int ni = i + dr[k];
            int nj = j + dc[k];
            if(0 <= ni && ni < N && 0 <= nj && nj < N) {
                if(map[ni][nj] == 'X') {    // 인접한 것 중에 색칠할 곳 발견
                    if(color[ni][nj] == 0) dfs(ni, nj, c == 1 ? 2 : 1);     // 색칠 안 돼있으면 하기(다른색으로)
                    answer = Math.max(answer, 2);       // 인접한 두 곳에 색칠했으니까 적어도 2
                    if(color[ni][nj] == c) answer = Math.max(answer, 3);        // 인접한 곳이 나랑 같은 색이면 색깔 추가해야하므로 3
                }
            }
        }
    }
}
