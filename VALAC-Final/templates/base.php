<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>VALAC,l'agence de voyage de vos rêves</title>
    <link rel="icon" type="image/png" href="https://discord.com/channels/946310933892960266/946310933892960271/955592452117524490">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
    <style>.barre-de-navigation {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  height:6.5vh;
}
.element-barre-de-navigation {
  float: left;
}

.element-barre-de-navigation a{
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
.element-barre-de-navigation  a:hover {
  background-color: #111;
  color:rgb(250,250,250)
 }

 </style>
</head>

<body>
    <section  style="background-image:url({{image}});background-size:cover;" class="hero is-primary is-fullheight">

<ul class="barre-de-navigation">
                {{boutonsBarreNav}}
</ul>
        <div class="hero-body">
            <div class="container has-text-centered">
               {% block content %}
               {% endblock %}
               {{reservations}}
            </div>
        </div>

    </section>
</body>

</html>