import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9663_1 {

    static int N;
    static boolean[] col, diag1, diag2;
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        col = new boolean[N];
        diag1 = new boolean[N+N-1];
        diag2 = new boolean[N+N-1];

        queen(0);
        System.out.println(cnt);
    }

    public static void queen(int r) {
        if(r == N) {
            cnt++;
            return;
        }

        for(int i = 0; i < N; i++) {
            if(check(r, i)) {
                set(r, i, true);
                queen(r+1);
                set(r, i, false);
            }
        }
    }

    public static boolean check(int i, int j) {
        if(col[j]) return false;
        if(diag1[i+j]) return false;
        if(diag2[N-j+i-1]) return false;
        return true;
    }

    public static void set(int i, int j, boolean val) {
        col[j] = val;
        diag1[i+j] = val;
        diag2[N-j+i-1] = val;
    }
}
