$path = 'C:\Users\rishe\Desktop\PROJECT\blogger-template.xml'
$content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
Set-Clipboard -Value $content

$check = Get-Clipboard -Raw
Write-Host "SUCCESS: Clipboard loaded with blogger-template.xml ($($check.Length) characters)!"
Write-Host "Starts with: $($check.Substring(0, 45))"
Write-Host "Ends with: $($check.Substring($check.Length - 30))"
Write-Host "Ready for immediate paste (Ctrl+V) into Blogger Theme -> Edit HTML!"
