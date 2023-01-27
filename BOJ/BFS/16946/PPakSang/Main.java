package org.example.bfs.벽부수고이동하기4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * 1인 칸 만나면 bfs 로 몇 칸 있는지 확인 -> 해당 칸의 답
 */

public class Main {
    static int[] dirX = {1, -1, 0, 0};
    static int[] dirY = {0, 0, 1, -1};

    static int N;
    static int M;
    static boolean[][] map;
    static SpaceInfo[][] cnt;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        map = new boolean[N][M];
        cnt = new SpaceInfo[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == '1') map[i][j] = true;
            }
        }

        int spaceNum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!map[i][j] && !visited[i][j]) countSpace(i, j, spaceNum++);
            }
        }

        Set<Integer> spaceCheck = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!map[i][j]) sb.append(0);
                else {
                    int result = 1;
                    for (int k = 0; k < 4; k++) {
                        int nX = i + dirX[k];
                        int nY = j + dirY[k];

                        if (checkRange(nX, nY) && !map[nX][nY]) {
                            int sNum = cnt[nX][nY].space;
                            if (!spaceCheck.contains(sNum)) {
                                spaceCheck.add(sNum);
                                result +=  cnt[nX][nY].count;
                            }
                        }
                    }
                    spaceCheck.clear();
                    sb.append(result%10);
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    static void countSpace(int x, int y, int spaceNum) {
        Queue<Position> q = new LinkedList<>();
        Queue<Position> q2 = new LinkedList<>();
        visited[x][y] = true;

        q.add(new Position(x, y));
        int result = 1;
        while(q.size() > 0) {
            Position p = q.poll();
            q2.add(p);

            for (int i = 0; i < 4; i++) {
                int nX = p.x + dirX[i];
                int nY = p.y + dirY[i];

                if (checkRange(nX, nY) && !visited[nX][nY] && !map[nX][nY]) {
                    visited[nX][nY] = true;
                    q.add(new Position(nX, nY));
                    result++;
                }
            }
        }

        while(q2.size() > 0) {
            Position p = q2.poll();
            cnt[p.x][p.y] = new SpaceInfo(spaceNum, result);
        }
    }

    static boolean checkRange(int x, int y) {
        if (x >= N || x < 0) return false;
        if (y >= M || y < 0) return false;

        return true;
    }

    static class Position {
        int x;
        int y;

        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class SpaceInfo {
         int space;
         int count;

         SpaceInfo(int space, int count) {
             this.space = space;
             this.count = count;
         }
    }
}
