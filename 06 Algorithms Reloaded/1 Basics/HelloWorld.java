// one public class per file (no more)
// the public class has to match the file name
// public makes the class available outside of this package
public class HelloWorld{
    /*
        Block comment
    */

    // public (before a method/function) makes this method accessible outside the class
    /* private (in place of public, but not here)...
    ...makes the method only accessible in the class itself */
    // static - there is only one, its the same for all instances of this class
    // void means the function returns nothing.
    // 'main' is the name of the function
    // String[] means an array of strings
    public static void main(String[] args){ 
        // the above line is a special signature for the main function in your class
        System.out.println("Hello World");

    }
}

class VariablesAndConstants{

    public static void main(String[] args){
        // variables. must declare the type with the variable name
        int a = 5;
        int b = 3;

        System.out.println(a + "+" + b + "=" + (a+b));

        System.out.println("Without Paren:" + a + "+" + b + "=" + a+b);
        
        // Formatting (like in python ?)
        // Use %s  for a string 
        // %d for anytype
        // See format specifiers for others
        System.out.println(String.format("a = %s", a));
        System.out.println(String.format("a = %d, b=%s", a, b));

        // the word final makes a variable constant.
        final int THIS_IS_A_CONSTANT = 10;
        System.out.println(THIS_IS_A_CONSTANT);

        // can declare without a value;
        int c;
        c = 15;
        System.out.println(c);
    }

}

class DataTypeExamples{

    public static void main(String[] args){
        int a;
        float numberPointZero; // floats are 32 bit
        double bigNumberPointZero; // doubles are 64 bit
        String textTextText;    // must use double quotes for a string
        char aSingleCharacter; // use single quotes for a char - ex: 'A'
        boolean trueFalse;

        // nope:
        //float example = 1.5; <- the number 1.5 is a double.

        // double example - the literal on the right is a double
        bigNumberPointZero = 38726943.25748;
        System.out.println(bigNumberPointZero);

        // casting a literal double to a float
        numberPointZero = (float) 1.5;

        // assigning a float to a float
        numberPointZero = 1.5f;

        textTextText = "Hi this is a string";

        trueFalse = true;

        aSingleCharacter = 'H';

        System.out.println(aSingleCharacter);
    }

}

// Arrays 
// arrays here are traditional arrays. 
// fixed in size
// type of data in them is uniform
class ArrayExample{
    public static void main(String[] args){
        // initialization
        int x;  // <- for a variable
        int[] y; // <- creates an array of integers

        // creation of an array of specific size
        double[] nums = new double[10];
        System.out.println(nums);
        System.out.println(nums[0]);
        System.out.println(nums.length);    // getting the length

        nums[0] = 'A';
        System.out.println(nums[0]);

        int[] grades = {80, 95, 90, 1};//* this is only an example not actual grades
        String[] names = {"Eduardo", "Carson", "Daniel", "Jacob"};

        System.out.println(names[3] + " is number " + grades[3]);

    }
}


// Operators
class ArithmeticOperators {
    // + addition
    // - subtraction
    // * multiplication
    // 5/2  integer division
    // 1f / 2   float division
    // (float) 1 / 2  float division -> 0.5
    // (double) 1/2  
    // %   mod
    // Math.pow(2, 3)   2 to the power of 3
    
}

class RelationalOperators{
    // ==   equality
    // inequality
        // greater than   >
        // greater than or equal to   >=
        // less than is < 
        // less than or equal to <=
        // != is not equal to
}

class LogicalOperators{
    // && for AND
    // || for OR
    // ! for NOT
}

class BitwiseOperators{
    // bitwise and &
    // bitwise or is |
    // bitwise xor  ^
    // bitwise not ~
    // left shift <<
    // right shift >>
}

class PrefixAndPostfixOperators{

    public static void main(String[] args){
        int i = 0;
        int j = 0;
        int result_i;
        int result_j;

        // the postfix operator i++ 
        // increments the variable by 1 
        // ANNNNNNNNNDDDDDDD it returns the variable BEFORE the change
        result_i = i++; 

        // the prefix operator ++i
        // increments the variable by 1
        // ANNNDDDDDDD it returns the result AFTER the change
        result_j = ++j;

        System.out.println(i);
        System.out.println(j);
        System.out.println(result_i);
        System.out.println(result_j);

    }
}

