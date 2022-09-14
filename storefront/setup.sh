# create virtual environment
python3 -m venv .venv

# if arg is "activate" then activate virtual environment
if [ "$1" = "activate" ]; then
    source .venv/bin/activate
fi
