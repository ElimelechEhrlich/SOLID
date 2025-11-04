class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        
    def __str__(self):
        return f'title: {self.title}, author: {self.author}, content: {self.content}'


class Save_To_List: 
    def __init__(self):
        self.books_list = []
    def save_to_list(self, book):
        self.books_list.append(book.__str__())


b1 = Book('AAA', 'BBB', 'CCCCC')
b2 = Book('DDD', 'EEE', 'FFFFF')
save_To_List = Save_To_List()
save_To_List.save_to_list(b1)
save_To_List.save_to_list(b2)
print (save_To_List.books_list)


