import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2143 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int[] arr1 = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) arr1[i] = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(br.readLine());
        int[] arr2 = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++) arr2[i] = Integer.parseInt(st.nextToken());

        List<Integer> list1 = sum(arr1, n);
        List<Integer> list2 = sum(arr2, m);
        Collections.sort(list1);
        list2.sort(Collections.reverseOrder());

        int i = 0, j = 0;
        long cnt = 0;
        while(i < list1.size() && j < list2.size()) {
            int num1 = list1.get(i);
            int num2 = list2.get(j);
            int sum = num1 + num2;
            if(sum == T) {
                long cnt1 = 0;
                while(i < list1.size() && list1.get(i) == num1) { cnt1++; i++; }
                long cnt2 = 0;
                while (j < list2.size() && list2.get(j) == num2) { cnt2++; j++; }
                cnt += cnt1 * cnt2;
            }
            else if(sum > T) j++;
            else i++;
        }
        System.out.println(cnt);
    }

    public static List<Integer> sum(int[] arr, int n) {
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            int sum = 0;
            for(int j = i; j < n; j++) {
                sum += arr[j];
                list.add(sum);
            }
        }
        return list;
    }

}