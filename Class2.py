class multipleFunctions():
    def SubFields():
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print ("Sub-fields in AI are")
        for list in Lists:
            print (list)
            
    def OddEven():
        Num=int(input("Enter a Number="))
        if((Num%2)==0):
            print(Num," is a Even Number")
        else:
            print(Num," is a Odd Number")

    def eligible():
        gender = input("Enter your Gender=")
        age = int(input("Enter your Age="))
        if (gender=="Male" and age>= 21):
            print("ELIGIBLE")
            msg = "ELIGIBLE"
        elif (gender=="Female" and age>= 18):
            print("ELIGIBLE")
            msg = "ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            msg = "NOT ELIGIBLE"
        return msg

    def percentage():
        marks = [98,87,95,95,93]
        i=1
        total=0
        for subj in marks:
            print ("Subject",i,"=",subj)
            total=total+subj
            i=i+1
        print ("Total =", total)
        print ("Percentage=", total/len(marks))

    def triangle():
        Height = int(input("Height:"))
        Breadth= int(input("Breadth:"))
        print ("Area formula: (Height*Breadth)/2")
        print ("Area of Triangle: ", (Height*Breadth)/2)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth1= int(input("Breadth1:"))
        print ("Perimeter formula: Height1+Height2+Breadth")
        print ("Perimeter of Triangle:", Height1+Height2+Breadth1)
    