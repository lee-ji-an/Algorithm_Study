package org.example.simulation.모노미노도미노2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 행 0 ~ 3 는 열 0 ~ 9
 * (0 1 2 3) (4 5) (6 7 8 9)
 *
 * 블록 놓고 우, 하 이동
 *
 * [이동]
 * t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
 * t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
 * t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
 *
 * t1
 * 우: 열을 증가시키면서 블록 있는지 확인
 * 하: 행을 증가시키면서 블록 있는지 확인
 *
 * t2
 * 우: 열을 증가시키면서 블록 있는지 확인
 * 하: 2개의 행을 증가시키면서 블록 있는지 확인
 *
 * redBlue 의 1*2 가 redGreen 2*1 이랑 똑같음
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[][] redBlue = new boolean[4][10];
        boolean[][] redGreen = new boolean[4][10];

        int N = Integer.parseInt(br.readLine());


        int[] reverseDir = new int[] {0, 1, 3, 2};
        int result = 0;
        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int t = Integer.parseInt(temp[0]);
            int x = Integer.parseInt(temp[1]);
            int y = Integer.parseInt(temp[2]);

            result += play(redBlue, t, x, y);
            result += play(redGreen, reverseDir[t], y, x);
        }

        int boardCnt = 0;
        for (int i = 6; i <= 9; i++) {
            for (int j = 0; j < 4; j++) {
                if (redBlue[j][i]) {
                    boardCnt++;
                }
                if (redGreen[j][i]) {
                    boardCnt++;
                }
            }
        }
        System.out.println(result);
        System.out.println(boardCnt);
    }


    static int play (boolean[][] board, int dir, int x, int y) {
        int result = 0;
        switch (dir) {
            case 1: {
                while (y+1 < 10 && !board[x][y+1]) {
                    y++;
                }
                board[x][y] = true;
                break;
            }
            case 2: {
                int y2 = y+1;
                while (y2+1 < 10 && !board[x][y2+1]) {
                    y++;
                    y2++;
                }
                board[x][y] = true;
                board[x][y2] = true;
                break;
            }
            case 3: {
                int x2 = x+1;
                while (y+1 < 10 && !board[x][y+1] && !board[x2][y+1]) {
                    y++;
                }
                board[x][y] = true;
                board[x2][y] = true;
                break;
            }
        }

        for (int i = 9; i >= 6; i--) {
            if (canCrash(board, i)) {
                move(board, i);
                result++;
                i++;
            }
        }


        int cnt = 0;
        for (int i = 5; i >= 4; i--) {
            for (int j = 0; j < 4; j++) {
                if (board[j][i]) {
                    cnt++;
                    break;
                }
            }
        }

        if (cnt == 1) { moveToEnd(board, 8); }
        else if (cnt == 2) { moveToEnd(board, 7); }

        return result;
    }

    static boolean canCrash(boolean[][] board, int y) {
        boolean crash = true;
        for (int i = 0; i < 4; i++) {
            if (!board[i][y]) {
                crash = false;
                break;
            }
        }
        return crash;
    }

    static void move(boolean[][] board, int end) {
        for (int i = end; i-1 >= 4; i--) {
            for (int j = 0; j < 4; j++) {
                board[j][i] = board[j][i-1];
                board[j][i-1] = false;
            }
        }
    }

    static void moveToEnd(boolean[][] board, int from) {
        int end = 9;
        for (int i = from; i >= 4; i--) {
            for (int j = 0; j < 4; j++) {
                board[j][end] = board[j][i];
                board[j][i] = false;
            }
            end--;
        }
    }
}
