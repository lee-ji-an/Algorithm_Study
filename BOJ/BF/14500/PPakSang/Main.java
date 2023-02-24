package org.example.BF.테트로미노;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static int row;
    static int col;

    static int[][] map;

    static int max = Integer.MIN_VALUE;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        row = Integer.parseInt(temp[0]);
        col = Integer.parseInt(temp[1]);

        map = new int[row][col];
        for (int i = 0; i < row; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < col; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                max = Math.max(max, map[i][j]);
            }
        }


        answer = 0;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                answer = Math.max(answer, calc(0, i, j, visited, 0));
            }
        }
        System.out.println(answer);
    }

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    static int calc(int cnt, int x, int y, boolean[][] visited, int sum) {
        if (cnt == 4) return sum;

        visited[x][y] = true;
        int result = 0;

        int min = Integer.MAX_VALUE;
        int around = 0;
        int aroundCnt = 0;
        for (int i = 0; i < 4; i++) {
            int nX = x + dirX[i];
            int nY = y + dirY[i];

            if (!checkRange(nX, nY) || visited[nX][nY]) continue;

            aroundCnt++;
            around += map[nX][nY];
            min = Math.min(min, map[nX][nY]);

            if (answer < sum + max*(4-cnt)) {
                result = Math.max(result, calc(cnt+1, nX, nY, visited, sum + map[nX][nY]));
            }
        }
        visited[x][y] = false;
        if (aroundCnt == 4) around -= min;
        return Math.max(result, map[x][y] + around);
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= row) return false;
        if (y < 0 || y >= col) return false;
        return true;
    }
}
