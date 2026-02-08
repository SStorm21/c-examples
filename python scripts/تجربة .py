import random
number_of_numbers = 7  
max_number = 100 
random_numbers = [str(random.randint(1, max_number)) for _ in range(number_of_numbers)]
solid_number = "".join(random_numbers)
print(solid_number) 
