from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format_: str,
        year: int,
        rating: str,

    ):
        self.title = title
        self.format_ = format_
        self.year = year
        self.rating = rating


    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        total_ = []
        for category in collection:
            for decade in category:
                for movie in decade.iter("movie"):
                    movies.append(movie)
        for elem in movies:
            total_.append(cls(*elem))
        return total_


if __name__ == '__main__':
    movies_ = Movie.from_xml("movies.xml")