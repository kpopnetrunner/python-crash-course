# 22_user_albums.py

# 8-8. User Albums. Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album's artist and title. Once you have
# the information, call make_album() with the user's input and print the
# dictionary that's created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, songs=None):
    """Return an album's information formatted in a dictionary."""
    album_dictionary = {'artist_name': artist_name, 'album_name': album_title}
    if songs:
        album_dictionary['songs'] = songs
    return album_dictionary

# This is an infinite loop.
while True:
    print("\nPlease enter the name of an artist and album:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album_information = make_album(artist_name, album_title)
    print(album_information)
