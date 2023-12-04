"""Restaurant rating lister."""

def restaurant_rating_lister(file):
    data = open(file)

    # store in this empty dictionary
    restaurant_ratings = {}
    # looks like this 
    # RestaurantName:Rating

    # reads the ratings from the file 
    for line in data:
        line = line.rstrip()
        restaurant, rating = line.split(":")[:]
        restaurant_ratings[restaurant] = int(rating)

        # put these into restaurant_ratings = {} (our dictionary)
    return restaurant_ratings
    # storing restaurant_ratings 

def sort_ratings(ratings):
    """Sort the returned dictionary from restaurant lister"""
    # sample output: (output we're expecting):
    # Donut You Want Me Baby is rated at 1.
    # Eclair And Present Danger is rated at 5.
    
    # put everything in alphabetical order 
    
    # for loop - to print each time 
        # print(f"{RestaurantName} is rated at {rating}.")

    for restaurant, rating in sorted(ratings.items()):
        print(f"{restaurant} is rated at {rating}.")
    



# sort_ratings(restaurant_rating_lister("scores.txt"))
scores = restaurant_rating_lister("scores.txt")
sort_ratings(scores)
