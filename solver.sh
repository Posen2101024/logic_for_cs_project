
if [ ${#} -eq 0 ]; then
	model="example"
else
	model="${1}"
fi

rules="rules.pl"
query="query.pl"

cd $(dirname "${0}")/"${model}"

while read line; do

	if [ -n "${line}" ]; then

		echo "${line}\nhalt." > ".command.tmp"

		swipl --quiet "${rules}" < ".command.tmp"

		rm -f ".command.tmp"

	fi

done < "${query}" > solutions.out

cat solutions.out
