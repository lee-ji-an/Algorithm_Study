import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14225 {

    public static int sum(String set, int[] arr) {
        int sum = 0;
        int num = 1;
        for(int i = set.length()-1; i >= 0; i--) {
            if(set.charAt(i) == '1') sum += arr[num];
            num++;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int max = 0;
        for(int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            max += arr[i];
        }
        int set = (1 << N) - 1;
        boolean[] sums = new boolean[max + 1];
        for(int subset = set; subset > 0; subset = (subset - 1) & set) sums[sum(Integer.toBinaryString(subset), arr)] = true;

        int answer = 0;
        for(int i = 1; i <= max; i++) {
            if(!sums[i]) {
                answer = i;
                break;
            }
        }
        if(answer == 0) answer = max + 1;
        System.out.println(answer);
    }
}
