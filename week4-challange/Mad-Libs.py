

   #User inputs
name = input("What is your name:")
age = int(input("How old are you:"))
city = input("what city do u live in:")
food = input("what is your favourite food:")
activity = input("Enter some activity here:")

   #conditional statment based on age
if age < 12:
   description = "a young lad"
elif 12 <= age <= 18:
   description = " explosive teenager"
elif 18 <= age <= 25:
   description = "an early adult"
else:
   decription = "an adult of great wisdom"   

   #conditional statements based on food
if food in ['Jellof Rice', 'Nkwobi', 'Ogbono Soup']:
   print("You are Nigerian")
elif food in ['Jambalaya', 'Buffalo wings', 'Lobster rolls']:
   print("You must be American")
elif food in ['Kimchi', 'Dim Sim', 'Sushi']:
   print("You must be asian")
else:
   print(f"{food} sounds nice, but i cant say where youre a native of 🥺")

   #conditional statememts based on city
if city in ['Abuja', 'Lagos', 'Kano', 'Enugu']:
   description = "a city in Nigeria"
elif city in ['New York', 'Los Angeles', 'Chicago', 'Miami']:
   description = "a city in the United States of America"
elif city in ['Jakarta','Beijing','Fukuoka','Shanghai']:
   description = 'an asian city'
else:
   print (f" {city} sounds cool, but i cant say where it is🦹🏼‍♂️")

   #mad Lib story based on user inputs
print("\nHere is your story:\n")
print(f"I've come across someone named {name}, just about {age} years old ,he seems like {description} and was such a joy to be with")
print(f"often times i get to meet people from {city} and ask them about the {food} there")
print(f"usually people from {city} would say the love to eat {food} and do some {activity} which is common in those places")

   #conditional statement based on activity
if activity in ['dancing', 'soccer','meditation']:
   print(f'everyone in {city} find {activity} aesthetically appealing')
elif activity in ['Holi','Great wall of China', 'origami']:
   print (f'asians bravery in {activity} and dedication makes them standout at whatsoever range')
