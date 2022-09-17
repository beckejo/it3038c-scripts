function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
function getUser{
    ($env:USERNAME)
}
function getHostname{
    (HOSTNAME)
}
function getPSVersion{
    ($HOST.Version)
}
function getDayName{
    ((get-date).DayOfWeek)
}
function getMonthName{
    ((get-culture).datetimeformat.getmonthname((get-date).month))
}
function getDayNumber{
    (get-date).day
}
function getYear{
    (get-date).year
}

$IP = getIP
$User = getUser
$Hostname = getHostname
$PSVersion = getPSVersion
$DayName = getDayName 
$MonthName = getMonthName
$DayNumber = getDayNumber
$Year = getYear


$BODY = ("This machine's IPv4 address is $IP. The current user is $User, and the hostname is $Hostname. The PowerShell version is $PSVersion. Today's date is $DayName, $MonthName $DayNumber $Year.")

Send-MailMessage -To "beckejo@mail.uc.edu" -From "jaycbecker3@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)      