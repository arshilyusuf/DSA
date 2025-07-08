# push.ps1
Set-Location "C:\Users\arshi\OneDrive\Desktop\Questions"
git add .

# Include both date and time in the commit message
$dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Commit on $dateTime"

git push -u origin main
