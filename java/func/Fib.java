class Fib{
void fibb(int n){
int i,a,b,c;
a=0;
b=1;
//System.out.println(a);
//a=1;
for (i=0;i<n;i++){
	System.out.println(a);
	c=a;
	a=b;
	b=c+a;
	}
}
public static void main(String args[]){
Fib f=new Fib();
f.fibb(10);
}
}
