while True:
    inp = input().split()
    if inp[0] == "0":
        break
    q = int(inp[0])
    d = int(inp[1])
    p = int(inp[2])
    page = int((p*d*q)/(p-q))
    if page > 1:
        print(f"{page} paginas")
    else:
        print(f"{page} pagina")