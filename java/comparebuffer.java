import java.util.Scanner;
class comparebuffer{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println("input string buffer");
String y=in.nextLine();
StringBuffer a=new StringBuffer(x);
System.out.println(x.contentEquals(a));
System.out.println(x.contentEquals(y));
}
}
