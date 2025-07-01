<?php
$correct_password = "Believe_me"; // Change this

// Check if password is correct and action is set
if (isset($_GET['pass']) && $_GET['pass'] === $correct_password && isset($_GET['set'])) {
    $status = ($_GET['set'] === 'on') ? 'on' : 'off';
    file_put_contents("status.txt", $status);
    echo "Status set to: $status";
} else {
    echo "Access Denied.";
}
?>

