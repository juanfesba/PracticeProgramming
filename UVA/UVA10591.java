package uva;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.HashMap;

public class UVA10591 {
    public static void main(String[] arg) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        //OutputStream outS=System.out;
        PrintWriter out=new PrintWriter(System.out);
        Integer T=Integer.valueOf(reader.readLine().trim());
        HashMap<Integer,Boolean>visited;
        int current;
        int mod;
        int count;
        Integer tmp;
        boolean flag;
        //StringBuilder ans=new StringBuilder("");
        for(int t=1;t<=T;t++){
            count=0;
            Integer N=Integer.valueOf(reader.readLine().trim());
            tmp=N;
            visited=new HashMap<Integer,Boolean>();
            flag=true;
            while(flag) {
                if(N==1) {
                    flag=false;
                    continue;
                }
                if(visited.get(N)==null)visited.put(N,true);
                else {
                    count=-1;
                    flag=false;
                    continue;
                }
                count+=1;//204,20,4,16,37,58,89,145,42
                current=0;
                while(N!=0) {
                    mod=N%10;
                    current+=Math.pow(mod, 2);
                    N/=10;
                }
                N=current;
            }
            if(count!=-1)out.format("Case #%d: %d is a Happy number.\n", t,tmp);
            else out.format("Case #%d: %d is an Unhappy number.\n", t,tmp);
        }
        out.close();
    }
}
