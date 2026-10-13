def classify_grade(score: int) -> str:
    """Classify an integer score as passing or failing."""
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError("score must be an integer from 0 through 100")

    return "Pass" if score >= 60 else "Fail"


if __name__ == "__main__":
    try:
        score = int(input("Enter a score from 0 to 100: "))
        result = classify_grade(score)
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print(f"Grade: {result}")
