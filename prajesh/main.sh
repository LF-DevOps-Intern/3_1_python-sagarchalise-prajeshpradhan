#!/usr/bin/env bash

ARGS=""
SHORT=u:
LONG=url:,http_server::

OPTS=$(getopt -o $SHORT -l $LONG -- "$@")

eval set -- "$OPTS"

while :
do
  key="$1"

  case "$1" in
    -u|--url)
      ARGS="$ARGS $1 $2"
      url=$1
      shift 2
      ;;
    --http_server)
      ARGS="$ARGS $1"
      shift # past argument
      shift # past value
      ;;
    --)
      shift;
      break
      ;;
    *)
      echo "Unexpected option: $1"
      ;;
  esac
done


: ${url:?URL is missing}


# Install Python if not exist 
if ! python3 --version
then 
    printf "\npython not installed\n\n"
    sudo apt install -y python3
    printf "\npython installed\n"
fi

# Venv is separated out in Ubuntu/Debian generally Python3 ships with it
sudo apt install -y python3.8-venv
printf "\npython venv is installed\n\n"

# Create Virtial Enviornmant
python3 -m venv ~/cli
printf "\npython venv is created\n\n"

# Activate Environment
source ~/cli/bin/activate
printf "\npython venv is activated\n\n"

# Install Required packages
pip install .

# Run the Python CLI application
./run.py $ARGS

# Deactivate Vitual Environment
deactivate
