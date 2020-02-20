#!/bin/bash

rm outputs/*
cat  "./tests/a_example.txt"      | python3 librarian.py  > "./outputs/a_example.txt"
cat "tests/b_read_on.txt"         | python3 librarian.py > "outputs/b_read_on.txt"
cat "tests/c_incunabula.txt"      | python3 librarian.py  > "outputs/c_incunabula.txt"
cat "tests/d_tough_choices.txt"   | python3 librarian.py > "outputs/d_tough_choices.txt"
cat "tests/e_so_many_books.txt"   | python3 librarian.py > "outputs/e_so_many_books.txt"
cat "tests/f_libraries_of_the_world.txt" | python3 librarian.py > "outputs/f_libraries_of_the_world.txt"


