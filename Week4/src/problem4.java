import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.lang.*;
import java.util.*;

/**
 * Created with IntelliJ IDEA.
 * User: peterconerly
 * Date: 4/16/12
 * Time: 3:47 PM
 * To change this template use File | Settings | File Templates.
 */

public class problem4 {
    //public static int dataLength = 9;
    public static int dataLength = 875714; //= 9;
    public static Vertex[] graph = new Vertex[dataLength];
    public static Stack<Integer> finishingStack = new Stack<Integer>();

    public static class Vertex {
        public int leader = -1;
        public boolean explored = false;
        public List<Integer> incoming = new ArrayList<Integer>();
        public List<Integer> outgoing = new ArrayList<Integer>();

        public void addOutgoing(int endpoint) {
            outgoing.add(endpoint);
        }
        public void addIncoming(int endpoint) {
            incoming.add(endpoint);
        }
    }

    public static void DFS_Loop_Reverse() {
        for(int i = 0; i < dataLength ; i++) {
            if (!graph[i].explored) {
                DFS_Reverse(i);
            }
        }
    }
    public static void DFS_Reverse(int vertex) {
        if (graph[vertex].explored) {
            throw new RuntimeException();
        }
        graph[vertex].explored = true;

        for( int j : graph[vertex].incoming) {
            if (!graph[j].explored) {
                DFS_Reverse(j);
            }
        }
        finishingStack.push(vertex);
    }

    public static void DFS_Loop_Normal() {
        while (!finishingStack.empty()) {
            int item = finishingStack.pop();
            if (!graph[item].explored) {
                DFS_Normal(item, item);
            }
        }
    }
    public static void DFS_Normal(int vertex, int leadership) {
        if (graph[vertex].explored) {
            throw new RuntimeException();
        }
        graph[vertex].explored = true;
        graph[vertex].leader = leadership;
        for( int j : graph[vertex].outgoing) {
            if (!graph[j].explored) {
                DFS_Normal(j, leadership);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(new File("./Week4/src/SCC.txt"));
        //Scanner in = new Scanner(new File("./Week4/src/sample.txt"));
        //Scanner in = new Scanner(new File("C:/Users/Peter/SCC/SCC.txt"));

        for (int i = 0; i < graph.length; i++) {
            graph[i] = new Vertex();
        }
        while (in.hasNextInt()) {
            int vertex = in.nextInt() - 1;
            int endpoint = in.nextInt() - 1;
            graph[vertex].addOutgoing(endpoint);
            graph[endpoint].addIncoming(vertex);
        }
        in.close();

        //processing
        DFS_Loop_Reverse();
        for (int i = 0; i < graph.length; i++) {
            graph[i].explored = false;
        }
        DFS_Loop_Normal();

        HashMap<Integer, Integer> tally = new HashMap<Integer, Integer>();
        for (int i = 0; i < graph.length; i++) {
            int key = graph[i].leader;
            if (tally.containsKey(key)) {
                tally.put(key, tally.get(key) + 1);
            } else {
                tally.put(key, 1);
            }
        }
        List<Integer> componentSizes = new ArrayList<Integer>(tally.values());
        Collections.sort(componentSizes);
        Collections.reverse(componentSizes);

        for (int i = 0; i < 5; i++) {
            System.out.println(componentSizes.get(i));
        }
    }
}

/* Answers:
434821
968
459
313
211
*/