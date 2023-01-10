import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class P2529 {

    /** 내 풀이 */
    public static String make(int k, char[] c, int[] q) {
        int[] arr = new int[k+1];
        arr[0] = q[0];
        int idx = 1;
        for(int i = 1; i <= k; i++) {
            if ((c[i] == '>' && arr[i - 1] > q[idx]) ||
                    (c[i] == '<' && arr[i - 1] < q[idx])) arr[i] = q[idx++];
            else {
                int j = i;
                for (; c[i] == c[j]; j--) arr[j] = arr[j - 1];
                arr[j] = q[idx++];
            }
        }

        return Arrays.toString(arr).replaceAll("[\\[\\], ]", "");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        char[] c = new char[k+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= k; i++) c[i] = st.nextToken().charAt(0);

        int[] q = IntStream.range(9-k, 10).map(i -> 18-k-i).toArray();
        System.out.println(make(k, c, q));
        q = IntStream.range(0, k+1).toArray();
        System.out.println(make(k, c, q));
    }

    /** 최백준씨 풀이 활용 */
    static String maxVal = "0";
    static String minVal = Integer.toString(Integer.MAX_VALUE);
    static char[] c;

    public static boolean check(String s, int k) {
        for(int i = 0; i < k; i++) {
            if(c[i] == '<' && s.charAt(i) > s.charAt(i+1)) return false;
            if(c[i] == '>' && s.charAt(i) < s.charAt(i+1)) return false;
        }
        return true;
    }
    public static void permutation(int[] arr, String res, int r, boolean[] visited, boolean max) {
        if(r == 0) {
            if(check(res, arr.length-1)) {
                if(max) maxVal = maxVal.compareTo(res) > 0 ? maxVal : res;
                else minVal = minVal.compareTo(res) < 0 ? minVal : res;
            }
        }

        for(int i = 0; i < arr.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                permutation(arr, res + arr[i], r-1, visited, max);
                visited[i] = false;
            }
        }
    }

    public static void main1(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        c = new char[k];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < k; i++) c[i] = st.nextToken().charAt(0);
        int[] min = IntStream.range(0, k+1).toArray();
        int[] max = IntStream.range(0, k+1).map(i -> 9-i).toArray();
        permutation(max, "", k+1, new boolean[k+1], true);
        permutation(min, "", k+1, new boolean[k+1], false);
        System.out.println(maxVal);
        System.out.println(minVal);
    }
}
