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
flask run --host=0.0.0.0 --port=5000
