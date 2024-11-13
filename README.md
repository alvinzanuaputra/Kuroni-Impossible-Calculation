[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wn_8YGI-)

<div align=center>

|    NRP     |       Nama        |         Kelas          |
| :--------: | :---------------: | :--------------------: |
| 5025231064 | Alvin Zanua Putra | Matematika Diskrit - E |

</div>

<br>

# Kuroni and Impossible Calculation (Codeforces 1305C)

# Daftar Isi

1. [Deskripsi Masalah](#deskripsi-masalah)
2. [Solusi Kode](#solusi-kode)
3. [Penjelasan Kode](#penjelasan-kode)
4. [Analisis Optimasi dengan Prinsip Pigeonhole](#analisis-optimasi-dengan-prinsip-pigeonhole)
5. [Langkah Penyelesaian](#langkah-penyelesaian)
6. [Contoh Perhitungan](#contoh-perhitungan)
7. [Hasil](#hasil)
8. [Kesimpulan](#kesimpulan)

## Deskripsi Masalah

Membuat program dengan batas waktu per tes1 detik, batas memori per tes256 megabita disini saya menggunakan python.

#### Dengan soal :

Untuk menjadi raja Codeforces, Kuroni harus memecahkan masalah berikut.
Dia diberikan `n` angka `a1, a2, ..., an`. Bantu Kuroni menghitung `∏1 ≤ i < j ≤ n | ai - aj |`. Karena hasilnya bisa sangat besar, outputnya adalah modulo `m`.
Jika Anda tidak terbiasa dengan notasi pendek `∏1 ≤ i < j ≤ n |ai-aJ|` sama dengan `| a1 - a2 | * |a1 - a3| * ... * |a1 - an| * |a2 - a3| * |a2 - a4| * ... *|a2 - an|* ...*|an - 1 - an|`. Dengan kata lain, ini adalah produk dari `|a2 -a3|` untuk semua `1 ≤ i < j ≤ n`.

**Masukan**:

Baris pertama berisi dua bilangan bulat `n, m (2 <= n <= 2 * 10^5, 1 <= m <= 1000)` — jumlah angka dan modulo.

Baris kedua berisi `n` integer `a1, a2, ... an (0 <= ai <= 10^9)`.

**Keluaran** :

Angka tunggal — `∏1 ≤ i < j ≤ n|ai - aj|` mod m.

#### Contoh 1

**Input**:

```
2 10
8 5
```

**Output**:

```
3
```

#### Contoh 2

**Input**:

```
3 12
1 4 5
```

**Output**:

```
0
```

#### Contoh 3

**Input**:

```
3 7
1 4 9
```

**Output**:

```
1
```

## Solusi Kode

Kode Python berikut menyelesaikan masalah ini dengan memanfaatkan prinsip _pigeonhole_ untuk optimasi.

```python
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

# masukan
n, m = map(int, input().split())
a = list(map(int, input().split()))

# cetak
print(solve(n, m, a))
```

Klik [Link Google Colab](https://colab.research.google.com/drive/1CNKsKDkl35-BK2ZkMR1xArzqZqlO9c-w?usp=sharing) untuk menjalankan dan menganalisis kode ini di Google Colab.

# Penjelasan kode

```bash
def solve(n, m, a):
    if n > m:
        return 0
```

Fungsi solve dimulai dengan memeriksa apakah jumlah elemen `n` lebih besar dari nilai `m`. Berdasarkan prinsip `pigeonhole`, jika `n > m`, maka pasti ada dua elemen dalam `a` yang memiliki selisih `0` jika dihitung dalam modulo `m`, yang akan membuat hasil perkalian menjadi `0`. Jadi, jika `n > m`, kita langsung mengembalikan hasil `0`.

```bash
    result = 1
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            result = (result * diff) % m
            if result == 0:
                return 0
    return result
```

Jika `n` tidak lebih besar dari `m`, kita inisialisasi result dengan `1`. Kemudian, kita melakukan iterasi for untuk setiap pasangan elemen `(i, j)` dengan `i < j`, menghitung selisih absolut `|ai - aj|`, dan memperbarui `result` dengan mengalikan `diff` lalu mengambil hasil `modulo m`. Jika pada titik tertentu result menjadi `0`, kita langsung mengembalikan `0` karena hasil akhir akan tetap `0`.

```bash
# masukan
n, m = map(int, input().split())
a = list(map(int, input().split()))

# cetak
print(solve(n, m, a))
```

Bagian ini membaca input: `n` dan `m` dari input pertama, lalu daftar angka `a`. Terakhir, kita memanggil fungsi `solve` dan mencetak hasilnya.

### Langkah Penyelesaian

1. **Cek Kondisi Pigeonhole**: Jika `(n > m)`, kita langsung mengembalikan hasil `0` karena ada kemungkinan produk bernilai `0` dalam modulo `m`.
2. **Perhitungan Selisih**: Jika `(n > m)`, kita menghitung setiap pasangan selisih `|ai - aj|`, kemudian mengambil modulus `m` setiap kali hasil diperbarui.
3. **Penghentian Awal**: Jika selama perhitungan ditemukan hasil produk yang bernilai `0`, kita dapat langsung menghentikan perhitungan dan mengembalikan hasil `0`.

### Contoh Perhitungan

- **Input** : `n = 3, m = 12, a = [1, 4, 5]`

  Perhitungan selisih: `|1 - 4| = 3, |1 - 5| = 4, |4 - 5| = 1`.
  Produk selisih: `3 * 4 * 1 = 12 ≡ 0 (mod 12)`.

- **Output**: `0`, karena hasil perkalian `modulo 12` menghasilkan `0`.
- **Input**: `n = 3, m = 7, a = [1, 4, 9]`

  Perhitungan selisih: `|1 - 4| = 3, |1 - 9| = 8 ≡ 1 (mod 7), |4 - 9| = 5`.
  Produk selisih: `3 * 1 * 5 = 15 ≡ 1 (mod 7)`.

- **Output** : `1`.

## Analisis Optimasi dengan Prinsip Pigeonhole

Prinsip _pigeonhole_ menyatakan bahwa jika `(n > m)`, maka pasti ada dua elemen dalam daftar yang memiliki sisa pembagian yang sama saat dibagi `(m)`. Hal ini menyebabkan salah satu perbedaan `|ai - aj|` bernilai `0` dalam modulo `m`, yang membuat hasil perkalian akhir menjadi `0`.

## Hasil

- Submission di Google Colab :

  ![alt text](/assets/image.png)

  ![alt text](/assets/image-1.png)

  ![alt text](/assets/image-2.png)

- Submission di Code Force :
  ![alt text](/assets/image-3.png)

## Kesimpulan

Dengan demikian, Prinsip `Pigeonhole` dalam program ini digunakan untuk mengeluarkan hasil `0` ketika `n > m`, menghitung hasil dengan efisien, memanfaatkan prinsip _pigeonhole_ untuk mempercepat perhitungan pada kondisi tertentu.
