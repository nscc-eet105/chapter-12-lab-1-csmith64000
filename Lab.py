# Name: Christopher Smith
# Lab Number: Chapter 12 - Lab 1
# Date: 07/14/2025


def main():
    print("State Capital's Game\n")

    # Dictionary with 5 states and their capitals
    capitals = {
        "Ohio": "Columbus",
        "Michigan": "Lansing",
        "Indiana": "Indianapolis",
        "Illinois": "Springfield",
        "West Virginia": "Charleston"
    }

    correct = 0
    incorrect = 0

    for state, capital in capitals.items():
        print(f"What is the capital of {state}?")
        answer = input("Type your answer: ").strip()

        if answer.lower() == capital.lower():
            print("Good job!\n")
            correct += 1
        else:
            print(f"Sorry the answer is {capital}.\n")
            incorrect += 1

    print(f"You answered {correct} correctly and {incorrect} incorrectly.")

# Run the main function
main()
