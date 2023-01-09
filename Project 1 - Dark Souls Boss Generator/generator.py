"""System module."""
import sys,random


first = ('Asylum','Taurus','Bell','Moonlight','Capra','Gaping','Stray','Chaos Witch','Great Grey Wolf','Iron','Crossbreed','Ornsetein','Smough','Dark Sun',
         'Pinwheel','Gravelord','Seath','The Four','Ceaseless','Centipede','Firesage','Bed','Gwin','Sanctuary','Artorias','Black Dragon','Manus',
         "Executioner's",'Looking','the Skeleton','Flexible','Lost Sinner','Bellfry','Ruin','Royal Rat','Royal Rat','Scorpioness',
         "The Duke's Dear","Old Dragonslayer",'Covetous','Smelter','Old Iron King','Guardian','Demon of Song','Velstadt','Vendrick','Darklurker',
         'Dragonrider','Twin Dragonriders','Prowling Magnus','Giant Lord','Acient','Throne','Nashandra','Aldia','Elana','Sinh','Afflicted','Acient Soldier',
         'Cerah','Fume','Sir','Burnt','Aava','Lud','Zallen','Iudex','Vordt','Curse-Rotted','Crystal','Deacons','High Lord','Old','Pontiff','Yhorm','Aldrich',
         'Dancer','Dragonslayer','Oceiros','Champion','Lothric','Nameless','Demon Prince','Sister',"Champions's",'Gravetender','Halflight','Darkeater',
         'Slave Knight')

last = ('Demon','Gargoyles','Butterfly','Dragon','Quelaag','Sif','Golem','Priscilla','Gwyndolin','Nito','the Scaleless','Kings','Discharge','of Chaos',
        'Lord of Cinder','Guardian','the Abysswalker','Kalameet','Father of the Abyss','the Last Giant','the Pursuer','Chariot','Glass Knight','Lords',
        'Sentry','Sentinels','Vanguard','Authority','Najka','Freja','the Baneful Queen','The Rotten','The Royal Aegis','and Congreagation','Watcher',
        'Defender','Scholar of the First Sin','Squalid Queen','Slumbering Dragon','Graverobber','Varg','the Old Explorer','Knight','Alonne','Ivory King',
        "The King's Pet",'Gundyr','of the Boreal Valley','Greatwood','Sage','Abyss Watchers','of the Deep','Wolnir','Demon King','Sulyvahn','the Giant',
        'Devourer of Gods','Armour','the Consumed King','Younger Prince','Wyvern','King','Soul of Cinder','in Pain','from Below','Friede','Gravetender',
        'Prince','Greatwolf','Spear of the Church','Midir','Gael')


def generateBossName():
    firstName = random.choice(first)
    lastName = random.choice(last)

    bossName = f"[{firstName} {lastName}]\n\n"
    print(bossName, file=sys.stderr) #print boss name in red