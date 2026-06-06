def generate_table(n):
    table = ""
    for j in range(1, 11):
        table += f"{n} x {j} = {n*j}\n"
    with open(f"table/multi_{n}.txt", "w") as file:
            file.write(table)


for i in range(2, 21):
    generate_table(i)