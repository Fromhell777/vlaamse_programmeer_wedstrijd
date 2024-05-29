export DESIGN_WORK_DIR=`pwd`

alias cw='cd $DESIGN_WORK_DIR'

alias run_opgave='python3 main.py < opgave.invoer'
alias run_voorbeeld='python3 main.py < voorbeeld.invoer'
alias run_wedstrijd='python3 main.py < wedstrijd.invoer'

alias check_opgave='python3 main.py < opgave.invoer > test.txt && diff test.txt opgave.uitvoer'
alias check_voorbeeld='python3 main.py < voorbeeld.invoer > test.txt && diff test.txt voorbeeld.uitvoer'
alias check_wedstrijd='python3 main.py < wedstrijd.invoer > test.txt && diff test.txt wedstrijd.uitvoer'

VPM_CPP_OPTIONS="-g -Wall -std=c++20 -Wall -Wextra -pedantic -Werror -O3 -pthread"
alias run_opgave_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < opgave.invoer'
alias run_voorbeeld_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < voorbeeld.invoer'
alias run_wedstrijd_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < wedstrijd.invoer'

alias check_opgave_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < opgave.invoer > test.txt && diff test.txt opgave.uitvoer'
alias check_voorbeeld_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < voorbeeld.invoer > test.txt && diff test.txt voorbeeld.uitvoer'
alias check_wedstrijd_cpp='g++ $VPM_CPP_OPTIONS -I../../../include -o program main.cpp && ./program < wedstrijd.invoer > test.txt && diff test.txt wedstrijd.uitvoer'
