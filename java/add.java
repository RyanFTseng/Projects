import java.util.Scanner;
class add
{
public static void main (String args[])
{
System.out.println("add,subtract,multiply, or divide?");
Scanner d=new Scanner(System.in);
String oper;
oper=d.nextLine();

System.out.println("input 1st number");
Scanner a=new Scanner(System.in);
int x;
x=a.nextInt();

System.out.println("input 2nd number");
Scanner b=new Scanner(System.in);
int y;
y=b.nextInt();

int z;
z=0;

{
if (oper.equals("add"))
        {
        z=x+y;
        }
else if (oper.equals("subtract"))
        {
        z=x-y;
        }
else if (oper.equals("multiply"))
        {
        z=x*y;
        }
else if (oper.equals("divide"))
        {
        z=x/y;
        }


while (true)
{

System.out.println("What is "+x+" "+oper+" " +y+"?");
Scanner c=new Scanner(System.in);
int n;
n=c.nextInt();

if (n==z)
	{
	System.out.println(x+oper+y+"="+n+"is correct");
	break;
	}
else
	{
	System.out.println(x+" "+oper+" "+ y+"="+n+"is incorrect, try again");
	}

}
}
}
}
