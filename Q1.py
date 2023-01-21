# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:22:23 2021

@author: Sadaf Pasha
"""
#Opening input files for entering the details and output file to show the BMI results.
def main():
    file1=open("input.csv", "a")
    file2=open("bmi.csv", "a")

    
    Name = input("Enter the your name")
    print("Name is:", Name, file=file1)

    Height = float(input("Enter your Height in centimeters:"))
    print("Height is:", Height, file=file1)

    Weight = float(input("Enter your Weight in kilograms:"))
    print("Weight is:", Weight, file=file1)

    print("\n",file=file1)

    Height = Height/100

    #Calculating the Body mass index
    BMI = float(Weight/(Height*Height))
    B = round(BMI,2)

    print("The BMI is:", B, file=file2)
    
    if B < 18.5:
        file2.write("Underweight\n")
        file2.write("\n")

    elif B >= 18.5 and B < 25:
        file2.write("Normal\n")
        file2.write("\n")

    elif B >= 25 and B < 30:
        file2.write("Overweight\n")
        file2.write("\n")
    else:
        file2.write("Obesity\n")
        file2.write("\n")



    file1.close()
    file2.close()




main()