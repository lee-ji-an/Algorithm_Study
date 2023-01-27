package org.example.bfs.레이저통신;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 방향에서 90 도 틀기 -> 현재 위치에서 방향 정보가 존재한다 (방향 따라서 dirX, dirY 선택)
 * 비용: 거울 갯수, 특정 위치에서 거울 갯수가 이전보다 적으면 확인 해야함, 방향 (수직으로 놓으면 거울 하나 늘어남, 따라서 기존에 들어오는 거울 갯수가 이전과 같아도 넣어야함 -> 시간 초과 나면 그 자리에서 방향 따라 최적화)
 *
 * 1. 오는 방향으로 갈래
 * 2. 상, 하 -> 좌, 우
 * 2. 좌, 우 -> 상, 하
 */

public class Main {

    static int[][] dirsV = new int[][] {{0, 0}, {1, -1}};
    static int[][] dirsH = new int[][] {{1, -1}, {0, 0}};

    static int[] dirV = new int[]{1, 3};
    static int[] dirH = new int[]{0, 2};

    //북 동 남 서
    static int[] dirsX = new int[] {1, 0, -1, 0};
    static int[] dirsY = new int[] {0, 1, 0, -1};

    static char[][] map;
    static int[][][] visited;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        map = new char[M][N];
        visited = new int[M][N][4];

        boolean flag = false;
        Location startL = null;
        Location endL = null;
        for (int i = 0; i < M; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    visited[i][j][k] = Integer.MAX_VALUE;
                }
                map[i][j] = line.charAt(j);
                if (map[i][j] == 'C') {
                    if (!flag) {
                        startL = new Location(i, j);
                        flag = true;
                    }
                    else endL = new Location(i, j);
                }
            }
        }

        System.out.println(bfs(startL, endL));
    }

    static int bfs(Location start, Location end) {
        int result = Integer.MAX_VALUE;
        Queue<Position> q = new LinkedList<>();

        q.add(new Position(start.x, start.y, 0, 0));
        q.add(new Position(start.x, start.y, 0, 1));
        q.add(new Position(start.x, start.y, 0, 2));
        q.add(new Position(start.x, start.y, 0, 3));

        while (q.size() > 0) {
            Position cur = q.poll();
            int[][] rDirs = getReverseDirs(cur.dir);

            int[] rDirX = rDirs[0];
            int[] rDirY = rDirs[1];
            int[] nextRDir = getNextRDir(cur.dir);

//            수직 이동
            for (int i = 0; i < 2; i++) {
                int nX = cur.location.x + rDirX[i];
                int nY = cur.location.y + rDirY[i];
                if (checkRange(nX, nY) && map[nX][nY] != '*') {
                    if (nX == end.x && nY == end.y) result = Math.min(result, cur.cnt+1);
                    if (visited[nX][nY][nextRDir[i]] > cur.cnt+1) {
                        visited[nX][nY][nextRDir[i]] = cur.cnt+1;
                        q.add(new Position(nX, nY, cur.cnt+1, nextRDir[i]));
                    }
                }
            }

            int nX = cur.location.x + dirsX[cur.dir];
            int nY = cur.location.y + dirsY[cur.dir];

            if (checkRange(nX, nY) && map[nX][nY] != '*') {
                if (nX == end.x && nY == end.y) result = Math.min(result, cur.cnt);
                if (visited[nX][nY][cur.dir] > cur.cnt) {
                    visited[nX][nY][cur.dir] = cur.cnt;
                    q.add(new Position(nX, nY, cur.cnt, cur.dir));
                }
            }
        }

        return result;
    }

    private static int[] getNextRDir(int dir) {
        if (dir == 0 || dir == 2) return dirV;
        return dirH;
    }

    static boolean checkRange(int x, int y) {
        if (x >= M || x < 0) return false;
        if (y >= N || y < 0) return false;
        return true;
    }

    static int[][] getReverseDirs(int dir) {
        if (dir == 0 || dir == 2) return dirsV;
        return dirsH;
    }

    static class Location {
        int x;
        int y;

        public Location(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static class Position {
        Location location;
        int cnt;
        int dir; // 북 동 남 서 0 1 2 3

        Position(int x, int y, int cnt, int dir) {
            this.location = new Location(x, y);
            this.cnt = cnt;
            this.dir = dir;
        }

    }
}
