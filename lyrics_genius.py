import lyricsgenius

client_access_token = "kLxktps7zneNyDod1aF4g-Uy_RDBblfNvL-CK-aACZzVJ6dXNNhqgQLfq-v6q3od"

genius = lyricsgenius.Genius(client_access_token)

artist = genius.search_artists("Ariana Grande")
artist_id = artist["sections"][0]["hits"][0]["result"]["id"]
artist_img = artist["sections"][0]["hits"][0]["result"]["image_url"]
artist_name = artist["sections"][0]["hits"][0]["result"]["name"]
# print(artist)

# lyric search function
def lyric_search(phrase):
    lyric_search = genius.search_lyrics(search_term=phrase, per_page=1, page=1)
    song_title = lyric_search["sections"][0]["hits"][0]["result"]["title"]
    song_artist = lyric_search["sections"][0]["hits"][0]["result"]["primary_artist"]["name"]
    lyrics = genius.search_song(title=song_title, artist=song_artist)
    song_lyrics = lyrics.lyrics
    song_id = lyric_search["sections"][0]["hits"][0]["result"]["id"]
    song = genius.song(song_id=song_id)
    song_description = song["song"]["description"]["plain"]
    song_art_image_url = song["song"]["song_art_image_url"]
    return song_title, song_artist, song_lyrics, song_description, song_art_image_url

# print(lyric_search("can't leave rap alone the game needs me"))

# artist search function
def artist_search(artist):
    artist_info_dict = genius.search_artists(search_term=artist, per_page=1, page=1)
    artist_id = artist_info_dict["sections"][0]["hits"][0]["result"]["id"]
    artist_image_url = artist_info_dict["sections"][0]["hits"][0]["result"]["image_url"]

    # Number 1 method of finding songs for particular artist: brings back tracks that Kid Cudi is in (even ones he's not a primary
    # artist on --> should we get those search results back too?):

    # artist_songs = genius.artist_songs(artist_id=artist_id, sort="popularity")

    ## --> extension of Number 1 method (for loop): this will bring back tracks from above search where Cudi is the primary artist, but
    ## it yields less results as method Number 3 below

    # for song in artist_songs["songs"]:
        # if song["primary_artist"]["name"] == artist:
            # print(song)

    # Number 2 method of finding songs for particular artist: brings back tracks that are by Kid Cudi and also tracks that are
    # covers that other people did of Cudi's tracks --> don't think this is a good option:

    # artist_songs = genius.search_songs(search_term=artist)

    # Number 3 method of finding songs for particular artist: brings back 5 most popular tracks by artist -->
    # feel either this method of Number 1 will be the best methods

    artist_songs = genius.search_songs(search_term=artist, per_page=5, page=1)

    # this code could be some sort of "index" page for each artist's songs
    # besides index page we will have for users adding their own lyrics
    for song in artist_songs["hits"]:
        song_title = song["result"]["title"]
        song_artist_names = song["result"]["artist_names"]
        song_art_image_url = song["result"]["song_art_image_url"]
        print(song_title, song_artist_names, song_art_image_url)

    return

# *** function to define: when user clicks on song from list rendered in for loop above, bring them to individual song page
# with lyrics --> need song_id for this

# print(artist_search("Kid Cudi"))

# artist and song search function
def artist_and_song_search(title, artist):
    song_info = genius.search_song(title=title, artist=artist) # this search takes a second or two to run --> write code for 
    # letting user know that the song information/lyrics are loading...
    song_id = song_info.id
    song_lyrics = song_info.lyrics
    song = genius.song(song_id)
    song_description = song["song"]["description"]["plain"]
    song_artists = song["song"]["artist_names"]
    song_art_image_url = song["song"]["song_art_image_url"]
    song_title = song["song"]["title"]
    return song_title, song_artists, song_description, song_art_image_url, song_lyrics

# print(artist_and_song_search("Devil In A New Dress", "Kanye West"))

# song search
def song_search(title):
    song_info = genius.search_songs(search_term=title)

    for song in song_info["hits"]:
        song_artists = song["result"]["artist_names"]
        song_title = song["result"]["title"]
        song_art_image_url = song["result"]["song_art_image_url"]
        song_id = song["result"]["id"]
        print(song_artists, song_title, song_art_image_url, song_id)

    return

# *** function to define: when user clicks on song from list rendered in for loop above, bring them to individual song page
# with lyrics --> need song_id for this

# print(song_search("I Want You Around"))

# song render function (for artist + individual song search --> when user clicks on ind song in looped list of songs)
# general idea: more functionality added later when we start to include view functions and templates
def song_render(song_id):
    song = genius.song(song_id)
    lyrics = genius.lyrics(song_id)
    song_artists = song["song"]["artist_names"]
    song_description = song["song"]["description"]["plain"]
    song_art_image_url = song["song"]["song_art_image_url"]
    song_album = song["song"]["album"]["name"]
    return song_artists, song_album, song_art_image_url, song_description, lyrics

print(song_render(4308790))