# Monthly Report Automation

A beginner Python project that turns a monthly transactions file into a summary report.

## Why I'm building this

In finance and administrative work, I built monthly reports in Excel by hand: collecting transactions, grouping them, and checking the totals. I'm learning Python to automate that process.

## What it does

- Reads a CSV file of sample transactions (dummy data only, no real financial information)
- Groups spending by month
- Prints a monthly spending report

## How to run it

1. Make sure Python 3 is installed
2. Download this repository
3. Run this command in the project folder:

```
python3 report.py
```

## Sample output

```
Monthly spending report
-----------------------
2026-01: 181.00
2026-02: 135.75
2026-03: 151.25
```

## What I learned

- How to group transactions by month using the first part of each date
- How to reuse the same dictionary-totals approach from my first project on a new problem

## Next steps

- Add totals by category within each month
- Save the report to a new file
