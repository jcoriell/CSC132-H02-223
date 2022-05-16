public class ShapeTest {
    public static void main(String[] args){
        Rectangle r = new Rectangle(4, 3);
        r.draw();
        System.out.println(r); // calls the toString method

        Square mySquare = new Square(8);
        mySquare.draw();

        Triangle tea = new Triangle(6);
        tea.draw();

    }
}

//abstract classes can't be instantiated as objects
abstract class Shape{
    // instance variables
    // protected means accessible within this class and subclasses
    protected int length;
    protected int width;

    //private is only accessible within this class
    //private int aPrivateInstanceVariable;

    // constructor
    public Shape(int l, int w){
        length = l; 
        width = w;
    }

    // more than one constructor? yes.
    public Shape(){
        length = 1;
        width = 1;
    }

    public void draw(){
        for (int i=0; i < width; i++){
            for (int j=0; j < length; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // abstract methods (must be implemented in subclasses)
    //abstract void foo();

    public String toString(){
        String result = "";

        for (int i = 0; i < width; i++){
            for (int j=0; j < length; j++){
                result += "* ";
            }
            result += "\n";
        }
        result += "\n";

        return result;
    }

    // getters and setters
    public int getLength(){
        return length;
    }

    public void setLength(int value){
        length = value;
    }

}

// inheritance
// multiple inheritance can be faked with "interfaces" in java
class Rectangle extends Shape{

    public Rectangle(int l, int w){
        super(l, w);
    }

}

class Square extends Shape{

    public Square(int s){
        super(s, s);
    }

}

class Triangle extends Shape{

    public Triangle(int s){
        super(s,s);
    }

    public void draw(){
        for (int i=0; i < width; i++){
            for (int j=0; j < width - i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // TODO: implement toString()

}
