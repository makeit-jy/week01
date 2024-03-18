import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main { 	
	
	public static void main(String[] args) throws Exception {	
		//System.setIn(new FileInputStream("C:\\Users\\user\\Test_WorkSpace\\Test\\src\\input.txt"));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));		
		
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		
		if(N<100) {
			cnt = N;
			bw.write(cnt+"");
		}
		else {			
			while(N>=100) {
				int a = N/100;
				int b = N/10%10;
				int c = N%10;
				
				if((a-b)==(b-c)) {
					cnt++;
				}		
				N--;
			}			
			bw.write(cnt+99+"");
		}		
		bw.flush();
		br.close();
		bw.close();	
	}	
}