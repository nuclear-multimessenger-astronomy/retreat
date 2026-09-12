def available_books(catalogue, genre=None, min_year=None, max_year=None):

    available = {}
    for book_id, book in catalogue.items():
        if book["checked_out"]:
            continue
        if genre is not None and book["genre"] != genre:
            continue
        if min_year is not None and book["year"] < min_year:
            continue
        if max_year is not None and book["year"] > max_year:
            continue
 
        available[book_id] = book
 
    return available, len(available)

DEMO_CATALOGUE = {
    "V-01": {"title": "Twenty Thousand Leagues Under the Seas", "author": "Jules Verne",
             "genre": "adventure", "year": 1870, "checked_out": False},
    "V-02": {"title": "Around the World in Eighty Days", "author": "Jules Verne",
             "genre": "adventure", "year": 1873, "checked_out": False},
    "S-01": {"title": "Treasure Island", "author": "Robert Louis Stevenson",
             "genre": "adventure", "year": 1883, "checked_out": True},
    "C-01": {"title": "The Moonstone", "author": "Wilkie Collins",
             "genre": "detective", "year": 1868, "checked_out": False},
}

if __name__ == "__main__":

    shelf, count = available_books(DEMO_CATALOGUE, genre="adventure", min_year=1870)
    print(count, shelf)