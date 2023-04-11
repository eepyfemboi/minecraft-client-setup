import urllib.request
import os

# Checking if the "mods" folder exists
modfolder_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'mods')
if not os.path.exists(modfolder_path):
    os.makedirs(modfolder_path)

# Setting download link variables
forge_download_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar"
lambda_download_url = "https://github.com/lambda-client/lambda/releases/download/3.3.0/lambda-3.3.0.jar"

# Setting input variables
download_forge = input("Do you want to install forge? (Y/N): ")
download_lambda = input("Do you want to install lambda? (Y/N): ")


# Setting a variable which might be used later.
download_forge_request_2 = "N"

# Setting filenames
forge_filename = "forge-1.12.2-14.23.5.2860-installer.jar"
lambda_filename = "lambda-3.3.0.jar"

# Installing forge if download_forge is true (the .upper() makes sure its in uppercase)
if download_forge.upper() == "Y":
    print("Downloading forge...")
    urllib.request.urlretrieve(forge_download_url, os.path.join(modfolder_path, forge_filename))
    print("Forge downloaded\nRunning forge installer...")
    os.system('java -jar ' + os.path.join(modfolder_path, forge_filename))
    input("The forge installer should start soon\nPress Enter when you have finished installing forge...")
elif download_forge.upper() == "N":
    download_forge_request_2 = input("These mods will not work unless forge is installed. If you have not already installed forge, please do so now. (Y/N)")

# Doublechecking for forge install
if download_forge_request_2.upper() == "Y":
    print("Downloading forge...")
    urllib.request.urlretrieve(forge_download_url, os.path.join(modfolder_path, forge_filename))
    print("Forge downloaded\nRunning forge installer...")
    os.system('java -jar ' + forge_filename)
    input("Press enter to continue...")
elif download_forge_request_2.upper() == "N":
    print("\n\n")

# Checking if lambda should be installed
if download_lambda.upper() == "Y":
    print("Downloading lambda...")
    urllib.request.urlretrieve(lambda_download_url, os.path.join(modfolder_path, lambda_filename))
    print("Successfully installed lambda")
elif download_lambda.upper() == "N":
    print("download_lambda == False; lambda not installed")

input("Press enter to finish installation and close the program...")
