class News:
    def __init__(self, _id, _title, _text):
        self.id = _id
        self.title = _title
        self.details = _text

all_news = [
    News(1, "Title 1", "News details 01"),
    News(2, "Title 2", "News details 02"),
    News(3, "Title 3", "News details 03"),
    News(4, "Title 4", "News details 04"),
    News(5, "Title 5", "News details 05")
]