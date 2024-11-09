
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wn_8YGI-)

<div align=center>

|    NRP     |       Nama        |         Kelas         |
| :--------: | :---------------: | :-------------------: |
| 5025231064 | Alvin Zanua Putra | Matematika Diskrit - E |

</div>

<br>

# Kuroni and Impossible Calculation (Codeforces 1305C)

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

Kode Python berikut menyelesaikan masalah ini dengan memanfaatkan prinsip *pigeonhole* untuk optimasi.

```python
def solve(n, m, a):
    result = 1
    # Loop untuk menghitung produk |ai - aj|
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            result = (result * diff) % m
            if result == 0:  # Jika hasil sudah 0, langsung keluar
                return 0
    return result

# Membaca input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Memanggil fungsi dan mencetak hasil
print(solve(n, m, a))
```

Klik [Link Google Colab](https://colab.research.google.com/drive/1CNKsKDkl35-BK2ZkMR1xArzqZqlO9c-w?usp=sharing) untuk menjalankan dan menganalisis kode ini di Google Colab.

## Analisis Optimasi dengan Prinsip Pigeonhole

Prinsip *pigeonhole* menyatakan bahwa jika `(n > m)`, maka pasti ada dua elemen dalam daftar yang memiliki sisa pembagian yang sama saat dibagi `(m)`. Hal ini menyebabkan salah satu perbedaan `|ai - aj|` bernilai `0` dalam modulo `m`, yang membuat hasil perkalian akhir menjadi `0`.

### Langkah Penyelesaian

1. **Cek Kondisi Pigeonhole**: Jika `(n > m)`, kita langsung mengembalikan hasil `0` karena ada kemungkinan produk bernilai `0` dalam modulo `m`.
2. **Perhitungan Selisih**: Jika `(n > m)`, kita menghitung setiap pasangan selisih `|a_i - a_j|`, kemudian mengambil modulus `m` setiap kali hasil diperbarui.
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


Dengan demikian, solusi ini menghitung hasil dengan efisien, memanfaatkan prinsip *pigeonhole* untuk mempercepat perhitungan pada kondisi tertentu.
