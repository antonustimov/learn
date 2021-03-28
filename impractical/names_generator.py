""" bla-bla-bla docstring"""
import sys
import random
def main():
    first = ('Baby Oil1', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'",
             'Bowel Noises', 'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks',
             'Chad', 'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
             'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy',
             'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Сап', 'Oinks',
             'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Skidmark',
             'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
             'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston ’Jazz Hands’", 'Worms')
    second = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout',
              'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs',
              'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
              'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
              'Kingfish', 'Listenbee', "M’Bernbo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
              'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
              'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush',
              'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
              'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
              'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
              'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        first_name = random.choice(first)
        print('Welcome to funny names generator (like in film "Psych") \n \n')
        last_name = random.choice(second)
        print(f'{first_name} {last_name}', file=sys.stderr)
        user_choice = input('\n \n Wanna one more fn name? '
                            'press "Enter" for "Yes" and "N" for "No"')
        if user_choice.lower() == 'n':
            break


    print("Bye-bye!")

if __name__ == '__main__':
    main()
