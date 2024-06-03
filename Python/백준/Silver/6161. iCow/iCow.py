def play_icow(N, T, ratings):
    played_songs = []

    for _ in range(T):
        # Find the song with the highest rating
        max_rating = max(ratings)
        song_to_play = ratings.index(max_rating)
        
        # Record the song to be played
        played_songs.append(song_to_play + 1)
        
        # Set the rating of the played song to zero
        played_song_rating = ratings[song_to_play]
        ratings[song_to_play] = 0
        
        # Distribute the points of the played song
        if N > 1:
            distribute_points = played_song_rating // (N - 1)
            remainder = played_song_rating % (N - 1)
            
            for i in range(N):
                if i != song_to_play:
                    ratings[i] += distribute_points
            
            # Distribute the remainder points
            for i in range(N):
                if i != song_to_play and remainder > 0:
                    ratings[i] += 1
                    remainder -= 1

    return played_songs

# Read input
N, T = map(int, input().split())
ratings = [int(input()) for _ in range(N)]

# Get the sequence of songs played
result = play_icow(N, T, ratings)

# Output the result
for song in result:
    print(song)
