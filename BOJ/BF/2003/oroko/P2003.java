import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P2003 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int sum = 0;
        int cnt = 0;
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < N; i++) {
            int n = Integer.parseInt(st.nextToken());
            q.add(n);
            sum += n;
            while(sum > M) sum -= q.remove();
            if(sum == M) cnt++;
        }
        System.out.println(cnt);
    }
}
