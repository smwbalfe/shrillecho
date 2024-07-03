# Check if the script is running with administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "This script requires administrative privileges. Please run the script as an administrator."
    Exit
}

# Define the list of ports to check and stop processes on
$ports = @(8001, 3000, 5000)

foreach ($port in $ports) {
    # Attempt to get the process IDs listening on the current port
    $processes = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique

    # Check if any processes were found
    if ($processes) {
        foreach ($procId in $processes) {
            # Attempt to stop the process
            try {
                Stop-Process -Id $procId -Force -ErrorAction Stop
                Write-Output "Successfully stopped process with PID: $procId on port $port"
            } catch {
                Write-Error "Failed to stop process with PID: $procId on port $port. Error: $_"
            }
        }
    } else {
        Write-Output "No processes found listening on port $port."
    }
}
