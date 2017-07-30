import webbrowser

class Movie():
    # a __doc__ for my class
    """This class provides a way to store movie related information"""
    # triple quotes to define my doc. in multiple lines

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # the constructor of the class that will create its objects
    def __init__(self, movie_title, movie_storyline,
                     poster_img, trailer_youtube):
    # self is the object being created
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube
        # all these variables apove called instance variables

    def showTrailer(self):
    #a fun. defined inside a class called instance method
        webbrowser.open(self.trailer_youtube_url)
