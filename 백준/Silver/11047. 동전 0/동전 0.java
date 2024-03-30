import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main { 		
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));		

		String line = br.readLine();
		String[] num = line.split(" ");
		
		int N = Integer.parseInt(num[0]);
		int K = Integer.parseInt(num[1]);
		
		int[] arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		int result = K;
		int cnt = 0;
		
		for(int i=N-1; i>=0; i--) {
			if(result >= arr[i]) {
				while(result >= arr[i]) {
					result -= arr[i];
					cnt++;					
					if(result == 0) {
						bw.write(cnt+"");
						break;
					}
				}
			}
		}
		
	    bw.flush();
		br.close();
		bw.close();	
	}	
}