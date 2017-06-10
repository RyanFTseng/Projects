import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
class circleper{
public static void main (String args[]){
int radius=0;
System.out.println("input radius");
try{
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
radius=Integer.parseInt(br.readLine());
}

catch(NumberFormatException ne)
{
System.out.println("invalid radius"+ne);
System.exit(0);
}
catch(IOException ioe)
{
System.out.println("IO ERROR"+ ioe);
System.exit(0);
}

double perimeter=Math.PI*2*radius;
System.out.println(perimeter);
}
}
