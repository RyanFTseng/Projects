import java.util.Scanner;
class beforeunicode{
public static void main (String args[]){
System.out.println("input string");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println(x);
int y=x.codePointBefore(1);
System.out.println("unicode before index 1 = "+y);
}
}

