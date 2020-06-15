class Ab{
int factorial(int n){
int x=n;
for (int i=1;i>n-1;i++){
	n=n*(x-1);
	x=x-i;
}
return(n);
}

public static void main(String args[]){
Ab fac= new Ab();

System.out.println(fac.factorial(5));
}
}
