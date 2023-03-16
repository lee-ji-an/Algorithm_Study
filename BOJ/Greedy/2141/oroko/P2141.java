import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class P2141 {

    /*
     * 우체국을 기준으로 양쪽의 총 사람 수가 비슷할수록 유리하다
     * 즉, 왼쪽부터 사람 수를 누적하면서, 총 사람수의 절반이 되면 그곳에 세우자*/
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long sum = 0L;
        Village[] villages = new Village[N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            villages[i] = new Village(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            sum += villages[i].weight;
        }

        Arrays.sort(villages, Comparator.comparingInt(o -> o.pos));

        if(sum % 2 != 0) sum++;
        long partSum = 0L;
        for(int i = 0; i < N; i++) {
            partSum += villages[i].weight;
            if(partSum >= sum/2) {
                System.out.println(villages[i].pos);
                break;
            }
        }
    }

    static class Village {
        int pos, weight;

        public Village(int pos, int weight) {
            this.pos = pos;
            this.weight = weight;
        }
    }
}
