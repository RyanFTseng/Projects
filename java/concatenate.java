import java.util.Scanner;
class concatenate{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println("input string 2");
String y=in.nextLine();
System.out.println(x.concat(y));
}
}
