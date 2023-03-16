import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class P2374 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();
        list.add(Integer.parseInt(br.readLine()));
        int last = list.get(0);
        int max = last;
        for(int i = 1; i < N; i++) {
            int n = Integer.parseInt(br.readLine());
            if(n != last) {
                list.add(n);
                last = n;
                max = Math.max(max, last);
            }
        }

        long cnt = 0;
        while(list.size() > 1) {
            int min = Integer.MAX_VALUE;
            int upNum = Integer.MAX_VALUE;
            for(int i = 0; i < list.size(); i++) {
                if(list.get(i) < min) {
                    upNum = Integer.MAX_VALUE;
                    if(i > 0) upNum = Math.min(upNum, list.get(i-1));
                    if(i < list.size()-1) upNum = Math.min(upNum, list.get(i+1));
                    min = list.get(i);
                }
            }
            cnt += upNum - min;
            list.remove(Integer.valueOf(min));
        }

        System.out.println(cnt);
    }
}