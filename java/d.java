import java.util.Scanner;
class d
{
public static void main(String args[])
{
Scanner in =new Scanner(System.in);
while (true)
{
	System.out.println("input number");
	int n;
	n=in.nextInt();
	if (n!=0)
	{
	System.out.println(n);
	continue;
	}
	else
	{
	break;
	}
}
}
}

