#awk commands  Notes 


awk -F "|" '$NF ~ /10/  { n++}; END { print n}' file_nmae #count number of 10 in last column 

 awk -F "|" '$1 ~ /^0$/ { n++ }; END {print n}' file_name
 
 awk -F "|" '$1 == 0 ; END {print NR}'  file_last_awk.txt
 
 awk -F "|" '{print NR ":" $0}' file_last_awk.txt
 
 
 cat file_last_awk.txt|awk -F "|" '{print $1}'|grep -n '^0$'
 
 
echo "1 2 4 6"| awk  '{ for(i = 1;i <= NF; i++);  total = total+$i };END {print total}'

--awk command 
awk -F "|" '{ a[$0}++} END { (for x in a) print( a[x],x}' input.txt


I will choose Linux.
I will choose MAC OS.
I will choose Microsoft Windows.
I will choose Linux.
I will choose MAC OS.
I will choose Microsoft Windows.
I will choose Linux.
I will choose MAC OS.
I will choose Microsoft Windows.
I will choose Linux.
I will choose MAC OS.
I will choose Microsoft Windows.
A,B,C,D,E,F,G,H,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
chmod u=rwx,g=rwx,o=r abc.txt

apple
Apple
APPLE
aPPLE

tolower($0)
awk 'tolower($0)~ '/apple/' {print $0}' awk_reg.txt
sed -n '/apple/pi' awk_reg.txt
awk '/apple/{f=1}f' awk_reg.txt

awk '{a[$1]++} END {print}' file_last_awk.txt

for o in `awk '{print $1}' file_last_awk.txt| sort | uniq `; do sed -n "/$o/p" file_last_awk.txt | sed "s/$o//g" |sed "1i  $o"|sed '/^$/d'; done  



for o in `awk '{print $1}' file_last_awk.txt| sort | uniq `; do sed -n "/$o/p" file_last_awk.txt ; done
for o in `awk '{print $1}' file_last_awk.txt| sort | uniq `; do sed -n "/$o/p" file_last_awk.txt | sed "s/$o//g"




find uniq lines using qwk 
awk -F "|" '!a[$1$3]++' file_last_awk.txt


hostname -I |grep -E '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,1}.[0-9]{1,3}'



awk 'NR<=40 && NR>=30 {print NR}' lines.txt
awk 'END {print NR}' lines.txt
sed -n \$= lines.txt

start=$(date +%s.%N)
sed -n \$= lines.txt
dur=$(echo "$(date +%s.%N) - $start" | bc)
printf "Execution time: %.6f seconds" $dur
performance ascpts;


11001  Sales     45   $3000
11002  HR        32   $1500
11003  Marketing 26   $1200
11004  HR        25   $2500