import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1182 {

    static int cnt = 0;
    static int N, S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());
        add(arr, 0, 0);
        System.out.println(S == 0 ? cnt - 1 : cnt);
    }

    static void add(int[] arr, int start, int sum) {
        if(sum == S) cnt++;

        for(int i = start; i < N; i++) add(arr, i+1, sum + arr[i]);
    }
}
