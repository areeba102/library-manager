# Personal Library Manager

## Overview
The **Personal Library Manager** is a command-line program that allows users to manage their book collection. Users can **add, remove, search, edit, and display books**, as well as track their reading progress. The program also includes **file handling**, allowing users to save and load their library from a file.

## Features
- **Add a Book**: Enter book details (title, author, publication year, genre, and read status) to add it to the library.
- **Remove a Book**: Delete a book from the library using its title.
- **Search for a Book**: Find books by title or author.
- **Edit Book Details**: Modify existing book information.
- **Display All Books**: View the entire book collection.
- **Display Statistics**: See total books and the percentage of books read.
- **Save and Load Library**: The program automatically saves the library to `library.json` and loads it on startup.

## Installation
1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Navigate to the project directory in the terminal.
4. Run the program:
   ```sh
   python library.py
   ```

## Usage
Once the program starts, you will see a menu with options:
```
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Edit a book
5. Display all books
6. Display statistics
7. Exit
Enter your choice:
```
- **To add a book**, enter `1` and provide the book details.
- **To remove a book**, enter `2` and type the book title.
- **To search for a book**, enter `3`, then choose to search by title or author.
- **To edit a book**, enter `4` and select the book you want to modify.
- **To display all books**, enter `5`.
- **To view statistics**, enter `6`.
- **To exit**, enter `7` (your library will be saved automatically).

## File Handling
- The program **automatically saves** the book collection to `library.json` when exiting.
- On startup, it **loads** the previously saved books.

## Requirements
- Python 3.x

## Contributing
Feel free to contribute by improving the features or fixing bugs. Fork the repository and submit a pull request.

## License
This project is open-source and free to use.

