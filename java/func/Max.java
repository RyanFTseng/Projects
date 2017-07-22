
class Max{
int mx,m;
int max(a[]){
for (m=0;m<4;m++){
	if (a[m]>a[m+1])
	mx=a[m];
	else
	mx=a[m+1];
}
return mx;
}

public static void main(String args[]){
int a[]=new int[3];
a[0]=5;
a[1]=4;
a[2]=6;
Max q=new Max();
System.out.println(q.max(a[]));

}
}
