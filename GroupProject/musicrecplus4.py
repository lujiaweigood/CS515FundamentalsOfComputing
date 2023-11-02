"""
Group Project Part 2
Date: Apr 12 2022
Authors: Deng Xiong, Gautham Prem Krishnan, Jiawei Lu
Group: 16

"""

import os.path

data = 'musicrecplus.txt'
# data1 = "musicrecplus_ex1.txt"
# data2 = "musicrecplus_ex2_a.txt"
# data3 = "musicrecplus_ex2_b.txt"

def main():
    """
    Loads database, the user and the preferences

    Parameters:
        None: main function
    
    Returns:
        None: data loaded

    """

    if os.path.isfile(data): # check if the file exists
        
        users = get_users(data) # will change the data1 to requried txt file.
        print('Welcome!')
        n1 = 'Enter your name (put a $ symbol after your name if you wish your preferences to remain private): '
        username = input(f"{n1}")
        if username not in users:
            enter_preferences(username, users) # update the data not file 
        # go to the menu
        menu_options(username, users, data)

    else: # If the file musicrecplus.txt does not exist upon starting the program, create it.
        print('Creating a txt file for the data......')
        file = open('musicrecplus.txt', 'w')
        file.close()
        print('Done. Please run the program again.')
    
def menu_display():
    """
    Displays the menu as required.

    Parameters:
        None: print the menu
    
    Returns:
        None: display complete

    """
    print('Enter a letter to choose an option:',
            'd - Delete preferences',
            'e - Enter preferences',
            'r - Get recommendations',
            'p - Show most popular artists',
            'h - How popular is the most popular',
            'm - Which user has the most likes',
            'q - Save and quit',
            's - The most up-to-date preference', sep = '\n')

def get_users(file_name):
    """
    Loads database, the user and the preferences

    @author: Deng

    Parameters:
        file: data txt file
    
    Returns:
        None: users data loaded

    """
    users = {} # with no duplicate users.
    file = open(file_name, 'r')
    for line in file:
        if not line:
            break
        [username, bands] = line.strip().split(":")
        band_list = bands.split(",")
        band_list.sort()
        users[username] = band_list
    file.close()
    return users

def menu_options(x, y, z): # I will finish this and upload it shortly
    """
    Proceeds the menu options based on the user input

    @author: Deng

    Parameters:
        x(str): username
        y(users): users
        z(txt): data
    
    Returns:
        None: option preceeds

    """
    
    while True:

        menu_display() # printOUT menu

        choice = input() # get user input

        if choice == 'e':
            enter_preferences(x, y)
        elif choice == 'd':
            print('This is going to delete the preferences in the file.')
            print("Unsaved information can't be deleted")
            
            try:
                delete_preferences(x,y,z)
            except KeyError:
                print('if you are a new user, you should save your preferences first.')
                
        elif choice == 'r':
            try:
                fix_bugs(z)
            except KeyError:
                print('There are no enough users to compare')

            recs = recommendations(x, y)
            if not recs:
                print('No recommendations available at this time')
            else:
                for rec in recs:
                    print(rec)
        elif choice == 'p':
            l, h = show_most_popular_artist(y) #likes hotlist
            if not h:
                print('Sorry, no artists found.')
            elif len(h) >= 3: # top 3
                print('The top3 artists:')
                for artist in h[:3]:
                    print(artist)
            else:
                print('The most popular artists:')
                for artist in h:
                    print(artist)
        elif choice == 'h':
            popular = how_popular_is_the_most_popular_artist(y)
            if not popular:
                print('Sorry, no artists found.')
            else:
                print(popular)
        elif choice == 'm':
            popular = which_user_likes_the_most_artists(y)
            if not popular:
                print('Sorry, no user found.')
            else:
                for user in popular:
                    print(user)
        elif choice == 'q':
            save_and_quit(y, z)
            break
        elif choice == 's':
            show_preference(y)
        elif choice == '\n':
            print('If you want to quit, enter q')
        else:
            print('Error: option missing', 'Please check the given options.', sep = '\n')
            

def enter_preferences(a, b):
    """
    Gets the user preference and save it to the database

    @author: Deng

    Parameters:
        a(str): username
        b(users): users
        
    
    Returns:
        None: preference got

    """
    pref = [] # preference
    while True:
        artist = input("Enter an artist that you like (Enter to finish): ")
        if not artist:
            break

        '''if the user entered artists “eminem”, “TMBG”, and “Kerkylas of Andros”, 
        the program will convert those to “Eminem”, “Tmbg”, and “Kerky- las Of Andros”. 
        So they will be stored in the file, and printed, in the converted form.'''

        art = artist.lower().title() # Artist names are standardized using “title case”
        if art in pref:
            print('You already entered this artist in your preferences. Try putting a new preference.')
            print('This program follows the title case standard. Ex. ee equals to Ee and EE')
            continue
        pref.append(art)
    
    pref.sort() # The artist list must in sorted order
    
    b[a] = pref # updates the user

def numMatches(a,b): # text book ch5 p161, p179
    """
    Returns the number of matches between two lists

    @author: Deng

    Parameters:
        a(list): a list
        b(list): b list
        
    
    Returns:
        int: the number of matches

    """
    # o(n) = n^2
    # count = 0
    # for x in a:
    #     if x in b:
    #         count += 1
    # return count

    # o(n) = nlogn
    a.sort()
    b.sort()
    count, i, j = 0, 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            count += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return count

def drop(a,b): # textbook p197
    """
    Returns a new list that contains only elements in list b that were not in list a

    @author: Deng

    Parameters:
        a(list): a list
        b(list): b list
        
    
    Returns:
        c(list): new list

    """

    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            c.append(b[j])
            j += 1
    while j < len(b): # append the rest
        c.append(b[j])
        j += 1
    return c

def findBestUser(a, b): # textbook p197
    """
    Finds the user whose tastes are closest to the current user except private users

    @author: Deng

    Parameters:
        a(str): username
        b(users): users
        
    
    Returns:
        bestUser(str): best user name

    """
    users = b.keys()
    bestUsers = []
    bestScore = 0
    for user in users:
        if user[-1] == '$':
            continue
        if b[user] == ['']:
            continue
        if b[user] != b[a]:
            cp, mp = b[user], b[a] # current and main preferences
            score = numMatches(cp, mp)
            if score > bestScore:
                bestScore = score
                bestUsers = [user]
            elif score == bestScore:
                bestUsers.append(user)
    return bestUsers

def recommendations(a,b): # textbook p197
    """
    Returns a recommended artists for a user

    @author: Deng

    Parameters:
        a(str): username
        b(users): users
        
    
    Returns:
        list: recommendation complete

    """
    bestUsers = findBestUser(a, b)
    
    new_list = []
    for user in bestUsers:
        new_list = new_list + drop(b[a], b[user])

    # remove duplicates
    l = []
    for i in new_list:
        if i not in l:
            l.append(i)
    
    l.sort()
    return l

def show_most_popular_artist(users):
    """
    Returns the most popular artist

    @author: Jiawei

    Parameters:
        b(users): users
        
    
    Returns:
        None: return most popular artist 

    """
    allPref = []
    for usr in users:
        allPref += users[usr]
    allPref = sorted(allPref)

    artistRank = {}  # {name1 : likes, name2 : likes, ...}
    currentArtist = ""
    for artist in allPref:
        if artist != currentArtist:
            currentArtist = artist
            artistRank[artist] = 0
        artistRank[artist] = artistRank[artist] + 1
    # print(artistRank)

    hotList = []
    likes = 0
    for artist in artistRank:
        if artistRank[artist] > likes:
            hotList = [artist]
            likes = artistRank[artist]
        elif artistRank[artist] == likes:
            hotList.append(artist)
    hotList = sorted(set(hotList))
    print((likes, hotList))
    return (likes, hotList)

def how_popular_is_the_most_popular_artist(users):
    """
    Returns the number of likes the most popular artist received

    @author: Jiawei

    Parameters:
        y(users): users
        
    
    Returns:
        None: just print or str: user

    """
    return show_most_popular_artist(users)[0]

def which_user_likes_the_most_artists(users):
    """
    Returns the full name(s) of the user(s) who like(s) the most artists.

    @author: Gautham

    Parameters:
        b(users): users
    
    Returns:
        str: user or (str)s: users or None: just print the username(s) i have put this in the menu
    """
    number_of_artist = 0
    user_list = []
    user_return=[]
    for username, artist_list in users.items():
        if username[-1] == '$':
            continue
        if users[username] == ['']:
            continue
        else:

            if username[-1] != '$' and len(artist_list) == number_of_artist:
                user_list.append(username)
            elif username[-1] != '$' and len(artist_list) > number_of_artist:
                number_of_artist = len(artist_list)
                user_list = [username]
                user_return.append(username)
    return user_return

def save_and_quit(b,c):
    """
    Returns the full name(s) of the user(s) who like(s) the most artists.

    @author: Gautham

    Parameters:
        b(users): users
        c(txt): data
        
    Returns:
        None: save the file and quit
    """
    # open(c, 'w').close()
    # data = open(c, 'r+')
    # for user in b:
    #     data.write(user+':'+b[user]+"\n")
    # data.close()
    

    # my suggesting coding according to textbook p199

    file = open(c, "w")
    for user in b:
        toSave = str(user) + ":" + ",".join(b[user]) + \
                    "\n"
        file.write(toSave)
    file.close() 
     

"""--------Following are the extras------"""

def delete_preferences(a,b,c):
    """
    Removes preferences from musicrecplus.txt

    Parameters:
        a(str): username
        b(dict): users
        c(txt): data file
    
    Returns:
        None: delete preference complete

    @author: Deng

    """
    # To start, a list of the user’s current preferences should be listed so that the user knows what can be deleted.
    print(b[a])
    # you can just have them type out the name exactly as it is presented.
    pref = b[a]
    while True:
        deletion = input('Please enter the preference you want to delete here: ')
        if not deletion or deletion not in pref:
            print('Not found')
            break
        
        for x in pref:
            if x == deletion: 
                b[a].remove(x)
    
    save_and_quit(b,c)

def show_preference(users):
    """
    
    @author: Jiawei

    """
    ret = []
    for key in users:
        ret.append((key,len(users[key])))
    ret.pop()
    if len(ret) == 0:
        print("No user found")
    else:
        for usr in sorted(ret):
            print(usr)

def fix_bugs(file):
    """
    Helper function for get recommendations bugs

    @author: Gautham

    """
    return len(get_users(file)) >= 1
        

if __name__ == '__main__':
    main()