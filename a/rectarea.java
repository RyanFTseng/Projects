import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
class rectarea{
public static void main (String args[]){
int w=0;
int l=0;
System.out.println("input length");

try{
BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
l=Integer.parseInt(br.readLine());
}

catch(NumberFormatException ne)
{
System.out.println("invalid length"+ne);
System.exit(0);
}

catch(IOException ioe)
{
System.out.println("IO Error"+ioe);
System.exit(0);
}

System.out.println("input width");

try{
BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
w=Integer.parseInt(br.readLine());
}

catch(NumberFormatException ne)
{
System.out.println("invalid width"+ne);
System.exit(0);
}

catch(IOException ioe)
{
System.out.println("IO Error"+ioe);
System.exit(0);
}

double area = l*w;
System.out.println(area);
}
}

