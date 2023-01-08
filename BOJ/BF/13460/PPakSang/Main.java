package org.example.BF.구슬탈출2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 상 하 좌 우 기울여보기
 * 2^2 * 10 -> 2^20
 * 하 으로 기울였을 때
 * 각 라인 별로 자리 체크
 * # -> 모든 값 초기화 (점의 위치 픽스)
 * R or B -> 점의 위치로 이동 or true 이면 골인 (B 는 실패)
 * 0 -> true
 */

public class Main {
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);

        Character[][] map = new Character[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        calc(map, N, M, 1, 2);
        calc(map, N, M, 1, 0);
        calc(map, N, M, 1, 1);
        calc(map, N, M, 1, 3);

        System.out.println(min <= 10 ? min : -1);
    }

    static void calc(Character[][] map, int N, int M, int cur, int dir) {
        if (cur == 11) return;

        Character[][] newMap = new Character[N][M];
        for (int i = 0; i < N; i++) {
            newMap[i] = Arrays.copyOf(map[i], M);
        }

        if (dir == 0) {
            for (int j = 0; j < M; j++) {
                int dot = N-1;
                boolean flag = false;
                boolean R = false;
                boolean B = false;

                for (int i = N-1; i >= 0; i--) {
                    char c = newMap[i][j];
                    if (c == '#') {
                        flag = false;
                        dot = i-1;
                    }
                    if (c == 'O') {
                        flag = true;
                    }
                    if (c == 'B') {
                        if (flag) B = true;
                        if (dot != i) {
                            newMap[dot][j] = 'B';
                            newMap[i][j] = '.';
                        }
                        dot = dot-1;
                    }
                    if (c == 'R') {
                        if (flag) R = true;

                        if (dot != i) {
                            newMap[dot][j] = 'R';
                            newMap[i][j] = '.';
                        }
                        dot = dot-1;
                    }
                }
                if (!B && R) {
                    min = Math.min(min, cur);
                    return;
                }
                if (B) {
                    return;
                }

            }
        } else if (dir == 1) {
            for (int j = 0; j < M; j++) {
                int dot = 0;
                boolean flag = false;
                boolean R = false;
                boolean B = false;

                for (int i = 0; i < N; i++) {
                    char c = newMap[i][j];
                    if (c == '#') {
                        flag = false;
                        dot = i+1;
                    }
                    if (c == 'O') {
                        flag = true;
                    }
                    if (c == 'B') {
                        if (flag) B = true;
                        if (dot != i) {
                            newMap[dot][j] = 'B';
                            newMap[i][j] = '.';
                        }
                        dot = dot+1;
                    }
                    if (c == 'R') {
                        if (flag) R = true;
                        if (dot != i) {
                            newMap[dot][j] = 'R';
                            newMap[i][j] = '.';
                        }
                        dot = dot+1;
                    }
                }
                if (!B && R) {
                    min = Math.min(min, cur);
                    return;
                }
                if (B) {
                    return;
                }
            }
        } else if (dir == 2) {
            for (int j = 0; j < N; j++) {
                int dot = M-1;
                boolean flag = false;
                boolean R = false;
                boolean B = false;

                for (int i = M-1; i >= 0; i--) {
                    char c = newMap[j][i];
                    if (c == '#') {
                        flag = false;
                        dot = i-1;
                    }
                    if (c == 'O') {
                        flag = true;
                    }
                    if (c == 'B') {
                        if (flag) B = true;
                        if (dot != i) {
                            newMap[j][dot] = 'B';
                            newMap[j][i] = '.';
                        }
                        dot = dot-1;
                    }
                    if (c == 'R') {
                        if (flag) R = true;
                        if (dot != i) {
                            newMap[j][dot] = 'R';
                            newMap[j][i] = '.';
                        }
                        dot = dot-1;
                    }
                }

                if (!B && R) {
                    min = Math.min(min, cur);
                    return;
                }
                if (B) {
                    return;
                }
            }
        } else if (dir == 3) {
            for (int j = 0; j < N; j++) {
                int dot = 0;
                boolean flag = false;
                boolean R = false;
                boolean B = false;

                for (int i = 0; i < M; i++) {
                    char c = newMap[j][i];
                    if (c == '#') {
                        flag = false;
                        dot = i+1;
                    }
                    if (c == 'O') {
                        flag = true;
                    }
                    if (c == 'B') {
                        if (flag) B = true;
                        if (dot != i) {
                            newMap[j][dot] = 'B';
                            newMap[j][i] = '.';
                        }
                        dot = dot+1;
                    }
                    if (c == 'R') {
                        if (flag) R = true;
                        if (dot != i) {
                            newMap[j][dot] = 'R';
                            newMap[j][i] = '.';
                        }
                        dot = dot+1;
                    }
                }

                if (!B && R) {
                    min = Math.min(min, cur);
                    return;
                }
                if (B) {
                    return;
                }
            }
        }

        calc(newMap, N, M, cur+1, 0);
        calc(newMap, N, M, cur+1, 1);
        calc(newMap, N, M, cur+1, 2);
        calc(newMap, N, M, cur+1, 3);
    }

}
