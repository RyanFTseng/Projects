import java.util.Scanner;
class linearsearch{
public static void main (String args[]){
int array[],x,y,i,n;
System.out.println("input");
Scanner a=new Scanner(System.in);
x=a.nextInt();
array=new int[x];
n=0;
System.out.println("input");
for (i=0;i<x;i++){
	array[i]=a.nextInt();
	}

System.out.println("input search value");

y=a.nextInt();

for (i=0;i<x;i++){
	if (array[i]==(y)){
	System.out.println(y+ " is present at"+ (i+1));
	n=n+1;
	}

if (i==x){
System.out.println(y+" is not present at "+(i+1));
	}
System.out.println(n+" occurrences");
}
}
}

