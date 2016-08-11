import media
import fresh_tomatoes

"""With the imported class file, media, movies
are created using the Movie() class."""
toy_story = media.Movie("Toy Story",
                        "https://goo.gl/2G6Ab7",
                        "https://goo.gl/yuDEHP")

avatar = media.Movie("Avatar",
                     "https://goo.gl/z8A39O",
                     "https://goo.gl/qBlcP8")

school_of_rock = media.Movie("School of Rock",
                             "https://goo.gl/CBgeVI",
                             "https://goo.gl/8wC8F9")

ratatouille = media.Movie("Ratatouille",
                          "https://goo.gl/mVnsif",
                          "https://goo.gl/LFekic")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://goo.gl/5SwfMf",
                                "https://goo.gl/O1dwTH")

hunger_games = media.Movie("Hunger Games",
                           "https://goo.gl/zSnSH0",
                           "http://goo.gl/ap2MXs")

# movies below, stores the list of movies created above.
movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

# Call open_movies_page function to generate webpage.
fresh_tomatoes.open_movies_page(movies)
