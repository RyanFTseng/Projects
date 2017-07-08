class Animal{
void eat(){System.out.println("eating...");}
}
class dog extends Animal{
void bark(){System.out.println("barking...");}
}

class TestInheritance{
public static void main(String args[]){
dog d = new dog();
d.bark();
d.eat();
}
}
