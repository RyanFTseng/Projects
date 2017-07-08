interface A{
void a();
void b();
void c();
void d();
}

abstract class B implements A{
public void c(){System.out.println("c");}
}

class M extends B{
public void a(){System.out.println("a");}
public void b(){System.out.println("b");}
public void d(){System.out.println("d");}
}

class Test5{
public static void main (String args[]){
A a = new M();
a.a();
a.b();
a.c();
a.d();
}
}
