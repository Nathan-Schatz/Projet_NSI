<?php

$user = 'root'
$pass = 'nP7tQDZkeshZ'

$db = new PDO('mysql:host=185.27.134.222;dbname=if0_38612225_com_database', $user, $pass)

if (isset($_POST['pseudo']), $_POST['com']) && !empty($_POST['pseudo']) && !empty($_POST['com']) {
    $pseudo = htmlspecialchars($_POST['pseudo'])
    $com = htmlspecialchars($_POST['com'])
    $db = new PDO('mysql:host=')
}


user :  if0_38612225
password : nP7tQDZkeshZ

?>