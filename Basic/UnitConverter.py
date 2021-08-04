## Unit Converter App
import sys
choice = 0
def manu():
    print("*"*20 +" MANU "+"*"*20)
    print("Chose your Option: ")

    print("1 : Area")
    print("2 : Length")
    print("3 : Temperature")
    print("4 : Speed")
    print("5 : Mass")
    print("6 : Exit")
    

def area():
    acre = 0.0
    squre_meter = 0.0
    squre_feet = 0.0
    print("\nSelect Units To Convert:")

    print("1: Acres(ac) To Squre Meter(m^2)")
    print("2: Acres(ac) To Squre feet(ft^2)")
    print("3: Squre Meter(m^2) To Acres(ac)")
    print("4: Squre Meter(m^2) To Squre feet(ft^2)")
    print("5: Squre feet(ft^2) To Squre Meter(m^2)")
    print("6: Squre feet(ft^2) To Acres(ac)")
    print("7: Exit")
    area_choice = int(input("Enter Your Choice: "))

    if area_choice == 1:
        acre = float(input("\nEnter your area in Acres(ac): "))
        squre_meter = acre/0.00024711
        print("Your area in squre meter is:",round(squre_meter,3))
        print()
        area()
    
    elif area_choice == 2:
        acre = float(input("\nEnter your area in Acres(ac): "))
        squre_feet = acre * 43560
        print("Your area in squre feet is:",round(squre_feet,3))
        print()
        area()

    elif area_choice == 3:
        squre_meter = float(input("\nEnter your area Meter Square(m^2): "))
        acre = squre_meter *  0.00024711
        print("Your area in Acre(ac) is:",round(acre,5))
        print()
        area()
    
    elif area_choice == 4:
        squre_meter = float(input("\nEnter your area Meter Square(m^2): "))
        squre_feet = squre_meter *  10.764
        print("Your area in Squre feet is:",round(squre_feet,3))
        print()
        area()
    
    elif area_choice == 5:
        squre_feet = float(input("\nEnter your area Square feet(ft^2): "))
        squre_meter = squre_feet /  10.764
        print("Your area in Acre(ac) is:",round(squre_meter,3))
        print()
        area()

    elif area_choice == 6:
        squre_feet = float(input("\nEnter your area Square feet(ft^2): "))
        acre = squre_feet *  0.000022957
        print("Your area in Acre(ac) is:",round(acre,6))
        print()
        area()
    
    elif area_choice == 7:
        sys.exit()
    else:
        print("\nEnter correct Choice!! Try Again:")
        area()
    

manu()
choice = int(input("Enter Your Choice: "))
if choice == 1:
    area()

