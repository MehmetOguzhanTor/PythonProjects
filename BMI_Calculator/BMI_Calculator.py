import argparse

def BMI_Calculator(Weight, Height): #Body mass index calculator
    Height = Height/100
    return Weight/(Height*Height)

def BMI_Analysis(BMI): #Analysing the BMI of the person
    if BMI <= 16:
        print("you are severely underweight")
    elif BMI <= 18.5:
        print("you are underweight")
    elif BMI <= 25:
        print("you are Healthy")
    elif BMI <= 30:
        print("you are overweight")
    else:
        print("you are severely overweight")

def main():
    parser = argparse.ArgumentParser(description='Calculate BMI and provide analysis.')
    parser.add_argument('-W', '--weight', type=float, help='Weight in Kg')
    parser.add_argument('-H', '--height', type=float, help='Height in centimeters')

    args = parser.parse_args()

    Weight = args.weight
    Height = args.height
    
    if Weight is None or Height is None:
        Weight = float(input("Enter your Weight in Kg: "))
        Height = float(input("Enter your height in centimeters: "))

    BMI = BMI_Calculator(Weight, Height) #Calculating the BMI of the person

    if BMI>0:
        print("your Body Mass Index is: ", BMI)
        BMI_Analysis(BMI)
    else:
        print("Please enter valid details.")

if __name__ == "__main__":
    main()
