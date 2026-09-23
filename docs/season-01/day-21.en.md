<p align="center"><a href="day-21.md">中文</a> &nbsp;&nbsp;·&nbsp;&nbsp; <b>English</b></p>

# Day 21 · The frozen close table

[Phase I · Models](../../README.en.md) · runs

What you learn today: `days/data/panel.csv` has 160 rows, AAA and BBB, 80 sessions each, from 2024-01-02 through 2024-04-23. AAA has 1 blank close. A second read of the file text matches. The table is frozen in the repository. It is not redrawn at runtime, and it is not the five handwritten closes of days 1–20.

## Plain-language account

Open `days/data/panel.csv` in the repository and count the rows. The file has 160 of them. The names are AAA and BBB, 80 sessions each. AAA runs from 2024-01-02 through 2024-04-23, and BBB uses that same span of dates. 160 is 80 plus 80. One AAA close cell is blank. The program counts that cell as 1. Today does not fill it, and does not replace it with a neighboring close.

The check that the file was not swapped between reads compares the file text. The program reads the text at the path, reads it again, and the two strings match, so it prints `second read matches = true`. A blank close parses as NaN. NaN is not equal to NaN, so a comparison of parsed dictionaries would report a change in a file that did not change. Today's check stops at the text.

Days 1 through 20 used five closes written into the formulas: 2.1, 3.9, 6.2, 20.0, and 10.4. The residuals, the direction counts, and the noise column of those days grow out of those five numbers. From today the closes are read from these 160 rows. The script does not sample. Run it again and the text is the same text. The dates stop at 2024-04-23 and the row count stops at 160. A later hit rate or sum of squares that cites this table is a calculation on this file.

## Core

```text
path = days/data/panel.csv
rows = 160
second read matches = true
AAA dates 2024-01-02 .. 2024-04-23
AAA blank closes = 1
the table is not resampled
```

The path is `days/data/panel.csv` inside the repository. `rows = 160` is the length of the table: two names, 80 rows each, both dated 2024-01-02 through 2024-04-23. The blank-close count on AAA is 1. A blank count for BBB is not reported today.

The second read compares the two return values of `read_text()` on that path. Equality means the file text is unchanged. The check does not parse an empty string into NaN and then compare dictionaries. The empty cell stays in the file and is counted as 1.

The handwritten five closes and this table are two sets of numbers. The five closes stay in the formulas of the first twenty days. Today's object is the table frozen in the repository. The last printed line says the table is not resampled: the run does not redraw the rows and does not generate another table.

## Further out

A frozen table ties later scores to one file. Running the script again reads the same path. When the two texts match, the source of the numbers was not replaced between runs. The boundary of the table is 160 rows, a last date of 2024-04-23, and 1 blank AAA close. A rule discussed after today is a calculation on the records in those 160 rows, together with the blank that has already been counted.

A blank close is a missing cell. When a later day differences adjusted closes, it first keeps rows whose close and adjusted close are both finite. Today only counts the missing cell and checks that the text can be read twice and still match. Filling the blank would change the length of the usable rows. That step is not taken today.

The length 160 is the number of rows in the file. It is not a sample size drawn at runtime. AAA's 80 rows plus BBB's 80 rows are still 160, and the table has no third name. The dates 2024-01-02 through 2024-04-23 are the span written in the file. They are not an interval the program generates from a calendar. The blank that is counted is AAA's single cell. Reading the file text twice and requiring a match makes "the table was not replaced" a check that can be run again. After parsing, an empty cell becomes NaN, and NaN is not equal to itself, so a dictionary comparison cannot serve as that check. When the texts match, a second opening of the same path still faces the same table.

The identity of the table also says what the program is doing. It reads this file in the repository. It does not refresh the rows at runtime, and it does not resample them. From day 22, lagged signs, splits, and regressions are calculations on this frozen table. A different path, or a different file text, would make the printed 160 and the single blank a different report.

Identity checks: 160 rows, dual read text match, one AAA blank close, dates through 2024-04-23, no resampling. Parsed NaN dict compare is intentionally avoided; later days inherit this frozen file.
Text-stable panel identity underpins every later AAA segment count—160 rows, one blank AAA close, no resampling.
Panel identity (160 rows, one AAA blank close, text-stable reads) is prerequisite for every later AAA metric—do not swap files silently.
## What the run showed

```bash
python days/21-fixed-table/fixed_table.py
```

The script prints `path = days/data/panel.csv`, `rows = 160`, `second read matches = true`, AAA dates from 2024-01-02 through 2024-04-23, `AAA blank closes = 1`, and `the table is not resampled`. The implementation is [`fixed_table.py`](../../days/21-fixed-table/fixed_table.py).

Today hands in the identity of the table: 160 rows, AAA and BBB with 80 sessions each, one blank AAA close, two reads of the file text that match, and no resampling at runtime. Next, yesterday's adjusted-move sign calls today, beside the coin-flip baseline 0.5000.

