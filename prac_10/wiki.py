import wikipedia

try:
    title = input(">>> ")
    while title != "":
        page = wikipedia.page(title, auto_suggest=False)
        print(f"{page.title}, {page.summary}, {page.url}")
        title = input(">>> ")
    print("Error- Input blank")
except wikipedia.exceptions.PageError:
    # no such page, return a random one
    print(f"Error - Page non existant")
except wikipedia.exceptions.DisambiguationError:
    # this is a disambiguation page, get the first real page (close enough)
    print(f"Error")
    # sometimes the next page has the same name (different caps), so don't try the same again
