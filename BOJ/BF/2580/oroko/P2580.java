import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class P2580 {

    static boolean[][] rows, cols, areas;
    static List<Pos> list;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[9][9];
        rows = new boolean[9][10];     // i행에 j가 존재함
        cols = new boolean[9][10];     // i열에 j가 존재함
        areas = new boolean[9][10];     // i구역에 j가 존재함
        list = new ArrayList<>();
        for(int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 9; j++) {
                int n = Integer.parseInt(st.nextToken());
                board[i][j] = n;
                if(n > 0) {
                    rows[i][n] = true;
                    cols[j][n] = true;
                    areas[(i/3)*3+(j/3)][n] = true;
                }
                else list.add(new Pos(i, j));
            }
        }
        write(board, 0);
    }

    public static boolean write(int[][] board, int r) {
        if(r == list.size()) {
            for(int i = 0; i < 9; i++) System.out.println(Arrays.toString(board[i]).replaceAll("[\\[\\],]", ""));
            return true;
        }

        Pos blank = list.get(r);
        for(int i = 1; i <= 9; i++) {
            if(rows[blank.i][i] ||
                    cols[blank.j][i] ||
                    areas[(blank.i/3)*3+(blank.j/3)][i]) continue;

            board[blank.i][blank.j] = i;
            rows[blank.i][i] = true;
            cols[blank.j][i] = true;
            areas[(blank.i/3)*3+(blank.j/3)][i] = true;

            if(write(board, r+1)) return true;

            rows[blank.i][i] = false;
            cols[blank.j][i] = false;
            areas[(blank.i/3)*3+(blank.j/3)][i] = false;
        }
        return false;
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}