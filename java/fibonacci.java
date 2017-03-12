import java.util.Scanner;
class fibbonacci
{
public static void main(String args[])
{

System.out.print("input");
Scanner in = new Scanner(System.in);
int x = in.nextInt();
int a=0;
int b=1;
int c;

if (x==1)
	{
	System.out.println(a);
	}
if (x==2)
        {
        System.out.println(a);
	System.out.println(b);
        }
else if (x>2)
	{
	System.out.println(a);
	System.out.println(b);
	System.out.println(b);
	for (int n=2;n<=x;n++)
		{
		c=a+b;
		//System.out.println(a+b);
		a=b;
		b=c;
		System.out.println(c);

		}
	}
}
}
