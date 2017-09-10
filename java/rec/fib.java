import java.util.Scanner;
class fib{
public static void main(String args[]){
int i,x;
System.out.println("input");
Scanner in=new Scanner(System.in);
x = in.nextInt();
for (i=0;i<x;i++)
	System.out.println(fibb(i));

}
static int fibb(int x){
if (x==1||x==0)
return x;
else
return(fibb(x-2)+fibb(x-1));

}
}

