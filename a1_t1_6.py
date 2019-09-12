def f_to_k(f):


    k = (f - 32) * 5/9 + 273.15
    return k

f = 48.0
k = f_to_k(f)

print("fahrenheit of" + str(f) + "is" + str(k) + "in fahrenheit")
