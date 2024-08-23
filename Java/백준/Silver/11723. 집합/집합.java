import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        OutputStream out = System.out;
        PrintWriter writer = new PrintWriter(out);
        
        int M = Integer.parseInt(br.readLine());
        int bitMask = 0;
        final int ALL_MASK = (1 << 20) - 1;

        for (int i = 0; i < M; i++) {
            String[] input = br.readLine().split(" ");
            String command = input[0];

            if (command.equals("all")) {
                bitMask = ALL_MASK;
            } else if (command.equals("empty")) {
                bitMask = 0;
            } else {
                int x = Integer.parseInt(input[1]) - 1;

                switch (command) {
                    case "add":
                        bitMask |= (1 << x);
                        break;
                    case "remove":
                        bitMask &= ~(1 << x);
                        break;
                    case "check":
                        writer.println((bitMask & (1 << x)) != 0 ? 1 : 0);
                        break;
                    case "toggle":
                        bitMask ^= (1 << x);
                        break;
                }
            }
        }

        writer.flush();
    }
}