import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class P1208 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());
        List<Integer> list1 = sum(0, N/2, arr);     // 0 ~ N/2-1 범위의 부분 수열의 합 리스트 구하기
        List<Integer> list2 = sum(N/2, N, arr);     // N/2 ~ N-1 범위의 부분 수열의 합 리스트 구하기
        Collections.sort(list1);
        list2.sort(Collections.reverseOrder());

        // 투포인터로 탐색
        int i = 0, j = 0;
        long cnt = 0;
        while(i < list1.size() && j < list2.size()) {
            int num1 = list1.get(i);
            int num2 = list2.get(j);
            int sum = num1 + num2;
            if(sum == S) {
                long cnt1 = 0;
                while(i < list1.size() && list1.get(i) == num1) { cnt1++; i++; }
                long cnt2 = 0;
                while (j < list2.size() && list2.get(j) == num2) { cnt2++; j++; }
                cnt += cnt1 * cnt2;
            }
            else if(sum > S) j++;
            else i++;
        }
        if(S == 0) --cnt;
        System.out.println(cnt);
    }

    // 각 부분수열의 합을 저장한 List 반환
    public static List<Integer> sum(int start, int end, int[] arr){
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < 1<<(end-start); i++) {
            int sum = 0;
            for(int j = 0; j < (end-start); j++) {
                if((i & 1<<j) != 0) sum += arr[j+start];
            }
            list.add(sum);
        }
        return list;
    }
}
