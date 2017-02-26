import java.util.Scanner;
class div10
{
public static void main(String args[])
{
System.out.println("input number");
Scanner a=new Scanner(System.in);
int x;
x=a.nextInt();
if (x%10==0)
{
System.out.println("divisible by 10");
}
else
{
System.out.println("not divisible by 10");
}
}
}
