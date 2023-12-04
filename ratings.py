"""Restaurant rating lister."""

def restaurant_rating_lister(file):
    restaurant_ratings = open(file)

    # store in this empty dictionary
    new_dict = {}
    # looks like this 
    # RestaurantName:Rating

    # reads the ratings from the file 
    for line in restaurant_ratings:
        RestaurantName, Rating = line.rstrip().split(":")[:]

    # needs to put ratings in alphabetical order by Restaurant name
    # from hint #2: sorted() to sort afterwards for alphabetical order
    # sorted(new_dict)
    

    # sample output: (output we're expecting)
    # Donut You Want Me Baby is rated at 1.
    # Eclair And Present Danger is rated at 5.
    return None

restaurant_rating_lister:("scores.txt")
