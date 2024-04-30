# !/bin/bash
if read -t 0.1 line; then
    echo $line ,0
fi
sleep 0.1
done < /dev/ttyS0