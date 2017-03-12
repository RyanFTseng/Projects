import java.util.Scanner;

class factorialrecursion

{
public static void main(String args[])
{
System.out.println("input");
Scanner a= new Scanner(System.in);
int x=a.nextInt();
int factorial=fact(x);
System.out.println(fact(x));
}


static int fact(int x)

{
if (x==0)
	{
	return(1);
	}
else
	{
	return(x*fact(x-1));
	}
}


}
