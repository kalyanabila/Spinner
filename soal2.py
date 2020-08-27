# Soal 2 List Spinner

def counterClockwise(data):      # Membuat function dg nama function counterClockwise dan parameter data 
    
    for a in range(len(data)):    # Looping dgn menggunakan jumlah/ len pada parameter data
        for b in range(a):          # Looping in Looping 
            data[a][b], data[b][a] = data[b][a], data[a][b]  # [1][0] , [0][0]  -> [0][0], [0][1]
    
    hasil = []                     
    for c in range(1,len(data)+1):   # c merupakan baris index data
        c = -c                         # me reverse c
        hasil.append(data[c])       # menambahkan elemen 'data' ke 'hasil' dengan urutan terbalik
    return hasil                      # me return kan var hasil


List_awal = [[1,2,3],[4,5,6],[7,8,9]]
print(counterClockwise(List_awal))    # menampilkan hasil penggunaan function