while True:
    try:
        m, n = map(int, input().split())
        arr = []
        for i in range(m):
            ano_arr = list(map(int, input().split()))[:n]
            arr.append(ano_arr)
        total = 0
        for i in range(m):
            total += sum(arr[i])
        bag = int(total/60)
        liter = total - (int(total/60)*60)
        print(f"{bag} saca(s) e {liter} litro(s)")
    except EOFError:
        break