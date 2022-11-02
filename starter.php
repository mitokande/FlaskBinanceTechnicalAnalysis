
<?php 

exec("python3.6  /var/www/vhosts/zen-boyd.85-95-240-181.plesk.page/httpdocs/server.py ",$output);
print_r($output);
exit();

?>