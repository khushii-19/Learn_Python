def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")  

        #ye nhi chalta print agar finally likha h to he chelga even if the function returns tab bhi chalgea ye vrna return k baad koi  functin ni chalta

        



main()