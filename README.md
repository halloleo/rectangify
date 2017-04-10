# Rectangify

Create tables from cell lists, i.e. making 1-dimensional *lists* into 2-dimensional *rectangles*

Here the help:

    usage: rectangify.py [-h] [-o OUT] [-m STR] [-r NUM] INPUT

    Create tables from cell lists

    positional arguments:
      INPUT                 input file (or '-' for stdin)

    optional arguments:
      -h, --help            show this help message and exit
      -o OUT, --out OUT     save output in file OUT instead of stdout
      -m STR, --marker STR  marker designating the start of a new column (default: '---')
      -r NUM, --rows NUM    number of rows (instead of marker)


And here an example:

    $ cat flights_cols.txt
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

    $  ./rectangify.py flights_cols.txt 
    Date,From - To,Flight ,Departs Arrives
    29-Jun-17 ,Sydney - Beijing ,EK174 ,19:40 05:30 (30-Jun-17)
    05-Jul-17 ,Beijing - Frankfurt ,EK931 ,14:00 18:15 
    12-Aug-17 ,Frankfurt - Shanghai ,EK736 ,20:00 13:05 (13-Aug-17)
    13-Aug-17,Shanghai - Sydney,EK175,19:35 08:10 (14-Aug-17)
