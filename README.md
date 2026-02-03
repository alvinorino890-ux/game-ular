# game-ular
tugas sentra python

1.🐍 Deskripsi Game Ular (Snake Game)

Game Ular adalah game klasik sederhana yang dibuat menggunakan bahasa pemrograman Python dengan bantuan library Tkinter sebagai tampilan grafis.
Pada game ini, pemain mengontrol seekor ular yang bergerak di dalam arena kotak-kotak untuk memakan apel.

Setiap kali ular memakan apel, skor akan bertambah dan panjang tubuh ular meningkat. Game ini dilengkapi dengan beberapa fitur tambahan seperti sistem nyawa, high score, dan tombol restart, sehingga permainan menjadi lebih menarik dan tidak langsung berakhir saat terjadi tabrakan.

Game ini melatih logika pemrograman, penggunaan fungsi, event keyboard, serta konsep game loop.

🎮 Cara Bermain Game Ular
Game dimulai dengan ular berada di tengah layar.
Pemain menggerakkan ular menggunakan tombol arah pada keyboard:
⬆️ Atas
⬇️ Bawah
⬅️ Kiri
➡️ Kanan

Ular harus diarahkan untuk memakan apel berwarna merah.
Setiap apel yang dimakan akan menambah skor dan panjang ular.
Pemain harus menghindari tabrakan agar game tidak berakhir.

📜 Rules / Aturan Game Ular
❌ Ular tidak boleh menabrak dinding arena.
❌ Ular tidak boleh menabrak tubuhnya sendiri.
❤️ Ular memiliki 3 nyawa.

Jika menabrak, nyawa berkurang 1.
Jika nyawa masih ada, game akan dilanjutkan.
☠️ Jika nyawa habis, maka Game Over.
🏆 Skor tertinggi akan disimpan sebagai High Score.
🔁 Pemain dapat menekan tombol Restart untuk memulai ulang game setelah Game Over.
🔄 Ular tidak bisa langsung berbalik arah (misalnya dari kiri langsung ke kanan).
🎯 Tujuan Game

Tujuan dari game ini adalah:
Mengumpulkan skor sebanyak mungkin
Melatih kecepatan berpikir dan refleks pemain
Menghindari tabrakan selama permainan berlangsung

2.penjelasan high score

High Score adalah skor tertinggi yang pernah dicapai oleh pemain dalam game ular.
Fitur ini digunakan untuk menyimpan pencapaian terbaik pemain, sehingga pemain memiliki target untuk mendapatkan skor yang lebih tinggi di setiap permainan.
Pada game ini, High Score tidak hilang meskipun game ditutup, karena disimpan ke dalam sebuah file bernama highscore.txt.

⚙️ Cara Kerja High Score

Saat game dijalankan, sistem akan:
Mengecek apakah file highscore.txt tersedia
Jika ada, skor tertinggi akan dibaca dan ditampilkan
Jika tidak ada, high score akan bernilai 0

Selama permainan:
Skor akan bertambah setiap kali ular memakan apel

Saat Game Over:
Skor saat ini dibandingkan dengan High Score
Jika skor lebih besar, maka:
High Score diperbarui
Data disimpan ke file highscore.txt

💾 Fungsi High Score:
🏁 Memberi tantangan kepada pemain untuk mengalahkan skor sebelumnya
📊 Menjadi indikator kemampuan pemain
💡 Membuat game lebih menarik dan kompetitif
💾 Menyimpan data secara permanen menggunakan file
