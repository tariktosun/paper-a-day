<?php
  shell_exec("/home/tariktosun/tariktosun.com/paper-a-day/move_file.sh " . $_GET["filepath"]);
  echo "Moved file " . $_GET["filepath"] . " to /read.";
?>
