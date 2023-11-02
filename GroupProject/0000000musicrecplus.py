"""
Group Project Part 2
Date: Apr 12 2022
Authors: Deng Xiong, Gautham Prem Krishnan, Jiawei Lu
Group: 16

"""

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
    users = users(data1)
    print('Welcome!')
    n1 = 'Enter your name (put a $ symbol after your name if you wish your preferences to remain private): '
    username = input(f"{n1}")
    if username in users:
        menu(username, users)
    else:
        preferences(username, users, data1)
    

def users(file_name):
    """
    Loads database, the user and the preferences

    Parameters:
        file: data txt file
    
    Returns:
        None: users data loaded

    """
    users = {}
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

def menu(x, y): # I will finish this and upload it shortly
    """
    Displays the menu

    Parameters:
        x(str): username
        y(users): users
    
    Returns:
        None: menu displayed

    """
    pass


def preferences(a, b, c):
    """
    Gets the user preference and save it to the database

    @author: Deng

    Parameters:
        a(str): username
        b(users): users
        c(txt): data
    
    Returns:
        None: preference got

    """
    pass

def recommendations(a,b):
    """
    Returns a recommended artists for a user

    @author: Deng

    Parameters:
        a(str): username
        b(users): users
        
    
    Returns:
        None: recommendation complete

    """
    pass

def show_most_popular_artist(users):
    """
    Returns the most popular artist

    @author: Jiawei

    Parameters:
        b(users): users
        
    
    Returns:
        None: recommendation complete

    """
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

    @author: Jiawei

    """
    print(show_most_popular_artist(users)[0])

def which_user_likes_the_most_artists(users):
    """
    
    @author: Gautham

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

def save_and_quit():
    """
    
    @author: Gautham

    """
    pass

"""--------Following are the extras------"""

def delete_preference():
    """
    
    @author: Deng

    """
    pass

def show_preference(users):
    """
    
    @author: Jiawei

    """
    print(users.items())

def fix_bugs():
    """
    Helper function for get recommendations

    @author: Gautham

    """
    pass

if __name__ == '__main__':
    main()
    print(show_most_popular_artist())