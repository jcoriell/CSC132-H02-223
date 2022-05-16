public class Repetition {
    public static void main(String[] args){
        // while loops
        int i = 0;
        while (i < 10){
            System.out.println(++i);
            //i++;
        }

        // do while (always executes at least one time)
        int j = 10;
        do{
            System.out.println(j);
            j--;
        }
        while(j > 0);

        // for loops
        // general structure: for( initialization ; condition ; change)
        
        for (int k=0; k < 10; k++){
            System.out.println(k);
        }

        // incrementing by something other than 1
        for (int k=0; k < 10; k+=2){
            System.out.println(k);
        }

        // incrementing over two things
        // not the same as a nested for loop
        for (int m=0, n=0; m < 10 && n < 10; m++, n+=2){
            System.out.println("(" + m + "," + n + ")");
        }

        double[] mathConstants = new double[5];

        mathConstants[0] = 3.14159287; //pi
        mathConstants[1] = 2.71828; //e
        mathConstants[2] = 1.73; // sqrt(2)
        mathConstants[3] = 1.62; //phi (see golden ratio)

        // for each item 
        for (double d : mathConstants){
            System.out.print(d + " ");
        }
        System.out.println();

    }
}
