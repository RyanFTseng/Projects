import java.util.Scanner;
import java.util.Random;
class random
{
public static void main(String args[])
{
Random rand = new Random();
int n=rand.nextInt(1000)+1;
int b=1;
int c=0;
while (b==1){
System.out.println("guess number between 1 and 1000");
Scanner a= new Scanner(System.in);
int x=a.nextInt();
if (x>n){
	System.out.println("too high");
	c=c+1;
	}
else if(x<n){
	System.out.println("too low");
	c=c+1;
	}
else if(x==n){
	c=c+1;
	System.out.println("you got it");
	System.out.println("you took "+c+" tries");
	b=0;
	}
}
}
}
