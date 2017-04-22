import java.util.Scanner;
class chararray{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String str = in.nextLine();
char[]arr=new char[] {' ' ,' ',' ',' ',' ',' ',' ',' '};
str.getChars(4,10,arr,2);
System.out.println(str);
}
}
