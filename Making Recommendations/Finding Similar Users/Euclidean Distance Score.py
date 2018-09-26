online_music = {
    'Donald':{'Taylor Swift':3.5,'Rihanna':3.0,'Justin Bieber':4.0},
    'Chandler':{'Taylor Swift':3,'Rihanna':3.5,'Justin Bieber':4.5},
    'Ruby':{'Rihanna':5.0,'Justin Bieber':2.0,'Demi Lovato':3.5, 'MJ':3.0},
    'Zoya':{'Taylor Swift': 3.0, 'Rihanna':2.0, 'Justin Bieber':4.0,'Demi Lovato':3.0},
    'Sam': {'Rihanna':3.0, 'Justin Bieber':3.5, 'MJ':4.0},
    'Robert': {'Rihanna':1.0,'Justin Bieber':2.5,'Demi Lovato':2.5}
}

import math

def euclidean_distance_score(music_data, person1, person2):
    music_1 = music_data[person1]
    music_2 = music_data[person2]

    sum_of_square = 0
    for key in music_1:
        if key in music_2:
            sum_of_square += (music_1[key]-music_2[key]) ** 2

    return 1/(math.sqrt(sum_of_square) + 1)

Donald_similar = []
for x in online_music:
    if x != 'Donald':
        Donald_similar.append((x, euclidean_distance_score(online_music, 'Donald', x)))

Donald_similar.sort(key=lambda u: u[1], reverse=True)

print(Donald_similar)