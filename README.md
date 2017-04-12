# Rectangify

Create tables from cell lists, i.e. making 1-dimensional *lists* into 2-dimensional *rectangles*. 

This is often helpful when copying tables from PDFs to text files: Usually each cell appears on its own line; depending on how the PDF was generated, adjacent lines belong either to the same column or to the same row; all columns/rows appear one after another.

Look at the examples to get a feel for typical input files.

## Examples

Let's start with a **columns list**:

    $ cat flights_cols_unmarked.txt
    Date
    29-Jun-17 
    05-Jul-17 
    12-Aug-17 
    13-Aug-17
    From - To
    Sydney - Beijing 
    Beijing - Frankfurt 
    Frankfurt - Shanghai 
    Shanghai - Sydney
    Flight 
    EK174 
    EK931 
    EK736 
    EK175
    Departs Arrives
    19:40 05:30 (30-Jun-17)
    14:00 18:15 
    20:00 13:05 (13-Aug-17)
    19:35 08:10 (14-Aug-17)

This file contains cells on each line, one column after another; each column seems to have 5 items (rows). So let's convert this into a CSV table:

    $ rectangify.py -i 5 flights_cols_unmarked.txt 
    Date,From - To,Flight,Departs Arrives
    29-Jun-17,Sydney - Beijing,EK174,19:40 05:30 (30-Jun-17)
    05-Jul-17,Beijing - Frankfurt,EK931,14:00 18:15
    12-Aug-17,Frankfurt - Shanghai,EK736,20:00 13:05 (13-Aug-17)
    13-Aug-17,Shanghai - Sydney,EK175,19:35 08:10 (14-Aug-17)

Analog for a **rows list**:

    $ cat food_rows.txt 
    ---
    Meal
    Is vegetarian?
    Prepare time
    Taste rating
    ---
    Spaghetti with prawn-chili sauce
    no
    25min
    ****
    ---
    Carrot, lentil & orange soup
    yes
    35min
    ***
    ---
    Curried tofu with rice
    yes
    30min
    **

Here we have a file where each block of lines is marked by a marker string ("---"). Each block of lines seems to resemble a row of the table. So we can convert it into a CSV table with the following command:

    $ rectangify.py --convert ROWS food_rows.txt 
    Meal,Is vegetarian?,Prepare time,Taste rating
    Spaghetti with prawn-chili sauce,no,25min,****
    "Carrot, lentil & orange soup",yes,35min,***
    Curried tofu with rice,yes,30min,**

Note: If you want pretty tables for Markdown processing or just to look at, install the powerfull [`csvkit`][csvkit] and pipe `rectangify`'s output through `csvlook` or use the lighter Python3-only [`csvtomd`][csvtomd]. I use here `csvlook`:

    $ rectangify.py -c ROWS food_rows.txt | csvlook
    | Meal                             | Is vegetarian? | Prepare time | Taste rating |
    | -------------------------------- | -------------- | ------------ | ------------ |
    | Spaghetti with prawn-chili sauce |          False |      0:25:00 | ****         |
    | Carrot, lentil & orange soup     |           True |      0:35:00 | ***          |
    | Curried tofu with rice           |           True |      0:30:00 | **           |

[csvkit]: https://github.com/wireservice/csvkit

[csvtomd]: https://github.com/mplewis/csvtomd

## Installation

For the moment `rectangify` is just a sole Python script. It runs under Python 2.7 and Python 3.5. Download the [ZIP][] and unpack it. Then install the dependency via

    $ pip install -r requirements.txt 

Put the script `rectangify.py` somewhere in your path and make it executable. Now you should be good to go! Test it by issuing:

    $ rectangify.py --help
    usage: rectangify.py [-h] [-c {COLS,ROWS}] [-o OUT] [-m STR] [-i NUM] INPUT

    create CSV tables from a list of columns/rows

    positional arguments:
      INPUT                 input file (or '-' for stdin)

    optional arguments:
      -h, --help            show this help message and exit
      -c {COLS,ROWS}, --convert {COLS,ROWS}
                            convert mode to use: 'COLS' (cells of one column are
                            listed together) or 'ROWS' (cells of one row are
                            listed together). (default: 'COLS')
      -o OUT, --out OUT     save output in file OUT instead of stdout
      -m STR, --marker STR  marker line designating the start of a new column/row
                            (without the newline).(default: '---')
      -i NUM, --items NUM   number of items until the next column/row starts (has
                            precedence over marker)


[ZIP]: https://github.com/halloleo/rectangify/archive/master.zip
