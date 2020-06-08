
root="${1}"
goal="${2}"

cd $(dirname "${0}")/"${root}"

swipl --quiet -s "main.pl" -g "${goal}" --stack_limit=32g
