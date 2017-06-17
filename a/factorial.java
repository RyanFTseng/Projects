import java.util.Scanner;
class factorial{
public static void main (String args[]){
int i,x,j;
System.out.println("input");
Scanner in = new Scanner(System.in);
x=in.nextInt();
int y=x;
for (i=0;i<=y;i++){
	x=x*(y-1);
	y=y-1;
}
System.out.println(x);

}
}
