import java.util.Scanner;
class evenodd
{
public static void main(String args[])
{
System.out.println("input number");
Scanner a=new Scanner(System.in);
int x;
x=a.nextInt();
if (x%2==0)
{
System.out.println("even");
}
else
{
System.out.println("odd");
}
}
}
