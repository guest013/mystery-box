import random

key = ("m","a","g","i","c")

def generate():
    digit = [random.randint(1,5) for i in range(5)]

    PIN = str(digit[0])+str(digit[1])+str(digit[2])+str(digit[3])+str(digit[4])
    code = key[0]*digit[0]+key[1]*digit[1]+key[2]*digit[2]+key[3]*digit[3]+key[4]*digit[4]
    return PIN, code

generate()
