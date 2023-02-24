package org.example.simulation.원판돌리기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
 * 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
 * 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
 *
 * N M T
 * N: 원판 갯수
 * M: 숫자 갯수
 * T: 원판 돌리기
 *
 * 0 0 0 3
 * 2 5 0 4
 * 5 3 1 3
 * 0 0 1 3
 *
 * 상하는 범위 벗어나면 끝
 * 좌우는 범위 벗어나면 반대편 확인
 */

public class Main {
    static int[][] plates;
    static int N;
    static int M;

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        int T = Integer.parseInt(temp[2]);

        plates = new int[N+2][M+2];

        for (int i = 1; i <= N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 1; j <= M; j++) {
                plates[i][j] = Integer.parseInt(temp[j-1]);
            }
            plates[i][0] = plates[i][M];
            plates[i][M+1] = plates[i][1];
        }

        for (int i = 0; i < T; i++) {
            temp = br.readLine().split(" ");
            //x 배수
            int x = Integer.parseInt(temp[0]);
            //d 방향
            int d = Integer.parseInt(temp[1]);
            //k 몇번
            int k = Integer.parseInt(temp[2]);

            for (int j = 1; j*x <= N; j++) {
                // 돌릴 원판 번호
                int num = j*x;
                move(num, d, k);
            }

            if (!checkAdj()) {
                adjustPlate();
            }
        }

        int result = 0;
        for (int x = 1; x <= N; x++) {
            for (int y = 1; y <= M; y++) {
                if (plates[x][y] > 0) result += plates[x][y];
            }
        }

        System.out.println(result);
    }

    static void move(int row, int dir, int k) {
        int[] plate = plates[row];
        int[] result = new int[plate.length];

        k = dir == 1 ? M - k : k;


        for (int i = 1; i <= k; i++) {
            result[i] = plate[M-k+i];
        }
        for (int i = k+1; i <= M; i++) {
            result[i] = plate[i-k];
        }
        result[0] = result[M];
        result[M+1] = result[1];

        plates[row] = result;
    }

    static boolean checkAdj() {
        int[][] nPlates = new int[N+2][M+2];

        boolean result = false;
        for (int x = 1; x <= N; x++) {
            for (int y = 1; y <= M; y++) {
                int num = plates[x][y];
                if (num == 0) continue;
                boolean flag = false;

                for (int k = 0; k < 4; k++) {
                    int nX = x + dirX[k];
                    int nY = y + dirY[k];

                    if (plates[nX][nY] == num) {
                        result = true;
                        flag = true;
                    }
                }

                if (flag) nPlates[x][y] = 0;
                else nPlates[x][y] = plates[x][y];
            }
            nPlates[x][0] = nPlates[x][M];
            nPlates[x][M+1] = nPlates[x][1];
        }

        plates = nPlates;
        return result;
    }

    static void adjustPlate() {
        int num = 0;
        int sum = 0;
        for (int x = 1; x <= N; x++) {
            for (int y = 1; y <= M; y++) {
                if (plates[x][y] > 0) {
                    sum += plates[x][y];
                    num++;
                }
            }
        }

        float avg = (float)sum/num;
        for (int x = 1; x <= N; x++) {
            for (int y = 1; y <= M; y++) {
                if (plates[x][y] == 0) continue;

                if (plates[x][y] < avg) {
                    plates[x][y] = plates[x][y] + 1;
                } else if (plates[x][y] > avg) {
                    plates[x][y] = plates[x][y] - 1;
                }
            }
            plates[x][0] = plates[x][M];
            plates[x][M+1] = plates[x][1];
        }
    }
}
