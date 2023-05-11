import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P20366 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] snows = new int[N];
        for(int i = 0; i < N; i++) snows[i] = Integer.parseInt(st.nextToken());

        List<Snowman> list = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            for(int j = i+1; j < N; j++) list.add(new Snowman(i, j, (long) snows[i] + snows[j]));
        }

        list.sort((o1, o2) -> Long.compare(o1.height, o2.height));

        Long min = Long.MAX_VALUE;
        for(int i = 0; i < list.size()-1; i++) {
            Snowman s1 = list.get(i);
            Snowman s2 = list.get(i+1);
            if(s1.different(s2)) min = Math.min(min, s2.height-s1.height);
        }

        System.out.println(min);
    }

    static class Snowman {
        int i, j;
        Long height;

        public Snowman(int i, int j, Long height) {
            this.i = i;
            this.j = j;
            this.height = height;
        }

        public boolean different(Snowman s) {
            return this.i != s.i && this.i != s.j && this.j != s.i && this.j != s.j;
        }
    }
}
