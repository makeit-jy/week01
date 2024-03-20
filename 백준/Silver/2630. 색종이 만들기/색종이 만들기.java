import java.util.Scanner;

public class Main {
    static int[][] map;
    static int white = 0;
    static int blue = 0;

    public static void main(String[] args) throws Exception { 	
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();        
        map = new int[n][n];

        for(int i = 0; i< n; ++i){
            for(int j = 0; j< n; ++j){
                map[i][j] = scan.nextInt();
            }
        }
        scan.close();

        //같은 색들로 존재하는지 확인 -> 아니라면 분할
        doProcess(n, 0, 0);

        System.out.println(white);
        System.out.println(blue);
    }

    private static void doProcess(int n, int front, int rear) { 
        if(findSameColor(n, front, rear)){		// 종료조건
            if(map[front][rear] == 0) {
            	white++;
            }
            else {
            	blue++;
            }            
            return;
        }
        else{	                                   // 논리(재귀)

	        //같은 색이 아니라면				   	// 4개로 쪼개서 자기자신을 부른다(재귀로 실행시킨다)
   	        doProcess(n/2, front, rear);			
	        doProcess(n/2, front, rear + (n/2));
	        doProcess(n/2, front + (n/2), rear);
	        doProcess(n/2, front + (n/2), rear + (n/2));
        }
    }

    private static boolean findSameColor(int n, int front, int rear) {
        int tmp = map[front][rear];
        for(int i=front; i<front+n; ++i){
            for(int j=rear; j<rear+n; ++j){
                if(tmp == map[i][j]) {
                    tmp = map[i][j];
                }
                else {
                    return false;
                }
            }
        }
        return true;
    }
}