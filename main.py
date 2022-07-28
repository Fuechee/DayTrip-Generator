print("Hello, this is the Day Trip Generator! This will help plan your vacation.")
import random

#Destination     
def determine_location(list_of_locations):
    for location in list_of_locations:
        random.shuffle(destinations)
        confirm_choice = input(f'Will {location} work? Enter Y/N: ')
        if confirm_choice == 'Y':
            print('Okay, lets continue to decide your mode of transportation.')
            break
        elif confirm_choice == 'N':
            print('No worries, we can choose another destination.')
            
destinations = ['Tokyo', 'Paris', 'Seoul', 'Syndey', 'honolulu', 'New York', 'Barcelona']
determine_location(destinations)

# #Transportation
transportations = ['Rental Car', 'Train', 'Rental Bike', 'Walking', 'Bus']
transportation = random.shuffle(transportations)

#Restaurants
tokyo_restaurants = ['Sukiyabashi Jiro Roppongi', 'Den', 'Bistro Shirube', 'Takahashi', 'Kanda Matsuya', 'Nigyocho Imahan', 'Kaneko Hannosuke']
paris_restaurants = ['Tawlet Paris', 'Bouche', 'Cafe de Luce', 'Collier de la Reine', 'Cafe Lignac', 'Substance', 'Le Mary Celeste']
seoul_restaurants = ['Na Jeong-sun Halmae Jjukkumi', 'Han Chu', 'Hanok Jip', 'Ejo', 'Balwoo Gongyang', 'Gwanghwamun Jip', 'Mapo Jeong Daepo']
syndey_restaurants = ['Quay', 'est.', 'Sydney Tower Buffet', "Tetsuya's", 'Bills', "Jamie's Italian Sydney", 'Rockpool Bar and Grill']
honolulu_restaurants = ['House Without A Key', "Merriman's", 'MW Restaurant', 'Mud Hen Water', 'The Pig and The Lady', "Helena's Hawaiian Food", 'Piggy Smalls']
new_york_restaurants = ['Burger Joint', 'The Halal Guys', 'Dommminique Ansel Bakery', 'Balthazar', "Katz's Delicatessen", 'Peter Luger Steak House', "Grimaldi's Pizza"]
barcelona_restaurants = ['Bar Canete', 'Martinez', 'Bar Brutal', 'Bodega La Puntual', 'Bar Morryssom', 'Parking Pizza', 'Salvaje']

list_of_restaurants = tokyo_restaurants + paris_restaurants + seoul_restaurants + syndey_restaurants + honolulu_restaurants + new_york_restaurants + barcelona_restaurants
for restaurants in list_of_restaurants:
    if tokyo_restaurants == 'Tokyo':
        import random
        random.shuffle(tokyo_restaurants)
    elif paris_restaurants == 'Paris':
        import random
        random.shuffle(paris_restaurants)
    elif seoul_restaurants == 'Seoul':
        import random
        random.shuffle(seoul_restaurants)
    elif syndey_restaurants == 'Syndey':
        import random
        random.shuffle(syndey_restaurants)
    elif honolulu_restaurants == 'Honolulu':
        import random
        random.shuffle(honolulu_restaurants)
    elif new_york_restaurants == 'New York':
        import random
        random.shuffle(new_york_restaurants)
    elif barcelona_restaurants == 'Barcelona':
        import random
        random.shuffle(barcelona_restaurants)

#Entertainment 
# tokyo_entertainment = ['Shinjuku Gyoen National Garden', 'Ueno Park and Ueno Zoo', 'Gina District', 'Tokyo Skytree']
# new_york_entertainment = ['Statue of Liberty', 'Central Park', 'Metropolitan Museum of Art', 'Time Square']
# paris_entertainment = ['Eiffel Tower', 'Musee du Louvre', 'Cathedrale Notre-Dame de Paris', 'Avenue des Champs-Elysees']
# seoul_entertainment = ['N Seoul Tower', 'Dongdaemun Design Plaza', 'Lotte World Tower', 'Gwangjang Market']
# syndey_entertainment = ['Syndey Opera House', 'Sydney Harbour Bridge', 'Royal Botanic Garden Syndey', 'Bondi Beach']
# honolulu_entertainment = ['Wakikiki Beach', 'Aloha Tower', 'USS Missouri Battleship', 'Polynesian Cultural Center']
# barcelona_entertainment = ['Sagrada Familia', 'Park Guell', 'Las Ramblas', 'Parc de Montjic and Magic Fountain']

#Confirming choices
# confirm_choice = input('Please confirm to complete the trip setup. Enter y/n: ')

