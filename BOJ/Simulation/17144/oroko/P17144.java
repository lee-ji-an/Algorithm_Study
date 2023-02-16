import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P17144 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int[][] dust = new int[R][C];
        int[] vacuum = new int[2];
        vacuum[0] = vacuum[1] = -1;
        Queue<Pos> q = new LinkedList<>();
        for(int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < C; j++) {
                dust[i][j] = Integer.parseInt(st.nextToken());
                if(dust[i][j] == -1) {
                    if(vacuum[0] == -1) vacuum[0] = i;
                    else vacuum[1] = i;
                }
            }
        }

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        for(int t = 0; t < T; t++) {
            // 미세먼지 확산
            for(int i = 0; i < R; i++) {
                for(int j = 0; j < C; j++) {
                    if(dust[i][j] > 0) q.add(new Pos(i, j, dust[i][j]));
                }
            }
            while(!q.isEmpty()) {
                Pos p = q.remove();
                int spread = p.dust / 5;
                for(int k = 0; k < 4; k++) {
                    int ni = p.i + dr[k];
                    int nj = p.j + dc[k];
                    if(0 <= ni && ni < R && 0 <= nj && nj < C) {
                        if(dust[ni][nj] == -1) continue;
                        dust[ni][nj] += spread;
                        dust[p.i][p.j] -= spread;
                    }
                }
            }

            // 공기청정기 작동
            // 위쪽 공기청정기
            int wi = vacuum[0]-1, wj = 0;
            dust[wi][wj] = 0;   // 공기청정기로 들어오는 먼지는 없애주고 시작
            for(int k = 0; k < 4; k++) {
                while(wi != vacuum[0] || wj != 0) {
                    int ni = wi + dr[k];
                    int nj = wj + dc[k];
                    if(0 <= ni && ni <= vacuum[0] && 0 <= nj && nj < C) {
                        if(dust[ni][nj] == -1) dust[wi][wj] = 0;
                        else dust[wi][wj] = dust[ni][nj];
                        wi = ni; wj = nj;
                    } else break;
                }
            }

            int[] dr1 = {1, 0, -1, 0};
            int[] dc1 = {0, 1, 0, -1};
            // 아래쪽 공기청정기
            wi = vacuum[1]+1; wj = 0;
            for(int k = 0; k < 4; k++) {
                while(wi != vacuum[0] || wj != 0) {
                    int ni = wi + dr1[k];
                    int nj = wj + dc1[k];
                    if(vacuum[1] <= ni && ni < R && 0 <= nj && nj < C) {
                        if(dust[ni][nj] == -1) dust[wi][wj] = 0;
                        else dust[wi][wj] = dust[ni][nj];
                        wi = ni; wj = nj;
                    } else break;
                }
            }
        }

        int sum = 0;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(dust[i][j] > 0) sum += dust[i][j];
            }
        }
        System.out.println(sum);
    }

    static class Pos {
        int i, j, dust;

        public Pos(int i, int j, int dust) {
            this.i = i;
            this.j = j;
            this.dust = dust;
        }
    }
}
