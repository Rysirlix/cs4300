import pytest

books = [
    "The Hunger Games, Suzanne Collins",
    "The Chronicles of Narnia, C.S. Lewis",
    "The Great Gatsby, F. Scott Fitzgerald",
    "The Lightning Thief, Rick Riordan ",
    "City of Bones, Cassandra Clare",
    "Dracula, Bram Stoker",
    "The Giver, Lois Lowry"
]

student_id = {
    "Tom": "s0413",
    "Clair": "s1456",
    "Ryan": "s1647",
    "Lisa": "s1756",
    "Rick": "s1988",
    "Morty": "s2074",
}

def books_first_3():
    return books[:3]

def get_id(id):
    return student_id.get(id)

def test_books_first_3():
    assert books_first_3() == [
    "The Hunger Games, Suzanne Collins",
    "The Chronicles of Narnia, C.S. Lewis",
    "The Great Gatsby, F. Scott Fitzgerald"
    ]

def test_get_id():
    assert get_id("Rick") == "s1988"
    assert get_id("Nothing") is None