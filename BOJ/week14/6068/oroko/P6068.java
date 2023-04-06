import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P6068 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Schedule[] schedules = new Schedule[N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            schedules[i] = new Schedule(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(schedules, (o1, o2) -> Integer.compare(o2.end, o1.end));

        int wakeup = Integer.MAX_VALUE;
        for(Schedule schedule : schedules) {
            if(schedule.end <= wakeup) wakeup = schedule.start;
            else wakeup -= schedule.end - schedule.start;
            if (wakeup < 0) {
                wakeup = -1;
                break;
            }
        }
        System.out.println(wakeup);
    }

    static class Schedule {
        int start, end;

        public Schedule(int required, int end) {
            this.start = end - required;
            this.end = end;
        }
    }
}
