import os
import subprocess
import ctypes
import getpass

class AutoWare:
    def __init__(self):
        self.current_user = getpass.getuser()
    
    def switch_user(self, username):
        try:
            if not self.is_user_exist(username):
                print(f"User '{username}' does not exist.")
                return
            print(f"Switching to user: {username}")
            self.lock_workstation()
            subprocess.call(['runas', f'/user:{username}', 'cmd.exe'])
        except Exception as e:
            print(f"An error occurred: {e}")

    def is_user_exist(self, username):
        try:
            user_info = subprocess.check_output(f"net user {username}", shell=True)
            return f"User name {username}" in str(user_info)
        except subprocess.CalledProcessError:
            return False

    def lock_workstation(self):
        try:
            print("Locking the workstation for security.")
            ctypes.windll.user32.LockWorkStation()
        except Exception as e:
            print(f"Failed to lock workstation: {e}")

    def list_users(self):
        try:
            users = subprocess.check_output("net user", shell=True).decode()
            user_list = users.split('\n')[4:-3]
            print("Available users:")
            for user in user_list:
                print(user.strip())
        except Exception as e:
            print(f"Failed to list users: {e}")

if __name__ == "__main__":
    auto_ware = AutoWare()
    auto_ware.list_users()
    username = input("Enter the username to switch to: ")
    auto_ware.switch_user(username)