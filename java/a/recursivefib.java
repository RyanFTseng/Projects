import java.util.Scanner;
class recursivefib{
	public static void main (String args[]){
	int i,x;
	System.out.println("input");
	Scanner in = new Scanner(System.in);
	x=in.nextInt();
	int a=fib(x);
	for(i=0;i<=x;i++){
		System.out.println("fibbonacci = "+fib(i));
		}
	}

static int fib(int z){
	if (z==0 || z==1){
		return z;
		}
	else{
		return fib(z-2)+fib(z-1);
		}
}
}
