# ------- Libraries ---------- #

import spacy 
nlp = spacy.load('en_core_web_md')


# Creating a function that compares a given movie to the other movies in the text files and recommends the most similar one. 
def recommended_movie(movie):
    movie = nlp(movie)
    movies = open("movies.txt", "r")
    movies_details = movies.readlines()

    similarity_list = []

    for item in movies_details:
        movie_desc = item.split(":")[1]  #movie_desc[1] as this is a list
        movie_desc = nlp(movie_desc)
        similarity_list.append(movie.similarity(movie_desc))

    recommended_movie_index = similarity_list.index(max(similarity_list))

    return movies_details[recommended_movie_index].split(":")[0]

# Given movie:
planethulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


# Calling the function to see what's the recommended movie based on the above movie. 
print ("Recommended movie to watch:")
print(recommended_movie(planethulk))