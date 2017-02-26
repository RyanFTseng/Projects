import java.util.Scanner;
class CtoF
{
public static void main(String args[])
{
System.out.println("input C temp");
Scanner a=new Scanner(System.in);
int C;
C=a.nextInt();
C=9*C/5+32;
System.out.println("F temp = "+C);
}
}
