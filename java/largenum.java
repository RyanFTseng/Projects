import java.util.Scanner;
class largenum
{
public static void main(String args[])
{
System.out.println("input x");
Scanner a=new Scanner(System.in);
int x=a.nextInt();

System.out.println("input y");
Scanner b=new Scanner(System.in);
int y=b.nextInt();

System.out.println("input z");
Scanner c=new Scanner(System.in);
int z=c.nextInt();

if (x>y && x>z)
{
System.out.println(x);
	if (y>z)
	{
	System.out.println(y);
	System.out.println(z);
	}
	else
	{
	System.out.println(z);
        System.out.println(y);
	}
}

if (y>z && y>x){
System.out.println(y);
        if (x>z)
        {
        System.out.println(x);
        System.out.println(z);
        }
        else
        {
        System.out.println(z);
        System.out.println(x);
        }
}
if (z>y && z>x)
{
System.out.println("z = largest number = "+z);
        if (x>y)
        {
        System.out.println("x=2nd largest number"+x);
        System.out.println("y=smallest number"+y);
        }
        else
        {
        System.out.println("y=2nd largest number"+y);
        System.out.println("x=smallest number"+x);
        }
}

}
}
