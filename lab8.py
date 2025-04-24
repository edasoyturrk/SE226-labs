class Archiveltem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year
    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"
    
    def __eq__(self, other):
        if isinstance(other, ArchiveItem):
            return self.uid == other.uid
        return False
    
    def is_recent(self, n):
        current_year = 2025
        return (current_year - self.year) <= n
        
class Article(Archiveltem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi
    
    def __str__(self):
        return f"Article -> {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"
class Book(Archiveltem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Book : {super().__str__()}, Author: {self.autho}, Pages: {self.pages}"

class Podcast(Archiveltem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration
    
    def __str__(self):
        return f"Podcast : {super().__str__()}, Host: {self.host}, Duration: {self.duration} mins"
    
def save_to_file(items, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in items:
            if isinstance(item, Book):
                line = f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}"
            elif isinstance(item, Article):
                line = f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}"
            elif isinstance(item, Podcast):
                line = f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}"
            file.write(line + "\n")

def load_from_file(filename):
    items = []
    if not os.path.exists(filename):
        return items
        
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == "Book":
                item = Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
            elif parts[0] == "Article":
                item = Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5])
            elif parts[0] == "Podcast":
                item = Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
            items.append(item)
    return items
    
def main():

    items = [
        Book("B001", "SE116", 2020, "x", 350),
        Book("B002", "SE226", 2008, "y", 464),
        Article("A101", "CE223", 2023, "z", "10.1234/ml567"),
        Article("A102", "CE215", 2021, "q", "10.5678/qc123"),
        Podcast("P301", "SE209", 2024, "a", 45),
        Podcast("P302", "GBE204", 2022, "b", 60)
    ]
    
    save_to_file(items, "archive.txt")
    print("all informations saved in text file.\n")
    
    loaded_items = load_from_file("archive.txt")
    

    print("all archived items")
    for item in loaded_items:
        print(item)
    

    print("\nItems in last 5 years:")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)
    

    print("\nArticles that DOI's start with 10.1234")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)

if __name__ == "__main__":
    main()

    

    
