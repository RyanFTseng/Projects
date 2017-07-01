abstract class Bike{
abstract void run();
}
class car extends Bike{
void run(){System.out.println("running safely...");}
public static void main (String args[]){
Bike obj = new car();
obj.run();
}
}
