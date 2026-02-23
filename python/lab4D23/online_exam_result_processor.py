# online_exam_result_processor.py

def process_results(scores):
    if len(scores) <= 2:
        print("Not enough scores to process.")
        return

    # Remove lowest 2 scores
    scores.sort()
    scores = scores[2:]

    # Add grace marks
    updated_scores = []
    for s in scores:
        if 30 <= s <= 35:
            s += 5
        updated_scores.append(s)

    # Count passed students
    passed = len([s for s in updated_scores if s >= 40])

    print("\nUpdated Scores:", updated_scores)
    print("Number of Students Passed:", passed)


scores_input = list(map(int, input("Enter student scores: ").split()))
process_results(scores_input)