import java.io.File;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Scanner;
/*
import java.util.*;
import static java.lang.Math.*;
import java.io.*;
*/
/**
 * Created with IntelliJ IDEA.
 * User: peterconerly
 * Date: 4/16/12
 * Time: 3:47 PM
 * To change this template use File | Settings | File Templates.
 */

public class problem4 {

    private class Vertix {
        int n = 0;

    }

    public String DFS(Vertix[] graph, int s) {
        //int s is start point.

        return "s";
    }

    public String DFS_Loop(Vertix[] graph) {
        return "s";
    }

    public static void main(String[] args) throws Exception {
        //input
        Scanner in = new Scanner(new File("SCC.txt"));
        int T = in.nextInt();
        in.nextLine();

        //processing


        //output
        PrintWriter out = new PrintWriter(new File("A.out"));


        for(int zz = 1; zz <= T; zz++) {
            String ans = "";
            String S = in.nextLine();
            for (int i = 0; i < S.length(); i++) {
                //ans += hm.get(S.charAt(i));
            }
            out.format("Case #%d: %s\n", zz, ans);
        }
        out.close();
    }
}
