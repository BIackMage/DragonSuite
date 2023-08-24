import os

# cd to the location of Crimson Suite to ensure scripts are called properly
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def crimson_dragon():
    os.system("python3 Crimson_Dragon//crimson_dragon.py")


def golden_dragon():
        os.system("python3 Golden_Dragon//golden_dragon.py")

def black_dragon():
        os.system("python3 Black_Dragon//black_dragon.py -port 8080")
        


def docker_cleanup():
    # stop all containers
    os.system("docker stop $(docker ps -a -q)")
    # remove all containers
    os.system("docker rm $(docker ps -a -q)")
    # remove all images
    os.system("docker rmi $(docker images -a -q)")
    # remove all volumes (not using these at initial commit)
    os.system("docker volume prune -a")


if __name__ == "__main__":
    while True:
        print("**** MAIN MENU ****")
        print("1 - Control Golden Dragon (Hidden Service)")
        print("2 - Control Crimson Dragon (Client/Exfil Node)")
        print("3 - Control Black Dragon (Flask Website for HS)")
        print("4 - Cleanup all Docker containters and images")
        print("Q/q - Quit")
        menu_choice = input(">>>  ")

        if menu_choice.lower() == "q":
            exit()
        elif menu_choice == "1":
            golden_dragon()
        elif menu_choice == "2":
            crimson_dragon()
        elif menu_choice == "3":
            black_dragon()        
        elif menu_choice == "4":
            docker_cleanup()
        else:
            print("Incorrect entry")

        print("\n\n")