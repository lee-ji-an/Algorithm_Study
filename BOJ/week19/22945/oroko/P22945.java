import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P5875 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());

        int i = 0, j = N-1;
        int max = 0;
        while(i < j) {
            max = Math.max(max, (j-i-1) * Math.min(arr[i], arr[j]));
            if(arr[i] > arr[j]) j--;
            else i++;
        }

        System.out.println(max);
    }
}
