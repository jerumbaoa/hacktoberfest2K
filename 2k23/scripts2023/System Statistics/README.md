# System Status Checker

A versatile shell script to check and display system status, providing information about various aspects of your system.

## Features

- Display current date and time.
- Check disk space availability.
- Monitor CPU usage.
- Monitor memory usage.
- Display network statistics.
- List the last login details.
- Show currently connected user.

## Usage

```bash
#1. Clone the repository:

git clone https://github.com/yourusername/system-status-checker.git

#2. Navigate to the project folder

cd system-status-checker

#3. Make the script executable:

chmod +x system_status_checker.sh

#4. Now you can run the script:

./system_status_checker.sh
``````


## Available Options:

- -d or --disk <directory>: Specify a directory to check disk space availability.
- -c or --cpu: Display CPU usage.
- -m or --memory: Display memory usage.
- -n or --network: Display network statistics.
- -l or --login <N>: Specify the number of login details to display.

## Examples:

Display disk space for the root directory:

```bash
#Display disk space for the root directory:
./system_status_checker.sh -d /

#Display CPU and memory usage:
./system_status_checker.sh -c -m

#Display network statistics and the last 5 login details:
./system_status_checker.sh -n -l 5

``````
