string = input ("Ingrese la cadena => ")
new_string = ""
def count_string(string):
    global new_string
    if len(string) %2 != 0:
        for i in range(len(string), 0, -1):
            new_string = new_string + string[i]
    return new_string

print(count_string(string))        

