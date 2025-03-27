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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
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
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>