# 🐍 Pygame Snake with Level Selection & Highscores

A classic **Snake game** built in Python using the **Pygame** library. The game features robust state management separating the Main Menu, an interactive Settings Menu for speed selection (3 difficulty levels), the active Gameplay, and a dedicated Game Over screen that tracks your best scores.

---

## 📸 Screenshots

| Main Menu | Level Settings | Gameplay & Highscore |
| :---: | :---: | :---: |
| ![Main Menu](https://github.com/Flockemon24/snake/docs/menu.png) | ![Settings](https://github.com/Flockemon24/snake/docs/settings.png) | ![Gameplay](https://github.com/Flockemon24/snake/docs/gameplay.png) |
| *Start Screen* | *Difficulty Levels (1-3)* | *Action & Live Score/Highscore* |


---

## ✨ Features

* **Complete State Management:** Seamless transitions between the Menu, Settings, active Gameplay, and Game Over states.
* **Persistent Highscore System:** Tracks and displays your all-time highest score both during gameplay and on the Game Over screen so you can always try to beat your personal best.
* **3 Speed Levels:** 
  * **Level 1 (Slow):** Relaxed pace, perfect for beginners (`160ms` delay).
  * **Level 2 (Normal):** The classic, balanced Snake experience (`100ms` delay).
  * **Level 3 (Fast):** A hardcore mode demanding lightning-fast reflexes (`50ms` delay).
* **Visual UI Feedback:** The Settings Menu dynamically highlights the currently active difficulty level in green.
* **Refined Mechanics:** Grid-based movement, responsive controls with anti-self-inversion logic, and precise collision detection.

---

## 🎮 Controls

### In Menus & UI
* <kbd>Space</kbd> – Start Game / Try Again
* <kbd>S</kbd> – Open Settings Menu (Level Selection)
* <kbd>M</kbd> – Return to Main Menu
* <kbd>1</kbd> / <kbd>2</kbd> / <kbd>3</kbd> – Select Level 1, 2, or 3 (while in the Settings Menu)

### In-Game (Gameplay)
* <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> – Control the snake (Arrow Keys)
* *Note: Instant reversal into the opposite direction is blocked to prevent accidental self-collision.*

---

## 🛠️ Requirements & Installation

To run this game, you need **Python 3** and the **Pygame** library installed on your system.

1. **Clone the repository or copy the code:**
   ```bash
   git clone https://github.com/Flockemon24/snake
   cd snake
   ```

2. **Install Pygame:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the game:**
   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```text
├── main.py            # The complete game code including loops, UI, and logic
├── requirements.txt   # Required libraries
└── README.md          # Project documentation (this file)
```

---

## 📝 License

This project is licensed under the MIT License. Feel free to modify, distribute, and build upon it for your own purposes.
