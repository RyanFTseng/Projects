import java.util.Scanner;
class containstring{
public static void main (String args[]){
System.out.println("input string");
Scanner in=new Scanner(System.in);
String x=in.nextLine();
System.out.println("input string");
String y=in.nextLine();
if (x.contains(y)==true){
	System.out.println(y+" is in "+x);
	}
else{
	System.out.println(y+" is not in "+x);
	}


}
}

