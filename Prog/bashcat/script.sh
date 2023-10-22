        exec 3<>/dev/tcp/bashcat/666
        a="\""

        function find(){
                n=$1
                # Permet de savoir si il faut renvoyer la taille ou non.
                v=$2

                i=${n[7]}
                champ=${n[16]}
                champ=${champ::-2}
                champ=${champ:1}
                champ="$a$champ$a"
                cat list.csv | while read line; do
                        n=($(echo $line | tr "," "\n"));
                        if [ "${n[0]}" = $champ ]
                        then
                                t="${n[i-1]}"
                                t=${t:1}
                                t=${t::-1}
                                t="$t"
                                if [ $v = 1 ]
                                then
                                        echo $t >&3
                                else
                                        echo ${#t} >&3
                                fi
                        fi
                done   
        }

        while read -r response; do
                echo $response
                n=($(echo $response | tr " " "\n"));
                if [ "${n[0]}" = "Quelle" ]
                then
                        find $n 1
                elif [ "${n[0]}" = "Combien" ]
                then
                        find $n 0
                fi
        done <&3