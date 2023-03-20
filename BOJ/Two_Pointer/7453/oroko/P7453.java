import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P7453 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[4][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 4; j++) arr[j][i] = Integer.parseInt(st.nextToken());
        }

        int len = N*N;
        int[] sum1 = new int[len];
        int[] sum2 = new int[len];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                sum1[i*N+j] = arr[0][i] + arr[1][j];
                sum2[i*N+j] = arr[2][i] + arr[3][j];
            }
        }

        Arrays.sort(sum1);
        Arrays.sort(sum2);

        long cnt = 0;
        int i = 0, j = len-1;
        while(i < len && j >= 0) {
            int sum = sum1[i] + sum2[j];
            if(sum == 0) {
                int cnt1 = 1, cnt2 = 1;
                while(i <= len-2 && sum1[i+1] == sum1[i]) {
                    i++;
                    cnt1++;
                }
                while(j > 0 && sum2[j-1] == sum2[j]) {
                    j--;
                    cnt2++;
                }
                cnt += (long) cnt1 * cnt2;
                i++;
                continue;
            }

            if(sum > 0) j--;
            else i++;
        }

        System.out.println(cnt);
    }
}
