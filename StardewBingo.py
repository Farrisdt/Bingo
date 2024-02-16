#!/usr/bin/env python
'''Creates a JSON list of 25 items to input into an online bingo game maker (bingosync.com).
Contents are decicated to videogame Stardew Valley.'''
from random import randrange, choice

flowers = ["Blue Jazz", "Tulip", "Poppy", "Summer Spangle", "Fairy Rose", "Sunflower"]
foreged_flowers = ["Sweet Pea", "Crocus"]

crop_veg = ["Cauliflower","Garlic","Green Bean","Kale","Parsnip","Potato", "Corn", "Hops", "Wheat", "Amaranth", "Artichoke", "Beet", "Bok Choy", "Radish", "Red Cabbage", "Eggplant", "Pumpkin", "Yam", "Tea Leaves", "Tomato", "Rice"]
foreged_veg = ["Fiddlehead Fern"]
GI_veg = ["Ginger", "Taro Root"]

crop_fruit = ["Strawberry", "Blueberry", "Hot Pepper", "Melon", "Starfruit", "Cranberry", "Grape", "Ancient Fruit", "Cactus Fruit", "Rhubarb"]
GI_fruit = ["Pineapple", "Qi Fruit"]
tree_fruit = ["Apple", "Apricot", "Cherry", "Orange", "Peach", "Pomegranate"]
GI_tree_fruit = ["Banana", "Mango"]
foreged_fruit = ["Blackberry", "Crystal Fruit", "Salmonberry", "Spice Berry", "Wild Plum", "Coconut"]

all_crops = crop_fruit + crop_veg + flowers
all_fruit = crop_fruit + tree_fruit + foreged_fruit
all_flower = flowers + foreged_flowers
all_veg = crop_veg + foreged_veg

other_forege = ["Sap", "Pine Cones", "Maple Seed", "Acorn", "Wild Horseradish", "Daffodil", "Leek", "Dandelion", "Spring Onion", "Hazelnut", "Winter Root", "Snow Yam", "Holly", "Cave Carrot"]
mushroom = ["Morel", "Common Mushroom", "Red Mushroom", "Chanterelle", "Purple Mushroom"]
GI_mushroom = ["Magma Cap"]
beach = ["Nautilus Shell", "Coral", "Sea Urchin", "Rainbow Shell", "Clam", "Cockle", "Mussel", "Oyster", "Seaweed"]
all_forege = foreged_flowers + foreged_fruit + foreged_veg + other_forege + mushroom + beach + ["Grape"]

tapped = ["Maple Syrup", "Oak Resin", "Pine Tar"]
animal_products = ["eggs", "duck eggs", "wool", "milk", "goats milk", "truffles"]

fish = ["Albacore", "Anchovy", "Blobfish", "Bream", "Bullhead", "Carp", "Catfish", 'Chub', "Dorado", "Eel", "Flounder", 'Ghostfish', 'Halibut', 'Herring', 'Ice Pip', 'Largemouth Bass', 'Lava Eel', 'Lingcod', 'Midnight Carp', 'Midnight Squid', 'Octopus', 'Perch', 'Pike', 'Pufferfish', 'Rainbow Trout', 'Red Mullet', 'Red Snapper', 'Salmon', 'Sandfish', 'Sardine', 'Scorpion Carp', 'Sea Cucumber', 'Shad', 'Slimejack', 'Smallmouth Bass', 'Spook Fish', 'Squid', 'Stonefish', 'Sturgeon', 'Sunfish', 'Super Cucumber', 'Tiger Trout', 'Tilapia', 'Tuna', 'Void Salmon', 'Walleye', 'Woodskip']
GI_fish = ['Lionfish', "Blue Discus"]

achievement_money = ["Greenhorn: earn 15000g", "Cowpoke: earn 50000g", "Homesteader: earn 250000g", "Millionaire: earn 1000000g", "Legend: earn 10000000g"]
achievement_shipping = ["Polyculture: Ship 15 of each crop", "Monoculture: Ship 300 of one crop", "Full Shipment: Ship every item"]
achievement_museum = ["A Complete Collection: Complete the Museum", "Treasure Trove: Donate 40 different items to the museum"]
achievement_help = ["Gofer: Complete 10 'Help Wanted' requests", "A Big Help: Complete 40 'Help Wanted' requests"]
achievement_friendship = ["A New Friend: Reach a 5-heart friend level with someone", "Best Friends: Reach a 10-heart friend level with someone", "The Beloved Farmer: Reach a 10-heart friend level with 8 people", "Cliques: Reach a 5-heart friend level with 4 people", "Networking: Reach a 5-heart friend level with 10 people", "Popular: Reach a 5-heart friend level with 20 people"]
achievement_food = ["Cook: Cook 10 different recipes", "Sous Chef: Cook 25 different recipes", "Gourmet Chef: Cook every recipe"]
achievement_house = ["Moving Up: Upgrade house once", "Living Large: Upgrade house twice"]
achievement_crafting = ["D.I.Y: Craft 15 diffrent items", "Artisan: Craft 30 diffrent items", "Craft Master: Craft every item"]
achievement_fishing = ["Fisherman: Catch 10 different fish", "Ol' Mariner: Catch 24 different fish", "Master Angler: Catch every fish", "Mother Catch: Catch 100 fish"]

bundles = [["Crafts Room", "Spring Foraging", "Summer Foraging", "Fall Foraging", "Winter Foraging", "Construction", "Exotic Foraging"],\
 ["Pantry", "Spring Crops", "Summer Crops", "Fall Crops", "Quality Crops", "Animal Bundle", "Artisan Bundle"],\
  ["Fish Tank", "River Fish", "Lake Fish", "Ocean Fish", "Night Fishing", "Crab Pot", "Speciality Fish"],\
  ["Boiler Room", "Blacksmith", "Geologist", "Adventurer"],\
   ["Bulletin Board", "Chef", "Dye", "Field Research", "Fodder", "Enchanter"],\
   ["Vault", "2,500", "5,000", "10,000", "25,000"]]

artisan_goods = ["honey", "wine", "pale ale", "beer", "mead", "cheese", "coffee", "green tea", "juice", "cloth", "mayonnaise", "oil", "pickles", "jelly", "aged roe", "sugar", "flour"]

buildings = ["barn and fill it", "big barn and fill it", "deluxe barn and fill it", "coop and fill it", "big coop and fill it", "deluxe coop and fill it", "fish pond and fill it", "mill", "shed", "big shed", "silo and fill it", "stable", "well", "all cabin types", "shipping bin"] #slime hutch
bach_men = ["Alex", "Elliott", "Harvey", "Sam", "Sebastian", "Shane"]
bach_women =["Haley", "Leah", "Maru", "Penny", "Abigail", "Emily"]

amount_range = ["15", "30", "50", "75", "100"]

item_types= [] #stardew item types


##Need to know
#grown/created vs. collected vs. randomly found(weapons, books, etc.)
#can make into artisan goods
#GI and level

class Item:
    '''An item that can be collected from stardew'''
    def __init__(self, type: str):
        self.type = type
class Challenge:
    '''Bingo goal'''
    def __init__(self, difficulty: int, ginger_island: bool=False):
        '''Difficulty is on a scale of 1 to 4, with 1 being easy and 4 being late game. Ginger_island is set to true for content that requires access to ginger island.'''
        ## Data ##
        self.diff = difficulty
        self.gi = Ginger_island

    ## Methods ##
    def generate_number(self):
        '''For Challenges Requireing Numbers'''
        number = (randrange(9)+1)*5
        return(number)


bingo_list = []
square = "Free Space"
while(len(bingo_list)<25):
    rand = randrange(6)
    #############################
    if rand == 0:
        #Crops/shipping
        croptions = all_crops + ["different flowers", "different vegitables", "different fruit", "Sweet Gem Berry"]
        other_croptions = ["Polyculture: Ship 15 of each crop", "Monoculture: Ship 300 of one crop", "quality", "Grow a giant crop", "tree"]
        crop_type = randrange(len(croptions)+30)-1
        if crop_type >= len(croptions):
            crop_type = choice(other_croptions)
            if crop_type == "quality":
                seasons_options = ["summer", "fall", "spring", "lots"]
                quality_options = ["lots", "gold quality", "silver quality"]
                season = choice(seasons_options)
                quality = choice(quality_options)
                if season == quality:
                    quality = "gold_quality"
                amount = choice(amount_range[:-1])
                if season == "lots":
                    amount = amount_range[amount_range.index(amount)+1]
                    square = f"Collect {amount} {quality} crops"
                elif quality == "lots":
                    amount = amount_range[amount_range.index(amount)+1]
                    square = f"Collect {amount} {season} crops"
                else: square = f"Collect {amount} {quality} {season} crops"
            elif crop_type == "tree":
                square = f"Harvest {randrange(5)+1} different fruit trees"
            else:
                square = crop_type                
        else:
            crop_type = croptions[crop_type]
            if(crop_type.startswith("different")):
                if(crop_type == "different flowers"):
                    crop_num = randrange(len(flowers))
                if(crop_type == "different vegitables"):
                    crop_num = randrange(len(all_veg))
                if(crop_type == "different fruit"):
                    crop_num = randrange(len(crop_fruit))
            else: crop_num = (randrange(10)+1)*10
            square = f"Ship {crop_num} {crop_type}"
    ################################
    if rand == 1:
        goods_options = ["D.I.Y: Craft 15 diffrent items", "Artisan: Craft 30 diffrent items", "Cook: Cook 10 different recipes", "Sous Chef: Cook 25 different recipes", "Have two buffs active at once", "Have 3 buffs active at once"]
        good = randrange(20)
        if good < 5:
            square = choice(goods_options)
        else:
            artisan = artisan_goods + tapped
            artisan = choice(artisan)
            amount = (randrange(1,5)*5)
            if(artisan == "honey"):
                flower = choice((flowers + ["any flower", ""]))
                square = f"Produce {amount} {flower} honey"
            if(artisan == ("wine" or "jelly")):
                frt = choice((all_fruit + ["any", "different"]))
                square = f"Produce {amount} {frt} {artisan}"
            if(artisan == ("juice" or "pickles")):
                veg = choice((all_veg + ["any", "different"]))
                square = f"Produce {amount} {veg} {artisan}"
            else:
                square = f"Produce {amount} {artisan}"
    ################################
    if rand == 2:
        friend_goals = ["A New Friend: Reach a 5-heart friend level with someone", "Reach level 1 friendship with 5 people", "Gofer: Complete 10 'Help Wanted' requests", "Get married", "Meet the Dwarf", "Put Lewis's shorts on display(grange or luau)", "Trigger a Marney and Mayor Lewis scandle scene", "Give a loved birthday gift", "Give a hated birtday gift", "Give someone the golden pumpkin", "Win the egg hunt", "Get the best Luau score", "Win the ice fishing competition", "Dance with someone at the flower dance", "Give a loved feast of the winter star gift", "Get the mermaids pearl at the night market", "Get caught digging in the trash by three different people in one day"]
        friend = choice(friend_goals)
        if friend == "Get married":
            girl = choice(bach_women)
            boy = choice(bach_men)
            rand = randrange(10)
            if(rand>8):
                square = "Move in Krobus"
            elif(rand>5):
                square = f"Marry {boy} or {girl}"
            else:
                square = f"Date {boy} or {girl}"
        else: square = friend
    ################################
    if rand == 3:
        option = choice(["museum", "bundle", "tools", "money"])
        if option == "bundle":
            bundle = choice(bundles)
            bundle_choice = randrange(len(bundle))
            if bundle_choice <2:
                bundle_choice = f"the {choice(bundle[1:])} bundle from the "
            elif bundle_choice == (len(bundle)):
                bundle_choice = ""
            else:
                bundle_choice = f"{bundle_choice} bundles from the "
            square = f"Complete {bundle_choice}{bundle[0]}"
        if option == "museum":
            museum = choice(["Treasure Trove: Donate 40 different items to the museum", "Collect 5 lost books", "donate", "Donate a bone artifact to the museum", "Donate 5 gems to the museum", "Break 25 geodes(any type)", "Break 5 omni geodes", "Break 5 frozen geodes", "Break 5 magma geodes"])
            if museum == "donate":
                square = f"Donate {randrange(1,8)*5} items to the museum"
            else: square = museum
        if option == "tools":
            tool_choice = choice(["upgrade", "Do not carry more than 3 tools", "no upgrade"])
            tool_quality = [" to copper", " to iron", " to gold", ""]
            if tool_choice == "upgrade":
                square = f"Upgrade {randrange(1,5)} tools{choice(tool_quality)}"
            if tool_choice == "no upgrade":
                square = f"Upgrade {randrange(3)} tools to {choice(tool_quality)}"
        if option == "money":
            square = choice((["Greenhorn: earn 15000g", "Cowpoke: earn 50000g", "Moving Up: Upgrade house once", "Living Large: Upgrade house twice", "build"]))
            if square == "build":
                square = f"Build a {choice(buildings)}"
    ################################
    if rand == 4:
        option = choice(["fishing", "mining", "foreging", "animals", "skills"])
        if option == "fishing":
            amount = (randrange(1,5)*5)
            location = choice(["ocean", "river", "lake", ""])
            quality= choice(["iridium quality", "gold quality", "silver quality", ""])
            if quality == "":
                square = f"Catch {amount} {choice(fish)}"
            else:
                square = f"Catch {amount} {quality} {location} fish"
        if option == "mining":
            option = choice(["level", "Complete a monster eradication goal", "One hit a slime", "weapon", "Die in the mines", "Find the stairs in less than 10 stones/monsters", "collect", "Create 50 copper bars", "Create 30 iron bars", "Create 10 gold bars"])
            if option == "level":
                square = f"Reach level {(randrange(1,21)*5)} of the mines"
            if option == "weapon":
                gear = ["shoes", "rings", "hats", "weapons"]
                square = f"Collect 15 {choice(gear)}"
            if option == "collect":
                ore = choice(["copper ore", "iron ore", "gold ore", "quartz"])
                square = f"Collect {choice(amount_range)} {ore}"
            else: square = option
        if option == "foreging":
            forigable = all_forege + ["any spring forege", "any summer forege","any fall forege","any winter forege", "any beach forege", "mushrooms"]
            forigable = choice(forigable)
            if (forigable.startswith("any") or (forigable == "Blackberry") or (forigable == "Salmonberry") or (forigable == "Grape")):
                amount = (randrange(1,5)*25)
            else:
                amount = (randrange(2,6)*5)
            square = f"Collect {amount} {forigable}"
        if option == "animals":
            square = f"Get 15 {choice(animal_products)}"
        if option == "skills":
            skill = randrange(6)
            if skill == 0:
                skill = choice(["mining", "farming", "foreging", "combat", "fishing"])
            else: skill = f"{skill} skills"
            lvl = randrange(3,6)
            if lvl == 5:
                square = f"Get a profession in {skill}"
            else: square = f"Get {skill} to level {lvl}"
    #Random###############################
    if rand >= 5:
        rando = choice(["Buy furniture from the traveling cart", "Have 15 tapped trees", "scarecrow", "Obtain a stardrop", "chest", "Collect 5 identical gems", "Collect 5 different gems", "Pass out at 2AM", "Complete one billboard quest", "Beat stage 1 of Prarie King","Don't move any furniture", "Don't use the TV", "Don't buy seeds from Pierre", "Don't go into Pierre's", "Fell a tree with bombs", "Grow 10 of every basic tree", "Skip a full season"])
        if(rando == "scarecrow"):
            crownum = randrange(6)+1
            if crownum == 6:
                crownum = choice(["the turnip head", "the witch", "the snowman", "the girl", "the racoon"])
            square = f"Collect {crownum} rarecrow"
        elif(rando == "chest"):
            chests = ["fish", "gems and minerals", "forigables", "flowers", "artisan goods", "trash", "crops", "green items", "red items", "blue items", "orange items", "yellow or gold items", "purple items", "pink items", "white or cream items", "grey or silver items"]
            square = f"Fill a chest with {choice(chests)}"
        else:
            square = rando
    if not square in bingo_list:
        bingo_list.append(square)
        if square == "Free Space":
            print (rand)

### Print JSON formated list to terminal ###
outstr = "["
temp = ""
for i in range(len(bingo_list)):
    f = "{" + f'"name": "{bingo_list[i]}"' + "}"
    outstr += str(f)
    if not i == len(bingo_list)-1:
        outstr += ",\n"
    else:
        outstr += "]"
    #print(bingo_list[i]) #used for plain text bingo sites
print(outstr)