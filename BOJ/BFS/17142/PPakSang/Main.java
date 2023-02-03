package org.example.bfs.연구실3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;

public class Main {
    static int[][] map;
    static List<Position> possible = new ArrayList<>();

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    static int N;
    static int blank = 0;

    static int answer = Integer.MAX_VALUE;

    static boolean[] visited;

    static int a =1 ;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String temp[] = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);

        map = new int[N][N];


        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                if (map[i][j] == 2) {
                    possible.add(new Position(i, j));
                } else  if (map[i][j] == 0) blank++;
            }
        }

        visited = new boolean[possible.size()];
        if (blank == 0) {
            System.out.println(0);
            return;
        }
        calc(0, 0, M);

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    static void calc(int prev, int cur, int max) {
        if (cur == max) {
            List<Position> init = new ArrayList<>();
            for (int i = 0; i < possible.size(); i++) {
                if (visited[i]) init.add(possible.get(i));
            }
            answer = Math.min(answer, bfs(init));
            return;
        }

        for (int i = prev; i < possible.size(); i++) {
            visited[i] = true;
            calc(i+1, cur+1, max);
            visited[i] = false;
        }
    }

    static int bfs (List<Position> init) {
        int result = 0;
        int pollute = 0;
        boolean[][] check = new boolean[N][N];
        Queue<Position> q = new LinkedList<>();
        for (Position p : init) {
            q.add(p);
            check[p.x][p.y] = true;
        }

        while (true) {
            int size = q.size();
            if (size == 0) break;
            result++;
            for (int c = 0; c < size; c++) {
                Position cur = q.poll();
                for (int i = 0; i < 4; i++) {
                    int nX = cur.x + dirX[i];
                    int nY = cur.y + dirY[i];

                    if (checkRange(nX, nY) && map[nX][nY] != 1) {
                        if (check[nX][nY]) continue;
                        if (map[nX][nY] == 0) pollute++;
                        if (pollute == blank) return result;
                        check[nX][nY] = true;
                        q.add(new Position(nX, nY));
                    }
                }
            }
        }

        return Integer.MAX_VALUE;
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= N) return false;
        return true;
    }

    static class Position {
        int x;
        int y;

        Position (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
