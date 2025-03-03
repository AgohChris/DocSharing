<!-- filepath: /Users/pyinv/Dev/DocSharing/share/templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscription</title>
</head>
<body>
    <h1>Inscription</h1>
    <form method="post" action="{% url 'register' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">S'inscrire</button>
    </form>
</body>
</html>

                       <p class="link">Forgot password <a href="{% url 'password_reset_email' %}">S'inscrire</a></p>


je vois ici que pour la réinitialisation du mot de passe nous avons utiliser directement les composants de djago mais moi ce n'est pas ce que je veux faire. Je veux qu'on code directement toute la partie nous même si dis moi a quoi aurais servis tout ces fichier HTMl que nous avons mis en place et de plus quand l'utilisateur veux modifier le mot c'est sur l'interface django admin qu'il tombe directement alors que normalement il n'est pas censer tomber dessus comme ça.
alors déja nous allons implémenter ça nous même. d'accord? Alors j'expliqe un peu plus.
quand l'utilisateur clique sur le bouton j'ai oublier mon mot de passe, une autre interface s'affiche lui demandan d'entrer son email quand il entre et valide, un code a 4 chiffre générer aléatoirement lui est envoyer par mail puis une interface s'affiche avec les champs vides qui attendent d'être remplis par le code alors l'utilisateur consulte sa boite mail et copie le code et le colle dans les champs vides. si le code coller est correcte, une interface s'affiche avec deux champs vide. lui demandant ainsi de choisir (saisir un nouveau mot de passe et confirmer) puis il valide avec le bouton valider  et le mot de passe change également dans la Bd il peut a nouveau se connecter.