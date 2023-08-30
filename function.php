<?php

function execute($url, $cmd, $type)
{
    $ch = curl_init();

    if ($type == "get" || $type == "post") {
        if ($type == "post") {
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $cmd);
        }

        curl_setopt($ch, CURLOPT_URL, $url . $cmd);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);

        $result = curl_exec($ch);
        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        curl_close($ch);

        return [$result, $httpcode];
    } elseif (
        $type == "http_user_agent_get" || $type == "http_accept_language_get" ||
        $type == "http_user_agent_post" || $type == "http_accept_language_post" ||
        $type == "http_aizawa_ninja"
    ) {

        $headers = [];

        if ($type == "http_accept_language_get" || $type == "http_accept_language_post") {
            $headers[] = 'Accept-Language: ' . $cmd;
        }

        if ($type == "http_aizawa_ninja") {
            $headers[] = 'Aizawa-Ninja: ' . base64_encode((string) $cmd);
        }

        if ($type == "http_user_agent_post" || $type == "http_accept_language_post") {
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $type);
        }

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_USERAGENT, $GLOBALS['user_agent']);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

        $result = curl_exec($ch);
        curl_close($ch);

        return (string) $result;
    }
}
