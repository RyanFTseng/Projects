import java.util.Scanner;
class table
{
public static void main(String args[])
{
Scanner in = new Scanner(System.in);
System.out.println("input number");
int n;
n=in.nextInt();
for (int i=1;i<11;i++)
	{
	int a;
	a=n*i;
	System.out.println(n+"x"+i+"="+a);
	}
}
}
