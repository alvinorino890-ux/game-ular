import tkinter as tk          # Library GUI Tkinter
import random                 # Untuk posisi acak apel
import os                     # Untuk cek file high score

# ================== KONFIGURASI ==================
WIDTH = 500                          # Lebar layar
HEIGHT = 500                         # Tinggi layar
SIZE = 25                            # Ukuran kotak
SPEED = 120                          # Kecepatan ular
HIGHSCORE_FILE = "highscore.txt"     # File penyimpan high score
MAX_LIVES = 3                        # Jumlah nyawa ular

# ================== GAME ULAR ==================
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        # Canvas utama
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.direction = "Right"   # Arah awal
        self.running = True        # Status game

        # Posisi awal ular
        self.snake = [(125, 250), (100, 250), (75, 250)]

        self.food = self.create_food()   # Buat apel
        self.score = 0                   # Skor saat ini
        self.high_score = self.load_high_score()  # High score dari file
        self.lives = MAX_LIVES           # Nyawa awal

        # Kontrol keyboard
        root.bind("<Up>", lambda e: self.change_direction("Up"))
        root.bind("<Down>", lambda e: self.change_direction("Down"))
        root.bind("<Left>", lambda e: self.change_direction("Left"))
        root.bind("<Right>", lambda e: self.change_direction("Right"))

        self.update()   # Mulai game

    # ================== LOAD HIGH SCORE ==================
    def load_high_score(self):
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "r") as f:
                return int(f.read())
        return 0

    # ================== SAVE HIGH SCORE ==================
    def save_high_score(self):
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(self.high_score))

    # ================== MEMBUAT APEL ==================
    def create_food(self):
        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)
        return (x, y)

    # ================== UBAH ARAH ==================
    def change_direction(self, new_dir):
        lawan = {"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}
        if new_dir != lawan.get(self.direction):
            self.direction = new_dir

    # ================== UPDATE GAME ==================
    def update(self):
        if not self.running:
            return

        x, y = self.snake[0]

        if self.direction == "Up": y -= SIZE
        elif self.direction == "Down": y += SIZE
        elif self.direction == "Left": x -= SIZE
        elif self.direction == "Right": x += SIZE

        head = (x, y)

        # Cek tabrakan
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or head in self.snake:
            self.lose_life()
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.update)

    # ================== KEHILANGAN NYAWA ==================
    def lose_life(self):
        self.lives -= 1

        if self.lives <= 0:
            self.game_over()
            return

        # Reset posisi ular jika masih ada nyawa
        self.snake = [(125, 250), (100, 250), (75, 250)]
        self.direction = "Right"
        self.draw()
        self.root.after(800, self.update)

    # ================== GAMBAR ==================
    def draw(self):
        self.canvas.delete("all")

        # Background kotak-kotak
        for i in range(0, WIDTH, SIZE):
            for j in range(0, HEIGHT, SIZE):
                warna = "#CAD43A" if (i+j)//SIZE % 2 == 0 else "#C6C636"
                self.canvas.create_rectangle(i, j, i+SIZE, j+SIZE, fill=warna, outline="")

        # Gambar ular
        for i, (x, y) in enumerate(self.snake):
            self.canvas.create_oval(x, y, x+SIZE, y+SIZE, fill="#BC7B2D", outline="")
            if i == 0:
                self.canvas.create_oval(x+6, y+7, x+11, y+12, fill="white")
                self.canvas.create_oval(x+14, y+7, x+19, y+12, fill="white")

        # Gambar apel
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+SIZE, fy+SIZE, fill="red", outline="")

        # Skor, High Score, Nyawa
        self.canvas.create_text(60, 15, text=f"🍎 {self.score}", fill="white", font=("Arial", 14, "bold"))
        self.canvas.create_text(WIDTH//2, 15, text=f"❤️ {self.lives}", fill="white", font=("Arial", 14, "bold"))
        self.canvas.create_text(WIDTH-80, 15, text=f"🏆 {self.high_score}", fill="white", font=("Arial", 14, "bold"))
        
        # Watermark / credit
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT - 10,
            text="by Alvino Aldorino",
            fill="white",
            font=("Arial", 10, "italic")
        )


    # ================== GAME OVER ==================
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.running = False

        self.canvas.create_text(WIDTH//2, HEIGHT//2 - 20, text="GAME OVER", fill="white", font=("Arial", 28, "bold"))

        restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 12, "bold"), command=self.restart)
        self.canvas.create_window(WIDTH//2, HEIGHT//2 + 20, window=restart_btn)

    # ================== RESTART ==================
    def restart(self):
        self.score = 0
        self.lives = MAX_LIVES
        self.direction = "Right"
        self.snake = [(125, 250), (100, 250), (75, 250)]
        self.food = self.create_food()
        self.running = True
        self.update()

# ================== JALANKAN ==================
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()