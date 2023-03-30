import java.io.*;
import java.util.*;

public class P14267 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Integer>[] employees = new List[N+1];
        for(int i = 1; i <= N; i++) employees[i] = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        st.nextToken();
        for(int i = 2; i <= N; i++) {
            int boss = Integer.parseInt(st.nextToken());
            employees[boss].add(i);
        }

        int[] compliment = new int[N+1];
        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            compliment[Integer.parseInt(st.nextToken())] += Integer.parseInt(st.nextToken());
        }

        doCompliment(employees, compliment);

        bw.write(String.valueOf(compliment[1]));
        for(int i = 2; i <= N; i++) {
            bw.write(" ");
            bw.write(String.valueOf(compliment[i]));
        }
        bw.flush();
    }

    static void doCompliment(List<Integer>[] employees, int[] compliment) {
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        while(!q.isEmpty()) {
            int employee = q.remove();
            for(int sub : employees[employee]) {
                compliment[sub] += compliment[employee];
                q.add(sub);
            }
        }
    }
}
