import random

traits = ["Active","Ambitious", "Art Lover", "Bookworm", "Cheerful",
    "Childish", "Creative", "Clumsy", "Dance Machine", "Erratic",
    "Foodie", "Genius", "Geek", "Gloomy", "Goofball", "High Maintenacne",
    "Hot-Headed", "Loner", "Loves Outdoors", "Lazy", "Materialistic",
    "Neat","Paranoid", "Romantic", "Self-Assured", "Squeamish", "Slob",
    "Self-Assured", "Unflirty", "Maker", "Music Lover", "Recycle Disciple",
    "Adventurous", "Child of the Islands", "Child of the Ocean", "Freegan","Glutton", "Green Fiend", 
    "Kleptomaniac", "Lactose Intolerant", "Overachiever" , "Perfectionist", "Rancher","Vegetarian"
    ,"Animal Enthusiast","Bro","Cat Lover","Dog Lover" ,"Evil", "Family Oriented","Good", "Hates Children",
    "Horse Lover", "Insider", "Jealous", "Loyal", "Mean", "Noncomittal", "Outgoing","Party Animal","Proper",
    "Self-Absorbed", "Snob","Socially Awkward"]
aspirations = ["Animal (Friend of the Animals)",
    "Athletic (Body Builder)", "Athletic (Extreme Sports Enthusiast)",
    "Athletic (Championship Rider)", "Creativity (Painter Extraordinaire)"
    "Creativity (Musical Genius)", "Creativity (Bestselling Author)",
    "Creativity (Mastor Actor/Actress)", "Creativity (Master Maker)",
    "Creativity (Lord/Lady of the Knits)", "Deviance (Public Enemy)",
    "Devience (Chief of Mischief)", "Deviance (Villainous Valentine)",
    "Family (Successful Lineage)", "Family (Big Happy Family)", 
    "Family (Vampire Family)", "Family (Super Parent)", "Food (Master Chef)"
    , "Food (Master Mixologist)", "Food (Expert Nectar Maker)", "Food (Appliance Wiz)"
    , "Fortune (Fabulously Wealthy)", "Fortune (Mansion Baron)", "Fortune (Market Magnate)"
    , "Knowledge (Renaissance Sim)", "Knowledge (Nerd Brain)", "Knowledge (Computer Whiz)",
    "Knowledge (Master Vampire)", "Knowledge (Archaeology Scholar)", "Knowledge (Spellcraft & Sorcery)",
    "Knowledge (Academic)", "Love (Serial Romantic)", "Love (Soulmate)", "Location (City Native)",
    "Location (StrangerVille Mystery)", "Location (Beach Life)", "Location (Mt.Komorebi Sightseer)",
    "Nature (Freelance Botanist)", "Nature (The Curator)", "Nature (Angling Ace)", "Nature (Outdoor Enthusiast)", 
    "Nature (Jungle Explorer)", "Nature (Purveyor of Potions)", "Nature (Eco Innovator)", "Nature (Country Caretaker)",
    "Popularity (Joke Star)", "Popularity (Party Animal)", "Popularity (Friend of the World)",
    "Popularity (Neighborhood Confidante)", "Popularity (Leader of the Pack)", "Popularity (Good Vampire)", "Popularity (World Famous Celebrity)",
    "Wellness (Inner Peace)", "Wellness (Self-Care Specialist)", "Wellness (Zen Guru)", "Werewolf (Werewolf Initiate)", "Werewolf (Lone Wolf)" ]
colors = ["Black", "Red", "Blue", "Green", "Orange", "Brown", "Gray", "Yellow", "White", "Pink", "Purple"]
styles = ["Boho", "Buisness Casual", "Chic", "Streetwear","Egirl", "Goth", "Preppy", "Sporty","Buisness","Rock"]

def randtrait(list):
    traitone = random.choice(list)
    list.remove(traitone)
    traittwo = random.choice(list)
    list.remove(traittwo)
    traitthree = random.choice(list)
    list.remove(traitthree)

    print("Your Traits:",traitone,",",traittwo,",",traitthree,"\n")

def randasp(list):
    aspiration = random.choice(list)
    print("Your Aspiration:",aspiration,"\n")

def randcolor(list):
    color = random.choice(list)
    print("Your color theme is ",color,"\n" )

def randstyle(list):
    style = random.choice(list)
    print("Your style is ",style,"\n")



if __name__ == '__main__':
    print("Welcome to the Randomizer!\n")
    randtrait(traits)
    randasp(aspirations)
    randcolor(colors)
    randstyle(styles)
