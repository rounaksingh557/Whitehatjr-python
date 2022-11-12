class MovieReview:

    def __init__(self, movie: str, story: int, actor: int,  music: int):
        self.movieName = movie,
        self.storyRating = int(story)
        self.actorRating = int(actor)
        self.musicRating = int(music)

        self.avg = (self.storyRating + self.actorRating + self.musicRating)/3

        self.movie = {
            "Movie Name": self.movieName,
            "Story Rating": self.storyRating,
            "Actor Rating": self.actorRating,
            "Music Rating": self.musicRating,
            "Avg Rating": self.avg
        }

    def add_movie_rating(self, movie_list: list):
        movie_list.append(self.movie)

    def avg_star_rating(self, movie_list: list):
        for movie in movie_list:
            if (movie["Avg Rating"] == 1):
                print("Thanks for your response, You rated the movie with:  *")
            elif (movie["Avg Rating"] == 2):
                print("Thanks for you response, You rated the movie with **")
            elif (movie["Avg Rating"] == 3):
                print("Thanks for your response, You rated the movie with ***")
            elif (movie["Avg Rating"] == 4):
                print("Thanks for your response, You rated the movie with ****")
            elif (movie["Avg Rating"] == 5):
                print("Thanks for your response, You rated the movie with *****")
            else:
                print("No rating provided")


MovieReviewsList = []
New_Movie = MovieReview("Onwards", 5, 5, 5)
New_Movie.add_movie_rating(MovieReviewsList)
New_Movie.avg_star_rating(MovieReviewsList)
