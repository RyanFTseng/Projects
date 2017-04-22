import java.util.Scanner;
class bytearray{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String x = in.nextLine();
byte[] byte_arr=x.getBytes();
String new_str= new String(byte_arr);
System.out.println(new_str);
}
}
