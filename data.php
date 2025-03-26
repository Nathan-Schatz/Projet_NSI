<?php

$db = new PDO('mysql:')

if (isset($_POST['pseudo']), $_POST['com']) && !empty($_POST['pseudo']) && !empty($_POST['com']) {
    $pseudo = htmlspecialchars($_POST['pseudo'])
    $com = htmlspecialchars($_POST['com'])

}