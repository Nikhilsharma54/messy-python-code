# Messy Python Code Improvement

`messy_code.py` is the original script. It works, but it is hard to read. `improved_code.py` is the same program after I cleaned it up with AI help.

## What was wrong
- One-letter names such as `f`, `a`, `x`, `y`, `l`, `m`
- One-space indentation and no blank lines
- Averaging, grading and printing all mixed in one function
- A long `if / elif` chain for grades
- The same call repeated for each student

## What I changed
- Gave everything clear names
- Split the work into `calculate_average`, `get_grade` and `print_result`
- Moved the grade limits into one list, `GRADE_LIMITS`
- Added docstrings and formatted the output

## Run
```
python messy_code.py
python improved_code.py
```
