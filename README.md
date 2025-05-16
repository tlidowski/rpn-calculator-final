# CLI RPN Calculator

A command-line reverse polish notation (RPN) calculator using Python.

## Table of Contents

1. [Description](#description)
2. [Architecture & Design](#architecture--design)  
   2.1 [Reasoning](#reasoning)  
   2.2 [Trade-offs](#trade-offs)
3. [Getting Started](#getting-started)  
   3.1 [Prerequisites](#prerequisites)  
   3.2 [Installation](#installation)
4. [Usage](#usage)  
   4.1 [Example Input/Output](#example-inputoutput)  
   4.2 [Future Roadmap](#future-roadmap)
5. [Contributing](#contributing)
6. [Contact](#contact)

## Description

This project is a command-line Reverse Polish Notation (RPN) calculator implemented in Python.

It supports the four default standard operators (+, -, \*, /) and is designed for UNIX-like CLI environments, using standard input and output.

## Architecture & Design

### Key features:

- Stack-based design: Operands are pushed and popped to evaluate expressions based on RPN calculations.
- Error handling & recovery: Handles invalid inputs and other errors/excceptions.
- Modular operator catalog: Supports expansion for more operators.
- Planned future developments: Supports expansion for alternate I/O input.

### Reasoning

#### Architecture

- Modular components
  - Easy to understand and maintain
  - Test components separately
  - Enables switching between components (ex. new inputs)
- Operator catalog
  - Separates the logic from implementation
  - Easy to add new operators
- Interface
  - Not tightly coupled with logic
  - Extend the project to support additional input methods
- SRP
  - Separates responsibilities in components
  - Cleaner code that's easier to maintain and debug

#### Testing: pytest

- Advantages:
  - Simple syntax and assertions
  - Detailed error tracing
  - Fixtures and parameters for testing
- Future changes to I/O handling won't affect tests for calculations:
  - Core functions (default operations, allowed input formats)
  - Error handling (ZeroDivisionError, ValueError)
  - Unique inputs (unicode, additional whitespace)
  - Float precision (float storage, comparisons with margin of error)
  - Edge cases (large/extreme values, negative zero)

#### Language Choice: Python

- Contributor's familiarity with past projects and experience
- Clean syntax for simplicity and readability (focus on design, data structures, and OOP principles)
- Available libraries for arithmetic, testing, and future expansions
- Cross-platform and easy to run/share projects

### Future Roadmap & Improvements

- Additional operators
- Alternative I/O
- Interactive CLI Commands (help, history, view)
- Additional testing methods (pytest-benchmark)
- UI enhancements (spacing, separating charcters, etc)
- Accessibility features (localization)

## Getting Started

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/) for installing dependencies

### Installation

1. `git clone` https://github.com/tlidowski/rpn-calculator-final.git
2. `cd rpn_calculator`
3. `pip install -e .`
4. Run using `rpn`

## Usage

### Example Input/Output

```
> 5
5
> 8
8
> +
13
```

```
> 5 5 5 8 + + -
-13.0
> 13 +
0.0
```

```
> -3
-3.0
> -2
-2.0
> *
6.0
> 5
5.0
> +
11.0
```

```
> 5
5
> 9
9
> 1
1
> -
8
> /
0.625
```

## Contact

- Tia Lidowski - tiallidowski@gmail.com
- Project Link - https://github.com/tlidowski/rpn-calculator-final.git

## Acknowledgements

- [CLI RPN Calculator Code Problem](https://github.com/snap-mobile/take-home-exercise.git)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Angular Convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)
