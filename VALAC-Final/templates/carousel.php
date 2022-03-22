<!DOCTYPE html>
<html lang="en">
<head>
  <title>Valac</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="{{ url_for('static', filename='style/style.css') }}">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script>
        function lienEtape(idCircuit,ordre,idUser){
            window.location = "http://127.0.0.1:5000/valac/editer-une-etape/"+idCircuit+"/"+ordre+"/"+idUser;
        }
        function lienCircuit(idCircuit,idUser){
            window.location = "http://127.0.0.1:5000/valac/editer-un-circuit/"+idCircuit+"/"+idUser;
        }
        function lienAfficherCircuitEnDetail(idCircuit,idUser){
            window.location = "http://127.0.0.1:5000/valac/afficher-circuit/"+idCircuit+"/"+idUser;
        }
  </script>
</head>
<body class="bodycarousel">
<ul class="barre-de-navigation">
                {{boutonsBarreNav}}
    <li class="element-barre-de-navigation dropdown"style="float:right">
        <div class="dropdown">
            <button class="dropbtn"{{dropbtn}}>Filtre par pays de départ</button>
            <div class="dropdown-content">
                {{menuDeroulantPays}}
            </div>
        </div>
    </li>
</ul>
<div class="containercarousel">
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Les slides-->
    <div class="carousel-inner">
        {{elements}}
    </div>

    <!--Boutons directionnels -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>

</body>
</html>