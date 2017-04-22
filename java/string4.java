import java.util.Scanner;
class string4{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String str = in.nextLine();
int hash_code=str.hashCode();
System.out.println(hash_code);
}
}
