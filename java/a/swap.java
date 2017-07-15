import java.util.Scanner;
class swap{
public static void main (String args[]){
int x,y;
System.out.println("input");
Scanner in = new Scanner(System.in);
x=in.nextInt();
System.out.println("input");
y=in.nextInt();

x=x+y;
y=x-y;
x=x-y;



System.out.println(x);
System.out.println(y);

}
}
