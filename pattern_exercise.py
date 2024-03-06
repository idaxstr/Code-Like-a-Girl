fabric_options = ['cotton','linen','denim']
cotton_garments = ['tshirt','shorts']
linen_garments = ['dress','pants','skirt']
denim_garments = ['jeans','vest','jacket']

for fabric in fabric_options:
    print(fabric)

while True:
    fabric_choice = input('enter fabric choice: ')
    if fabric_choice not in fabric_options:
        print('invalid fabric choice')
        continue

    garment_choice = input('enter garment choice: ').lower()

    if fabric_choice == 'cotton' and garment_choice not in cotton_garments:
        print('nope')
        continue
    elif fabric_choice == 'linen' and garment_choice not in linen_garments:
        print('nope')
        continue
    elif fabric_choice == 'denim' and garment_choice not in denim_garments:
        print('nope')
        continue
    else:
        print(f'you are making a {fabric_choice} {garment_choice}')
    break
    
