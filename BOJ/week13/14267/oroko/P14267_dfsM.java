import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P14267_dfsM {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Employee[] employees = new Employee[N+1];
        for(int i = 1; i <= N; i++) employees[i] = new Employee(i);

        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            int bossId = Integer.parseInt(st.nextToken());
            if(bossId == -1) continue;
            employees[bossId].addSubordinate(employees[i]);
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            employees[Integer.parseInt(st.nextToken())].doCompliment(Integer.parseInt(st.nextToken()));
        }

        bw.write(String.valueOf(employees[1].compliment));
        for(int i = 2; i <= N; i++) {
            bw.write(" ");
            bw.write(String.valueOf(employees[i].compliment));
        }
        bw.flush();
    }

    static class Employee {
        int id;
        List<Employee> subordinate;
        int compliment;

        public Employee(int id) {
            this.id = id;
            this.subordinate = new ArrayList<>();
            this.compliment = 0;
        }

        public void addSubordinate(Employee employee) {
            this.subordinate.add(employee);
        }

        public void doCompliment(int weight) {
            this.compliment += weight;
            subordinate.forEach(i -> i.doCompliment(weight));
        }
    }
}
