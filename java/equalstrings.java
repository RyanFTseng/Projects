import java.util.Scanner;
class equalstrings{
public static void main (String args[]){
	System.out.println("input string 1");
	Scanner a=new Scanner(System.in);
	String x=a.nextLine();
	System.out.println("input string 2");
	Scanner b=new Scanner(System.in);
	String y=b.nextLine();

int n=x.compareTo(y);
System.out.println(n);

if (x.equals(y)){
	System.out.println("equal strings");
}

else{
	System.out.println("strings not equal");
}

}
}
