import java.util.Scanner;
class binarysearch{
public static void main (String args[]){
int array[],x,y,i,first,last,mid;
System.out.println("input");
Scanner a=new Scanner(System.in);
x=a.nextInt();
array=new int[x];
System.out.println("input array");
for (i=0;i<x;i++){
	array[i]=a.nextInt();
	}

System.out.println("input search value");

y=a.nextInt();
first=0;
last=x;
mid=(last+first)/2;

while (first<=last){
	if (y<array[mid]){
	last=mid-1;
	}
	else if (y>array[mid]){
	first=mid+1;
	}
	else if (y==array[mid]){
	System.out.println(y+" is present at "+(mid+1));
	break;
	}
        mid=(last+first)/2;
        System.out.println(mid);
	}
if (first>last){
	System.out.print(y+" is not present");
	}
}
}

