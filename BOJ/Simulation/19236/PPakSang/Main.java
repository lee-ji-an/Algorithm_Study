package org.example.simulation.청소년상어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 7 6 2 3 15 6 9 8
 * 3 1 1 8 14 7 10 1
 * 6 1 13 6 4 3 11 4
 * 16 1 8 7 5 2 12 2
 *
 * ai는 물고기의 번호, bi
 *  ↑, ↖, ←, ↙, ↓, ↘, →, ↗
 */

public class Main {

    static int[] dirX = new int[]{0, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dirY = new int[]{0, 0, -1, -1, -1, 0, 1, 1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Shark shark = null;
        Fish[] fishes = new Fish[17];
        int[][] map = new int[4][4];
        for (int i = 0; i < 4; i++) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < 4; j++) {
                int num = Integer.parseInt(temp[j*2]);
                int dir = Integer.parseInt(temp[j*2+1]);
                map[i][j] = num;
                fishes[num] = new Fish(num, i, j, dir);
                if (i == 0 && j == 0) {
                    shark = new Shark(0, 0, dir, num);
                    fishes[num].killed = true;
                    map[i][j] = 0;
                }
            }
        }

        System.out.println(play(fishes, shark, map));
    }

    static int play(Fish[] fs, Shark sk, int[][] m) {
        Queue<Game> q = new LinkedList<>();
        q.add(new Game(fs, sk, m));

        int result = 0;
        while (q.size() > 0) {
            Game cur = q.poll();

            Fish[] fishes = cur.fishes;
            Shark shark = cur.shark;
            int[][] map = cur.map;

            for (int idx = 1; idx <= 16; idx++) {
                Fish fish = fishes[idx];
                if (fish.killed) {
                    continue;
                }

                for (int i = 0; i < 8; i++) {
                    int dir = fish.dir+i;
                    if (dir/9 == 1) {
                        dir = dir%9 + 1;
                    }

                    int nX = fish.x + dirX[dir];
                    int nY = fish.y + dirY[dir];
                    if (!inRange(nX, nY) || (cur.shark.x == nX && cur.shark.y == nY)) continue;

                    Fish nextFish = fishes[map[nX][nY]];
                    if (nextFish != null) {
                        nextFish.x = fish.x;
                        nextFish.y = fish.y;
                        map[fish.x][fish.y] = nextFish.num;
                    } else {
                        map[fish.x][fish.y] = 0;
                    }

                    fish.x = nX;
                    fish.y = nY;
                    fish.dir = dir;
                    map[nX][nY] = fish.num;
                    break;
                }
            }

            int sX = shark.x;
            int sY = shark.y;
            int sDir = shark.dir;

            boolean flag = false;
            for (int i = 1; i <= 3; i++) {
                int nX = sX + dirX[sDir]*i;
                int nY = sY + dirY[sDir]*i;

                if (!inRange(nX, nY)) { break; }
                if (map[nX][nY] == 0) { continue; }

                flag = true;

                int[][] nMap = new int[map.length][map[0].length];
                for (int j = 0; j < map.length; j++) {
                    for (int k = 0; k < map[0].length; k++) {
                        nMap[j][k] = map[j][k];
                    }
                }
                Shark nShark = new Shark(shark);

                Fish[] nFishes = new Fish[17];
                for (int j = 1; j < 17; j++) {
                    nFishes[j] = new Fish(fishes[j]);
                }

                Fish nFish = nFishes[nMap[nX][nY]];
                nFish.killed = true;
                nShark.x = nX;
                nShark.y = nY;
                nShark.dir = nFish.dir;
                nShark.cnt += nFish.num;
                nMap[nX][nY] = 0;

                q.add(new Game(nFishes, nShark, nMap));
            }

            if (!flag) {
                result = Math.max(result, shark.cnt);
            }
        }
        return result;
    }

    static boolean inRange(int x, int y) {
        if (x < 0 || x >= 4) return false;
        if (y < 0 || y >= 4) return false;
        return true;
    }

    static class Game {
        Fish[] fishes;
        Shark shark;
        int[][] map;

        public Game(Fish[] fishes, Shark shark, int[][] map) {
            this.fishes = fishes;
            this.shark = shark;
            this.map = map;
        }
    }

    static class Fish {
        int num;
        int x;
        int y;
        int dir;
        boolean killed = false;


        public Fish(int num, int x, int y, int dir) {
            this.num = num;
            this.x = x;
            this.y = y;
            this.dir = dir;
        }

        public Fish(Fish fish) {
            this.num = fish.num;
            this.x = fish.x;
            this.y = fish.y;
            this.dir = fish.dir;
            this.killed = fish.killed;
        }
    }

    static class Shark {
        int x;
        int y;
        int dir;
        int cnt;

        public Shark(int x, int y, int dir, int cnt) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.cnt = cnt;
        }

        public Shark(Shark shark) {
            this.x = shark.x;
            this.y = shark.y;
            this.dir = shark.dir;
            this.cnt = shark.cnt;
        }
    }
}
