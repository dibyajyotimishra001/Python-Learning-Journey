with open("demo.txt") as files:
    lines = files.read()

NewLine = lines.lower().replace("donkey", "#####")
with open("demo.txt", "w") as NewFiles:
    NewFiles.write(NewLine)