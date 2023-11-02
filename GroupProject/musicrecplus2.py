"""
Group Project Part 2
Date: Apr 12 2022
Authors: Deng Xiong, Gautham Prem Krishnan, Jiawei Lu
Group: 16

"""

import os.path

data1 = "musicrecplus_ex1.txt"
data2 = "musicrecplus_ex2_a.txt"
data3 = "musicrecplus_ex2_b.txt"

def main():
    """
    Loads database, the user and the preferences

    Parameters:
        None: main function

    Returns:
        None: data loaded

    """
    if os.path.isfile('musicrecplus.txt'): # check if the file exists
        users = get_users(data1) # will change the data1 to requried txt file.
        print('Welcome!')
        n1 = 'Enter your name (put a $ symbol after your name if you wish your preferences to remain private): '
        username = input(f"{n1}")
        if username in users:
            menu_display()
            menu_options(username, users, data1)
        else:
            preferences(username, users)
    else: # If the file musicrecplus.txt does not exist upon starting the program, create it.
        file = open('musicrecplus.txt', 'w')
        file.close()

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
            "s - The most up-to-date preference', sep = '\n'")

def get_users(file_name):
    """
    Loads database, the user and the preferences

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

    Parameters:
        x(str): username
        y(users): users
        z(txt): data

    Returns:
        None: option preceeds

    """

    while True:

        choice = input() # get user input

        if choice == 'e':
            preferences(x, y)
        elif choice == 'd':
            delete_preference(x,y)
        elif choice == 'r':
            recs = recommendations(x, y)
            if not recs:
                print('No recommendations available at this time')
            else:
                for rec in recs:
                    print(rec)
        elif choice == 'p':
            popular = show_most_popular_artist(y)
            if not popular:
                print('Sorry, no artists found.')
            else:
                for artist in popular:
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
            show_preference()
        else:
            print('Error: option missing', 'Please check the given options.', sep = '\n')

def preferences(a, b):
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
        a = artist.lower().title() # Artist names are standardized using “title case”
        pref.append(artist)

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
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(b[a], b[user])
        if score > bestScore and user[-1] != '$' and a != user:
            if len(drop(b[a], b[user])):
                bestScore = score
                bestUser = user
    return bestUser

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
    bestUser = findBestUser(a, b)
    if bestUser:
        recs = drop(b[a], b[bestUser])
        return recs
    else:
        return []

def show_most_popular_artist(users):
    """
    Returns the most popular artist

    @author: Jiawei

    Parameters:
        b(users): users


    Returns:
        None: recommendation complete

    """
    artists = []
    most_popular = 0
    popular_score = {}
    for username, artists in users.items():
        for artist in artists:
            if artist in popular_score and username[-1] != '$':
                popular_score[artist] += 1
            elif artist not in popular_score and username[-1] != '$':
                popular_score[artist] = 1
    for score in popular_score.values():
        if score > most_popular:
            most_popular = score
    return most_popular

def how_popular_is_the_most_popular_artist(users):
    """
    Returns the number of likes the most popular artist received

    @author: Jiawei

    Parameters:
        y(users): users


    Returns:
        None: just print or str: user

    """
    print(show_most_popular_artist(users)[0])

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
    for username, artist_list in users.items():
        if username[-1] != '$' and len(artist_list) == number_of_artist:
            user_list.append(username)
        elif username[-1] != '$' and len(artist_list) > number_of_artist:
            number_of_artist = len(artist_list)
            user_list = [username]
    return username


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
    open(c, 'w').close()
    data = open(c, 'r+')
    for user in b:
        data.write(user+':'+b[user]+"\n")
    data.close()

    '''
    # my suggesting coding according to textbook p199

    file = open(c, "w")
    for user in b:
        toSave = str(user) + ":" + ",".join(b[user]) + \
                    "\n"
        file.write(toSave)
    file.close() 
    '''

"""--------Following are the extras------"""

def delete_preference(a,b,c):
    """
    Removes preferences from musicrecplus.txt

    Parameters:
        a(str): username
        b(users): users
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
        for i in range(len(pref)):
            if pref[i] == deletion:
                del pref[i]
    b[a] = pref
    save_and_quit(b,c)

def show_preference():
    """

    @author: Jiawei

    """
    pass

def fix_bugs():
    """
    Helper function for get recommendations

    @author: Gautham

    """
    pass

if __name__ == '__main__':
    main()