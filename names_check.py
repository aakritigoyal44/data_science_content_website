def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(","," ")
        for i in data:
            print("hello",i)
            print(data)
            return len(data(" "))
            print(count_words("names.txt"))
