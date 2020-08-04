// 트리의 높이와 너비
// 중
// 트리, 구현
// 50분

package JAVA;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Node{
    int data;
    int left;
    int right;
    int num;

    Node(int data, int left, int right){
        this.data = data;
        this.left = left;
        this.right = right;
        this.num = 0;
    }
}

public class Boj_2250 {
    public static Map<Integer, Node> tree = new HashMap<>();
    public static int x = 1;

    public static void main(String[] args){
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt();

        for (int i =0;i<N;i++){
            scin.nextLine();
            int data = scin.nextInt();
            int left = scin.nextInt();
            int right = scin.nextInt();
            Node node = new Node(data, left, right);
            tree.put(data, node);
        }

        inOrder(tree.get(1));


    }

    static void inOrder(Node root){
        if(root.left!=-1){
            inOrder(tree.get(root.left));
        }
        root.num = x++;
        if(root.right!=-1){
            inOrder(tree.get(root.right));
        }
    }
    
}