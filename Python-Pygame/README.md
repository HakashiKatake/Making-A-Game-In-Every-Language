# Space Invaders Game - Python & Pygame

This is a classic Space Invaders-style arcade game built with Python and Pygame as part of the Making A Game In Every Language project.

![Gameplay Screenshot](img/bg.png)

## 🎮 Game Overview

Control your spaceship to defend against waves of aliens. Shoot down all the aliens to win, but be careful - they're shooting back! Your spaceship has a health bar that decreases when hit by alien projectiles.

## ⚙️ Prerequisites

- Python 3.x
- Pygame library

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HakashiKatake/Making-A-Game-In-Every-Language.git
   cd Making-A-Game-In-Every-Language/Python-Pygame
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   # Create virtual environment
   python -m venv myenv
   
   # Activate virtual environment
   # On Windows:
   myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install Pygame**
   ```bash
   pip install pygame
   ```

4. **Run the game**
   ```bash
   python main.py
   ```

## 🕹️ How to Play

### Controls
- **Movement**: Arrow keys (Left/Right) or A/D keys
- **Shoot**: Spacebar or Left Mouse Button
- **Quit**: Close the window

### Objective
Destroy all the alien ships without losing all your health. Your health bar is displayed below your spaceship and decreases when hit by alien projectiles.

## ✨ Game Features

- Multiple types of alien enemies with random selection
- Health system with visual health bar
- Sound effects for shooting and explosions
- Animated explosions
- Victory and defeat conditions
- Countdown timer before game start

## 🔍 Code Structure

- [`Python-Pygame/main.py`](Python-Pygame/main.py ) - Contains the entire game logic
- [`img/`](Python-Pygame/main.py ) - Contains all game assets (sprites and sound effects)
  - Spaceship sprite
  - Alien sprites (5 variations)
  - Bullet sprites
  - Explosion animation frames
  - Background image
  - Sound effects (laser, explosions)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Game created as part of the "Making A Game In Every Language" project
- Built with [Pygame](https://www.pygame.org), a set of Python modules designed for writing video games

---

> *"Let's journey through code, one game at a time!"* — Saurabh