# sed -i '3,$ s/_\+//g' data/*.txt

# sed -i '3,$ s/[0-9]\+\-[0-9]\+/-1/g'

sed -i '
3,$ s/[0-9]\+\-[0-9]\+/-1/g
3,$ s/_\+//g
:replace_space
	3,$ s/,\s\+,/,-1,/
	t replace_space
' data/*.txt
