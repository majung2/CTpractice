// 베스트셀러
// 하
// 탐색
// 40분 / 20분
package boj;

import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Boj_1302 {
    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt(); // 오늘 팔린 책의 개수
        scin.nextLine();

        Map<String,Integer> book = new HashMap<String, Integer>();

        for (int i=0;i<N;i++){
            String name = scin.nextLine();
            book.computeIfPresent(name, (String key, Integer value) -> ++value);
            book.putIfAbsent(name, 1);
        }
        
        int maxValue = (Collections.max(book.values()));
        TreeMap<String, Integer> tm = new TreeMap<String,Integer>(book);
        Iterator<String> iteratorKey = tm.keySet().iterator();

        while(iteratorKey.hasNext()){
            String key = iteratorKey.next();
            if (book.get(key)==maxValue){
                System.out.println(key);
                break;
            }
        }
        
        scin.close();

    }

}