debug=0

while getopts d: flag
do
    case "${flag}" in
        d) debug=${OPTARG};;
    esac
done

export FLASK_APP=motopp
export FLASK_DEBUG=$debug
echo "Starting Flask Server"
flask run
