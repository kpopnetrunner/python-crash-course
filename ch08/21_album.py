# 21_album.py

# 8-7. Album. Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are
# storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store
# the number of songs on an album. If the calling line includes a value for the
# number of songs, add that value to the album's dictionary. Make at least one
# new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, songs=None):
    """Return an album's information formatted in a dictionary."""
    album_dictionary = {'artist_name': artist_name, 'album_name': album_title}
    if songs:
        album_dictionary['songs'] = songs
    return album_dictionary

album_1 = make_album('TWICE', 'Twicetagram', '13')
album_2 = make_album('Itzy', 'Crazy in Love', '16')
album_3 = make_album('IU', 'Growing Up', '16')

print(album_1)
print(album_2)
print(album_3)
