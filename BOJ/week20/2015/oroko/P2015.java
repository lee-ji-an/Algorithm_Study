import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2015 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long K = Long.parseLong(st.nextToken());
        Map<Long, Long> map = new HashMap<>();
        long[] preSum = new long[N+1];

        st = new StringTokenizer(br.readLine());
        long answer = 0;
        for(int i = 1; i <= N; i++) {
            preSum[i] = preSum[i-1] + Long.parseLong(st.nextToken());
            if(map.containsKey(preSum[i]-K)) answer += map.get(preSum[i]-K);
            map.put(preSum[i], map.getOrDefault(preSum[i], 0L)+1);
        }

        answer += map.getOrDefault(K, 0L);

        System.out.println(answer);
    }
}
