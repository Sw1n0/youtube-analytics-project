import os

from googleapiclient.discovery import build

from src.channel import Youtube


class Video(Youtube):
    """Класс для видео"""
    def __init__(self, video_id):
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id
                                                    ).execute()
        try:
            self.title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
