import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9252 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();
        int l1 = s1.length();
        int l2 = s2.length();
        int[][] dp = new int[l1+1][l2+1];
        Pos[][] parent = new Pos[l1+1][l2+1];
        for(int i = 1; i <= l1; i++) {
            for(int j = 1; j <= l2; j++) {
                if(s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    parent[i][j] = new Pos(i-1, j-1);
                }
                else {
                    if(dp[i-1][j] > dp[i][j-1]) {
                        dp[i][j] = dp[i-1][j];
                        parent[i][j] = new Pos(i-1, j);
                    }
                    else {
                        dp[i][j] = dp[i][j-1];
                        parent[i][j] = new Pos(i, j-1);
                    }
                }
            }
        }
        System.out.println(dp[l1][l2]);
        if(dp[l1][l2] > 0) {
            StringBuilder sb = new StringBuilder();
            int i = l1, j = l2;
            while(dp[i][j] > 0) {
                if(s1.charAt(i-1) == s2.charAt(j-1)) sb.append(s1.charAt(i-1));
                Pos p = parent[i][j];
                i = p.i;
                j = p.j;
            }
            System.out.println(sb.reverse());
        }
    }

    static class Pos {
        int i, j;

        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
