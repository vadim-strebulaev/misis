with open("books_rowling.csv", encoding="utf-8") as file: # - читаю файл
    for i in file:
        curr = list(i.split(";")) # - информация о нынешней книге
        r = float(curr[-1].replace(",", ".")[:-1]) # - рейтинг нынешней книги
        if "Роулинг" in curr[1] and r > 8: # - если книга подходит, выводим её 
            print(curr[1], " - ", curr[-2], "\t", curr[-1], sep="", end="\r")
            
