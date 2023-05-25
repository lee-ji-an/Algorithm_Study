import java.io.*;

public class P1484 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int G = Integer.parseInt(br.readLine());

        boolean flag = false;
        for(int i = (int)Math.sqrt(G); i >= 1; i--) {
            if(G % i != 0) continue;
            int diff = i;
            int sum = G/i;

            if(sum == diff) continue;
            if((diff+sum) % 2 != 0) continue;
            int a = (diff + sum) / 2;
            bw.write(String.valueOf(a));
            bw.newLine();

            flag = true;
        }

        if(!flag) bw.write("-1");
        bw.flush();
    }
}
