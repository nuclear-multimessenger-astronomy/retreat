from available_books import available_books

def check_shelf(shelf, count, expected_ids):
    missing = sorted(set(expected_ids) - set(shelf))
    extra = sorted(set(shelf) - set(expected_ids))
    if missing or extra:
        print(f"Not quite. Missing: {missing or 'none'}. Shouldn't be there: {extra or 'none'}.")
    else:
        print(f"Congratulations, you found all {count} books available!")
 
 
TEST_CATALOGUE = {
    "G-01": {"title": "The Castle of Otranto", "author": "Horace Walpole",
             "genre": "gothic", "year": 1764, "checked_out": False},
    "G-02": {"title": "Frankenstein", "author": "Mary Shelley",
             "genre": "gothic", "year": 1818, "checked_out": False},
    "G-03": {"title": "Jane Eyre", "author": "Charlotte Bronte",
             "genre": "gothic", "year": 1847, "checked_out": True},
    "G-04": {"title": "Wuthering Heights", "author": "Emily Bronte",
             "genre": "gothic", "year": 1847, "checked_out": False},
    "G-05": {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde",
             "genre": "gothic", "year": 1891, "checked_out": False},
    "G-06": {"title": "Dracula", "author": "Bram Stoker",
             "genre": "gothic", "year": 1897, "checked_out": False},
    "G-07": {"title": "The Turn of the Screw", "author": "Henry James",
             "genre": "gothic", "year": 1898, "checked_out": False},
    "M-01": {"title": "Moby-Dick", "author": "Herman Melville",
             "genre": "adventure", "year": 1851, "checked_out": False},
    "W-01": {"title": "The Time Machine", "author": "H. G. Wells",
             "genre": "science fiction", "year": 1895, "checked_out": False},
    "E-01": {"title": "Middlemarch", "author": "George Eliot",
             "genre": "realism", "year": 1872, "checked_out": True},
}
 
EXPECTED = ["G-02", "G-04", "G-05", "G-06"]
 
 
if __name__ == "__main__":
 
    # The scored round: gothic novels between 1818 and 1897.
    check_shelf(*available_books(TEST_CATALOGUE, genre="gothic",
                                 min_year=1818, max_year=1897), EXPECTED)