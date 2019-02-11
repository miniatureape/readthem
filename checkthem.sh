for d in */ ; do
    cd "$d"
    remote=$(git remote show 2> /dev/null)
    if [ -z "$remote" ]
    then
        echo "$d" + "has no remote"
    fi
    cd "../"
done
