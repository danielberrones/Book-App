import tkinter as tk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
class BookApp:
    def __init__(self):
        self.book_list = []
        
    def add_book(self, title, author):
        book = Book(title, author)
        self.book_list.append(book)
        print(f"Added book: {book.get_title()} by {book.get_author()}")
        
    def display_books(self):
        print("Book List:")
        for book in self.book_list:
            print(f"{book.get_title()} by {book.get_author()}")
    
class BookGUI:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Book App")
        
        title_label = tk.Label(self.window, text="Title:")
        title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.window)
        self.title_entry.grid(row=0, column=1)
        
        author_label = tk.Label(self.window, text="Author:")
        author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.window)
        self.author_entry.grid(row=1, column=1)
        
        add_button = tk.Button(self.window, text="Add Book", command=self.add_book)
        add_button.grid(row=2, column=0)
        
        display_button = tk.Button(self.window, text="Display Books", command=self.display_books)
        display_button.grid(row=2, column=1)
        
        self.window.mainloop()
        
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        self.app.add_book(title, author)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        
    def display_books(self):
        self.app.display_books()

app = BookApp()
gui = BookGUI(app)

