package org.example.bfs.아기상어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 무게가 같거나 작으면 지나가고
 * 무게가 작으면 먹을 수 있다
 * 무게 만큼 먹으면 성장
 *
 *
 *
 * 매 시행마다 먹을 수 있는 물고기 비용(거리, 좌표) 체크
 * 가장 싼 비용의 물고기 먹고, 좌표 수정
 * (반복)
 * 더 이상 먹을 물고기가 없으면 끝
 *
 */

public class Main {
    static int[][] map;
    static Position babyP;
    static int size = 2;
    static int exp = 0;

    static int N;

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int i = N-1; i >= 0; i--) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                if (map[i][j] == 9) {
                    babyP = new Position(i, j, 0);
                    map[i][j] = 0;
                }
            }
        }
        System.out.println(calcTime());
    }

    static int calcTime() {
        int result = 0;

        while (true) {
            Queue<Position> q = new LinkedList<>();
            boolean[][] visited = new boolean[N][N];
            List<Position> possible = new LinkedList<>();
            q.add(babyP);
            visited[babyP.x][babyP.y] = true;

            while (q.size() > 0) {
                Position cur = q.poll();

                for (int i = 0; i < 4; i++) {
                    int nX = cur.x + dirX[i];
                    int nY = cur.y + dirY[i];

                    if (checkRange(nX, nY) && !visited[nX][nY] && size >= map[nX][nY]) {
                        visited[nX][nY] = true;
                        Position nextP = new Position(nX, nY, cur.cnt + 1);
                        if (map[nX][nY] != 0 && size > map[nX][nY]) {
                            possible.add(nextP);
                        }
                        q.add(nextP);
                    }
                }
            }

            if (possible.size() == 0) return result;
            Position nextBabyP = possible.get(0);

            for (int i = 1; i < possible.size(); i++) {
                Position compareP = possible.get(i);

                if (nextBabyP.cnt > compareP.cnt) nextBabyP = compareP;
                else if (nextBabyP.cnt == compareP.cnt){
                    if (compareP.x > nextBabyP.x) {
                        nextBabyP = compareP;
                    } else if (nextBabyP.x == compareP.x) {
                        if (nextBabyP.y > compareP.y) nextBabyP = compareP;
                    }
                }
            }

            result = nextBabyP.cnt;
            babyP = nextBabyP;
            if (size - (++exp) == 0) {
                size++;
                exp = 0;
            }
            map[nextBabyP.x][nextBabyP.y] = 0;
        }
    }

    static boolean checkRange(int x, int y) {
        if (x >= N || x < 0) return false;
        if (y >= N || y < 0) return false;
        return true;
    }

    static class Position {
        int x;
        int y;
        int cnt;

        Position(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
