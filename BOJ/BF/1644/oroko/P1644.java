import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class P1644 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        Queue<Integer> q = new LinkedList<>();
        int cnt = 0;
        for(int i = 1; i <= n; i++) {
            if(isPrime(i)) {
                q.add(i);
                sum += i;
                while(sum > n) sum -= q.remove();
                if(sum == n) cnt++;
            }
        }
        System.out.println(cnt);
    }

    public static boolean isPrime(int n) {
        if(n == 1) return false;
        if(n == 2) return true;
        for(int i = 2; i <= Math.sqrt(n); i++) {
            if(n % i == 0) return false;
        }
        return true;
    }
}
