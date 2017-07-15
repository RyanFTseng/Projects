import java.util.Scanner;
class l{
public static void main(String args[]){
int x,i,max,min,j;
min=9999;
max=0;
System.out.println("input array size");
Scanner in = new Scanner(System.in);
x=in.nextInt();
int array[]=new int[x];
System.out.println("input elements");
for (i=0;i<x;i++){
        array[i]=in.nextInt();
        }
for (i=0;i<x;i++){
	if (array[i]>max)
		max=array[i];
}
for (i=0;i<x;i++){
	if (array[i]<min)
		min=array[i];
}
System.out.println("Largest number="+max);
System.out.println("Smallest number="+min);

}
}


