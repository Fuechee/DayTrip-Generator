print("This is the Day Trip Generator! If you aren't sure about your vacation plans, the generator will help you with planning.")
import random

#Destination                
destinations = ['Tokyo, Japan', 'Paris, France', 'Seoul, South Korea', 'Syndey, Australia', 'Honolulu, Hawaii', 'New York City, New York', 'Barcelona, Spain']

yes = False

while yes == False:
    destination = random.choice(destinations)
    location = input(f'{destination} has been selected for your destination. Are you okay with this destination? Enter y/n: ')
    if location == 'y':
        print('Awesome, lets continue with deciding a mode of transportation.')
        yes == True
        break
    else:
        print('No worries, we can figure out another location.')

# #Transportation
transportations = ['using a rental car', 'going on a train', 'using a rental bike', 'walking', ' using a bus']

yes = False

while yes == False:
    transportation = random.choice(transportations)
    mode_of_transportation = input(f'{transportation} has been selected for your mode of transportation. Are you okay with this mode of transportaton? Enter y/n: ')
    if mode_of_transportation == 'y':
        print("Awesome, let's continue with deciding a restaurant to dine in.")
        yes == True
        break
    else:
        print('No worries, we can figure out another mode of transportation.')

#Restaurants
japan_restaurant = ['Sukiyabashi Jiro Roppongi', 'Den', 'Bistro Shirube', 'Takahashi', 'Kanda Matsuya', 'Nigyocho Imahan', 'Kaneko Hannosuke'] 
new_york_restaurant = ['Burger Joint', 'The Halal Guys', 'Dommminique Ansel Bakery', 'Balthazar', "Katz's Delicatessen", 'Peter Luger Steak House', "Grimaldi's Pizza"]
france_restaurant = ['Tawlet Paris', 'Bouche', 'Cafe de Luce', 'Collier de la Reine', 'Cafe Lignac', 'Substance', 'Le Mary Celeste']
korea_restaurant = ['Na Jeong-sun Halmae Jjukkumi', 'Han Chu', 'Hanok Jip', 'Ejo', 'Balwoo Gongyang', 'Gwanghwamun Jip', 'Mapo Jeong Daepo']
australia_restaurant = ['Quay', 'est.', 'Sydney Tower Buffet', "Tetsuya's", 'Bills', "Jamie's Italian Sydney", 'Rockpool Bar and Grill']
hawaii_restaurant = ['House Without A Key', "Merriman's", 'MW Restaurant', 'Mud Hen Water', 'The Pig and The Lady', "Helena's Hawaiian Food", 'Piggy Smalls']
spain_restaurant = ['Bar Canete', 'Martinez', 'Bar Brutal', 'Bodega La Puntual', 'Bar Morryssom', 'Parking Pizza', 'Salvaje']

confirmed_restaurants = japan_restaurant, new_york_restaurant, france_restaurant, korea_restaurant, australia_restaurant, hawaii_restaurant, spain_restaurant

yes = False

def determine_restaurant(destination,confirmed_restaurant):
    if destination == "Tokyo, Japan":
        confirmed_restaurant = random.choice(japan_restaurant)
    elif destination == "Paris, France":
        confirmed_restaurant = random.choice(france_restaurant)
    elif destination == "Seoul, South Korea":
        confirmed_restaurant = random.choice(korea_restaurant)
    elif destination == "Syndey, Australia":
        confirmed_restaurant = random.choice(australia_restaurant)
    elif destination == "Honolulu, Hawaii":
        confirmed_restaurant = random.choice(hawaii_restaurant)
    elif destination == "New York City, New York":
        confirmed_restaurant = random.choice(new_york_restaurant)
    elif destination == "Barcelona, Spain":
        confirmed_restaurant = random.choice(spain_restaurant)
    return confirmed_restaurant

while yes == False:
    restaurant = input(f'{determine_restaurant(destination, confirmed_restaurants)} has been selected as your restaurant. Are you okay with this restaurant? Enter y/n: ')
    if restaurant == 'y':
        print("Awesome, let's continue with deciding a entertainment activity.")
        yes == True
        break
    else:
        print('No worries, we can figure out another restaurant.')

confirmed_restaurant = determine_restaurant(destination, confirmed_restaurants)

#Entertainment 
japan_entertainment = ['Shinjuku Gyoen National Garden', 'Ueno Park and Ueno Zoo', 'Gina District', 'Tokyo Skytree']
new_york_entertainment = ['Statue of Liberty', 'Central Park', 'Metropolitan Museum of Art', 'Time Square']
france_entertainment = ['Eiffel Tower', 'Musee du Louvre', 'Cathedrale Notre-Dame de Paris', 'Avenue des Champs-Elysees']
korea_entertainment = ['N Seoul Tower', 'Dongdaemun Design Plaza', 'Lotte World Tower', 'Gwangjang Market']
australia_entertainment = ['Syndey Opera House', 'Sydney Harbour Bridge', 'Royal Botanic Garden Syndey', 'Bondi Beach']
hawaii_entertainment = ['Wakikiki Beach', 'Aloha Tower', 'USS Missouri Battleship', 'Polynesian Cultural Center']
spain_entertainment = ['Sagrada Familia', 'Park Guell', 'Las Ramblas', 'Parc de Montjic and Magic Fountain']

confirmed_entertainments = japan_entertainment, new_york_entertainment, france_entertainment, korea_entertainment, australia_entertainment, hawaii_entertainment, spain_entertainment

yes = False

def determine_entertainment(destination, confirmed_entertainment):
    if destination == "Tokyo, Japan":
        confirmed_entertainment = random.choice(japan_entertainment)
    elif destination == "Paris, France":
        confirmed_entertainment = random.choice(france_entertainment)
    elif destination == "Seoul, South Korea":
        confirmed_entertainment = random.choice(korea_entertainment)
    elif destination == "Syndey, Australia":
        confirmed_entertainment = random.choice(australia_entertainment)
    elif destination == "Honolulu, Hawaii":
        confirmed_entertainment = random.choice(hawaii_entertainment)
    elif destination == "New York City, New York":
        confirmed_entertainment = random.choice(new_york_entertainment)   
    elif destination == "Barcelona, Spain":
        confirmed_entertainment = random.choice(spain_entertainment) 
    return confirmed_entertainment

while yes == False:
    restaurant = input(f'{determine_entertainment(destination, confirmed_entertainments)} has been selected as your entertainment activity. Are you okay with this entertainment activity? Enter y/n: ')
    if restaurant == 'y':
        print("Awesome, let's continue confirming your vacation plan.")
        yes == True
        break
    else:
        print('No worries, we can figure out another activity.')

confirmed_entertainment = determine_entertainment(destination, confirmed_entertainments)

#Confirming choices
print("The Day Trip Generator has finished creating your day trip. Now let's confirm that this is the trip you wanted.")
print('The trip we have generated for you is: ')
print(f'Destination: {destination}')
print(f'Transportation: {transportation}')
print(f'Entertainment: {confirmed_entertainment}')
print(f'Restaurant: {confirmed_restaurant}')
confirm_choice = input('Would you like to finalize this trip? Enter y/n: ')
if confirm_choice == 'y':
    print(f'Your vacation plans will be going to {destination}, and will be {transportation}. You will be spending your day touring {confirmed_entertainment} and will be ending your night, dining at {confirmed_restaurant}.')
else:
    print('No worries, we can go back and look over the choices again.')





