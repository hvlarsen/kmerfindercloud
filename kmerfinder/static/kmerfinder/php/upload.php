<?php
use google\appengine\api\cloud_storage\CloudStorageTools;
$options = [ 'gs_bucket_name' => 'kmerfindercloud.appspot.com' ];
$upload_url = CloudStorageTools::createUploadUrl('/upload_handler.php', $options);
function debug_to_console( $data ) {

    if ( is_array( $data ) )
        $output = "<script>console.log( 'Debug Objects: " . implode( ',', $data) . "' );</script>";
    else
        $output = "<script>console.log( 'Debug Objects: " . $data . "' );</script>";

    echo $output;
}
debug_to_console( "Test" );
// A list of permitted file extensions
$allowed = array('png', 'jpg', 'gif','zip');

if(isset($_FILES['upl']) && $_FILES['upl']['error'] == 0){

	$extension = pathinfo($_FILES['upl']['name'], PATHINFO_EXTENSION);

	if(!in_array(strtolower($extension), $allowed)){
		echo '{"status":"error"}';
		exit;
	}
	else{
		echo $upload_url;
		exit;
	}
}
echo '{"status":"error"}';
exit;
?>