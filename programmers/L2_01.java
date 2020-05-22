// 쇠막대기
package programmers;

public class L2_01 {
    public static void main(String[] args){
        String arrangement = "()(((()())(())()))(())";

        // ( 를 만나면 쇠막대기 수 ++
        // () 를 만나면(레이저) > 현재쇠막대기 수 answer +
        // ) 를 만나면 쇠막대기 수 -- answer +
        int answer = 0;
        int stick = 0;

        for ( int i =0 ; i< arrangement.length();i++){
            if(arrangement.charAt(i)=='('){
                if(arrangement.charAt(i+1)==')'){ // 레이저, answer +=현재 쇠막대기 수 
                    answer+=stick;
                    i++;
                }else{ // 쇠막대기
                    stick++;
                }
            }else{ // 쇠막대기 끝
                stick--;
                answer++;
            }
        }

        System.out.println(answer);

    } 
    
}