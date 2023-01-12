import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1806 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long S = Integer.parseInt(st.nextToken());
        Queue<Integer> q = new LinkedList<>();
        long sum = 0;
        int len = N+1;
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            q.add(num);
            sum += num;
            if(sum > S) {
                while(!q.isEmpty() && sum - q.peek() >= S) sum -= q.remove();
            }
            if(sum >= S) len = Math.min(len, q.size());
        }
        if(len == N+1) len = 0;
        System.out.println(len);
    }
}
