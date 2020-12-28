import time

time = int(input('please input a time: '))
siblin = input("press 's' for sister or 'b' for brother: ").lower()
tv_show = input('please put in a TV show: ').lower()
first_color = input('your first color: ').lower()
second_color = input('your second color: ').lower()
# third_color = input('your third color: ').lower()
# fourth_color = input('your fourth color: ').lower()
chair = input('a type of chair: ').lower()
country = input('please enter a country').lower()
animal = input('please enter an Animal').lower()
parent = input("select 'f' for father or 'm' for mother: ").lower()
day = input('please enter a day: ').lower()
lunch_meat = input('enter the your favorite meat: ').lower()
game = input('please enter the name of video game: ').lower()
child = input("'b' for boy and 'g' for girl : ").lower()

if child.lower() == 'b':
    child = input("enter boy's name")
elif child.lower() == 'g':
    child = input("enter girl's name")

car_make = input('please enter the make of a car: ').lower()
number = int(input('enter a number: '))
number2 = int(input('enter another number: '))


if siblin.lower() == 's':
    siblin = 'Sister'
    he_or_she = 'she'
elif siblin.lower == 'b':
    siblin = 'Brother'
    he_or_she = 'he'
    
    
if parent.lower() == 'f':
    parent = 'father'
elif parent.lower() == 'm':
    parent = 'mother'
    

print(f"""It was {time} p.m. and my lazy old {siblin} had just woken up. As I watched my favourite T.V. show, {tv_show}, I sat down in my blue {chair}. When the show was over, I started flipping through the channels. The news caught my eye. I heard that a {animal} had been lost from the Central Zoo and was now roaming around in Cameroon. That was where I lived! I decided to tell my parents, but I thought that would worry them \n "Lunch!" called my {parent} from the kitchen. It was {day} so we were having {lunch_meat} sandwiches for lunch. After lunch, I watched my father play {game}. After that I decided to go call on {child}. But {he_or_she} was busy.\n"Bedtime!" called my father, "Tomorrow we're going to the Zoo!" The next morning I put on my green T-shirt and my jeans. I thought about what the people had said on the news. I started to get worried. When we got in the {car_make}, I asked, "How long will the ride be?" "At least {number} minutes." my mom answered. On the way there I saw the colours of {first_color} and {second_color} whisk by.\n"Oh no!" I gasped. "Stop the car!" SSSSSSCCCCCRRRRRREEEEEECCCCCCHHHHHHHH!!!!!!!!! "What is it honey?" asked my mom. "On the news it said that a {animal} was loose, and we just passed it!" "Oh honey, that's terrible!" my father said. "What should we do?" "Pick it up and bring it to the Zoo with us," I suggested. "Why don't we call the Zoo on my cell phone?" said my father. "We'll try anything, if it works," my mother said. My dad did so and the Central Zoo gave us {number2} dollars.  
""")
 