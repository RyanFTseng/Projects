class a{
void msg(){System.out.println("Hello");}
}
class b{
void msg(){System.out.println("Welcome");}
}
class c extends a,b{
public static void main(String args[]){
c obj = new c();
obj.msg();
}
}
