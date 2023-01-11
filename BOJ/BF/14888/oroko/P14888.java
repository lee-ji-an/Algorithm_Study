import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14888 {

    // 0 : + / 1 : - / 2 : * / 3 : %

    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    static int[] operands;

    public static int calculate(String operators) {
        int res = operands[0];
        for(int i = 0; i < operators.length(); i++) {
            char operator = operators.charAt(i);
            switch (operator) {
                case '0' : res += operands[i + 1]; break;
                case '1' : res -= operands[i + 1]; break;
                case '2' : res *= operands[i + 1]; break;
                default : res /= operands[i + 1];
            }
        }
        return res;
    }

    public static void perm(String str, String sub, int r, boolean[] visited) {
        if(r == 0) {
            int res = calculate(sub);
            max = Math.max(max, res);
            min = Math.min(min, res);
            return;
        }
        for(int i = 0; i < str.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                perm(str, sub + str.charAt(i), r-1, visited);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        operands = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) operands[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 4; i++) {
            int num = Integer.parseInt(st.nextToken());
            sb.append(String.valueOf(i).repeat(Math.max(0, num)));
        }

        perm(sb.toString(), "", sb.length(), new boolean[sb.length()]);
        System.out.println(max);
        System.out.println(min);
    }
}
