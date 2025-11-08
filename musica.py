import sys
from rich import print
from time import sleep

lines = [
    ("Me abraça, me aceita", 0.09),
    ("Me aceita assim, meu amor", 0.09),
    ("Me abraça, me beija", 0.08),
    ("Me aceita assim, como eu sou", 0.07),
    ("E deixa ser o que for", 0.06),
    ("O que for ", 0.2),
    ("Me abraça, me aceita", 0.06),
    ("Me aceita assim, meu amor", 0.06),
    ("Me abraça, me beija", 0.06),
    ("Me aceita assim, como eu sou ", 0.062),
    ("E deixa ser o que for", 0.062),
    ("O que for ", 0.062),
    ("Yeah", 0.3),
    ]

delays = [0.09, 0.08, 0.07, 0.06, 0.2, 0.06, 0.06, 0.06, 0.062, 0.062, 0.062, 0.3]
def printLyrics():
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[bold cyan]{char}[/bold cyan]", end='', flush=True)
            sys.stdout.flush()
            sleep(char_delay)
        print()  # Nova linha após cada linha da letra
        sleep(delays[i])
printLyrics()