<?php
session_start();
$db = new PDO('mysql:host=localhost;dbname=db-projet-nsi;charset=utf8;','root','');
if(isset($_POST['envoi'])){
    if(!empty($_POST['pseudo']) AND !empty($_POST['prénom']) AND !empty($_POST['email']) AND !empty($_POST['mdp'])) {
        $pseudo = htmlspecialchars($_POST['pseudo']);
        $prénom = htmlspecialchars($_POST['prénom']);
        $email = htmlspecialchars($_POST['email']);
        $mdp = password_hash($_POST['mdp'], PASSWORD_ARGON2ID);
        $insertUser = $db->prepare('INSERT INTO users(pseudo, prénom, email, mdp)VALUES(?,?,?,?)');
        $insertUser->execute(array($pseudo, $prénom, $email, $mdp));
        $recupUser = $db->prepare('SELECT * FROM users WHERE pseudo = ? AND prénom = ? AND email = ? AND mdp = ?');
        $recupUser->execute(array($pseudo, $prénom, $email, $mdp ));
        if($recupUser->rowCount() > 0) {
            $_SESSION['pseudo'] = $pseudo;
            $_SESSION['prénom'] = $prénom;
            $_SESSION['email'] = $email;
            $_SESSION['mdp'] = $mdp;
            $_SESSION['id'] = $recupUser->fetch()['id'];
        }
        echo $_SESSION['id'];
     } else{
        echo "Veuillez compléter tous les champs...";    
    }
}
?> 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="style1.css">
    <title>Inscription</title>
</head>
<body>
    <div class="box">
        <span class="boxLine"> </span>
         <form method="POST" action="" class="m-auto">
             <h2>INSCRIPTION</h2>
                <div class="inputBox">
                    <input type="text" placeholder="Pseudo" name="pseudo" autocomplete="off">
                    <i></i>
                </div>
                <div class="inputBox">
                    <input type="text" placeholder="Prénom" name="prénom" autocomplete="off">
                    <i></i>
                </div>
                <div class="inputBox">
                    <input type="email" placeholder="Adresse e-mail" name="email" autocomplete="off">
                    <i></i>
                </div>
                <div class="inputBox">
                    <input type="password" placeholder="Mot de Passe" name="mdp" autocomplete="off">
                    <i></i>
                </div>
                <button type="submit" name="envoi" class="button">S'inscrire</button>
                <div class="links">
                    <a href="connexion.php">Se connecter</a>
                </div>
        </form>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>