import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P1963 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int res = bfs(A, B);
            System.out.println(res != -1 ? res : "Impossible");
        }
    }

    // 소수인지 확인
    static boolean isPrime(int n) {
        for(int i = 2; i <= Math.sqrt(n); i++) {
            if(n % i == 0) return false;
        }
        return true;
    }

    // 1000 -> { 1, 0, 0, 0 }
    static int[] intToArray(int n) {
        int[] arr = new int[4];
        for(int i = 3; i >= 0; i--) {
            arr[i] = n % 10;
            n /= 10;
        }
        return arr;
    }

    // { 1, 0, 0, 0 } -> 1000
    static int arrayToInt(int[] arr) {
        int ret = 0;
        int r = 1000;
        for(int i = 0; i < 4; i++) {
            ret += arr[i] * r;
            r /= 10;
        }
        return ret;
    }

    static int bfs(int a, int b) {
        Queue<PWD> q = new LinkedList<>();
        q.add(new PWD(a, 0));
        Set<Integer> visited = new HashSet<>();
        while(!q.isEmpty()) {
            PWD p = q.remove();
            if(p.num == b) return p.cnt;
            int[] arr = intToArray(p.num);
            for(int i = 0; i < 4; i++) {
                int temp = arr[i];
                for(int j = 0; j <= 9; j++) {
                    if(i == 0 && j == 0) continue;  // 1000 미만은 x
                    if(arr[i] == j) continue;   // 해당 자리에 기존이랑 같은 수는 검사할 필요 x
                    arr[i] = j;
                    int n = arrayToInt(arr);
                    if(!visited.contains(n) && isPrime(n)) {
                        q.add(new PWD(n, p.cnt+1));
                        visited.add(n);
                    }
                    arr[i] = temp;
                }
            }
        }
        return -1;
    }

    static class PWD {
        int num;
        int cnt;
        PWD(int nums, int cnt) {
            this.num = nums;
            this.cnt = cnt;
        }
    }
}
