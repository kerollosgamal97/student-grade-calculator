PASS_SCORE = 50


def main():
    raw = input("Enter student grade (0-100): ")

    try:
        grade = float(raw)
    except ValueError:
        print("Invalid input: please enter a number between 0 and 100.")
        return

    if not 0 <= grade <= 100:
        print("Invalid input: grade must be between 0 and 100.")
        return

    print("Pass" if grade >= PASS_SCORE else "Fail")


if __name__ == "__main__":
    main()
