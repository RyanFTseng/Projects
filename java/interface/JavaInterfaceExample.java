interface IntExample{
public void sayHello();
}

public class JavaInterfaceExample implements IntExample{
public void sayHello(){
System.out.println("hello");
}

public static void main(String args[]){
JavaInterfaceExample javaInterfaceExample=new JavaInterfaceExample();
javaInterfaceExample.sayHello();
}
}
