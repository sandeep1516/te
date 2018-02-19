feets=int(input("number of feets :"))
if feets>100:
    print("high rates applied ")
elif feets<100:
    print("normal rates applied")
price_of_feet=int(input("enter price of feet :"))
casing=int(input("number of casing :"))
if casing>20:
    print("high rates applied ")
elif casing<20:
    print("Normal rates applied")
else :
     print("Normal rates applied")  
price_of_casing=int(input("enter price of casing :"))
Transport=int(input("Enter transport Charges :"))
Labour=int(input("Enter labourCharges :"))
sum=(feets*price_of_feet)+(casing*price_of_casing)+(Transport)+(Labour)
print(sum)
