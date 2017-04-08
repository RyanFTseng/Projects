import java.util.Scanner;
class stringindex{
public static void main (String args[]){
System.out.println("input string");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println("input index");
int i=in.nextInt();
System.out.println("input index 1");
int index=x.charAt(i);

System.out.println("The character at "+i+" is "+(char)index);
}
}

