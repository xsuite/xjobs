date > ./000_folder/${3:-000}.start
sleep 5
echo "Name: $1, Surname: $2 " > ./000_folder/${3:-000}.out
date > ./000_folder/${3:-000}.end
