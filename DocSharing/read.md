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

                       <p class="link">J'ai oublier mon mot de passe ? <a href="{% url 'password_reset_form' %}">S'inscrire</a></p>

