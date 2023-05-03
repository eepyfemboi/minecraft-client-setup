import urllib.request
import os

# Checking if the "mods" and lambda plugins folder exists
modfolder_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'mods')
lambda_plugins_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'lambda', 'plugins')
if not os.path.exists(modfolder_path):
    os.makedirs(modfolder_path)
if not os.path.exists(lambda_plugins_path):
    os.makedirs(lambda_plugins_path)

# Setting download link variables
jdk_download_url = "https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe"
forge_download_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar"
lambda_download_url = "https://github.com/lambda-client/lambda/releases/download/3.3.0/lambda-3.3.0.jar"
highway_tools_download_url = "https://github.com/lambda-plugins/HighwayTools/releases/download/10.3.1/HighwayTools-10.3.1.jar"

# Setting input variables
download_jdk = input("Do you want to install JDK? JDK is required to install forge. Please note that installing JDK will require administrator privalges in most cases. If you are not sure what you are doing, please copy/paste this download link into your browser: https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe (Y/N): ")
download_forge = input("Do you want to install forge? (Y/N): ")
download_lambda = input("Do you want to install lambda? (Y/N): ")
download_highway_tools = input("Do you want to install highwaytools for lambda? Please note that lambda is required for highwaytools to function. (Y/N): ")


# Setting a variable which might be used later.
download_forge_request_2 = "N"

# Setting filenames
jdk_filename = "jdk-20_windows-x64_bin.exe"
forge_filename = "forge-1.12.2-14.23.5.2860-installer.jar"
lambda_filename = "lambda-3.3.0.jar"
highway_tools_filename = "HighwayTools-10.3.1.jar"

# Installing JDK if download_jdk is true
if download_jdk.upper() == "Y":
    print("Downloading JDK...")
    urllib.request.urlretrieve(jdk_download_url, os.path.join(modfolder_path, jdk_filename))
    print("JDK downloaded\nRunning JDK installer...")
    os.system(f"start {os.path.join(modfolder_path, jdk_filename)}")
    input("The JDK installer should start soon\nPress Enter when you have finished installing JDK...")
elif download_jdk.upper() == "N" and download_forge.upper() == "Y":
    # Making sure that JDK is installed so that the program doesn't break
    input("The forge installer will not work unless JDK is installed. If you have not installed JDK yet, please do so now by copy/pasting this link into your browser https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe. If you are unsure, please ask a trusted friend for advice.")
else:
    print(f'Unknown value "{download_jdk}". Assuming False')

# Installing forge if download_forge is true (the .upper() makes sure its in uppercase)
if download_forge.upper() == "Y":
    print("Downloading forge...")
    urllib.request.urlretrieve(forge_download_url, os.path.join(modfolder_path, forge_filename))
    print("Forge downloaded\nRunning forge installer...")
    os.system('start java -jar {os.path.join(modfolder_path, forge_filename)}')
    input("The forge installer should start soon\nPress Enter when you have finished installing forge...")
elif download_forge.upper() == "N":
    download_forge_request_2 = input("These mods will not work unless forge is installed. If you have not already installed forge, please do so now. (Y/N)")
else:
    print(f'Unknown value "{download_forge}". Assuming False')

# Doublechecking for forge install
if download_forge_request_2.upper() == "Y":
    print("Downloading forge...")
    urllib.request.urlretrieve(forge_download_url, os.path.join(modfolder_path, forge_filename))
    print("Forge downloaded\nRunning forge installer...")
    os.system('java -jar ' + forge_filename)
    input("Press enter to continue...")
elif download_forge_request_2.upper() == "N":
    print("\n\n")
else:
    print(f'Unknown value "{download_forge_request_2}". Assuming False')

# Checking if lambda should be installed
if download_lambda.upper() == "Y":
    print("Downloading lambda...")
    urllib.request.urlretrieve(lambda_download_url, os.path.join(modfolder_path, lambda_filename))
    print("Successfully installed lambda")
elif download_lambda.upper() == "N":
    print("download_lambda == False; lambda not installed")
else:
    print(f'Unknown value "{download_lambda}". Assuming False')

# Checking if highway tools should be installed
if download_highway_tools.upper() == "Y":
    print("Downloading highwaytools...")
    urllib.request.urlretrieve(highway_tools_download_url, os.path.join(lambda_plugins_path, highway_tools_filename))
    print("Successfully installed highwaytools")
elif download_highway_tools.upper() == "N":
    print("download_highway_tools == False; highwaytools not installed")
else:
    print(f'Unknown value "{download_highway_tools}". Assuming False')

input("Press enter to finish installation and close the program...")
