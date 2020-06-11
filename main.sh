
cd $(dirname "${0}")

python3 goal.py

mv goal.pl prolog/main/goal.pl

sh prolog/solver.sh main goal
