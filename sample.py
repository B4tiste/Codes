from googleapiclient.discovery import build

api_key = "AIzaSyD27NvuByXB11cp02V1no_ZHQDBWPDDTVE"

# Création d'un service youtube
youtube = build('youtube', 'v3', developerKey=api_key)

requete = youtube.search().list(
    part='snippet',
    order='relevance',
    q='JTGILY give up'
)

reponse = requete.execute()

print(reponse)