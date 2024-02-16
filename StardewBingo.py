#!/usr/bin/env python
'''Creates a JSON list of 25 items to input into an online bingo game maker (bingosync.com).
Contents are decicated to videogame Stardew Valley.'''
from random import randrange, choice
impoty Elements

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