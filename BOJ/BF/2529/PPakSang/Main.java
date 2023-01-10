import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * k 개의 부등호, k+1 개의 숫자
 * 0~9 중 하나 선택
 * 첫 번 째는 아무거나 넣으면 되고
 * 그 다음 넣는 숫자 부터 이전 부등호 바탕으로 연산
 * 만족하면 다음 재귀, 아니면 다음 숫자
 */



public class Main {
    static String max;
    static String min;
    static String[] signs;

    static boolean[] visited = new boolean[10];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 부등호 갯수
        int k = Integer.parseInt(br.readLine());
        // 뽑을 숫자 갯수
        int num = k+1;

        max = "0".repeat(num);
        min = "9".repeat(num);
        signs = br.readLine().split(" ");

        permutation(num,0, "", -1);

        System.out.println(max);
        System.out.println(min);
    }

    static void permutation(int maxCnt, int cnt, String curStr, int prevNum) {
        if (cnt == maxCnt) {
            if (max.compareTo(curStr) < 0) {
                max = curStr;
            }
            if (min.compareTo(curStr) > 0) {
                min = curStr;
            }
            return;
        }

        for (int i = 0; i < 10; i++) {
            if (visited[i]) continue;

            if (cnt == 0 || check(signs[cnt-1], prevNum, i)) {
                visited[i] = true;
                permutation(maxCnt, cnt+1, curStr+i, i);
                visited[i] = false;
            }
        }
    }

    static boolean check(String sign, int prevNum, int curNum) {
        if (sign.equals(">")) {
            return prevNum > curNum;
        } else if (sign.equals("<")){
            return prevNum < curNum;
        }
        return false;
    }
}