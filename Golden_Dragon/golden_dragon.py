import requests
import os 
import subprocess

## THIS IS THE HIDDEN SERVICE SCRIPT (SERVER SIDE) ##

# number of vanity onion addresses to generate... leave at 1 for automation
num_onions = 1

# cd to the location of Golden_Dragon Dockerfile/docker-compose.yml files
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# hs_dir is where onion keys will go to be transferred into docker container (relative to base dir)
hs_dir = dname + "/Docker/hidden_service/"


def gen_onion_address():
    global num_onions
    global hs_dir
    
    print("**** Vanity Onion Address Generator ****")
    print("What is the prefix you would like? Shorter prefixes are generated faster.")
    prefix_addr = input(">>>  ")
    print("Your prefix will be {} and will be generated in the Dragon Suite directory.\n")
    os.system("../mkp224o-master/mkp224o -d ../Golden_Dragon/{}_keys {} -n {}".format(prefix_addr, prefix_addr, num_onions))

    # this goes into our overall folder, then into the first directory found
    # it will then copy the 3 onion/key files to our hs_dir to be used by the docker container
    for file in os.listdir(dname + "/" + prefix_addr + "_keys"):

        d = os.path.join(dname, prefix_addr + "_keys", file)
        if os.path.isdir(d):
            os.chdir(d)
            os.system("cp * \"{}\"".format(hs_dir))
            # output to terminal to display the actual onion address.
            print("The onion address is {}".format(file))
            break



def run_docker():
    global dname
    with open(dname + "/Docker/hidden_service/hostname") as f:
        # this gives a list... but there's only 1 element in the lists
        lines = f.readlines()           
    print("Starting Docker-Compose from {}".format(dname+"/Docker"))
    print("Hidden Service: {}".format(lines[0]))
    
    # check if our NAMED docker container exists
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    if "golden_dragon" in result.stdout:
        # docker container already exists... so we just need to start it
        print("Docker container found.  Restarting...")
        start_cmd = "docker start golden_dragon &"
        subprocess.Popen("{}".format(start_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    else:
        # no container found, build and run it.
        print("Docker container not found.  Building and starting...")
        docker_dir = dname+"/Docker"
        build_cmd = "docker build -t golden_dragon:latest ."
        run_cmd = "docker run -d --net=host --name golden_dragon golden_dragon:latest &"
        subprocess.Popen("cd {} && {} && {}".format(docker_dir, build_cmd, run_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

def stop_docker():
    global dname
    print("Stopping Golden Dragon")
    # start the docker container as a daemon
    subprocess.Popen("docker stop golden_dragon", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)


def launch_tor_browser():
    # not setup for this project as I didn't use it for my project
    # but here's where you would make a call to launch the tor browser if desired
    pass


def check_docker():
    os.system("docker ps")


if __name__ == "__main__":
    while(True):
        print("\n\n")
        print("**** Golden Dragon Main Menu ****")
        print("1 - Generate Vanity Onion Address")
        print("2 - Run Docker Container")
        print("3 - Stop Docker Container")
        print("4 - Check Docker Status")
        print("5 - Visit website via TOR Browser - Still in development")
        print("Q - Quit program")
        menu_choice = input(">>>  ")
        
        if menu_choice.lower() == "q":
            print("Exiting program...\n\n")
            exit()
        elif menu_choice == "1":
            gen_onion_address()
        elif menu_choice == "2":
            run_docker()        
        elif menu_choice == "3":
            stop_docker()
        elif menu_choice == "4":
            check_docker()            
        elif menu_choice == "5":
            launch_tor_browser()
        else:
            print("Invalid Choice")
        print("\n\n")
        
