// 중량제한
// 중상
// 이진 탐색
// 1시간

package boj;

import java.util.ArrayList;
import java.util.*;
import java.util.Scanner;

class Edge <V, W>{ // Edge를 하나의 클래스로 표현하여 입력
    private V v; // edge 끝 부분에 있는 vertex 번호
    private W weight; // edge에 부여된 가중치

    public void set(V v, W weight){
        this.weight = weight;
        this.v = v;
    }
}

public class Boj_1939 {
    static boolean bfs(int start, int end, int v, int N){
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(start);
        boolean[] visited = new boolean[N+1];
        visited[start] = true;
        while (!q.isEmpty()){
            int x = q.poll();


        }


        return true;
    }

    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt(); // 섬 개수
        int M = scin.nextInt(); // 다리 개수
        int start = 1000000000;
        int end = 1;

        ArrayList<Edge> bridges = new <Edge> ArrayList();
        Edge <Integer, Integer> ed = new <Integer, Integer> Edge();

        for (int i =0; i<N+1;i++)
            bridges.add(new <Integer, Integer> Edge()); // edge 초기화
            

   

        
        for (int i = 0 ; i<M ; i++){
            scin.nextLine();
            int s1 = scin.nextInt();
            int s2 = scin.nextInt();
            int w = scin.nextInt();



            start = (start<w)?start:w;
            end = (end>w)?end:w;


        }
        scin.nextLine();
        int start_node = scin.nextInt();
        int end_node = scin.nextInt();
        int result = start;

        //이진 탐색
        while(start<=end){
            int mid = (start+end)/2;
            if (bfs(start_node, end_node, mid, N)){
                result =mid;
                start = mid+1;
            }else{
                end = mid-1;
            }
        }


        System.out.println(result);
        scin.close();
    }
}