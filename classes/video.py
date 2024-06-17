"""Video Class"""
import csv


class Video:
    list_of_videos = {}
    
    @classmethod
    def load_all_videos(cls):
        all_videos = []
        with open('./data/videos.csv', 'r') as videocsvfile:
            reader = csv.DictReader(videocsvfile)
            for row in reader: 
                new_video = Video(**row)
                all_videos.append(new_video)
        return all_videos

    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = id
        self._title = title
        self._rating = rating
        self.release_year = release_year
        self._copies_available = copies_available
        self.videos = []

        Video.list_of_videos[self._id] = self 

    @property
    def get_id(self):
        return self._id

    @property
    def get_title(self):
        return self._title
    
    @property
    def get_rating(self):
        return self._rating
    
    @property
    def get_copies_available(self):
        return self._copies_available
    
    @get_copies_available.setter
    def set_copies_available(self, available_copies):
        if isinstance(available_copies, int > 0):
                if available_copies is not str:
                    self._copies_available = available_copies
        else:
            raise TypeError(f"{available_copies} must be a number")
    
    def add_a_video(cls):
        pass

    def get_a_video_by_title(cls, title):
        if isinstance(title, str):
            for video_title, video_instance in cls.list_of_videos.items():
                if video_title == title:
                    return video_instance
                else: 
                    print(f"Video not found")

    def list_inventory(cls):
        return cls.list_of_videos

    def __repr__(self):
        return f"{self.get_id}, {self._title}, {self._rating}, {self.release_year}, {self._copies_available}"
    
