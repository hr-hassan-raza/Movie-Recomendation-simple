

# In[1]:

def mean(lst):
    return sum(lst) / len(lst)

def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))





# #### Task 1: Reading Data

# In[2]:


def read_ratings_data(f):
    d = {}
    with open(f) as f:
        for line in f:
            arr = line.split('|')
            if arr[0] in d.keys():
                d[arr[0]].append(float(arr[1]))
            else:
                d[arr[0]] = [float(arr[1])]
    return d
movie_ratings = read_ratings_data("movies_ratings.txt")
print("Movie Ratings Dictionary: ", movie_ratings)


# In[3]:


def read_movie_genre(f):
    d = {}
    with open(f) as f:
        for line in f:
            arr = line.split('|')
            d[arr[2][:-1]] = (arr[0])
    return d
movie_genre = read_movie_genre('movies_genere.txt')
print("Movie Genre Dictionary: ", movie_genre)


# #### Task 2: Processing Data

# In[4]:


def create_genre_dict(movie_genre):
    genre_dict = {}
    for movie, genre in movie_genre.items():
            if genre in genre_dict.keys():
                genre_dict[genre].append(movie)
            else:
                genre_dict[genre] = [movie]
    return genre_dict
genre_dict = create_genre_dict(movie_genre)
print("Genre Dictionary: ",genre_dict)


# In[5]:


def calculate_average_rating(movie_ratings):
    rating_average = {}
    for movie, ratings in movie_ratings.items():
        mean_r = mean(ratings)
        rating_average[movie] = round(mean_r,2)
    return rating_average
rating_average = calculate_average_rating(movie_ratings)
print("Average Rating Function Checking: ",rating_average)


# #### Task 3: Recommendation

# In[6]:


def get_popular_movies(rating_average, n=10):
    sorted_dict = sort_dict_by_value(rating_average, True)
    res = {}
    i = 0
    for movies,ratings in sorted_dict.items():
        res[movies] = ratings
        i = i + 1
        if (i == n):
            break
    return res
popular_movies = get_popular_movies(rating_average,4)
print("Popular Movie Function Testing",popular_movies )


# In[7]:


def filter_movies(rating_average, threshold):
    filtered_movies = {}
    for movie, rating in rating_average.items():
        if rating  == threshold:
            filtered_movies[movie] = threshold
    return filtered_movies
filter_movies = filter_movies(rating_average, 4)
print("Filter movies function testing", filter_movies)


# In[8]:


def get_popular_in_genre(genre, genre_dict, rating_average, n=5 ):
    moives_genre = genre_dict[genre]
    d = {}
    for i in moives_genre:
        d[i] = rating_average[i]
    res = get_popular_movies(d, n)
    return res
popular_genre = get_popular_in_genre('Adventure', genre_dict, rating_average, n=2)
print("Popular Genre Function Testing",popular_genre)


# In[9]:


def get_genre_rating(genre, genre_dict, rating_average):
    moives_genre = genre_dict[genre]
    d = {}
    for i in moives_genre:
        d[i] = rating_average[i]
    return d
gen_rat = get_genre_rating('Adventure', genre_dict, rating_average)
print("Get genre Rating Function", gen_rat )


# In[10]:


def genre_popularity(genre_dict, rating_average, n=5):
    mean_genre = {}
    for genre, ratings in genre_dict.items():
        genre_ratings = get_genre_rating(genre, genre_dict, rating_average)
        mean_r = round(mean(genre_ratings.values()),2)
        mean_genre[genre] = mean_r
    res = get_popular_movies(mean_genre, n)
    return res
genre_pop = genre_popularity(genre_dict, rating_average, n=5)
print("Genre Popularity function: ", genre_pop)


# ##### Task 4 (User Focused)

# In[11]:


def read_user_ratings(f):
    d = {}
    with open(f) as f:
        for line in f:
            arr = line.split('|')
            #print(int(arr[2]))
            if int(arr[2]) in d.keys():
                d[int(arr[2])].append((arr[0], float(arr[1])))
            else:
                d[int(arr[2])] = [(arr[0], float(arr[1]))]
    return d
users_data = read_user_ratings("movies_ratings.txt")
print("User Data Function Testing", users_data)


# In[12]:


def get_user_genre(user_id,users_data,movie_genre):
    movies_ratings = users_data[user_id]
    genre_rating_movie = []
    for i in movies_ratings:
        i = i + (movie_genre[i[0]],)
        genre_rating_movie.append(i)
    ratings_genre = {}
    for j in genre_rating_movie:
        if j[2] in ratings_genre.keys():
            ratings_genre[j[2]].append(j[1])
        else:
            ratings_genre[j[2]] = [j[1]]
    res = {}
    for genre,ratings in ratings_genre.items():
        res[genre] = mean(ratings)
    res = get_popular_movies(res, n=1)
    res = list(res.keys())[0]
    return res
genre_user_f = get_user_genre(1,users_data,movie_genre)
print("Get user genre function testing: ", genre_user_f)       


# In[13]:


def recommend_movies (user_id, users_data,movie_genre,rating_average):
    user_genre = get_user_genre(user_id,users_data,movie_genre) 
    genre_dict = create_genre_dict(movie_genre)
    users_top_movies_genre = genre_dict[user_genre]
    users_rated_movies = users_data[user_id]
    not_watched = []
    for i in users_rated_movies:
        if i[0] not in users_top_movies_genre:
            not_watched.append(i[0])
    result = {}
    for i in not_watched:
        result[i] = rating_average[i]
    res = get_popular_movies(result, n=3)
    return res
rc_movies  = recommend_movies(1, users_data,movie_genre,rating_average)
print("Recommend Movie Function: ", rc_movies)


# In[ ]:




