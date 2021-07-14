print("Enter principle amount")
prn = float(input())
print("what is the rate of intrest")
rate = float(input())
print("How many years?")
year = int(input())
for time in range(1, year + 1, 1):
    i = prn * rate
    nb = i + prn
    print("year = " + str(time))
    print("starting amount was = " + str(prn))
    print("you're ending balence of the year is = " + str(nb))
    prn = nb
