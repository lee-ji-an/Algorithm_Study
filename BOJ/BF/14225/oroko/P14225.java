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
        // 이렇게 할 수도 있음
        /*for(int i = 0; i < 1 << N; i++) {     // 000 ~ 111 까지 부분집합에 대해서 탐색
            int sum = 0;
            for(int j = 0; j < N; j++) {
                if(i & (1 << j) != 0) sum += arr[j];    // 해당 자리가 켜져있는지 확인
            }
            sums[sum] = true;
        }*/

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
