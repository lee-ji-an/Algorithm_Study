import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P3107 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] group = s.split(":");

        int insert = -1;
        for(int i = 0; i < group.length; i++) {
            if(group[i].equals("")) insert = i;
            StringBuilder sb = new StringBuilder(group[i]);
            while (sb.length() < 4) sb.insert(0, "0");
            group[i] = sb.toString();
        }

        StringBuilder sb = new StringBuilder(group[0]);
        for(int i = 1; i < group.length; i++) {
            sb.append(":").append(group[i]);
            if(i == insert) {
                for(int j = 0; j < 8-group.length; j++) sb.append(":").append("0000");
            }
        }

        while (sb.length() < 39) sb.append(":").append("0000");

        if(sb.length() > 39) sb.delete(0, 5);
        System.out.println(sb);
    }
}
