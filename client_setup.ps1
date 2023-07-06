$modfolder_path = Join-Path $env:APPDATA ".minecraft\mods"
$lambda_plugins_path = Join-Path $env:APPDATA ".minecraft\lambda\plugins"
if (-not (Test-Path $modfolder_path)) {
    New-Item -ItemType Directory -Path $modfolder_path | Out-Null
}
if (-not (Test-Path $lambda_plugins_path)) {
    New-Item -ItemType Directory -Path $lambda_plugins_path | Out-Null
}

$jdk_download_url = "https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe"
$forge_download_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar"
$lambda_download_url = "https://github.com/lambda-client/lambda/releases/download/3.3.0/lambda-3.3.0.jar"
$highway_tools_download_url = "https://github.com/lambda-plugins/HighwayTools/releases/download/10.3.1/HighwayTools-10.3.1.jar"

$download_jdk = Read-Host "Do you want to install JDK? JDK is required to install forge. Please note that installing JDK will require administrator privileges in most cases. If you are not sure what you are doing, please copy/paste this download link into your browser: https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe (Y/N): "
$download_forge = Read-Host "Do you want to install forge? (Y/N): "
$download_lambda = Read-Host "Do you want to install lambda? (Y/N): "
$download_highway_tools = Read-Host "Do you want to install highwaytools for lambda? Please note that lambda is required for highwaytools to function. (Y/N): "

$download_forge_request_2 = "N"

$jdk_filename = "jdk-20_windows-x64_bin.exe"
$forge_filename = "forge-1.12.2-14.23.5.2860-installer.jar"
$lambda_filename = "lambda-3.3.0.jar"
$highway_tools_filename = "HighwayTools-10.3.1.jar"

if ($download_jdk.ToUpper() -eq "Y") {
    Write-Host "Downloading JDK..."
    Invoke-WebRequest -Uri $jdk_download_url -OutFile (Join-Path $modfolder_path $jdk_filename)
    Write-Host "JDK downloaded"
    Write-Host "Running JDK installer..."
    Start-Process -FilePath (Join-Path $modfolder_path $jdk_filename)
    Read-Host "The JDK installer should start soon. Press Enter when you have finished installing JDK..."
}
elseif ($download_jdk.ToUpper() -eq "N" -and $download_forge.ToUpper() -eq "Y") {
    Read-Host "The forge installer will not work unless JDK is installed. If you have not installed JDK yet, please do so now by copy/pasting this link into your browser https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.exe. If you are unsure, please ask a trusted friend for advice."
}
else {
    Write-Host ('Unknown value "{0}". Assuming False' -f $download_jdk)
}

if ($download_forge.ToUpper() -eq "Y") {
    Write-Host "Downloading forge..."
    Invoke-WebRequest -Uri $forge_download_url -OutFile (Join-Path $modfolder_path $forge_filename)
    Write-Host "Forge downloaded"
    Write-Host "Running forge installer..."
    Start-Process -FilePath "java" -ArgumentList ("-jar", (Join-Path $modfolder_path $forge_filename))
    Read-Host "The forge installer should start soon. Press Enter when you have finished installing forge..."
}
elseif ($download_forge.ToUpper() -eq "N") {
    $download_forge_request_2 = Read-Host "These mods will not work unless forge is installed. If you have not already installed forge, please do so now. (Y/N)"
}
else {
    Write-Host ('Unknown value "{0}". Assuming False' -f $download_forge)
}

if ($download_forge_request_2.ToUpper() -eq "Y") {
    Write-Host "Downloading forge..."
    Invoke-WebRequest -Uri $forge_download_url -OutFile (Join-Path $modfolder_path $forge_filename)
    Write-Host "Forge downloaded"
    Write-Host "Running forge installer..."
    Start-Process -FilePath "java" -ArgumentList ("-jar", (Join-Path $modfolder_path $forge_filename))
    Read-Host "Press enter to continue..."
}
elseif ($download_forge_request_2.ToUpper() -eq "N") {
    Write-Host "`n`n"
}
else {
    Write-Host ('Unknown value "{0}". Assuming False' -f $download_forge_request_2)
}

if ($download_lambda.ToUpper() -eq "Y") {
    Write-Host "Downloading lambda..."
    Invoke-WebRequest -Uri $lambda_download_url -OutFile (Join-Path $modfolder_path $lambda_filename)
    Write-Host "Successfully installed lambda"
}
elseif ($download_lambda.ToUpper() -eq "N") {
    Write-Host "download_lambda == False; lambda not installed"
}
else {
    Write-Host ('Unknown value "{0}". Assuming False' -f $download_lambda)
}

if ($download_highway_tools.ToUpper() -eq "Y") {
    Write-Host "Downloading highwaytools..."
    Invoke-WebRequest -Uri $highway_tools_download_url -OutFile (Join-Path $lambda_plugins_path $highway_tools_filename)
    Write-Host "Successfully installed highwaytools"
}
elseif ($download_highway_tools.ToUpper() -eq "N") {
    Write-Host "download_highway_tools == False; highwaytools not installed"
}
else {
    Write-Host ('Unknown value "{0}". Assuming False' -f $download_highway_tools)
}

Read-Host "Press enter to finish installation and close the program..."
