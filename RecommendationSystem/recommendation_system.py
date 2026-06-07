# Movie Recommendation System
# Created by Ayush Padwekar

movies = {
    "action": ["John Wick", "Mad Max", "The Dark Knight"],
    "comedy": ["Hera Pheri", "Dhamaal", "3 Idiots"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"],
    "horror": ["The Conjuring", "Insidious", "Annabelle"],
    "romance": ["Titanic", "The Notebook", "La La Land"]
}

print("=" * 45)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 45)

while True:

    print("\nAvailable Genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Sci-Fi")
    print("4. Horror")
    print("5. Romance")

    choice = input("\nChoose a genre (1-5) or type genre name: ").lower()

    if choice == "1":
        choice = "action"
    elif choice == "2":
        choice = "comedy"
    elif choice == "3":
        choice = "sci-fi"
    elif choice == "4":
        choice = "horror"
    elif choice == "5":
        choice = "romance"

    if choice in movies:

        print("\nRecommended Movies For You:\n")

        for movie in movies[choice]:
            print("-", movie)

    else:
        print("\nSorry! Genre not available.")

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Movie Recommendation System.")
        break