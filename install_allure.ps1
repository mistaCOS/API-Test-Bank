$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$version = "2.36.0"
$url = "https://github.com/allure-framework/allure2/releases/download/$version/allure-$version.zip"
$zipPath = Join-Path $PSScriptRoot "allure-$version.zip"
$extractDir = Join-Path $PSScriptRoot "allure"
$binDir = Join-Path $extractDir "allure-$version" | Join-Path -ChildPath "bin"

if (Test-Path $binDir) {
    Write-Host "Allure already extracted at $binDir"
    Write-Host "Add to PATH: $binDir"
    exit 0
}

if (-not (Test-Path $zipPath)) {
    Write-Host "Downloading Allure $version..."
    Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing
}

Write-Host "Extracting..."
if (Test-Path $extractDir) { Remove-Item $extractDir -Recurse -Force }
Expand-Archive -Path $zipPath -DestinationPath $extractDir -Force

$allureBin = Get-ChildItem -Path $extractDir -Recurse -Filter "allure.bat" | Select-Object -First 1
if ($allureBin) {
    $binDir = $allureBin.DirectoryName
    Write-Host "Allure installed to: $binDir"
    Write-Host "Add to your user PATH: $binDir"
    Write-Host ""
    Write-Host "Allure requires Java 8+. Set JAVA_HOME or add java to PATH."
    Write-Host "Then run: allure serve allure-results"
} else {
    Write-Host "Extraction done. Look for allure.bat in: $extractDir"
}
