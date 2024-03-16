a = [] # - это будет массив со всеми книгами
with open("books.csv", encoding="utf-8") as file: # - читаю файл
    file.readline()
    for i in file:
        a.append(list(i.split(";")))


max_rating = 0 # - максимальный рейтинг книги
for i in a:
    curr_rat = int(100 * float(i[-1][:-1].replace(",", "."))) # - нынешний рейтинг
    max_rating = max(max_rating, curr_rat)

b = [[]] * max_rating # - это будет отсортированный массив

for i in a:
    for j in a:
        if i == j:
            break   # - эта сортировка изначально O(n), поэтому бегаем дополнительно по элементам, чтобы сложность была O(n * log n)
        
    b[int(100 * float(i[-1][:-1].replace(",", "."))) - 1] = i # - в итоге это сортировка, сложность которой O(n * log n)

while [] in b: # - удаление лишних элементов
    b.remove([])
    
for i in range(3):
    i = a[i]
    original_title = i[-2]
    authors = i[2]
    rating = i[-1]
    print(original_title, "-", authors, "-", rating) # - Выводим информацию о подходящей книге
