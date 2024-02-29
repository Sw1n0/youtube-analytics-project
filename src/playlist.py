# from src.video import PLVideo

import os

from googleapiclient.discovery import build

from helper.youtube_api_manual import printj


class PlayList:
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, play_list_id):
        self.play_list_id = play_list_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.__pl_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()

        #self.response = self.youtube.playlists().list(id=self.play_list_id,
        #                                              part='snippet',
        #                                              ).execute()
        #self.title = self.response['items'][0]['snippet']['title']

# pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# printj(pl.title)
