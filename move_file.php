<?php
  shell_exec("./move_file.sh " . $_GET["filepath"]);
  echo "Moved file " . $_GET["filepath"] . " to /read.";
?>
