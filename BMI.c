#include <stdio.h>

float CalcBMI(float weight, float hieght);
float CalcBMI20(float weight, float height);

int main(){
    float height, weight;
    int age;
    printf("Let's Calculate your BMI.\n");
    printf("First Enter your age : ");
    scanf("%d", &age);

    if ( age < 2){
        printf("You dont need BMI.");
        return 1;
    }

    printf("\n");
    printf("Enter your height in Metres : ");
    scanf("%f", &height);
    if( height > 3.00){
        height = (height/100);
    }
    printf("Enter your weight in Kilograms : ");
    scanf("%f", &weight);

   
    if (age > 2 && age <= 20){
       float bmi = CalcBMI20( weight, height);
        printf("Your BMI is : %f\n", bmi);
    } 
    else if(age > 20){
        float bmi = CalcBMI( weight, height);
        printf("Your BMI is : %f\n", bmi);
    }

    return 0;

}

float CalcBMI20(float weight, float height ){
    if (height < 0){
        printf("ENTER VALID HEIGHT.");
        return 0;
    }
float BMI = (weight/(height * height));

  if(BMI <= 18.2){
    printf("Underweight\n");
  }
  else if ( BMI > 18.2 && BMI <= 25.6){
    printf("Normal\n");
  }
  else if ( BMI > 25.6){
    printf("Obese");
  }
 return BMI;
}

float CalcBMI(float weight, float height){
    if (height < 0){
        printf("ENTER VALID HEIGHT.\n");
        return 0;
    }
    float BMI = (weight/(height * height));
    
    if (BMI <= 16){
        printf("You are Severely Thin. Eat FOOD you skinny.\n");
        
    }
    else if ( BMI > 16 && BMI <= 17){
        printf("You are Moderatly Thin. Get your daily protien intake.\n");
        
    }
    else if (BMI > 17 && BMI <= 18.5){
        printf("You are Thin. Eat FOOD.\n");
        
    }
    else if(BMI > 18.5 && BMI <=25){
        printf("You are perfectly normal. Don't forget yo maintain it with regular exercise.\n");
        
    }
    else if( BMI > 25 && BMI<= 30){
        printf("Slightly Overweight. Going out and having a walk will help reduce that.\n");
        
    } 
    else if (BMI > 40){
        printf("Get off that chair and run.\n");
    }
    return BMI;
}