import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P20440 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] entry = new int[N];
        int[] exit = new int[N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            entry[i] = Integer.parseInt(st.nextToken());
            exit[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(entry);
        Arrays.sort(exit);

        int e = 0, x = 0;
        int max = 0;
        int cnt = 0;
        int[] gap = new int[2];
        int t = 0;
        while(true) {
            while (e < N && entry[e] == t) {
                cnt++;
                e++;
            }
            if(gap[1] == 0 && cnt == max) gap[1] = t;

            while (x < N && exit[x] == t) {
                cnt--;
                x++;
            }
            if(cnt > max) {
                max = cnt;
                gap[0] = t;
                gap[1] = 0;
            }

            if(e >= N && x >= N) break;
            if(e < N) t = Math.min(entry[e], exit[x]);
            else t = exit[x];
        }

        System.out.println(max);
        System.out.println(gap[0] + " " + gap[1]);
    }
}
