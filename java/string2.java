import java.util.Scanner;
class string2{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String x = in.nextLine();
System.out.println("input string 2");
String y = in.nextLine();
if (x.contains(y)==true){
System.out.println("strings share data");
}
else if (y.contains(x)==true){
System.out.println("strings share data");
}

else{
System.out.println("strings dont share data");
}
}
}
