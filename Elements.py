#!/usr/bin/env python
'''Items required for StardewBingo'''

item_types = ["crop", "forigable", "fish", "gem", "mineral", "food", "tree"]
subtype = ["flower", "fruit", "vegitable", "ocean", "lake", "river", "beach"]
season = ["spring", "summer", "fall", "winter"]

class Item:
    '''An item that can be collected from stardew'''
    def __init__(self, type: str, subtype: str = NA, season: str = NA, artisan: bool):
        '''Type is the category of item from the item_types list. Subtype is only app;icable to some items (ie. ocean in fish or fruit in foregable). Only harvestable items have a season. Artisan is set to true if item can be used to make goods in kegs or preserves jars.'''
        self.type = type
        self.subtype = subtype
        self.season = season
        self.artisan = artisan
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


### Elements ###
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