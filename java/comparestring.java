import java.util.Scanner;
class comparestring{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println("input string 2");
String y=in.nextLine();
if (x.contentEquals(y)==true){
	System.out.println(x+" = "+y);
	}
else{
	System.out.println(x+" != "+y);
	}

}
}
