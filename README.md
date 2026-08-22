# KBC Quiz Game

A Python implementation of **Kaun Banega Crorepati (KBC)**, the popular Indian television quiz show. This interactive trivia game challenges players across three difficulty levels with strategic lifeline mechanics.

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Overview

KBC Quiz Game is a terminal-based trivia application that simulates the experience of competing in India's premier quiz show. Players must answer progressively difficult questions while strategically utilizing lifelines to reach the ultimate goal of answering all questions correctly.

## Features

- **Three Difficulty Levels**: Easy, Medium, and Extreme
- **Progressive Gameplay**: 5 questions per difficulty level with increasing complexity
- **Four Strategic Lifelines**:
  - **50-50**: Eliminates two incorrect answers
  - **Audience Poll**: Shows simulated audience voting percentages
  - **Double Dip**: Grants two attempts for a single question
  - **Expert Advice**: Expert recommendation on the correct answer
- **Comprehensive Question Bank**: 75+ diverse questions spanning:
  - Geography & History
  - Science & Mathematics
  - General Knowledge
  - Culture & Literature
  - Indian Studies
- **Score Tracking**: Real-time feedback on performance

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/kbc-game.git
cd kbc-game
```

2. No external dependencies required! The game uses only Python's standard library.

## Usage

### Running the Game

```bash
python kbc.py
```

### Game Flow

1. **Welcome Screen**: Read game rules and instructions
2. **Select Difficulty**: Choose between Easy, Medium, or Extreme
3. **Answer Questions**: Answer 5 questions at your selected difficulty level
4. **Use Lifelines**: Select lifelines strategically to help answer questions
5. **Win Condition**: Answer all 5 questions correctly to win

### Example Session

```
hello user! wellcome to KBC game 
before starting the Game let me tell you some rules and instructions--->

->you have to complete 5 levels in the difficulty you chose to win this game
->you will be given four lifelines
->you can choose any lifeline you want and can choose maximum of 1 lifelines for each level

Choose the difficulty level
A)easy
B)medium
C)extreme
```

## Game Rules

1. **Difficulty Levels**: Each level must be completed sequentially within the chosen difficulty tier
2. **Lifeline Usage**: Each lifeline can be used only once per game
3. **One Lifeline Per Question**: You may use at most one lifeline per question
4. **Correct Answers**: Type the option letter (A, B, C, or D) in uppercase
5. **Winning**: Successfully answer all 5 questions in your chosen difficulty to win

## Difficulty Levels

### Easy
- Basic general knowledge questions
- Suitable for beginners
- Examples: Capitals, basic science facts, fundamental history

### Medium
- Intermediate complexity questions
- Requires moderate knowledge
- Examples: Advanced geography, historical events, scientific concepts

### Extreme
- Challenging and specialized questions
- High difficulty level
- Examples: Obscure historical facts, complex scientific theories, specialized knowledge

## Lifelines Explained

### 50-50
Removes two incorrect options, leaving the correct answer and one incorrect option.

### Audience Poll
Displays simulated audience voting percentages for each option (weighted toward the correct answer).

### Double Dip
Allows two attempts to answer the current question. First incorrect answer doesn't end the game; you get a second try.

### Expert Advice
An expert in the field suggests the correct answer based on their analysis.

## Project Structure

```
kbc-game/
├── kbc.py                 # Main game file
├── README.md             # Project documentation
├── LICENSE               # MIT License
└── .gitignore           # Git ignore rules
```

## Code Architecture

### Key Functions

- `random_cho(arg)`: Randomly selects a question from the question bank
- `fifty_fifty(question)`: Implements the 50-50 lifeline logic
- `audience_poll(question)`: Generates simulated audience voting data
- `double_dip(question)`: Manages two-attempt lifeline functionality
- `expert_advice(question)`: Provides expert recommendation
- `life_line()`: Manages lifeline selection and usage tracking
- `difficulty_f(difficulty, level_list)`: Main game engine for question progression

### Question Format

Questions are stored as dictionaries with the following structure:

```python
{
    'question': 'Q1. Question text here?',
    'options1': {
        'A': 'Option A text',
        'B': 'Option B text',
        'C': 'Option C text',
        'D': 'Option D text'
    },
    'options': 'A) Option A   B) Option B   C) Option C   D) Option D',
    'answer': 'C'  # Correct option
}
```

## System Requirements

- **RAM**: Minimal (< 10 MB)
- **Storage**: ~50 KB
- **Platform**: Windows, macOS, Linux
- **Terminal**: Any standard terminal/console

## Future Enhancements

- [ ] Score leaderboard system
- [ ] Custom question bank loading from CSV/JSON
- [ ] Difficulty-based scoring system with prize tiers
- [ ] Graphical user interface (GUI) with Tkinter
- [ ] Multiplayer modes
- [ ] Question categories selection
- [ ] Hint system
- [ ] Timed questions for increased difficulty
- [ ] Database integration for persistent scoring

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Areas for Contribution

- Adding new questions
- Improving code documentation
- Refactoring and code optimization
- Bug fixes
- Feature implementations

## Bug Reports

Found a bug? Please open an issue with:
- Description of the bug
- Steps to reproduce
- Expected vs. actual behavior
- Python version and operating system

## Performance Notes

- Game runs entirely in memory
- No database queries or network calls
- Instant question loading
- Minimal CPU usage
- Suitable for low-end systems

## Troubleshooting

### Issue: Input not recognized
**Solution**: Ensure you're entering uppercase letters (A, B, C, or D) only

### Issue: Lifeline already used
**Solution**: Each lifeline can only be used once per game. Choose a different lifeline or proceed without one.

### Issue: Game crashes unexpectedly
**Solution**: Ensure Python 3.6+ is installed and you're running the latest version of the code

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## Acknowledgments

- Inspired by Sony Entertainment Television's **Kaun Banega Crorepati**
- Built with Python's standard library
- Question database compiled from general knowledge sources

## Author

Developed as an educational project to demonstrate Python game development and interactive programming concepts.

## Support

For questions or issues, please open an issue on the GitHub repository or contact the development team.

---

**Enjoy the game and may you become a Crorepati!** 🎉
