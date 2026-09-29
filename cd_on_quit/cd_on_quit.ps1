function wyrm() {
    param (
        [string[]]$Params
    )
    $wyrm_location = [Environment]::GetFolderPath("LocalApplicationData") + "\Programs\wyrm\wyrm.exe"
    $Wyrm_LAST_DIR_PATH = [Environment]::GetFolderPath("LocalApplicationData") + "\wyrm\lastdir"

    & $wyrm_location @Params

    if (Test-Path $Wyrm_LAST_DIR_PATH) {
        $Wyrm_LAST_DIR = Get-Content -Path $Wyrm_LAST_DIR_PATH
        Invoke-Expression $Wyrm_LAST_DIR
        Remove-Item -Force $Wyrm_LAST_DIR_PATH
    }
}
