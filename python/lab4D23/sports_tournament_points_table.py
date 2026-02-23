# sports_tournament_points_table.py

def process_points(points):
    # Replace negative points with 0
    points = [p if p >= 0 else 0 for p in points]

    # Sort leaderboard descending
    points.sort(reverse=True)

    winner = points[0] if len(points) > 0 else None
    runner_up = points[1] if len(points) > 1 else None

    print("\nLeaderboard:", points)
    print("Winner Points:", winner)
    print("Runner-Up Points:", runner_up)


points_input = list(map(int, input("Enter team points: ").split()))
process_points(points_input)
