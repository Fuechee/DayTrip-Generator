print("Hello, this is the Day Trip Generator! This will help plan your vacation.")
import random

#Destination                
destinations = ['Tokyo, Japan', 'Paris, France', 'Seoul, South Korea', 'Syndey, Australia', 'Honolulu, Hawaii', 'New York City, New York', 'Barcelona, Spain']
destination = random.choice(destinations)

yes = False

while yes == False:
    location = input(f'{destination} has been selected for your destination. Are you okay with this destination? Enter y/n: ')
    if location == 'y':
        print('Awesome, lets continue with deciding a mode of transportation.')
        yes == True
        break
    else:
        print('No worries, we can figure out another location.')

# #Transportation
transportations = ['Rental Car', 'Train', 'Rental Bike', 'Walking', 'Bus']
transportation = random.choice(transportations)

yes = False

while yes == False:
    location = input(f'{transportation} has been selected for your mode of transportation. Are you okay with this mode of transportaton? Enter y/n: ')
    if location == 'y':
        print('Awesome, lets continue with deciding a restaurant to dine in.')
        yes == True
        break
    else:
        print('No worries, we can figure out another mode of transportation.')

#Restaurants
tokyo_restaurants = ['Sukiyabashi Jiro Roppongi', 'Den', 'Bistro Shirube', 'Takahashi', 'Kanda Matsuya', 'Nigyocho Imahan', 'Kaneko Hannosuke']
paris_restaurants = ['Tawlet Paris', 'Bouche', 'Cafe de Luce', 'Collier de la Reine', 'Cafe Lignac', 'Substance', 'Le Mary Celeste']
seoul_restaurants = ['Na Jeong-sun Halmae Jjukkumi', 'Han Chu', 'Hanok Jip', 'Ejo', 'Balwoo Gongyang', 'Gwanghwamun Jip', 'Mapo Jeong Daepo']
syndey_restaurants = ['Quay', 'est.', 'Sydney Tower Buffet', "Tetsuya's", 'Bills', "Jamie's Italian Sydney", 'Rockpool Bar and Grill']
honolulu_restaurants = ['House Without A Key', "Merriman's", 'MW Restaurant', 'Mud Hen Water', 'The Pig and The Lady', "Helena's Hawaiian Food", 'Piggy Smalls']
new_york_restaurants = ['Burger Joint', 'The Halal Guys', 'Dommminique Ansel Bakery', 'Balthazar', "Katz's Delicatessen", 'Peter Luger Steak House', "Grimaldi's Pizza"]
barcelona_restaurants = ['Bar Canete', 'Martinez', 'Bar Brutal', 'Bodega La Puntual', 'Bar Morryssom', 'Parking Pizza', 'Salvaje']

restaurants = random.choice()

yes = False

while yes == False:
    location = input(f'{list_of_restaurants} has been selected. Are you okay with this restaurant? Enter y/n: ')
    if location == 'y':
        print('Awesome, lets continue with deciding a restaurant.')
        yes == True
        break
    else:
        print('No worries, we can figure out another restaurant.')


#Entertainment 
tokyo_entertainment = ['Shinjuku Gyoen National Garden', 'Ueno Park and Ueno Zoo', 'Gina District', 'Tokyo Skytree']
new_york_entertainment = ['Statue of Liberty', 'Central Park', 'Metropolitan Museum of Art', 'Time Square']
paris_entertainment = ['Eiffel Tower', 'Musee du Louvre', 'Cathedrale Notre-Dame de Paris', 'Avenue des Champs-Elysees']
seoul_entertainment = ['N Seoul Tower', 'Dongdaemun Design Plaza', 'Lotte World Tower', 'Gwangjang Market']
syndey_entertainment = ['Syndey Opera House', 'Sydney Harbour Bridge', 'Royal Botanic Garden Syndey', 'Bondi Beach']
honolulu_entertainment = ['Wakikiki Beach', 'Aloha Tower', 'USS Missouri Battleship', 'Polynesian Cultural Center']
barcelona_entertainment = ['Sagrada Familia', 'Park Guell', 'Las Ramblas', 'Parc de Montjic and Magic Fountain']

entertainment = random.choice()

#Confirming choices
confirm_choice = input('Please confirm to complete the trip setup. Enter y/n: ')
if confirm_choice == 'y':
    print(f'Your vacation plans will be going to ')

