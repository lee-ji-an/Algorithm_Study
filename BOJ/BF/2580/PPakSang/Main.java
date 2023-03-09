package org.example.BF.스도쿠;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 스도쿠: 같은 라인, 같은 공간
 * (0,0) (0,1) (0,2)
 * (1,0) (1,1) (1,2)
 *
 * (행 인덱스/3, 열 인덱스/3) -> 공간 정보
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] map = new int[9][9];
        boolean[][][] space = new boolean[3][3][10];

        List<Position> blank = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < 9; j++) {
                int num = Integer.parseInt(temp[j]);
                map[i][j] = num;
                space[i/3][j/3][num] = true;

                if (num == 0) {
                   blank.add(new Position(i, j));
                }
            }
        }

        play(0, blank.size(), blank, map, space);
    }

    static boolean play (int cur, int max, List<Position> blank, int[][] map, boolean[][][] space) {
        if (cur == max) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(map[i][j] + " ");
                }
                System.out.println();
            }
            return true;
        }

        Position p = blank.get(cur);
        int x = p.x;
        int y = p.y;
        int spaceX = x/3;
        int spaceY = y/3;

        for (int next = 1; next <= 9; next++) {
            boolean flag = true;
            for (int i = 0; i < 9; i++) {
                if (space[spaceX][spaceY][next] || map[x][i] == next || map[i][y] == next) {
                    flag = false;
                    break;
                }
            }

            if (!flag) continue;

            space[spaceX][spaceY][next] = true;
            map[x][y] = next;
            if (play(cur+1, max, blank, map, space)) { return true; }
            space[spaceX][spaceY][next] = false;
            map[x][y] = 0;
        }
        return false;
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
