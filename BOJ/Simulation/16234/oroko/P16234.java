import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P16234 {

    static int N, L, R;
    static int[][] people;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        people = new int[N][N];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) people[i][j] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        while(true) {
            // 국경 열기
            int[][] numbering = new int[N][N];
            int id = 1;
            Map<Integer, Integer> id_cnt = new HashMap<>();
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(numbering[i][j] == 0) {
                        int res = bfs(i, j, numbering, id);
                        if(res >= 0) id_cnt.put(id++, res);
                    }
                }
            }

            // 연 곳이 없으면 그만
            if(id_cnt.isEmpty()) break;

            // 인구 이동
            cnt++;
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(numbering[i][j] != 0) people[i][j] = id_cnt.get(numbering[i][j]);
                }
            }
        }

        System.out.println(cnt);
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    public static int bfs(int i, int j, int[][] numbering, int id) {
        Queue<Country> q = new LinkedList<>();
        q.add(new Country(i, j));
        numbering[i][j] = id;
        int sum = 0;
        int cnt = 0;
        while(!q.isEmpty()) {
            Country c = q.remove();
            sum += people[c.i][c.j];
            cnt++;
            for(int k = 0; k < 4; k++) {
                int ni = c.i + dr[k];
                int nj = c.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < N) {
                    if(numbering[ni][nj] == 0) {
                        int gap = Math.abs(people[c.i][c.j] - people[ni][nj]);
                        if(L <= gap && gap <= R) {
                            q.add(new Country(ni, nj));
                            numbering[ni][nj] = id;
                        }
                    }
                }
            }
        }
        if(cnt == 1) {
            numbering[i][j] = 0;
            return -1;
        }
        return sum / cnt;
    }

    static class Country {
        int i, j;

        public Country(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}