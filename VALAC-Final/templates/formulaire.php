{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}


{% block styles %}
{{ super() }}
  <link rel="stylesheet"
          href="{{ url_for('static', filename='style/style.css') }}">
{% endblock %}


{% block title %}
Valac
{% endblock %}


{% block content %}

<div class="form-wrapper" style="background-image:url({{image}});background-size:cover;">
    <ul class="barre-de-navigation">
            {{boutonsBarreNav}}
    </ul>
    <p  class="erreur" {{erreur}}>Vous ne pouvez pas supprimer votre propre compte</p>
    <iframe style="display:none;"src="http://localhost/uploadblobvalac/formImage.html"style="width:100vw;" class="insertion image">
        <p>Votre navigateur ne supporte aucune iframe !</p>
    </iframe>
	<div class="container">
		{{ wtf.quick_form(form) }}
	</div>
</div>

{% endblock %}