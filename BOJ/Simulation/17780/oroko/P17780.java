import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P17780 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][N];
        String[][] move = new String[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                move[i][j] = "";
            }
        }
        Piece[] pieces = new Piece[K + 1];
        for (int i = 1; i <= K; i++) {
            st = new StringTokenizer(br.readLine());
            pieces[i] = new Piece(Integer.parseInt(st.nextToken()) - 1,
                    Integer.parseInt(st.nextToken()) - 1,
                    Integer.parseInt(st.nextToken()) - 1);
            move[pieces[i].i][pieces[i].j] = String.valueOf((char) ((i - 1) + 'A'));
        }

        int[] dr = {0, 0, -1, 1};
        int[] dc = {1, -1, 0, 0};
        int cnt = 0;
        boolean find = false;
        while (!find) {
            cnt++;
            if (cnt > 1000) {
                cnt = -1;
                break;
            }
            for (int i = 1; i <= K; i++) {
                Piece p = pieces[i];
                if (move[p.i][p.j].charAt(0) != (char) (i - 1 + 'A')) continue;
                boolean moved = false;
                int ni = p.i + dr[p.dir];
                int nj = p.j + dc[p.dir];
                if (0 <= ni && ni < N && 0 <= nj && nj < N) {
                    switch (map[ni][nj]) {
                        case 0: {  // 흰색
                            int ci = p.i, cj = p.j;
                            move[ni][nj] += move[p.i][p.j];
                            for (int s = 0; s < move[ci][cj].length(); s++) {
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                            }
                            move[ci][cj] = "";
                            moved = true;
                            break;
                        }
                        case 1: {  // 빨간색
                            int ci = p.i, cj = p.j;
                            move[ni][nj] += new StringBuilder(move[p.i][p.j]).reverse().toString();
                            for (int s = 0; s < move[ci][cj].length(); s++) {
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                            }
                            move[ci][cj] = "";
                            moved = true;
                            break;
                        }
                        case 2: {  // 파란색
                            p.dir = reverseDir(p.dir);
                            ni = p.i + dr[p.dir];
                            nj = p.j + dc[p.dir];
                            if (0 <= ni && ni < N & 0 <= nj && nj < N) {
                                if (map[ni][nj] == 0) {
                                    int ci = p.i, cj = p.j;
                                    move[ni][nj] += move[p.i][p.j];
                                    for (int s = 0; s < move[ci][cj].length(); s++) {
                                        pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                        pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                                    }
                                    move[ci][cj] = "";
                                    moved = true;
                                } else if (map[ni][nj] == 1) {
                                    int ci = p.i, cj = p.j;
                                    move[ni][nj] += new StringBuilder(move[p.i][p.j]).reverse().toString();
                                    for (int s = 0; s < move[ci][cj].length(); s++) {
                                        pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                        pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                                    }
                                    move[ci][cj] = "";
                                    moved = true;
                                }
                            }
                        }
                    }
                }
                else { // 파란색처럼
                    p.dir = reverseDir(p.dir);
                    ni = p.i + dr[p.dir];
                    nj = p.j + dc[p.dir];
                    if (0 <= ni && ni < N & 0 <= nj && nj < N) {
                        if (map[ni][nj] == 0) {
                            int ci = p.i, cj = p.j;
                            move[ni][nj] += move[p.i][p.j];
                            for (int s = 0; s < move[ci][cj].length(); s++) {
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                            }
                            move[ci][cj] = "";
                            moved = true;
                        } else if (map[ni][nj] == 1) {
                            int ci = p.i, cj = p.j;
                            move[ni][nj] += new StringBuilder(move[p.i][p.j]).reverse().toString();
                            for (int s = 0; s < move[ci][cj].length(); s++) {
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].i = ni;
                                pieces[move[ci][cj].charAt(s) - 'A' + 1].j = nj;
                            }
                            move[ci][cj] = "";
                            moved = true;
                        }
                    }
                }
                if (moved && move[ni][nj].length() >= 4) {
                    find = true;
                    break;
                }
            }
        }

        System.out.println(cnt);
    }

    static int reverseDir(int dir) {
        return dir % 2 == 0 ? dir + 1 : dir - 1;
    }

    static class Piece {
        int i, j, dir;

        public Piece(int i, int j, int dir) {
            this.i = i;
            this.j = j;
            this.dir = dir;
        }
    }
}

