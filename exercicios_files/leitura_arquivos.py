with open ("a", "r", encoding="utf-8") as f:
    for i in f:
        print(i, end=" ")
        if "o" in i:
            print("Tem o nessa linha")