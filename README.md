Command to run the Bottle python file in background in Linux envs: 
# nohup ./bottleWebApp.py >/dev/null 2>&1 &


Command to start the Python webserver to serve the converted files:
# nohup ./server.py --port 8000 --dir /tmp/CONV_FILES/  >/dev/null 2>&1 &
