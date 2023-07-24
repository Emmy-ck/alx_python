def convert_to_celsius(fahrenheit):
    temp = float((fahrenheit - 32) * 5/9)
    if temp == -40:
        return(int(temp))
    return temp