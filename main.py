import csv
import datetime

from googleapiclient.discovery import build

api_key = "AIzaSyD27NvuByXB11cp02V1no_ZHQDBWPDDTVE"

chaines = {
    {
        id : '',
    }
}

"""
liste.csv file : 

 - Col 1 : Group name
 - Col 2 : Info
 - Col 3 : Song release date
 - Col 4 : Song URL
 - Col 4 : Teaser #1 URL
 - Col 4 : Teaser #2 URL
"""


def csv_to_dict(file_name):
    """
    Read csv file and return a dict
    """
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


d = csv_to_dict('liste.csv')

"""
for elem in d :
    if song url is no empty :
        pass
    else :
        if date de sortie is not today :
            if teaser 1 is empty :
                look for teaser 1 url with "teaser" in the title
            else :
                if teaser 2 is empty :
                    look for teaser 2 url with "teaser" in the title, different from the teaser 1 url
                else :
                    pass
        else :
            search for song url without "teaser" in title
"""


def get_video_title(url):
    """
    Return the title of the video
    """
    # Création d'un service youtube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Création d'une requête
    requete = youtube.videos().list(
        part='snippet',
        id=url.split('=')[1]
    )

    # Exécution de la requête
    reponse = requete.execute()

    return reponse['items'][0]['snippet']['title']


def get_url(info, group_name, teaser_number):
    """
    Return the url of the song
    """
    # Création d'un service youtube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Création d'une requête
    requete = youtube.search().list(
        part='snippet',
        order='relevance',
        q='{} {} {}'.format(info, group_name, teaser_number)
    )

    # Exécution de la requête
    reponse = requete.execute()

    banword_list = [
        'trailer',
        'unit',
        'cover'
    ]

    for i in range(5):
        trouve = False
        # Si le titre du vidéo contient ne contient pas un mot interdit, on recupère l'id et break
        for banword in banword_list:
            if banword in reponse['items'][i]['snippet']['title'].lower():
                trouve = True
                break

        if not trouve:
            id = reponse['items'][i]['id']['videoId']
            break

    return 'https://www.youtube.com/watch?v={}'.format(id)


for element in d:
    if element['Song URL'] != '':
        pass
    else:

        # Identification de la date de sortie
        date_sortie = element['Song release date']
        date_sortie = date_sortie.split('/')
        date_sortie = date_sortie[2] + '-' + \
            date_sortie[1] + '-' + date_sortie[0]

        # Identification de la date du jour
        date_jour = datetime.datetime.now().strftime('%Y-%m-%d')

        if date_sortie != date_jour:
            if element['Teaser #1 URL'] == '':
                # Si il y a le mot "teaser" dans le titre de la vidéo, on la prends
                if 'teaser' in get_video_title(get_url(element['Info'], element['Group name'], 'teaser')).lower():
                    element['Teaser #1 URL'] = get_url(
                        element['Info'], element['Group name'], 'teaser')
            else:
                if element['Teaser #2 URL'] == '':
                    # Si il y a le mot "teaser" dans le titre de la vidéo, on la prends
                    if 'teaser' in get_video_title(get_url(element['Info'], element['Group name'], 'teaser')).lower():
                        element['Teaser #2 URL'] = get_url(
                            element['Info'], element['Group name'], 'teaser')
                else:
                    pass
        else:
            # On se connecte aux châines sur lesquelles la musique est susceptible d'être diffusée


            pass

# Write the dict to a new csv file
with open('liste_new.csv', 'w', newline='') as csvfile:
    fieldnames = ['Group name', 'Info', 'Song release date',
                  'Song URL', 'Teaser #1 URL', 'Teaser #2 URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(d)
