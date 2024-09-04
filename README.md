### Commands
1. `make setup` - Sets up a venv folder in src folder. 
2. `make install` - installs all required python dependencies
3. `make start-local` - starts a local firebase emulator instance which you can then access the API via `http://localhost:5001` usually

Format for making requests to the API: `http://localhost:5001/<region>/function-name>`
- Note: Simply going to this URL will show you the list of available functions