# DragonSuite

DragonSuite is a project consisting of three components that together create a suite of tools for working with TOR services and data manipulation. The suite includes:

## 1. Golden_Dragon

Golden_Dragon is a dockerized TOR hidden service. It provides a secure and anonymous platform for hosting services that are accessible only through the TOR network.

## 2. Crimson_Dragon

Crimson_Dragon is a dockerized TOR Proxy designed to facilitate sending data to the Golden_Dragon hidden service. This proxy acts as an intermediary, ensuring secure and anonymous communication between the sender and the hidden service.

## 3. Black_Dragon (Optional)

Black_Dragon is an optional component of DragonSuite. It consists of a sample Flask App hosting a TOR Primer. This component is primarily meant to showcase how data can be ingested from TOR HTML requests, embedded into an HTML document, and then returned to the user. The Black_Dragon component accepts data via both GET and POST requests, embedding the provided text string into the TOR Primer webpage before sending it back to the user.

## Getting Started

To begin working with the DragonSuite project, it is recommended to use the provided `setup.sh` script. The script is tailored for Linux environments but can be adapted for Windows. The setup process involves configuring and launching the various components of the suite, allowing you to quickly set up your TOR-based infrastructure.

After the `setup.sh` runs to completion, launch the project using `python3 Dragon_Suite.py`.  The user will be presented with a menu based system, allowing control of a single portion of the project.  For this reason, if the user wants to run all portions of the project on a single computer, it might be easiest to open a new terminal (or tab) for each functionality desired.  

## Generating Vanity .onion Addresses

DragonSuite utilizes the `mkp224o` project to generate vanity TOR `.onion` addresses. The process is menu-based, and the Python scripts are well-commented to guide you through modifications for future development. Vanity addresses provide a personalized touch to your TOR services, making them more memorable and recognizable.

Feel free to explore and modify the DragonSuite components according to your needs. The suite provides a comprehensive set of tools for working with TOR services, data manipulation, and secure communication.

Please note that while the project's primary focus is on Linux environments, it is possible to adapt the components for Windows usage, especially the final Docker containers.

**Note:** This readme provides a high-level overview of the DragonSuite project and its components. For detailed instructions on installation, configuration, and usage, please refer to the documentation provided for relevant supporting frameworks or the code comments themselves.