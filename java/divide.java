import java.util.Scanner;
class divide
{
public static void main (String args[])
{

System.out.println("1st number");
Scanner a =new Scanner(System.in);
int x;
x=a.nextInt();

System.out.println("2nd number");
Scanner b = new Scanner(System.in);
int y;
y=b.nextInt();

try 
	{
	int z;
	z=x/y;
	System.out.print(z);
	}
catch(ArithmeticException e)
	{
	System.out.println("Division by 0");
	}

}
}
