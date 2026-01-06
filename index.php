<?php
$response = file_get_contents("http://127.0.0.1:5000/increment/home");
$data = json_decode($response, true);
$count = $data['view_count'];
?>
<!DOCTYPE html>
<html>
<head><title>Page Counter</title></head>
<body>
    <h1>This page was visited <?php echo $count; ?> times.</h1>
</body>
</html>
