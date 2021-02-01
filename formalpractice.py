import random
import time
from japanese import(Character, Set, User)

print('Japanese Character test by Yuhan Zhou')

def create_anslst(train, a):
    """To create a list with the random-selected character's romaji and 3 other random selected romaji.

    Set, num -> lst"""
    lst = []
    characters = train.getCharacters()
    lst.append(characters[a].getRomaji())
    while len(lst) < 4:
        b = random.randint(0,45)
        if characters[b].getRomaji() not in lst:
            lst.append(characters[b].getRomaji())
    random.shuffle(lst)
    return lst

def test(lst, train, a):
    """To let the user answer from the list of 4 choices
    and return whether the answer is correct or not.

    lst, Set, num -> str"""
    characters = train.getCharacters()
    print("1:",lst[0],"\n2:",lst[1],"\n3:",lst[2],"\n4:",lst[3])
    inpt = eval(input('> '))
    while inpt not in (1,2,3,4):
        print("Invalid choice. Please choose again.")
        inpt = eval(input('> '))
    if lst[inpt - 1] == characters[a].getRomaji():
        return "Correct!"
    else:
        characters[a].addTimewrong()
        return "Wrong. The correct answer is " + characters[a].getRomaji()
        
        
def writefile(filename, user, finish, start, t1):
    """To write a file that contains the information of user's test result
    including time entry, userid, characters got wrong, time taken.

    str, User, float, float, float -> None """
    try:
        with open (filename,'a') as f:
            f.write('\n')
            f.write(time.strftime('%Y-%m-%d-%H %I:%M',t1))
            f.write('\n')
            f.write(user.getUserid())
            f.write('\n')
            f.write('The character you got wrong:\n')
            for char in sorted(user.getTestedcharacters(), reverse = True):
                if char.getTimewrong() > 0:
                    f.write(str(char) + '\t')
                    f.write(str(char.getTimewrong()) + ' times\n')
            f.write('Time taken：%.2f sec\n' % (finish-start))
            
    except OSError:
        print("There is an error with the filename.")
    
def main():
    """
    The main function of this program:
    Record local and start time.
    Create User according to input.
    Choose for test mode.
    Run the test of a character with 4 choices of prounounciation 50 times.
    Write the log of test in file. 
    

    None -> None"""
    t1 = time.localtime(time.time())
    start = time.time()
    
    userid = input("Please enter your user id: ")
    user = User(userid)
    
    print('''Please choose the mode for practice:
            1: Hiragana
            2: Katakana
            3: Mixed ''')
    choice = eval(input("> "))
    
    while choice not in (1,2,3):
        print('Invalid choice. Please choose again.')
        choice = eval(input("> "))
        
    train = Set(userid)
    characters = train.getCharacters()
    
    if choice == 1:
        for i in range(50):
            a = random.randint(0,45)
            print('The pronunciation of', characters[a].getHiragana(),'is:')
            print(test(create_anslst(train, a), train, a))
            if characters[a] not in user.getTestedcharacters():
                user.addTestedcharacters(characters[a])
            
    elif choice == 2:
        for i in range(50):
            a = random.randint(0,45)
            print('The pronunciation of', characters[a].getKatakana(),'is:')
            print(test(create_anslst(train, a), train, a))
            print()
            if characters[a] not in user.getTestedcharacters():
                user.addTestedcharacters(characters[a])
            
    else:
        for i in range(50):
            a = random.randint(0,45)
            b = random.randint(1,2)
            if b == 1:
                print('The pronunciation of', characters[a].getKatakana(),'is:')
            else:
                print('The pronunciation of', characters[a].getHiragana(),'is:')
            print(test(create_anslst(train, a), train, a))
            print()
            if characters[a] not in user.getTestedcharacters():
                user.addTestedcharacters(characters[a])
            
    finish = time.time()
    print('\nCongratualtion! You have completed one test!' )
    print('Time taken：%.2f sec\n' % (finish-start))
    filename = "Training Log"
    writefile(filename, user, finish, start, t1)
    
main()

        

