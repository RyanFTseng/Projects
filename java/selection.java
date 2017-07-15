import java.util.Scanner;
class selection{
public static void main(String[] args){
int m,i,min,y,index,j;
System.out.println("input array size");
Scanner in=new Scanner (System.in);
m=in.nextInt();
System.out.println("input array elements");
int a[]=new int[m];
for (i=0;i<m;i++)
        a[i]=in.nextInt();
min=9999;
y=a[0];
index=0;
for (i=0;i<m-1;i++){
	min=i;
	for (j=i+1;j<m;j++)
        	if (a[j]<a[min])
		min=j;
	if (min!=i){
	index=a[i];
	a[i]=a[min];
	a[min]=index;}
}
for (i=0;i<m;i++)
        System.out.print(a[i]);

}
}




