import java.util.Scanner;
class recursionfibonaci{

public static void main(String args[]){
System.out.println("input");
Scanner in=new Scanner(System.in);
int x=in.nextInt();
int a=0;
int b=1;
int c;
for (int i=0;i<=x;i++){
System.out.println(fib(i));
}
}

static int fib(int x){

	if (x==0 || x==1){
	return x;
	}

	else{
	return fib(x-2)+fib(x-1);
	}
}


}
