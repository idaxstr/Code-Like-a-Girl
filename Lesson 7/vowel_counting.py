def vowel_counting(full_name):
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for character in full_name:
        if character in vowels:
            count += 1

    print(f'My full name is {full_name}')
    print(f'{full_name} has {count} vowels')


