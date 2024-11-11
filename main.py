def solve(n, m, a): 
    # Jika ada lebih banyak elemen daripada nilai m, hasilnya pasti 0 (pigeonhole principle)
    if n > m:
        return 0

    result = 1
    # Loop untuk menghitung produk |ai - aj|
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            result = (result * diff) % m
            if result == 0:  # Jika hasil sudah 0, tidak perlu melanjutkan
                return 0
    return result

# Membaca input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Memanggil fungsi dan mencetak hasil
print(solve(n, m, a))
