import java.math.BigInteger;
import java.util.Scanner;
class binary
{
public static void main(String args[])
{
System.out.println("input");
Scanner a=new Scanner(System.in);
int x=a.nextInt();

System.out.println(Integer.toBinaryString(x));
System.out.println("octal "+Integer.toString(x,0));
System.out.println("binary "+Integer.toString(x,2));
System.out.println("hex "+Integer.toString(x,16));
}
}

