oddno = [num for num in range(1,50,2)]
cubes = list(map(lambda x: x**3, oddno))
print("Cubes of odd numbers:")
print(cubes)
divByThree=list(filter(lambda x: x%3 ==0,oddno))
print("Numbers divisible by 3: ", divByThree)