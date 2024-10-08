class Assignments2():
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
          print(temp)
            
    def OddEven():
        num = int(input("Enter a number: "))
        if (num % 2) == 0:
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))
            
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=='Male'):
            if(age >=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gender=='Female'):
            if(age >18):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        else:
            print('INVALID INPUT DATA')

    def percentage():
            m1=int(input("Subject1= "))
            m2=int(input("Subject2= "))
            m3=int(input("Subject3= "))
            m4=int(input("Subject4= "))
            m5=int(input("Subject5= "))
            Total = m1+m2+m3+m4+m5
            print("Total : ",m1+m2+m3+m4+m5)
            Percent = (Total / 500) * 100
            print("Percentage : ",Percent)

    def triangle():
            Height=int(input("Height:"))
            breadth=int(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            print("Area of Triangle: ",(Height*breadth)/2)
            Height1=int(input("Height1:"))
            Height2=int(input("Height2:"))
            breadth=int(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triangle: ",Height1+Height2+breadth)