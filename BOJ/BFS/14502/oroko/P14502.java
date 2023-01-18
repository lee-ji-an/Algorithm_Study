package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P14502 {

    static int N, M;
    static int[][] map;
    static Queue<Pos> q;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        q = new LinkedList<>();
        List<Pos> list = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == 2) q.add(new Pos(i, j));
                else if(map[i][j] == 0) list.add(new Pos(i, j));
            }
        }
        combination(list, 0, 3, new boolean[list.size()]);
        System.out.println(max);
    }

    public static void combination(List<Pos> list, int start, int r, boolean[] visited) {
        if(r == 0) {
            int[][] aMap = new int[N][M];
            for(int i = 0; i < N; i++) aMap[i] = map[i].clone();
            for(int i = 0; i < list.size(); i++) {
                if(visited[i]) {
                    Pos p = list.get(i);
                    aMap[p.i][p.j] = 1;
                }
            }
            max = Math.max(max, bfs(aMap));
            return;
        }

        for(int i = start; i < list.size(); i++) {
            visited[i] = true;
            combination(list, i+1, r-1, visited);
            visited[i] = false;
        }
    }

    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static int bfs(int[][] map) {
        Queue<Pos> aQ = new LinkedList<>(q);
        boolean[][] visited = new boolean[N][M];
        while(!aQ.isEmpty()) {
            Pos p = aQ.remove();
            if(visited[p.i][p.j]) continue;
            map[p.i][p.j] = 2;
            visited[p.i][p.j] = true;
            for(int k = 0; k < 4; k++) {
                int ni = p.i + dr[k];
                int nj = p.j + dc[k];
                if(0 <= ni && ni < N && 0 <= nj && nj < M) {
                    if(!visited[ni][nj] && map[ni][nj] == 0) {
                        aQ.add(new Pos(ni, nj));
                    }
                }
            }
        }
        int cnt = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(map[i][j] == 0) cnt++;
            }
        }
        return cnt;
    }

    static class Pos {
        int i, j;
        Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
