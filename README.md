# nba-stat-tweeter
This is a Python script to both fetch stats from the latest NBA games, and post them to Twitter. It uses the Twitter API and the nba-api for Python.

The script expects the Twitter authentication items in the file at the following location: "~/keys/twitter/keys"

The script requires numpy for Python, however it is not included in requirements.txt. This is because I could not get the script to run with pip3's version of numpy. I instead installed it with "sudo apt-get install python3-numpy"
