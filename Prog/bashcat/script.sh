exec 3<>/dev/tcp/bashcat/666
a="\""
while read -r response; do
        echo $response
        echo ";"
        n=($(echo $response | tr " " "\n"));
        if [ "${n[0]}" = "Quelle" ]
        then
                echo ${n[@]}
                i=${n[7]}
                champ=${n[16]}
                champ=${champ::-2}
                champ=${champ:1}
                champ="$a$champ$a"
                echo $i
                echo $champ
                cat list.csv | while read line; do

                        n=($(echo $line | tr "," "\n"));
                        if [ "${n[0]}" = $champ ]
                        then
                                t="${n[i-1]}"
                                t=${t:1}
                                t=${t::-1}
                                t="$t"
                                echo $t
                                echo $t >&3
                        fi
                done
        elif [ "${n[0]}" = "Combien" ]
        then
                echo ${n[@]}
                i=${n[7]}
                champ=${n[16]}
                champ=${champ::-2}
                champ=${champ:1}
                champ="$a$champ$a"
                echo $i
                echo $champ
                cat list.csv | while read line; do

                        n=($(echo $line | tr "," "\n"));
                        if [ "${n[0]}" = $champ ]
                        then
                                t="${n[i-1]}"
                                t=${t:1}
                                t=${t::-1}
                                t="$t"
                                echo $t
                                echo ${#t}
                                echo ${#t} >&3
                        fi
                done
        fi
done <&3