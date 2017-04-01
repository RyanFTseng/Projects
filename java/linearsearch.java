import java.util.Scanner;
class linearsearch{
public static void main (String args[]){
int array[],x,y,i;
System.out.println("input");
Scanner a=new Scanner(System.in);
x=a.nextInt();
array=new int[x];

System.out.println("input");
for (i=0;i<x;i++){
	array[i]=a.nextInt();
	}






System.out.println("input search value");
//Scanner b=new Scanner(System.in);

 y=a.nextInt();

for (i=0;i<x;i++){
	//System.out.println(i);
	if (array[i]==(y)){
	System.out.println(y+ " is present at"+ (i+1));
	break;
	}

if (i==x)
System.out.println(y+" is not present at "+(i+1));
}
}
}

