alias run_opgave='python3 main.py < opgave.invoer'
alias run_voorbeeld='python3 main.py < voorbeeld.invoer'
alias run_wedstrijd='python3 main.py < wedstrijd.invoer'

alias check_opgave='python3 main.py < opgave.invoer > test.txt && diff test.txt opgave.uitvoer'
alias check_voorbeeld='python3 main.py < voorbeeld.invoer > test.txt && diff test.txt voorbeeld.uitvoer'
alias check_wedstrijd='python3 main.py < wedstrijd.invoer > test.txt && diff test.txt wedstrijd.uitvoer'
