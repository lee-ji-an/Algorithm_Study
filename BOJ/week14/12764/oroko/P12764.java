import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P12764 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Duration[] durations = new Duration[N];
        PriorityQueue<Integer> available = new PriorityQueue<>();
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            durations[i] = new Duration(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            available.add(i);
        }
        Arrays.sort(durations, Comparator.comparingInt(o -> o.start));

        Map<Integer, Integer> computers = new HashMap<>();
        PriorityQueue<Use> using = new PriorityQueue<>();
        for(Duration d : durations) {
            while(!using.isEmpty() && d.start >= using.peek().duration.end) available.add(using.remove().computerId);
            int computerId = available.remove();
            using.add(new Use(d, computerId));
            computers.put(computerId, computers.getOrDefault(computerId, 0)+1);
        }

        StringBuilder sb = new StringBuilder();
        for(int key : computers.keySet()) {
            sb.append(computers.get(key)).append(" ");
        }
        System.out.println(computers.size());
        System.out.println(sb);
    }

    static class Duration {
        int start, end;

        public Duration(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    static class Use implements Comparable<Use> {
        Duration duration;
        int computerId;

        public Use(Duration duration, int computerId) {
            this.duration = duration;
            this.computerId = computerId;
        }

        @Override
        public int compareTo(Use o) {
            return Integer.compare(this.duration.end, o.duration.end);
        }
    }
}
