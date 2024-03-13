import datetime
import isodate

from src.channel import Youtube


class PlayList(Youtube):
    def __init__(self, play_list_id):
        self.play_list_id = play_list_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.play_list_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()

        self.response = self.youtube.playlists().list(id=self.play_list_id,
                                                      part='snippet',
                                                      ).execute()
        self.title = self.response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={play_list_id}'
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=self.video_ids
                                                        ).execute()

    def show_best_video(self):
        most_likes = 0
        best_video = ""
        for video in self.video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > most_likes:
                most_likes = like_count
                best_video = video['id']
        return f'https://youtu.be/{best_video}'

    @property
    def total_duration(self):
        duration = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            video_duration = isodate.parse_duration(iso_8601_duration)
            duration += video_duration
        return duration
