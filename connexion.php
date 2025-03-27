<?php
session_start();
$db = new PDO('mysql:host=localhost;dbname=db-projet-nsi;charset=utf8;','root','');
if(isset($_POST['envoi'])){
    if(!empty($_POST['pseudo']) AND !empty($_POST['mdp'])){
        $pseudo = htmlspecialchars($_POST['pseudo']);
        $recupUser = $db->prepare('SELECT * FROM users WHERE pseudo = ?');
        $recupUser->execute(array($pseudo));
        $user = $recupUser->fetch();
        if ($user && password_verify($_POST['mdp'], $user['mdp'])) {
            $_SESSION['id'] = $user['id'];
            echo $_SESSION['id'];
        } else{
            echo "Votre mot de passe ou votre email est incorrect";
        }

    }else{
    echo "Veuillez compléter tous les champs...";    
}
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style6.css">
    <title>Connexion</title>
</head>
<body>
    <div class='box'>
        <form method="POST">
            <h2>CONNEXION</h2>
                <div class="inputBox">
                    <input type="text" placeholder="Pseudo" name="pseudo" autocomplete="off">
                    <i></i>
                </div>
                <div class="inputBox">
                    <input type="password" placeholder="Mot de Passe" name="mdp" autocomplete="off">
                    <i></i>
                </div>
                <button class="button" type="submit" name="envoi">Se connecter</button>
                <div class="links">
                    <a href="inscription.php">S'inscrire</a>
                </div>
        </form>
    </div>
</body>
</html>