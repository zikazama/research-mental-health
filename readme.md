# Cara Install
1. Jalankan `git clone https://github.com/zikazama/research-mental-health.git`
2. Python3 index.py

# Penjelasan
Berikut adalah kode untuk melakukan penelitian tentang mental health.

## Mengumpulkan data twitter
-   **API Twitter**: Menggunakan Twitter API untuk mengakses dan mengumpulkan tweet yang relevan. Anda bisa menggunakan endpoint seperti `GET search/tweets` untuk mencari tweet berdasarkan kata kunci yang terkait dengan kesehatan mental (misalnya, "depresi", "kecemasan", "stres", "bantuan", dll.).
-   **Filter Bahasa**: Menggunakan parameter `lang=id` untuk memastikan hanya tweet dalam bahasa Indonesia yang dikumpulkan.

## Proses data
-   **Pembersihan Data**: Menghilangkan tweet duplikat, hapus tanda baca, URL, mention, hashtag, dan karakter khusus lainnya.
-   **Tokenisasi**: Memisahkan teks tweet menjadi kata-kata atau token untuk analisis lebih lanjut.
-   **Normalisasi**: Mengubah semua teks menjadi huruf kecil dan lakukan stemming atau lemmatization untuk mengurangi variasi kata.

## Analisis
Menggunakan model pembelajaran mesin atau alat analisis sentimen seperti TextBlob, VADER, atau model berbasis transformator (misalnya BERT) yang telah dilatih untuk bahasa Indonesia untuk mendeteksi sentimen dan emosi dalam tweet. Disini saya menggunakan transformator dari python.

## Klasifikasi
-   **Kategorisasi**: Mengkategorikan tweet berdasarkan tingkat keparahan atau jenis masalah kesehatan mental yang diungkapkan.
-   **Visualisasi Data**: Membuat visualisasi data untuk menggambarkan distribusi sentimen dan jenis masalah kesehatan mental di antara tweet.