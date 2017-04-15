import java.util.Scanner;
class stringunicode{
public static void main (String args[]){
System.out.println("input string");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println(x);
int y=x.codePointAt(0);
int z=x.codePointAt(x.length()-1);
System.out.println(y);
System.out.println(z);
}
}



