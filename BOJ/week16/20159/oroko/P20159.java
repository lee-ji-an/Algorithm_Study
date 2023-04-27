import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P20159 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] cards = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i ++) {
            if(i-2 >= 0) cards[i] = cards[i-2];
            cards[i] += Integer.parseInt(st.nextToken());
        }

        if(N == 2) {
            System.out.println(Math.max(cards[0], cards[1]));
            return;
        }

        int max = 0;
        for(int i = 0; i < N; i++) {
            int sum;
            if(i%2 == 0) {
                sum = i-2 >= 0 ? cards[i-2] : 0;
                sum += cards[N-1] - (i-1 >= 0 ? cards[i-1] : 0);
            }
            else {
                sum = cards[i-1];
                sum += cards[N-3] - (i-2 >= 0 ? cards[i-2] : 0);
            }
            max = Math.max(max, sum);
        }

        System.out.println(max);
    }
}
