class Ab{
int factorial(int n){
int x=1,i;

for ( i=1;i<=n;i++)
	x=x*i;

return x;
}

public static void main(String args[]){
Ab fac= new Ab();

System.out.println(fac.factorial(5));
}
}
