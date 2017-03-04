import java.util.Scanner;
class factorial
{
public static void main(String args[])
{
System.out.println("input number");
Scanner a= new Scanner(System.in);
int x=a.nextInt();
int y=x;
for(int i=0;i<=y;i++)
{
x=x*(y-1);
y=y-1;
}
System.out.println(x);
}
}
