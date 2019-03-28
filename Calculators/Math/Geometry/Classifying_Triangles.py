#Instructions:
#Go the bottom of the file and edit the inputs for what you need done
#--------------------------------------------------------------------
nums = input("What are the numbers? Seperate each one with a comma\n")

lst_str = nums.split(",")
lst_int = []
for string in lst_str:
    integer = float(string)
    lst_int.append(integer)

def classify_triangle(lst):
    sorted_lst = sorted(lst)
    c = sorted_lst[0] ** 2
    a = sorted_lst[1] ** 2
    b = sorted_lst[2] ** 2
    if c == a + b:
        print("Triangle is a right triangles because:  " + str(c) + "=" + str(a) + "+" + str(b))
    elif c > a + b:
        print("Triangle is a obtuse triangle because:  " + str(c) + ">" + str(a) + "+" + str(b))
    elif c < a + b:
        print("Triangle is a acute triangle because:  " + str(c) + "<" + str(a) + "+" + str(b))
    else:
        print("Error")

classify_triangle(lst_int)
