import java.util.Scanner;
class recursivefactorial{
public static void main (String args[]){
int x;

System.out.println("input");
Scanner in = new Scanner(System.in);
x=in.nextInt();
int a=facto(x);
System.out.println("factorial= "+a);
}

static int facto(int z){
if (z<=1){
	return 1;
	}
else{
	return z*facto(z-1);
}
}
}
