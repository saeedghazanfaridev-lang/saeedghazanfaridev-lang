# A beginner project based on Python Crash Course, Chapters 1–7.

study_topics = [
    "Variables and strings",
    "Lists",
    "Dictionaries",
    "while loops",
]

while True:
    print("\n=== Python Study Topics ===")
    print("1. Show study topics")
    print("2. Add a study topic")
    print("3. Remove the last topic")
    print("4. Quit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        if study_topics:
            print("\nTopics to study:")
            for topic in study_topics:
                print(f"- {topic}")
        else:
            print("\nYour topic list is empty.")

    elif choice == "2":
        new_topic = input("Enter a topic: ").strip()

        if new_topic:
            study_topics.append(new_topic)
            print(f'Added "{new_topic}".')
        else:
            print("The topic cannot be empty.")

    elif choice == "3":
        if study_topics:
            removed_topic = study_topics.pop()
            print(f'Removed "{removed_topic}".')
        else:
            print("There are no topics to remove.")

    elif choice == "4":
        print("Keep learning. Goodbye!")
        break

    else:
        print("Invalid option. Enter a number from 1 to 4.")
