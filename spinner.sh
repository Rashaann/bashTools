spinner()
{
    local pid=$!
    local delay=0.75
    local spinstr='|/-\'
    local count=0
    while [ $count != 8 ]; do
        local temp=${spinstr#?}
        printf " %c  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
        count=$(( $count + 1 ))
    done
    printf "    \b\b\b\b"
}