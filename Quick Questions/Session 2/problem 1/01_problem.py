with open("poem.txt") as files:
    read = files.read()

read1 = read.lower()
print(read1.count("twinkle"))