# Print ou the grade-school multiplication table up to 12x12

for number in range(1, 13):

    print(f"Table de {number}: ")

    for multiple in range(1, 13):
        print(f"{multiple} x {number} = {multiple * number}")
    
    print("================")


