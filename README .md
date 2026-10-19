# 🎯 KBC Quiz Game

A terminal-based Python version of **Kaun Banega Crorepati (KBC)**, the Indian TV quiz show. Pick a difficulty, answer five questions in a row, and use four lifelines wisely. One wrong answer ends the game.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Lifelines](#lifelines)
- [Question Bank](#question-bank)
- [How It Works](#how-it-works)
- [Known Issues](#known-issues)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## Features

- **3 difficulty levels**: Easy, Medium and Extreme
- **5 rounds per game**: each round picks one random question from a pool of 3, so replays feel different
- **4 lifelines**: 50-50, Audience Poll, Double Dip and Expert Advice
- **Case-insensitive input**: `b` and `B` both work
- **Zero dependencies**: standard library only (`random`)

---

## Project Structure

```
kbc-game/
├── KBC_functions.py   # Lifelines, game engine (difficulty_f), welcome text, difficulty prompt
├── KBC_question.py    # Question bank for all 3 difficulties + game launch
└── README.md
```

| File | Responsibility |
|---|---|
| `KBC_functions.py` | `random_cho`, `fifty_fifty`, `audience_poll`, `double_dip`, `expert_advice`, `life_line`, `difficulty_f`. Also prints the rules and asks for the difficulty. |
| `KBC_question.py` | Builds `level1`–`level5` for the chosen difficulty and calls `difficulty_f(...)`. |

---

## Getting Started

### Prerequisites

- Python 3.6 or higher (uses f-strings). No `pip install` needed.

### Clone

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### Run

`KBC_question.py` uses `difficulty` and `difficulty_f`, which are defined in `KBC_functions.py`, so the two files must be linked. Add this line at the **very top** of `KBC_question.py`:

```python
from KBC_functions import *
```

Then start the game:

```bash
python KBC_question.py
```

> Running `KBC_functions.py` alone only shows the rules and asks for a difficulty. Running `KBC_question.py` without the import above fails with `NameError: name 'difficulty' is not defined`.

---

## How to Play

1. Read the rules and choose a difficulty:
   - `A` → Easy
   - `B` → Medium
   - `C` → Extreme
2. For each of the 5 rounds, the game shows a question with four options.
3. Before answering, you are asked whether you want a lifeline (`yes` / `no`).
4. Type the option letter (`A`, `B`, `C` or `D`) to answer.
5. Answer all 5 correctly to win. A wrong answer ends the game and reveals the correct option.

### Rules

| Rule | Detail |
|---|---|
| Lifelines per game | 4 in total, each usable **once** |
| Lifelines per question | At most **one** |
| Wrong answer | Game over |
| Win condition | 5 correct answers in a row |

### Sample session

```
hello user! wellcome to KBC game
...
there are three difficulty level:-
A)easy
B)medium
C)extreme
Choose the difficulty level
A
you have chosen EASY level !

Q1. Which planet is known as the Red Planet?

A) Venus   B) Mars   C) Jupiter  D) Saturn

do you want to choose life line??
enter 'yes' or 'no' : no
enter your option
B
WOW!
your answer is correct
```

---

## Lifelines

At the lifeline prompt, answer `yes`, then choose a letter:

| Key | Lifeline | What it does |
|---|---|---|
| `A` | **50-50** | Shows the correct option plus one random wrong option. |
| `B` | **Audience Poll** | Shows simulated vote percentages for all four options. The correct option gets a preset share (32–56%) and the remainder is split randomly. The correct option is **not guaranteed to be the top vote**. |
| `C` | **Double Dip** | Lets you try twice. The first guess is checked and you are told whether it was right. You then enter your final answer. |
| `D` | **Expert Advice** | Names the correct option. |

The welcome text in the code calls the fourth lifeline "phone a friend", while the implemented function is `expert_advice`.

---

## Question Bank

**45 questions in total**: 15 per difficulty (5 levels × 3 questions each). Topics include Indian history and polity, geography, science, general knowledge and culture.

| Difficulty | Level 1 → 5 style |
|---|---|
| Easy | Everyday facts (planets, capitals, basic science) |
| Medium | Moderate GK (history, economics, biology, geography) |
| Extreme | Specialised facts (physics, history, scientific terms) |

### Question format

```python
{
    'question': 'Q1. Which planet is known as the Red Planet?',
    'options1': {'A': 'Venus', 'B': 'Mars', 'C': 'Jupiter', 'D': 'Saturn'},  # used by lifelines
    'options':  'A) Venus   B) Mars   C) Jupiter  D) Saturn',               # shown to the player
    'answer':   'B'
}
```

### Adding questions

1. Open `KBC_question.py` and find the difficulty block (`"A"`, `"B"` or `"C"`) and the `levelN` list.
2. Append a dictionary in the format above.
3. Keep the keys `A`–`D` exactly (no spaces) and make `options` match `options1`.

---

## How It Works

```
KBC_functions.py                     KBC_question.py
┌───────────────────────┐            ┌──────────────────────────┐
│ print rules           │            │ if difficulty == "A": ...│
│ input() → difficulty  │───import──▶│ build level1..level5     │
│ lifelines + engine    │            │ difficulty_f(name,[...]) │
└───────────────────────┘            └──────────────────────────┘
```

**Game loop (`difficulty_f`)**, repeated for 5 rounds:

1. `random_cho` picks one question from the level's pool.
2. `life_line()` asks about a lifeline and returns a code (`0` none, `1`–`4` lifelines).
3. The matching lifeline function runs.
4. The player's answer is compared with `question['answer']`. A wrong answer breaks the loop.
5. Clearing all 5 rounds prints the congratulations message.

**State**: `life_used` (dict) and `life_count` (int) are module-level globals that track lifeline usage for the whole game.

---

## Known Issues

Found while reviewing and running the code. These are good first contributions:

| # | Issue | Where | Effect |
|---|---|---|---|
| 1 | `count` is only set after a correct answer. | `difficulty_f` | Wrong answer on **Question 1** crashes with `UnboundLocalError`. Fix: set `count = -1` before the loop. |
| 2 | Invalid lifeline letter (e.g. `Z`) is not validated. | `life_line` | `KeyError` crash. |
| 3 | After "already used" lifeline, the replacement choice is read but ignored and `0` is returned. | `life_line` | Player cannot swap to another lifeline. |
| 4 | Anything other than `A`/`B`/`C` at the difficulty prompt is accepted. | bottom of `KBC_functions.py` | Program ends silently. The `opt` list is defined but never used. |
| 5 | Double Dip reveals whether the first guess was correct, then asks for the answer again. | `double_dip` / `difficulty_f` | Behaves differently from the TV lifeline. |
| 6 | Answer input is not validated. | `difficulty_f` | Typing `X` counts as a wrong answer. |
| 7 | Easy, level 3 "national bird" question has a dictionary key `' D'` (with a space). | `KBC_question.py` | 50-50 / poll can print it with odd spacing. |
| 8 | Extreme levels 4 and 5 are labelled `Q1`–`Q3` instead of `Q4` / `Q5`. | `KBC_question.py` | Cosmetic mismatch. |
| 9 | The Doctrine of Lapse question asks for an "Indian ruler" but Lord Dalhousie was a British Governor-General. | `KBC_question.py` | Wording inaccuracy. |
| 10 | The "longest river" and "who gave the concept of zero" questions have debatable answers. | `KBC_question.py` | Consider rewording. |
| 11 | There is no prize money or score tracking. | – | Game is win or lose only. |
| 12 | Game logic runs at import time, with no `main()` or `if __name__ == "__main__"` guard. | both files | Hard to test or reuse. |

---

## Roadmap

- [ ] Fix the known issues above and add input validation
- [ ] Single entry point (`main.py`) with a `main()` function
- [ ] Prize ladder with safe levels (the real KBC experience)
- [ ] Load questions from JSON/CSV instead of hard-coded dictionaries
- [ ] Make Audience Poll and Expert Advice more realistic (not always correct or top-voted)
- [ ] Larger question bank, categories and no-repeat selection
- [ ] Leaderboard and score persistence
- [ ] Timed questions
- [ ] GUI (Tkinter) or web version
- [ ] Unit tests for lifeline logic

---

## Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

Bug reports should include steps to reproduce, expected vs actual behaviour, your Python version and your OS.

---

## License

Add a `LICENSE` file (for example MIT) before publishing and update this section to match.

## Acknowledgments

Inspired by Sony Entertainment Television's *Kaun Banega Crorepati*. This is an independent educational project and is not affiliated with the show or its producers.
