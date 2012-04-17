import java.io.File;
import java.util.Scanner;
import java.util.*;

/*
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

    int vlength = 875714;
    public static Vertix[] graph = new Vertix[875714];
    //= new Array(875714);


    public static class Vertix {
        public int n;
        public int leader;
        public boolean explored = false;
        public int finishingTime;
        public List<Integer> edges = new ArrayList<Integer>();

        public Vertix(int v) {
            n = v;
        }

        public void addEdge(int edge) {
            edges.add(edge);
        }

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
        Scanner in = new Scanner(new File("./Week4/SCC.txt"));

        int previous = -1;
        while (in.hasNextInt()) {
            int vertix = in.nextInt();
            int edge = in.nextInt();
            if (vertix != previous) {
                graph[vertix] = new Vertix(vertix);
                previous = vertix;
            }
            graph[vertix].addEdge(edge);
        }

        //processing
        System.out.println(graph.length);


        //output
        //PrintWriter out = new PrintWriter(new File("A.out"));

        //out.format("Case #%d: %s\n", zz, ans);
        //out.close();
    }
}
