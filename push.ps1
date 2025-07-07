# push.ps1
Set-Location "C:\Users\arshi\OneDrive\Desktop\Questions"
git add .
$date = Get-Date -Format "yyyy-MM-dd"
git commit -m "Commit on $date"
git push -u origin main
