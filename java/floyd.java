import java.util.Scanner;
class floyd
{
public static void main(String args[])
{
int n=1;
System.out.print("input number");
Scanner z =new Scanner(System.in);
int x=z.nextInt();
for (int i=0;i<x+1;i++){
	for (int h=0;h<i;h++)
	{
	System.out.print(n+" ");
	n=n+1;
	}
	System.out.println(" ");
}
}
}
