import java.util.Scanner;
class nesttable
{
public static void main(String args[])
{
Scanner in = new Scanner(System.in);
System.out.println("input 1st number");
int m;
m=in.nextInt();
System.out.println("input 2nd number");
int n ;
n=in.nextInt();


for (m=m;m<=n;m++)
	{
	for (int i=1;i<=11;i++)
		{
		System.out.println(m+"x"+i+"="+(m*i));
		}
	}
}
}
