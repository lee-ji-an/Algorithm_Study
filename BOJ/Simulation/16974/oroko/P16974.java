import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P16974 {

    static long[] patty;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long X = Long.parseLong(st.nextToken());

        patty = new long[N+1];
        patty[0] = 1;
        long len = 1;
        for(int i = 1; i <= N; i++) {
            patty[i] = 1 + patty[i-1] * 2;
            len = 3 + (len * 2);
        }

        System.out.println(burger(1, len, X, N));
    }

    public static long burger(long left, long right, long X, int lev) {
        if(lev == 0) return patty[lev];

        if(X == left) return 0;
        if(X == right) return patty[lev];

        long mid = (left + right) / 2;
        if(X == mid) return patty[lev-1]+1;

        if(X <= mid-1) return burger(left+1, mid-1, X, lev-1);
        return patty[lev-1] + 1 + burger(mid+1, right-1, X, lev-1);
    }

}
