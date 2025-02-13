# AutoWare

AutoWare is a Python-based utility designed to facilitate fast switching between multiple user accounts on Windows with enhanced security measures.

## Features

- **User Switching**: Quickly switch between user accounts without the need to log out and back in.
- **Security**: Automatically locks the workstation during the switch to ensure security.
- **User Listing**: Lists all available user accounts on the system for easy selection.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AutoWare.git
   ```

2. Navigate to the directory:

   ```bash
   cd AutoWare
   ```

3. Run the script:

   ```bash
   python AutoWare.py
   ```

## Usage

1. Run the `AutoWare.py` script.
2. The program will list all available user accounts.
3. Enter the username you want to switch to.
4. The workstation will lock for security, and you will be prompted for the password of the selected account.

## Limitations

- Requires administrative privileges for certain operations.
- Only works on Windows operating systems.
- Assumes the `runas` command is available and functional.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this tool at your own risk. Ensure you have proper permissions to switch between user accounts on your machine.