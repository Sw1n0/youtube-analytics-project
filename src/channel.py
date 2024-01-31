import json
import os
from pprint import pprint

from googleapiclient.discovery import build

from dotenv import load_dotenv


load_dotenv("../.env")

import isodate


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        # self.channel_name =

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pprint(channel)

    @property
    def title(self):
        return self.channel["items"][0]["snippet"]["title"]

    @property
    def video_count(self):
        return self.channel["items"][0]["statistics"]["videoCount"]

    @property
    def url(self):
        return f'https://www.youtube.com/channel/{self.channel["items"][0]["id"]}'

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def channel_description(self):
        return self.channel["items"][0]["snippet"]["description"]

    @property
    def subscribers_count(self):
        return self.channel["items"][0]["statistics"]["subscriberCount"]

    @property
    def view_count(self):
        return self.channel["items"][0]["statistics"]["viewCount"]

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name):
        info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        json_text = json.dumps(info)
        with open(file_name, "w") as file:
            json.dump(json_text, file)
