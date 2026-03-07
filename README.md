# cache-eviction

## Student Information
- **Name:** Steven Davis
- **UFID:** 63144483

- **Name:** Sebastian Robalino-Ordonez
- **UFID:** 84159795

## Instructions to Compile/Build
This project is written in Python, so it does not require an explicit compilation or build step. Ensure you have Python 3 installed on your system.
You can verify your installation by running:
```bash
python --version
```
*(Depending on how Python is installed, you might need to use `python3` instead of `python`)*

## Instructions to Run the Program
1. Open a terminal or command prompt.
2. Navigate to the `src` directory within the project folder. **This is required because the file paths are relative.**
   ```bash
   cd src
   ```
3. Run `main.py` using Python:
   ```bash
   python main.py
   ```
The program will automatically process the four provided example input files located in `../data/` and print out the cache eviction results for LRU, FIFO, and OPTFF policies.

### Example Commands:
```bash
cd cache-eviction/src
python main.py
```

## Assumptions
- **Python Version:** The script is assumed to run on Python 3.x.
- **Input Format:** 
  - Line 1: Contains the values for `k` (cache size) and `m` (number of requests) separated by a space.
  - Line 2: Contains `m` integers representing the sequence of page requests, separated by spaces.
- **File Structure:** The script `main.py` expects the input files (`example1.in`, `example2.in`, `example3.in`, `example4.in`) to be located exactly at the relative path `../data/`. The script must be executed from inside the `src` directory.
- **Output:** The output is printed directly to standard output (the terminal) per the format in `main.py`. It shows the input file path followed by the results sequence for exactly three algorithms: LRU, FIFO, and OPTFF.

## Written Component Solutions
[see pdf for solutions](Programming_Assignment_2_Written.pdf)