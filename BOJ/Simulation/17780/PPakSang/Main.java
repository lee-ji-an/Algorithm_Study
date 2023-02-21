package org.example.simulation.새로운게임;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 말 움직이기
 * 빨간색 칸 -> 이동 후 말 쌓인 것 반대로
 * 파란색 칸 -> 반대 방향으로 이동 (반대도 파란색이면 더 이상 보지 않는다)
 *
 * 위치를 Queue 로 저장, 해당 위치에 말 정보를 따로 저장
 *
 * 말 위치 별로 상태 저장
 * 위치 - 말 정보
 * 말 정보 (List<말>
 * 말 방향
 *
 * 1. 위치 추출
 * 2. 말 정보 확인, 타겟 방향에 있는 색깔 확인
 * 3. 흰색 -> 이동
 * 4. 막혀있거나 파란색 -> 방향 반대 이동 or 반대도 파란색이면 Queue에 더이상 집어넣지 않는다
 * 5. 빨간색 -> 순서 반대 후 이동
 * 새로운 칸 도착하면 Queue 에 추가
 */

//동서북남
public class Main {
    static int[] dirX = new int[]{0, 0, -1, 1};
    static int[] dirY = new int[]{1, -1, 0, 0};
    static int[] reverseDir = new int[]{1, 0, 3, 2};

    static int N;

    static int[][] map;
    static Deque<Horse>[][] horseInfo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        N = Integer.parseInt(temp[0]);
        int K = Integer.parseInt(temp[1]);

        map = new int[N][N];
        horseInfo = new Deque[N][N];
        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                horseInfo[i][j] = new ArrayDeque<>();
            }
        }

        Position[] horseP = new Position[K];
        for (int i = 0; i < K; i++) {
            temp = br.readLine().split(" ");

            int x = Integer.parseInt(temp[0])-1;
            int y = Integer.parseInt(temp[1])-1;
            int dir = Integer.parseInt(temp[2])-1;

            horseInfo[x][y].add(new Horse(i, dir));
            horseP[i] = new Position(x, y);
        }

        int result = 0;
        while (true) {
            result++;
            if (result > 1000) break;

            boolean isMoved = false;
            for (int t = 0; t < K; t++) {
                Position cur = horseP[t];
                Deque<Horse> horseDirs = horseInfo[cur.x][cur.y];
                Horse horse = horseDirs.getFirst();
                Integer horseDir = horse.dir;

                if (horse.num != t) continue;

                int nX = cur.x + dirX[horseDir];
                int nY = cur.y + dirY[horseDir];

                if (!checkRange(nX, nY) || map[nX][nY] == 2) {
                    horseDir = reverseDir[horseDir];
                    horse.dir = horseDir;
                }

                nX = cur.x + dirX[horseDir];
                nY = cur.y + dirY[horseDir];

                if (!checkRange(nX, nY) || map[nX][nY] == 2) {
                    continue;
                }

                isMoved = true;

                int hS = horseDirs.size();
                if (map[nX][nY] == 0) {
                    for (int i = 0; i < hS; i++) {
                        Horse toMoveHorse = horseDirs.pollFirst();
                        horseP[toMoveHorse.num].x = nX;
                        horseP[toMoveHorse.num].y = nY;
                        horseInfo[nX][nY].addLast(toMoveHorse);
                    }
                } else if (map[nX][nY] == 1) {
                    for (int i = 0; i < hS; i++) {
                        Horse toMoveHorse = horseDirs.pollLast();
                        horseP[toMoveHorse.num].x = nX;
                        horseP[toMoveHorse.num].y = nY;
                        horseInfo[nX][nY].addLast(toMoveHorse);
                    }
                }

                if (horseInfo[nX][nY].size() >= 4) {
                    System.out.println(result);
                    return;
                }
            }
            if (!isMoved) break;
        }

        System.out.println(-1);
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= N) return false;
        return true;
    }

    static class Horse {
        int num;
        int dir;

        public Horse(int num, int dir) {
            this.num = num;
            this.dir = dir;
        }
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
