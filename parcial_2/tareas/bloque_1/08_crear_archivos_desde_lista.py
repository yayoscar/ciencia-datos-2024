My_friends = ["Fátima", "Chepes", "Jonathan"]
for secondary in My_friends:
    with open(f"{secondary}.txt", "w") as archivo:
        archivo.write(secondary)