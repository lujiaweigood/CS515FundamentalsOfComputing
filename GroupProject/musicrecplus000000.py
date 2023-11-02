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
    users = user(data2)
    print('Welcome!')
    n1 = 'Enter your name (put a $ symbol after your name if you wish your preferences to remain private): '
    username = input(f"{n1}")
    if username in users:
        menu(username, users, data1)
    else:
        preferences(username, users, data1)


def user(file_name):
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


def menu(x, y, z):  # I will finish this and upload it shortly
    """
    Displays the menu

    Parameters:
        x(str): username
        y(users): users
        z(txt): data
    
    Returns:
        None: menu displayed

    """
    print('Enter a letter to choose an option:',
          'e - Enter preferences',
          'r - Get recommendations',
          'p - Show most popular artists',
          'h - How popular is the most popular',
          'm - Which user has the most likes',
          'q - Save and quit', sep='\n')

    while True:

        choice = input()  # get user input

        if choice == 'e':
            preferences(x, y, z)
        elif choice == 'r':
            recs = recommendations(x, y)
            if not recs:
                print('No recommendations available at this time')
            else:
                for rec in recs:
                    print(rec)
        elif choice == 'p':
            popular = most_popular_artist(y)
            if not popular:
                print('Sorry, no artists found.')
            else:
                for artist in popular:
                    print(artist)
        elif choice == 'h':
            popular = how_popular(y)
            if not popular:
                print('Sorry, no artists found.')
            else:
                print(popular)
        elif choice == 'm':
            popular = which_user(y)
            if not popular:
                print('Sorry, no user found.')
            else:
                for user in popular:
                    print(user)
        elif choice == 'q':
            save_and_quit(y, z)
            break
        else:
            print('Error: option missing', 'Please check the given options.', sep='\n')


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


def recommendations(a, b):
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


def most_popular_artist(users):
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


def how_popular(users):
    """

    @author: Jiawei

    """
    print(most_popular_artist(users)[0])


def which_user(users):
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


if __name__ == "__main__":
    main()
