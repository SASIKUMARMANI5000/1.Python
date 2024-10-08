class multifunction():
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<18.5): 
            print("Underweight") 
            message="Underweight" 
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message

    def OddEven():
        num=int(input("Enter the Number:"))
        if((num%2)==0):
            print("Even Number")
            message="Even Number"
        else:
            print("odd Number")
            message="odd Number"
        return message    