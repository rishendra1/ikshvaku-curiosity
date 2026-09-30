$path = 'C:\Users\rishe\Desktop\PROJECT\curiosity-machine.html'
$content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
Set-Clipboard -Value $content

$check = Get-Clipboard -Raw
Write-Host "SUCCESS: Clipboard loaded with curiosity-machine.html ($($check.Length) characters)!"
Write-Host "Ready for immediate paste (Ctrl+V) into Blogger Page (HTML view) or browser!"
