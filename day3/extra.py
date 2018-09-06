def custom_missing_number(list):
    missing_numbers = []
    pointer = min(list)
    max_pointer = max(list)
    count = max(list)

    # finding missing number in list 
    while count > 0:
        if not pointer in list and pointer < max_pointer:
            missing_numbers.append(pointer)
        
        pointer = pointer + 1
        count = count - 1
    
    print(missing_numbers)
    return missing_numbers
       