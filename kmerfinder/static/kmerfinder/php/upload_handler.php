<?php
var_dump($_FILES);
$gs_name = $_FILES['upl']['name'];
move_uploaded_file($gs_name, 'gs://kmerfindercloud.appspot.com/new_file.txt');
?>