def generate_cube_numbers_beginner(limit):
    number = 2 
    while True:
        cube = number * number * number  
        if cube < limit:
            yield cube  
            number = number + 1  
        else:
            return  
