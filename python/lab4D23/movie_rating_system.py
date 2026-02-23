# movie_rating_system.py

def analyze_ratings(ratings):
    # Remove invalid ratings
    valid_ratings = [r for r in ratings if 1 <= r <= 5]

    if not valid_ratings:
        print("No valid ratings available.")
        return

    average = sum(valid_ratings) / len(valid_ratings)
    five_star = valid_ratings.count(5)

    valid_ratings.sort()

    print("\nValid Ratings:", valid_ratings)
    print("Average Rating:", round(average, 2))
    print("Number of 5-Star Ratings:", five_star)


ratings_input = list(map(int, input("Enter movie ratings (1-5): ").split()))
analyze_ratings(ratings_input)
