import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P20442 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int L = s.length();
        int[] R = new int[L];

        if(s.charAt(0) == 'R') R[0] = 1;

        for(int i = 1; i < L; i++) {
            if(s.charAt(i) == 'R') R[i] = R[i-1] + 1;
            else R[i] = R[i-1];
        }

        int left = 0, right = L-1;
        int answer = R[L-1];
        int leftK = s.charAt(left) == 'K' ? 1 : 0;
        int rightK = s.charAt(right) == 'K' ? 1 : 0;

        while (left < right) {
            if(leftK > 0 && rightK > 0) {
                int r = R[right] - (left == 0 ? 0 : R[left-1]);
                int temp = r > 0 ? Math.min(leftK, rightK) * 2 + r : 0;
                answer = Math.max(answer, temp);
            }

            if(leftK > rightK) {
                right--;
                if(s.charAt(right) == 'K') rightK++;
            }
            else {
                left++;
                if(s.charAt(left) == 'K') leftK++;
            }
        }

        System.out.println(answer);
    }
}
