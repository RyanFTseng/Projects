import java.util.Scanner;
class string3{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String x = in.nextLine();
System.out.println("input string 2");
String y = in.nextLine();
if (x.equalsIgnoreCase(y)==true){
System.out.println("Strings equal");
}
else{
System.out.println("Strings not equal");
}
}
}
