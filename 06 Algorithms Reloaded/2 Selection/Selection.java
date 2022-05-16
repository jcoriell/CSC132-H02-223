

class IfElse{

    public static void main(String[] args){
        double score = 85.0;
        char letterGrade;

        letterGrade = calcLetterGrade(score);
        System.out.println(letterGrade);
        
    }

    public static char calcLetterGrade(double value){
        if (value >= 89.5){
            return 'A';
        }
        else if (value >= 79.5){
            return 'B';
        }
        else if (value >= 69.5){
            return 'C';
        }
        else if (value >= 59.5){
            return 'D';
        }
        else{
            return 'F';
        }
        
    }
}

// switch example
class SwitchExample{
    public static void main(String[] args){
        char letterGrade = 'A';
        String feedback;
        String feedbackFallThrough;

        feedback = determineFeedback(letterGrade);
        feedbackFallThrough = determineFeedbackWithFallThrough(letterGrade);
        System.out.println(feedback);
        System.out.println(feedbackFallThrough);

    }


    public static String determineFeedback(char grade){
        // grade is the 'condition'. 
        // these conditions are restricted to certain data types
        switch (grade){
            case 'A': //<- colon
                String name = "Josh";
                return "Excellent Job " + name; 
            case 'B': return "Great Job";
            case 'C': return "Good Job";
            case 'D': return "It's ok.";
            case 'F': return "Maybe next time";
            default: return "Not a valid grade";
        }
    }

    public static String determineFeedbackWithFallThrough(char grade){
        switch (grade){
            case 'A':                       // returns case of B. This is called fall through
            case 'B': return "Great Job";
            case 'C': return "Good Job";
            case 'D': 
            case 'F': return "Maybe next time";
            default: return "Not a valid grade";
        }
    }
}