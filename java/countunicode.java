import java.util.Scanner;
class countunicode{
public static void main (String args[]){
System.out.println("input string");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println(x);

int y=x.codePointCount(0,x.length());
System.out.println(y);
}
}

