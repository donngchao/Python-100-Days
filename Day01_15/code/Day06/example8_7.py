# encoding: utf-8
'''
@author: developer
@software: python
@file: example8_7.py
@time: 2019/12/15 21:16
@desc:
'''


def make_album(singer_name, album_name, number_of_songs=''):
    """创建一个描述音乐专辑的字典"""
    album_info = {'singer': singer_name, 'album': album_name}
    if number_of_songs:
        album_info['number_of_songs']=number_of_songs
    return album_info


album = []

while True:
    singer = input("\nPlease input the singer name：(enter q or quit to finish)")
    if singer == 'q' or singer == 'quit':
        break
    album_name = input("\nPlease input the album name：(enter q or quit to finish)")
    if album_name == 'q' or album_name == 'quit':
        break
    number_of_songs=input("\nPlease input the number of songs in this album：(enter q or quit to finish)")
    if number_of_songs == 'q' or number_of_songs == 'quit':
        break
    album.append(make_album(singer, album_name, number_of_songs))


print(album)



# print(make_album('jay chou', 'Jay'))
# print(make_album('jj lin', '100 days'))
# print(make_album('Fish Leong', 'Love sees the heart long', 10))

'''
Please input the singer name：(enter q or quit to finish)jay

Please input the album name：(enter q or quit to finish)jay

Please input the number of songs in this album：(enter q or quit to finish)2

Please input the singer name：(enter q or quit to finish)liangjingru

Please input the album name：(enter q or quit to finish)liang

Please input the number of songs in this album：(enter q or quit to finish)2

Please input the singer name：(enter q or quit to finish)q
[{'singer': 'jay', 'album': 'jay', 'number_of_songs': '2'}, {'singer': 'liangjingru', 'album': 'liang', 'number_of_songs': '2'}]

Process finished with exit code 0
'''
