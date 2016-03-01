<?php
var_dump($_FILES);
$gs_name = $_FILES['upl']['name'];
move_uploaded_file($gs_name, 'gs://my_bucket/new_file.txt');
?>