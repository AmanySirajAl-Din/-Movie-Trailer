import fresh_tomatoes
import media  # use the contents of my prev. Python file

# creating an objects of Movie class from my file media
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")  # NOQA

# fun. named __init__()(the constructor) is called;
# it initializes or creates space in memory for new instance toy_story

avatar = media.Movie("Avatar",
                "A marine on an alien planet",
                "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")  # NOQA

up = media.Movie("up",
            """Seventy-eight year old Carl Fredricksen
            	travels to Paradise Falls
            	in his home equipped with balloons,
            	inadvertently taking a young stowaway.""",
            "http://vignette3.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",  # NOQA
            "https://www.youtube.com/watch?v=qas5lWp7_R0")  # NOQA

hurry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
            """Seventy-eight year old Carl Fredricksen
            	travels to Paradise Falls
            	in his home equipped with balloons,
            	inadvertently taking a young stowaway.""",
            "http://www.gstatic.com/tv/thumb/movieposters/28630/p28630_p_v8_at.jpg",  # NOQA
            "https://www.youtube.com/watch?v=eKSB0gXl9dw")  # NOQA

hunger_games = media.Movie("The Hunger Games",
            """Adaptation of the first of J.K. Rowling's popular children's novels
                about Harry Potter, a boy who learns on his eleventh birthday
                that he is the orphaned son of two powerful wizards
                and possesses unique magical powers of his own.
                He is summoned from his life as an unwanted child
                to become a student at Hogwarts, an English boarding school for wizards.
                There, he meets several friends who become his closest allies
                and help him discover the truth about his parents' mysterious deaths.""",
            "http://4.bp.blogspot.com/-U2mdprflN-w/VgxrrvbSwRI/AAAAAAAAREg/Qu7dGddFQM0/s1600/The%2BHunger%2BGames.jpg",  # NOQA
            "https://www.youtube.com/watch?v=4S9a5V9ODuY")  # NOQA

divergent = media.Movie("Divergent",
            """Tris Prior (Shailene Woodley) lives in a futuristic world
                in which society is divided into five factions.
                As each person enters adulthood,
                he or she must choose a faction and commit to it for life.
                Tris chooses Dauntless (those who pursue bravery above all else).
                However, her initiation leads to the discovery that
                she is a Divergent and will never be able to fit into just one
                faction. Warned that she must conceal her status,
                Tris uncovers a looming war which threatens everyone she loves.""",
            "http://www.impawards.com/2014/posters/divergent_ver11.jpg",  # NOQA
            "https://www.youtube.com/watch?v=sutgWjz10sM")  # NOQA


# then making the website
movies = [toy_story, avatar, up, hurry_potter, hunger_games, divergent]
# movies list contains the objects from class Movie
# to pass it to open_movies_page() to create my movie trailer
fresh_tomatoes.open_movies_page(movies)
# open_movies_page it takes a list of movies 
# then creates and opens an HTML page or website,
# that shows those movies
