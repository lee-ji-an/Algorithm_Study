import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12865 {

    // D[i][j] = i번째 물건까지 고려했고, 배낭에 넣은 물건의 합이 j일 때, 가치의 최댓값
    // D[i][j] = max(D[i-1][j], D[i-1][j-W[i]] + V[i])
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Item[] items = new Item[N+1];
        for(int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            items[i] = new Item(Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()));
        }
        int[][] value = new int[N+1][K+1];
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= K; j++) {
                value[i][j] = value[i-1][j];    // item[i]를 넣지 않은 경우
                if(j - items[i].weight >= 0)
                    value[i][j] = Math.max(value[i][j],
                            value[i-1][j-items[i].weight] + items[i].value);    // i번째 물건을 넣지 않았을 때의 최대 가치에서 i번째 물건 가치 더하기
            }
        }
        System.out.println(value[N][K]);
    }

    static class Item {
        int weight, value;

        public Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
}
