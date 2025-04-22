import os
import sys
import time

def check_for_git():
    try:
        # Progress bar
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)

        # Check Git version
        exit_code = os.system("\ngit --version")
        if exit_code != 0:
            print("\nGit is not installed or not found in PATH.")
            return False
        else:
            print("\nGit is installed and accessible.")
            return True
    except Exception as e:
        print(f"Error occurred: {e}")


def ts_package():
    VERSION = "1.0.1"
    GITHUBURL = "https://github.com/Coolis1362/ts-package-OFFICAL-PACKAGE-MANAGER"
    print(f"ts-package PACKAGE MANAGER VERSION: {VERSION}")
    print("Type In 'help' For Commands")

    while True:
        user_input = input(">> ts-package ")

        if user_input.lower() == "exit":
            print("Exiting ts-package. Goodbye!")
            sys.exit(0)

        if user_input == "install":
            install_input = input(">> ts-package install Coolis1362/")

            if install_input.lower() == "Coolis1362":
                print("Error: Repository Coolis1362/Coolis1362 cannot be installed via ts-package.")
            else:
                try:
                    os.system(f"git clone https://github.com/Coolis1362/{install_input}")
                except Exception as e:
                    print(f"ts-package install Coolis1362/{install_input}: ERROR FOUND: ERROR CODE 792: {e}")
        if user_input == "git":
            git_input = input(">> ts-package git ")

            if git_input == "init":
                print("Rechecking Ig Git Is Installed...\n")
                try:
                    if check_for_git():
                        os.system("git init")
                    else:
                        print("git can't be found existing")
                        time.sleep(1)
                        sys.exit(0)
                except Exception as e:
                    print(f"Error occurred: {e}")
        if user_input == "upgrade -pre-stable":
            print("Rechecking For git...")
            try:
                if check_for_git():
                    os.system(f"git clone {GITHUBURL}-pre-stable")
                else:
                    print("git can't be found existing")
                    time.sleep(1)
                    sys.exit(0)
            except Exception as e:
                print(f"Error occurred: {e}")
        if user_input == "upgrade -stable":
            try:
                if check_for_git():
                    os.system(f"git clone {GITHUBURL}")
                else:
                    print("git can't be found existing")
                    time.sleep(1)
                    sys.exit(0)
            except Exception as e:
                print(f"Error occurred: {e}")
        if user_input == "upgrade -dev":
            try:
                if check_for_git():
                    os.system(f"git clone {GITHUBURL}-dev")
                else:
                    print("git can't be found existing")
                    time.sleep(1)
                    sys.exit(0)
            except Exception as e:
                print(f"Error occurred: {e}")
        if user_input == "upgrade -beta":
            try:
                if check_for_git():
                    os.system(f"git clone {GITHUBURL}-beta")
                else:
                    print("git can't be found existing")
                    time.sleep(1)
                    sys.exit(0)
            except Exception as e:
                print(f"Error occurred: {e}")
        if user_input == "help":
            print("install Coolis1362/")
            print("git")
            print("|-git init")
            print("upgrade")
            print("| upgrade -pre-stable")
            print("| upgrade -stable")
            print("| upgrade -dev")
            print("| upgrade -beta")
            print("install -u")

        if user_input == "install -u":
            github_user_input = input("GITHUB USER>> ")
            install_input2 = input(f">> ts-package install -u {github_user_input}/")
            print("Rechecking If git Is Installed")
            try:
                if check_for_git():
                    os.system(f"https://github.com/{github_user_input/{install_input2}}")
                else:
                    print("git can't be found existing")
                    time.sleep(1)
                    sys.exit(0)
            except Exception as e:
                print(f"Error occurred: {e}")




if __name__ == "__main__":
    if check_for_git():
        ts_package()
