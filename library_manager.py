import streamlit as st
import json
import os

# Page Styling
st.set_page_config(
    page_title="Areeba's Library Manager",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for Background Color
st.markdown(
    """
    <style>
        /* Make the content centered when sidebar is open */
        .main-container {
            max-width: 80%;
            margin: auto;
            transition: max-width 0.1s ease-in-out;
    }
    
    /* Full-width when sidebar is closed */
        .sidebar-hidden .main-container {
            max-width: 100%;
        }

    /* Adjust Streamlit content padding */
        .css-1d391kg { 
            padding: 2rem !important;
    }
        .stApp {
            background: linear-gradient(to right, #b5f8ff, #0c7d8a);
        }
        /* Gradient Background for Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(to top, #0c7d8a, #c3dedd);
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# JSON file for storing books
FILE_PATH = "library.json"

# Load existing books from file
def load_library():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save books to file
def save_library(library):
    with open(FILE_PATH, "w") as file:
        json.dump(library, file, indent=4)

# Load the library
library = load_library()

# Streamlit UI
st.title("📚Library Manager by Areeba Faisal")

# Navigation menu
menu = st.sidebar.radio("Menu", ["Add Book", "Remove Book", "Search Book", "View All Books", "Statistics"])

# Add a Book
if menu == "Add Book":
    st.header("📖 Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        if title and author and genre:
            new_book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read_status
            }
            library.append(new_book)
            save_library(library)
            st.success(f"📚 Book '{title}' added successfully!")
        else:
            st.warning("⚠️ Please fill in all fields.")

# Remove a Book
elif menu == "Remove Book":
    st.header("🗑️ Remove a Book")
    book_titles = [book["title"] for book in library]
    
    if book_titles:
        book_to_remove = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != book_to_remove]
            save_library(library)
            st.success(f"📕 Book '{book_to_remove}' removed successfully!")
    else:
        st.warning("⚠️ No books available to remove.")

# Search for a Book
elif menu == "Search Book":
    st.header("🔍 Search for a Book")
    search_query = st.text_input("Enter book title or author")
    
    if st.button("Search"):
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        
        if results:
            st.subheader("📌 Search Results")
            for book in results:
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}, {book['genre']}) - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("⚠️ No matching books found.")

# Display All Books with UI Improvements
elif menu == "View All Books":
    st.header("📚 All Books in Your Library")
    
    if library:
        cols = st.columns(2)  # Adjust number of columns for responsive layout

        for index, book in enumerate(library):
            with cols[index % 2]:  # Arrange books in two columns
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #ddd; 
                        border-radius: 10px; 
                        padding: 15px; 
                        margin-bottom: 10px;
                        background-color: #f9f9f9;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    ">
                        <h4 style="color: #333;">📖 {book['title']}</h4>
                        <p><b>Author:</b> {book['author']}</p>
                        <p><b>Year:</b> {book['year']}</p>
                        <p><b>Genre:</b> {book['genre']}</p>
                        <p><b>Status:</b> {"✅ Read" if book["read"] else "❌ Unread"}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.warning("⚠️ No books in the library yet.")

# Library Statistics with Graph
elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books = len(library)

    if total_books > 0:
        read_books = sum(1 for book in library if book["read"])
        unread_books = total_books - read_books
        read_percentage = (read_books / total_books) * 100

        st.write(f"📚 **Total Books:** {total_books}")
        st.write(f"📖 **Books Read:** {read_books} ({read_percentage:.2f}%)")
        st.write(f"📖 **Books Unread:** {unread_books} ({100 - read_percentage:.2f}%)")
    
    else:
        st.warning("⚠️ No books in the library yet.")

# Footer
st.sidebar.info("📌 Developed by Areeba Faisal ❤️ ")
