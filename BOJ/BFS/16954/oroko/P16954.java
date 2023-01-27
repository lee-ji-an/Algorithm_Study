import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P16954 {

    static char[][] map = new char[8][8];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 8; i++) {
            map[i] = br.readLine().toCharArray();
        }
        System.out.println(bfs());
    }

    static int[] dr = {-1, -1, -1, 0, 1, 1, 1, 0, 0};
    static int[] dc = {-1, 0, 1, 1, 1, 0, -1, -1, 0};
    static int bfs() {
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(7, 0, 0));
        boolean[][][] visited = new boolean[8][8][9];
        while (!q.isEmpty()) {
            Pos p = q.remove();
            if(p.i == 0 && p.j == 7) return 1;
            for(int k = 0; k < 9; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < 8 && 0 <= nj && nj < 8) {
                    if(ni - p.time >= 0 && map[ni - p.time][nj] == '#') continue;
                    if(ni - p.time-1 >= 0 && map[ni - p.time-1][nj] == '#') continue;
                    if(!visited[ni][nj][k]) {
                        visited[ni][nj][k] = true;
                        q.add(new Pos(ni, nj, p.time+1));
                    }
                }
            }
        }

        return 0;
    }

    static class Pos {
        int i, j, time;

        public Pos(int i, int j, int time) {
            this.i = i;
            this.j = j;
            this.time = time;
        }
    }

}
