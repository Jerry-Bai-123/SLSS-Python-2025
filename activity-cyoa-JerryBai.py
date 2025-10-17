from tkinter import Variable
import time
import sys

print("Your head is in pain, it feels like something is inside it...")
time.sleep(4)
print(
    "You got woke up by the noise of the radio in your house, all you can see is darkness..."
)
time.sleep(4)
print("It's noon but... where is the sun?... You think you should check your radio...")
time.sleep(4)


print("--- Cough from a man who sounds seriously injured ---")
time.sleep(2)
print("...heavy breathing...")
time.sleep(3)
print(
    "I don't know will anyone hear this but, something is happening...(Radio noise)...sun... people crawled out... Not human... DO NOT GO OUT"
)
time.sleep(3)
print(
    '"You will meet people... Let them get in if you can. Some wear human skins, but do not belong."'
)
time.sleep(3)
print('"They have... perfect teeth, muddy nails, red eyes..."')
time.sleep(3)
print('"................Radio Noises...................."')
time.sleep(4)
print(
    '"Whatever I said before is not true, Do not let anything get into your house. Lock your doors and windows, do no answer anything!  EVERYTHING IS FAKE! EVERYTHING IS FAKE! EVERYTHING IS FAKE! INCLUDING YOURSELF"'
)
time.sleep(4)
print("--- RADIO STATIC FADES ---\n")
time.sleep(2)


player_name = input("You recalled your name, your name is...")

health = 5
team_count = 1
friendship = 0
dog_saved = False
hidden_fake = 0
inspections_left = 2
day = 1
ammo = 1


print(f"\nAlways remember your name, {player_name}... \n")

# 1
print("You heared your dg coming back from te outside Do you:")
print("1) Let him in")
print("2) Everything is dangerous! Radio is right I should prevent any danger!")
first = input("Choose 1 or 2: ")

if first == "1":
    dog_saved = True
    friendship = friendship + 2
    team_count = team_count + 1
    print("\nYo let yoour dog in... It looks the same as always...")
else:
    print("\nYou didn't answer... Later it run away itself...")
time.sleep(2)
# 2
print("\nA weary, dirty old man approaches to your door. What do you do?")
print("1) Talk to them")
print("2) Keep silence and hold your gun steady at the door")
choiceA = input("Choose 1 or 2: ")

if choiceA == "1":
    # s1
    print(
        "\n'Please let me in. Everything is wrong outside, have you seen a human like creature tearing up a full squad of armed soldier? I've been living on the streats for like my entire ;ife but I've never seen something like that... EVER! I wanted some protection but they refused me... yeah who woud carry a burden now... If only im a bit younger... If only... If only... "
    )
    print(
        "After talking, you can: 1) Inspect from the peephole  2) Let him in  3) Refuse"
    )
    subA = input("Choose 1, 2 or 3: ")
    if subA == "1":
        inspections_left -= 1
        print("\nInspection: teeth not perfect, nails muddy, eyes red.")
        print("Do you now: 1) Recruit  2) Refuse")
        subA2 = input("Choose 1 or 2: ")
        if subA2 == "1":
            team_count = team_count + 1
            print("\nYou let him in...")
        else:
            print("\nYou refused. The old man stared at your door... and left")
    elif subA == "2":
        team_count = team_count + 1
        friendship = friendship + 1
        print("\nYou invited him in... He looks a bit too happy...who knows? ")
    else:
        print(
            "\nYou refused him. The old man started shouting and swearing infront of your door... Talking about how people like you make the society worse and about how nice people were when he was young.."
        )
else:
    print(
        "\nYou refused him. The old man started shouting and swearing infront of your door... Talking about how people like you make the society worse and about how nice people were when he was young.."
    )

time.sleep(2)

print("\nA quiet woman stands at the gate. She smiles in a soft, practiced way.")
print('She says: "I can cook, stitch, I can help...')
print("Do you: 1) Talk  2) Inspect from the peephole  3) Refuse")
c = input("Choose 1, 2 or 3: ")

if c == "1":
    print(
        "\nShe telled a story of her and her dead baby... It's a sad story but way too many people are dying now... You think you shoudn't let emotion affect your choice "
    )
    print("After talking: 1) Invite in  2) Inspect  3) Refuse")
    s = input("Choose 1, 2 or 3: ")
    if s == "1":
        team_count += 1

        hidden_fake += 1
        print(
            "\nYou let her in. She smiles like a neighbor. You do not notice the small smear under one nail."
        )
        print("Later you will worry if that smile was too patient...")
    elif s == "2":
        if inspections_left > 0:
            inspections_left -= 1
            print(
                "\nInspection result: Teeth look fine, a speck of mud on one fingernail, eyes red, perhaps from crying?..."
            )
            print(" Do you: 1) Invite 2) Refuse")
            s2 = input("Choose 1 or 2: ")
            if s2 == "1":
                team_count += 1
                hidden_fake += 1
                print("\nYou invite her. She still have the smile on her face...")
            else:
                print(
                    "\nYou refused her. She stared at the peephole for a really long time..."
                )
        else:
            print(
                "\nYou have no inspections left... You tried to inspect but your eyes are hurting.... Maybe less video games... "
            )
    else:
        print(
            "\nYou refuse. You refused her. She stared at the peephole for a really long time..."
        )
else:
    if c == "2":
        print(
            "\nFrom the peephole you see that her teeth look fine, a speck of mud on one fingernail, eyes red, perhaps from crying?... You are unsure..."
        )
        print("Do you open? 1) Yes  2) No")
        choice2 = input("Choose 1 or 2: ")
        if choice2 == "1":
            team_count += 1
            hidden_fake += 1
            print("\nYou open. She still have the smile on her face...")
        else:
            print(
                "\nYou keep closed. You refused her. She stared at the peephole for a really long time..."
            )
    else:
        print("\nYou refuse. She tilts her head and disappears into the dark street.")

time.sleep(2)


# 3
print(
    "\nA small boy stands by the fence with a ragged doll... He looks like he's going to cry..."
)
print('He asks with a watery eyes: "I...Im Tommy, may I get in?"')
print("Do you: 1) Talk  2) Inspect  3) Ignore")
c = input("Choose 1, 2 or 3: ")

if c == "1":
    print(
        '\nTommy\'s voice is trembling: "They came at night... and mommy told me to run...later she tried to find me...but I dont think that is my mommy... I dont know where to go... I have only this doll... I can give this doll to you if you let in"'
    )
    print("After talking: 1) Let him in  2) Inspect  3) Tell him find another house")
    s = input("Choose 1, 2 or 3: ")
    if s == "1":
        team_count += 1
        friendship += 4
        print(
            "\nYou take little Tommy inside. He gave his doll to you... You said he can keep it... He's looks happy..."
        )
    elif s == "2":
        if inspections_left > 0:
            inspections_left -= 1
            print(
                "\nInspection: Teeth normal, nails muddy, eyes red from crying?... You really don't know... "
            )
            print("Let him in? 1) Yes  2) No")
            s2 = input("Choose 1 or 2: ")
            if s2 == "1":
                team_count += 1
                friendship += 4
                print(
                    "\nYou take little Tommy inside. He gave his doll to you... You said he can keep it... He's looks happy..."
                )
            else:
                print("\nYou send him away. He leaves slowly, small footsteps fading.")
        else:
            print(
                "\nNo inspections left. Your eyes are hurtin... maybe less video games? Later Tmmy left"
            )
    else:
        print("\nYou send him away. He cried and later left")
else:
    print(
        "\nYou ignored him. He dragged his doll and left... The doll's head is missing later..."
    )

time.sleep(2)


# day2

day = day + 1
print(f"\nNight falls. It is now day {day}.")

if hidden_fake > 0:
    if team_count > 1:
        team_count -= 1
        print(
            "In the night you hear a muffled sound. One companion is gone by morning... You made a mistake..."
        )
    else:
        health -= 2
        print(
            "You were attacked alone at night... Luckily you got your gun under your pillow... That thing made a deep scratch on your chest and vanished in the dark..."
        )

time.sleep(1)
if day % 2 == 0:
    required = day
    print("\nA pale male stand infront of your door... and stared...")
    print(
        f"They expect at least {required} people with you. Your group has {team_count}."
    )
    if team_count < required:
        print(
            "He smiled a bit too wide... You dont think a person can do it...That's the last thought you had... "
        )
        health = 0
    else:
        print("He frowned and stared at the peephole for a realy long time...")

time.sleep(1)

if health <= 0:
    print(
        f"\nBAD ENDING: {player_name}, The house falls silent. You expected emptiness as death arrives, but for some reason, death gave you another chance... take it and try another time... just be extra careful this time..."
    )
    sys.exit()

if health > 0:
    print(
        "\nYou survived...The night was harsh... You feel tired but it's time to sleep."
    )

time.sleep(3)


inspections_left = 2

# 4
print("\nA strong male knocks")
print(
    'He says: "My guy lemme in, shit tuff outside. Im a enginneeer I can fix stuff you know, just em lemme in I can also fight the thing you know whtever they call it "'
)
print("Do you: 1) invite him  2) Inspect  3) Refuse")
c = input("Choose 1, 2 or 3: ")

if c == "1":
    team_count += 1
    friendship += 1
    print(
        "\nYou invite the man. He laughs out loud and gives you a big hug... You really don't think he can do anything to the fake humans though... Your only friend iis your gun...."
    )
elif c == "2":
    if inspections_left > 0:
        inspections_left -= 1
        print(
            "\nInspection: Teeth are bad, nails muddy, eyes faint red. He seems worn."
        )
        print("Do you invite? 1) Yes  2) No")
        s = input("Choose 1 or 2: ")
        if s == "1":
            team_count += 1
            friendship += 1
            print(
                "\nYou invite the man. He laughs out loud and gives you a big hug... You really don't think he can do anything to the fake humans though... Your only friend is your gun...."
            )
        else:
            print("\nYou refuse. He looks frustrated and stomped away...")
    else:
        print("\nNo inspections left. He smashed the door real hard... and left...")
else:
    print("\nYou stay in silence. He smashed the door real hard... and left...")

time.sleep(1)

# 5

print(
    "\nYour neighbor, a young female, arrives. She is perfectly polite, smiling like a postcard."
)
print(
    'She says: "Ive heard the radio and it says its better to stay together with big groups... May I join?"'
)
print("Do you: 1) Accept  2) Inspect  3) Refuse")
c = input("Choose 1, 2 or 3: ")

if c == "1":
    team_count += 1
    hidden_fake += 1
    print("\nYou welcome Claire... She keeps that smile on her face...")
elif c == "2":
    if inspections_left > 0:
        inspections_left -= 1
        print(
            "\nInspection: Teeth very tidy, slight red in eyes, nails clean... You feel like inspections are useless now... How do you keep them out?..."
        )
        print("Invite? 1) Yes  2) No")
        s = input("Choose 1 or 2: ")
        if s == "1":
            team_count += 1
            hidden_fake += 1
            print("\nYou let Claire in. Her smile will linger in your dreams.")
        else:
            print("\nYou refuse. She looks disappointed but leaves politely.")
    else:
        print("\nNo inspections left. She waits and vanished at the corner")
else:
    print("\nYou refuse. She tilts her head and walks away humming a happy tune.")

time.sleep(1)

# 6

print("\nA soldier, dusty and tired, he points his gun at your door...")
print(
    'He says: "Please. Let me in... that thing slaughtered us... 14 people... 14 armed people... only im left... I need to be in now! Open the fkin door! Now!"'
)
print("Do you: 1) Let him in  2) Inspect  3) kill")
c = input("Choose 1, 2 or 3: ")

if c == "1":
    team_count += 1
    friendship += 1
    print(
        "\nHe joins your group and mumbles... You don't understand what he's murmering... You think it's something about... sun?"
    )
elif c == "2":
    if inspections_left > 0:
        inspections_left -= 1
        print("\nInspection: Teeth normal, nails muddy, eyes red.")
        print("Invite? 1) Yes  2) No")
        s = input("Choose 1 or 2: ")
        if s == "1":
            team_count += 1
            friendship += 1
            print(
                "\nHe joins your group and mumbles... You don't understand what he's murmering... You think it's something about... sun?"
            )
        else:
            print(
                "\nHe listened patiently and left... Did he really believe no one's living here?"
            )
    else:
        print(
            "\nHe listened patiently and left... Did he really believe no one's living here?"
        )
else:
    print(
        "\nYou located his chest from the peephole and pulled the trigger... Sometimes... human is the most dangerous thing..."
    )

time.sleep(1)

# day3
print("\nNight again. You try to sleep but the house is full of quiet sounds.")
if hidden_fake > 0:
    if team_count > 1:
        team_count -= 1
        print(
            "A living person is gone... sometimes you wonder... a person, raised by a family for years and years...  is just gone so quietly and quicky..."
        )
    else:
        health -= 2
        print(
            "A white pale hand extended from the dark... Your gun saved you again... but this time you're bleeding... will you survive?..."
        )

time.sleep(1)


day = day + 1
print(f"\nIt is now day {day}. Another day passes.")
day = day + 1
print(
    f"\nNo one knocked on the door... You lost track of the time... Night falls. It is now day {day}."
)
time.sleep(1)

if day % 2 == 0:
    required = day
    print("\nThe male arrives again... With skin even more pale...stared at your house")
    print(
        f"He expect at least {required} people with you. Your group has {team_count}."
    )
    if team_count < required:
        print(
            "He smile and the world goes dark. The breaking soound of the door is the last thing you hear..."
        )
        health = 0
        if health <= 0:
            print(
                f"\nBAD ENDING: {player_name}, The house falls silent. You expected emptiness as death arrives, but for some reason, death gave you another chance... take it and try another time... just be extra careful this time..."
            )
            sys.exit()
    else:
        print("He frowned and vanished in the dark...")

time.sleep(1)


if hidden_fake > 0:
    if team_count > 1:
        team_count -= 1
        print(
            "A living person is gone... sometimes you wonder... a person, raised by a family for years and years...  is just gone so quietly and quicky..."
        )
    else:
        health -= 2
        print(
            "You can hear the thing... you don't have time to treat your wounds... it's getting worse..."
        )

time.sleep(1)


# endings

print("\nDeath's chosen one")
if health <= 0:
    print(
        f"\nBAD ENDING: {player_name}, The house falls silent. You expected emptiness as death arrives, but for some reason, death gave you another chance... take it and try another time... just be extra careful this time..."
    )
elif hidden_fake == 0 and team_count >= 4:
    print(
        f"\nBEST ENDING: {player_name}, you and others all decide to stay in the basement... Food and resouces are enough... and you lost track of the time... until the radio made a sound... saying the sun is up again"
    )
elif hidden_fake > 0 and health > 0:
    print(
        f"\nMIXED ENDING: {player_name}, you and others all decide to stay in the basement... but something is wrong... You expected emptiness as death arrives, but for some reason, death gave you another chance... take it and try another time... just be extra careful this time... "
    )
elif team_count >= 2 and health > 0 and hidden_fake == 0:
    print(
        f"\nNormal ENDING: {player_name}, you kept them out... but you also don't have a lot of people left... You'll need to keep getting more people in the house... and who knows how long it's going to last?"
    )
else:
    print(
        f"\nAlone ENDING: {player_name}, you survived alone... Death is only the matter of time..."
    )

print("There are 5 endings... wanna try to do all 5?")
