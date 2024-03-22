import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;

public class Main {	
	public static void main(String[] args) throws Exception {
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));		
		
		int N =  Integer.parseInt(br.readLine());
		LinkedList<Integer> qu = new LinkedList<Integer>();
		
		for(int i=0; i<N; i++) {
			String[] input = br.readLine().split(" ");
			int output = -1;
			
			switch(input[0]) {
			
				case "push":
					qu.offer(Integer.parseInt(input[1]));
					break;
					
				case "pop":
					output = -1;
					if(!qu.isEmpty()) {
						output = qu.poll();
					}
					bw.write(output + "\n");
					break;
					
				case "size":
					output = qu.size();
					bw.write(output + "\n");
					break;
					
				case "empty":
					output = 1;
					if(!qu.isEmpty()) {
						output = 0;
					}
					bw.write(output + "\n");
					break;
					
				case "front":
					output = -1;
					if(!qu.isEmpty()) {
						output = qu.peek(); 
					}
					bw.write(output + "\n");
					break;
				case "back":
					output = -1;
					if(!qu.isEmpty()) {
						output = qu.peekLast();
					}
					bw.write(output + "\n");
					break;		
			}
		}				
	    bw.flush();
		br.close();
		bw.close();	
	}	
}