lst1 = [int(item)for item in input("Enter the list items:" ).split()]
sum_of_elements = sum(lst1)
n = len(lst1)
index = n//2

def mean():
    mean_of_num = sum_of_elements/n
    print(f"The mean of the set of numbers is {mean_of_num}")

mean()

print("  ")

def median():
    lst1.sort()
    median1 =(lst1[index])
    median2= (sum((lst1[index-1:index+1]))/2)

    if n%2 ==1:
        print(f"The median of the set of numbers is {median1}")
    else:
        print(f"The median of the set of numbers is {median2}")  
    
    

median()

print(" ")
def variance():
    average = sum_of_elements/n
    c =[(x-average)**2 for x in lst1]
    sum_of_squares = sum(c)
    value_of_variance = sum(c)/n
    print(f"The variance of the set of numbers is: {value_of_variance}")


variance()

print(" ")

def stddev():
    average = sum_of_elements/n
    c =[(x-average)**2 for x in lst1]
    sum_of_squares = sum(c)
    value_of_variance = sum(c)/n
    std_dev = value_of_variance**0.5
    print(f"The standard deviation of the set of numbers is :{std_dev}")


stddev()


print(" ")

def skewness():
    average = sum_of_elements/n
    c =[(x-average)**2 for x in lst1]
    sum_of_squares = sum(c)
    value_of_variance = sum(c)/n
    std_dev = value_of_variance**0.5
    median1 =(lst1[index])
    median2= (sum((lst1[index-1:index+1]))/2)

    skewness1 = (3* (average-median1))/(std_dev)
    skewness2 = (3* (average-median2))/(std_dev)

    if n% 2 == 1:
        print(f"The skewness of the set of numbers is {skewness1}" )
    else:
        print(f"The skewness of the set of numbers is {skewness2}")

skewness()


    


    






    












