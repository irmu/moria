from .Base import Base
from ..common import api

class Highlighteds(Base):
    has_dirs = True
    has_videos = True
    def setItems(self):
        self.items = api.highlighteds()
