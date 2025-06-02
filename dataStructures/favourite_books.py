# A dictionary to store information about my favourite book

book = {"title": "be the best", "author": "david ibiyeomie", "genre": "christian"}

print(f"The genre of my favourite book is {book.get("genre").title()}")

continue_ = "yes"
cc = "false"

while continue_ == "yes":
    get_information = str(input("Enter the information you want to get about the book (title/author/genre)")).lower()
    match get_information:
        case "title":
            print(f"The title of my favourite book is {book.get("title").title()}")
        case "author":
            print(f"The author of my favourite book is {book.get("genre").title()}")
        case "genre":
            print(f"The genre of my favourite book is {book.get("genre").title()}")
        case _:
            print(f"{get_information} is not included")
    
    continue_input = str(input("Do you want another information? (yes/no)")).lower()
    
    # To ensure the user input is yes or no
    while cc == "false":
        if continue_input == "yes":
            continue_ = continue_input
            cc = "true"
        elif continue_input == "no":
            continue_ = continue_input
            cc = "true"
        else:
            continue_input = str(input("Enter yes or no ")).lower()