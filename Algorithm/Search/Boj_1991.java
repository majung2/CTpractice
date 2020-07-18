// 트리 순회
// 하
// 트리, 구현
// 인강도움 / 20분
// Silver 1

package boj.Silver1;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Node{
    char data;
    char left;
    char right;

    Node(char data, char left, char right){
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

public class Boj_1991 {
    public static Map<Character, Node> tree = new HashMap<>();

    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt(); // 노드의 개수
        scin.nextLine();


        for (int i = 0; i < N; i++) {
            String data = scin.nextLine();
            Node NodeData = new Node(data.charAt(0), data.charAt(2), data.charAt(4));
            tree.put(data.charAt(0), NodeData);
        }

        pre_order(tree.get('A'));
        System.out.println();
        in_order(tree.get('A'));
        System.out.println();
        post_order(tree.get('A'));
        
        scin.close();
    }

    static void pre_order(Node root){
        System.out.print(root.data);
        if(root.left!='.'){ //왼쪽 먼저
            pre_order(tree.get(root.left));
        }
        if(root.right!='.'){
            pre_order(tree.get(root.right));
        }
    }

    static void in_order(Node root){
        if(root.left!='.'){ //왼쪽 먼저
            in_order(tree.get(root.left));
        }
        System.out.print(root.data);
        if(root.right!='.'){
            in_order(tree.get(root.right));
        }
    }
    
    static void post_order(Node root){
        if(root.left!='.'){ //왼쪽 먼저
            post_order(tree.get(root.left));
        }
        if(root.right!='.'){
            post_order(tree.get(root.right));
        }
        System.out.print(root.data);
    }

}





        // // pre
        // Stack<Character> st = new Stack<Character>(); // 오른쪽꺼 넣기
        // for (int count = 0, now = 0; count < N;) {
        //     System.out.print(tree[now][0]);
        //     count++;
        //     if (tree[now][2] != '.') {// 오른쪽이 있으면 stack에 넣기
        //         st.push(tree[now][2]);
        //     }
        //     if (tree[now][1] != '.') { // 왼쪽이 있으면 now 왼쪽으로 바꾸기
        //         for (int i = 0; i < N; i++) {
        //             if (tree[i][0] == tree[now][1]) {
        //                 now = i;
        //                 break;
        //             }
        //         }
        //     } else { // 없으면stack에서 하나 pop해서 now에 넣고 반복
        //         if (!st.empty()) {
        //             char temp = st.pop();
        //             for (int i = 0; i < N; i++) {
        //                 if (tree[i][0] == temp) {
        //                     now = i;
        //                     break;
        //                 }
        //             }
        //         }
        //     }
        // }