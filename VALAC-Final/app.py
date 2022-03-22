from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, BooleanField, IntegerField, \
    SelectField, DecimalField, DateField
from wtforms.validators import DataRequired, NumberRange
from singleton import DBSingleton
import bcrypt

db = DBSingleton.Instance()
if __name__ == '__main__':
    app = Flask(__name__)


    def stri(tuple):
        return str(tuple).strip("(),")


    def estAdmin(id):
        sql = "SELECT role from user where idUser=%s;"
        params: tuple = (id,)
        db.query(sql, False, params)
        role = str(db.result[0]).strip("(),")
        if role == "0":
            return False
        else:
            return True


    def boutonBackend(idUser):
        if estAdmin(idUser) == True:
            html = "<li class='element-barre-de-navigation'><a href='/valac/menu-edition/tout/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
            return html
        else:
            return ""


    def recupereCircuit(id):
        sql = "SELECT `nomCircuit`,`descriptif`,nbrPlacesDispo,prixInscription,dateDepart,duree, VD.nom AS villedepart, VA.nom AS villearrivee,url FROM circuit join `ville` `VD` ON (circuit.villeDepart_idVille = VD.idVille) JOIN `ville` `VA` ON ( circuit.villeArrivee_idVille = VA.idVille) join medias on medias.idAssociation=circuit.idCircuit where idCircuit=%s and associationTable='circuit';"
        param: tuple = (id,)
        db.query(sql, False, param)
        return db.result[0]


    def recupereEtape(idCircuit, ordre):
        sql = "SELECT idEtape,ordre,ville.nom,lieudevisite.label,lieudevisite.descriptif,etape.dateEtape,etape.duree,lieudevisite.prixVisite,url FROM `etape` join lieudevisite on etape.lieuDeVisite_codeLieu=lieudevisite.codeLieu join " \
              "ville on lieudevisite.ville_idVille=ville.idVille join medias on medias.idAssociation=lieudevisite.codeLieu where circuit_idCircuit=%s and ordre=%s and associationTable='lieudevisite'; "
        params: tuple = (idCircuit, ordre)
        db.query(sql, False, params)
        return db.result[0]


    def recupUser(id):
        sql = "SELECT nom, prenom, adresseEmail, identifiant FROM `user` WHERE idUser = %s"
        params: tuple = (id,)
        db.query(sql, False, params)
        return db.result[0]


    def nbEtapes(idCircuit):
        sql = "SELECT max(ordre) FROM `etape` where circuit_idCircuit=%s;"
        params: tuple = (idCircuit,)
        db.query(sql, False, params)
        if db.result[0] == (None,):
            return [0]
        else:
            return db.result[0]


    def verificationCircuitDejaExistant(nom):
        lecircuit: tuple = (nom,)
        sql = "SELECT nomCircuit FROM circuit WHERE nomCircuit = %s;"
        db.query(sql, False, lecircuit)
        if db.result == []:
            return False
        else:
            return True


    # fonction génerales qui sont uand meme assez pratique
    def verificationVilleDejaExistante(ville):
        laville: tuple = (ville,)
        sql = "SELECT nom FROM ville WHERE nom = %s;"
        db.query(sql, False, laville)
        if db.result == []:
            return False
        else:
            return True


    def verificationPaysDejaExistant(pays):
        lepays: tuple = (pays,)
        sql = "SELECT nom FROM pays WHERE nom = %s;"
        db.query(sql, False, lepays)
        if db.result == []:
            return False
        else:
            return True


    # c'est cheaté permet de transformer un tuple en string

    def recuperIdVille(ville):
        laville: tuple = (ville,)
        sql = "SELECT idVille FROM ville WHERE nom = %s;"
        db.query(sql, False, laville)
        villesId = db.result[0]
        return stri(villesId)


    def recupIdUser(identifiant):
        sql = "SELECT idUser from user where identifiant=%s"
        params: tuple = (identifiant,)
        db.query(sql, False, params)
        return stri(db.result[0])


    def selectionneUneImageAleatoire():
        sql = "SELECT url FROM medias where associationTable='circuit' or associationTable='lieudevisite' ORDER BY " \
              "RAND() LIMIT 1 "
        params: tuple = ()
        db.query(sql, False, params)
        image = str(db.result[0]).strip("(),")
        return image


    def UtilisateurExistant(email, identifiant):
        param: tuple = (email,)
        sql = "SELECT adresseEmail FROM user WHERE adresseEmail = %s;"
        db.query(sql, False, param)
        if not db.result == []:
            return True
        param: tuple = (identifiant,)
        sql = "SELECT identifiant FROM user WHERE identifiant = %s;"
        db.query(sql, False, param)
        if db.result == []:
            return False
        else:
            return True


    def UtilisateurEnregistre(identifiant, mdp):
        param: tuple = (identifiant,)
        sql = "SELECT identifiant, motDePasse FROM user WHERE identifiant = %s;"
        db.query(sql, False, param)
        if db.result == []:
            return False
        hashed_pwd = str(db.result[0][1]).encode('utf-8')
        mdp_is_correct = bcrypt.checkpw(mdp, hashed_pwd)
        return mdp_is_correct


    def menuDeroulant(idUser, lien):
        sql = "SELECT idPays,nom from pays;"
        paramVide: tuple = ()
        db.query(sql, False, paramVide)
        menuDeroulantPays = ""
        for pays in db.result:
            menuDeroulantPays = menuDeroulantPays + "<a href='http://127.0.0.1:5000/valac/" + lien + "/" + str(
                pays[0]) + "/" + idUser + "'>" + pays[1] + "</a>"
        return menuDeroulantPays


    def carouselEtape(idCircuit, idUser):
        sql = "SELECT label,ville.nom,url,medias.nom,ordre FROM `lieudevisite` join ville on lieudevisite.ville_idVille=ville.idVille " \
              "join etape on lieudevisite.codeLieu=etape.lieuDeVisite_codeLieu join circuit on " \
              "circuit.idCircuit=etape.circuit_idCircuit join medias on medias.idAssociation=lieudevisite.codeLieu " \
              "where circuit.idCircuit=%s and medias.associationTable='lieudevisite';"
        params: tuple = (idCircuit,)
        db.query(sql, False, params)
        ElementsCarousel = ""
        compteur = 0
        for etapes in db.result:
            compteur = compteur + 1
            nomEtape = stri(etapes[0])
            nomVille = stri(etapes[1])
            urlImg = stri(etapes[2])
            ordre = stri(etapes[4])
            if compteur == 1:
                classs = "item active"
            else:
                classs = "item"
            ElementsCarousel = ElementsCarousel + "<div onclick='lienAfficherEtapeEnDetail(" + idCircuit + "," + ordre + "," + idUser + ")' class='" + classs + "'style='width:60vw;background-image:url(" + urlImg + ");background-size: cover;height:50vh;background-position:center;'><div class='carousel-caption'><h3>" + nomEtape + "</h3><p>" + nomVille + "</p></div></div> "
        return ElementsCarousel


    def prixTotal(id):
        sql = "SELECT nomCircuit, idCircuit,(SUM(prixVisite) + prixInscription) AS prixTotal FROM circuit LEFT JOIN " \
              "etape ON circuit.idCircuit = etape.circuit_idCircuit LEFT JOIN lieudevisite ON lieudevisite.codeLieu = " \
              "etape.lieuDeVisite_codeLieu where idCircuit=%s GROUP BY idCircuit; "
        param: tuple = (id,)
        db.query(sql, False, param)
        return db.result[0]


    @app.route('/template/<name>')
    def template(name):
        return render_template('index.html', name=name)


    app.config['SECRET_KEY'] = 'un secret que bastos ne connait pas'
    Bootstrap(app)


    # redirection de chiassard
    @app.route('/valac/acces-refusé/<idUser>')
    def erreurAcces(idUser):
        return redirect("/valac/home/" + idUser)


    class FormulaireCreationEtape(FlaskForm):

        nom = StringField("Nom du lieu de l'étape", validators=[DataRequired()])
        description = StringField("Description", validators=[DataRequired()])
        prixVisite = IntegerField('Prix de la visite', validators=[DataRequired()])
        dateEtape = DateField("Date de l'étape", validators=[DataRequired()])
        duree = StringField('durée', validators=[DataRequired()])
        ville = StringField("ville de l'étape", validators=[DataRequired()])
        urlImg = StringField("URL de l'image", validators=[DataRequired()])
        valider = SubmitField('Valider')


    @app.route('/valac/ajouter-une-etape/<idCircuit>/<ordre>/<idUser>', methods=['GET', 'POST'])
    def ajoutEtape(idCircuit, ordre, idUser):
        if estAdmin(idUser) == False:
            return redirect("/valac/ajout-circuit")
        formEtape = FormulaireCreationEtape()
        if formEtape.valider.data == True:
            date = str(formEtape.dateEtape.data)
            ville: tuple = (formEtape.ville.data,)

            if verificationVilleDejaExistante(formEtape.ville.data) == True:
                sql = "SELECT idVille FROM ville WHERE nom = %s;"
                db.query(sql, False, ville)
                villeId = str(db.result[0]).strip("(),")
                sql = "INSERT INTO lieudevisite " \
                      "(label,descriptif,prixVisite,ville_idVille) VALUES (%s,%s,%s,%s)"
                params: tuple = (
                    formEtape.nom.data, formEtape.description.data,
                    formEtape.prixVisite.data, villeId)
                db.query(sql, False, params)
                sql = "SELECT MAX(codeLieu) from lieudevisite;"
                params: tuple = ()
                db.query(sql, False, params)
                codeLieu = str(db.result[0]).strip("(),")
                sql = "INSERT INTO etape " \
                      "(ordre, ville, dateEtape, duree,circuit_idCircuit,lieuDeVisite_codeLieu) VALUES (%s,%s,%s,%s,%s,%s); "
                params: tuple = (ordre, villeId, date, formEtape.duree.data, idCircuit, codeLieu)
                db.query(sql, False, params)
                sql = "INSERT INTO medias (idAssociation,url,nom,associationTable) VALUES ((SELECT MAX(codeLieu) from lieudevisite),%s,%s,'lieudevisite')"
                params: tuple = (formEtape.urlImg.data, formEtape.nom.data)
                db.query(sql, False, params)
                ordre = int(ordre) + 1
                url = "/valac/ajouter-une-etape/" + str(idCircuit) + "/" + str(ordre) + "/" + idUser
                return redirect(url)
            else:
                if verificationVilleDejaExistante(formEtape.ville.data) == False:
                    print("lieu depart non défini")
                    return redirect("/valac/ajout-ville/" + idUser)
        else:
            image = selectionneUneImageAleatoire()
            boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
            boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retour</a></li>"
            return render_template('formulaire.php', form=formEtape, image=image, boutonsBarreNav=boutonsBarreNav)


    class FormulaireCreationCircuit(FlaskForm):
        nom = StringField('nom', validators=[DataRequired()])
        description = StringField('description', validators=[DataRequired()])
        nbrplaces = IntegerField('nombre de places', validators=[DataRequired()])
        prixinscription = IntegerField('Prix inscription', validators=[DataRequired()])
        dateDepart = DateField('Date de depart', validators=[DataRequired()])
        duree = StringField('durée', validators=[DataRequired()])
        LieuDepart = StringField('lieu de depart', validators=[DataRequired()])
        LieuArrivee = StringField('lieu de arrivee', validators=[DataRequired()])
        urlImg = StringField("URL de l'image", validators=[DataRequired()])
        submit = SubmitField('Valider')


    @app.route('/valac/ajout-circuit/<idUser>', methods=['GET', 'POST'])
    def ajoutCircuit(idUser):
        estAdmin(idUser)
        formCircuit = FormulaireCreationCircuit()
        if formCircuit.validate_on_submit():
            if verificationVilleDejaExistante(formCircuit.LieuDepart.data) == True and verificationVilleDejaExistante(
                    formCircuit.LieuArrivee.data) == True:
                idVilleDep = recuperIdVille(formCircuit.LieuDepart.data)
                idVilleArr = recuperIdVille(formCircuit.LieuArrivee.data)
                date = str(formCircuit.dateDepart.data)
                params: tuple = (
                    formCircuit.nom.data, formCircuit.description.data, formCircuit.nbrplaces.data,
                    formCircuit.prixinscription.data, date,
                    formCircuit.duree.data, idVilleDep, idVilleArr)

                sql = "INSERT INTO circuit (nomCircuit, descriptif, nbrPlacesDispo, prixInscription,dateDepart,duree," \
                      "villeDepart_idVille,villeArrivee_idVille) VALUES (%s,%s,%s,%s,%s,%s,%s,%s); "

                db.query(sql, False, params)
                sql = "INSERT INTO medias (idAssociation,url,nom,associationTable) VALUES ((SELECT MAX(idCircuit) from circuit),%s,%s,'circuit')"
                params: tuple = (formCircuit.urlImg.data, formCircuit.nom.data)
                db.query(sql, False, params)
                sql = "SELECT MAX(idCircuit) from circuit"
                params: tuple = ()
                db.query(sql, False, params)
                url = "/valac/ajouter-une-etape/" + stri(db.result[0]) + "/1/" + str(idUser)
                return redirect(url)
            else:
                if verificationVilleDejaExistante(formCircuit.LieuDepart.data) == False:
                    print("lieu depart non défini")
                    return redirect("/valac/ajout-ville/" + idUser)
                if verificationVilleDejaExistante(formCircuit.LieuArrivee.data) == False:
                    print("lieu d'arrivée non défini")
                    return redirect("/valac/ajout-ville/" + idUser)

        else:
            image = selectionneUneImageAleatoire()
            boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
            boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retour</a></li>"
            return render_template('formulaire.php', boutonsBarreNav=boutonsBarreNav, form=formCircuit, image=image, )


    @app.route('/valac/menu-edition/<idPays>/<idUser>', methods=['GET', 'POST'])
    def menuEdition(idPays, idUser):
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)

        menuDeroulantPays = menuDeroulant(idUser, "menu-edition")
        if idPays == "tout":
            sql = "SELECT `idCircuit`, `nomCircuit`, VD.nom AS villedepart, VA.nom AS villearrivee,`url`,medias.nom FROM circuit join " \
                  "`ville` `VD` ON (circuit.villeDepart_idVille = VD.idVille) JOIN `ville` `VA` ON (" \
                  "circuit.villeArrivee_idVille = VA.idVille)  RIGHT JOIN medias ON medias.idAssociation=circuit.idCircuit where " \
                  "associationTable='circuit'; "
            params: tuple = ()
        else:
            sql = "SELECT `idCircuit`, `nomCircuit`, VD.nom AS villedepart, VA.nom AS villearrivee,`url`,medias.nom,idPays FROM " \
                  "circuit join `ville` `VD` ON (circuit.villeDepart_idVille = VD.idVille) JOIN `ville` `VA` ON ( " \
                  "circuit.villeArrivee_idVille = VA.idVille)  JOIN medias ON " \
                  "medias.idAssociation=circuit.idCircuit inner join ville on " \
                  "circuit.villeDepart_idVille=ville.idVille inner JOIN pays on ville.pays_idPays=pays.idPays where " \
                  "associationTable='circuit' and idPays=%s; "
            params: tuple = (idPays,)

        db.query(sql, False, params)
        html = ""
        compteur = 0
        for circuit in db.result:
            compteur = compteur + 1
            idCircuit = stri(circuit[0])
            nomCircuit = stri(circuit[1])
            nomVilleDepart = stri(circuit[2])
            nomVilleArrivee = stri(circuit[3])
            urlImg = stri(circuit[4])
            nomImg = stri(circuit[5])
            if compteur == 1:
                classs = "item active"
            else:
                classs = "item"
            html = html + "<div onclick='lienCircuit(" + idCircuit + "," + idUser + ")' class='" + classs + "'style='width:100%;'><img src='" + urlImg + "' alt='" + nomImg + "' style='width:100%;height:95vh;'><div class='carousel-caption'><h3>" + nomCircuit + "</h3><p>Départ: " + nomVilleDepart + " Arrivée: " + nomVilleArrivee + "</p></div></div> "
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Tout les circuits</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/ajout-circuit/" + idUser + "'>Nouveau circuit</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/ajout-humain/" + idUser + "'>Ajout Utilisateur</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/supprimer-humain/" + idUser + "'>Suppression Utilisateur</a></li>"

        dropbtn = "style='display:block;'"
        return render_template('carousel.php', elements=html, menuDeroulantPays=menuDeroulantPays,
                               boutonsBarreNav=boutonsBarreNav, dropbtn=dropbtn)


    # Formulaire de modification d'un circuit existant

    class FormulaireEditionCircuit(FlaskForm):
        nom = StringField('nom', validators=[DataRequired()])
        description = StringField('description', validators=[DataRequired()])
        nbrplaces = IntegerField('nombre de places', validators=[DataRequired()])
        prixinscription = IntegerField('Prix inscription', validators=[DataRequired()])
        dateDepart = DateField('Date de depart', validators=[DataRequired()])
        duree = StringField('durée', validators=[DataRequired()])
        LieuDepart = StringField('lieu de depart', validators=[DataRequired()])
        LieuArrivee = StringField('lieu de arrivee', validators=[DataRequired()])
        urlImg = StringField('URL image')
        submit = SubmitField('Valider', validators=[DataRequired()])

        def preremplir(self, id):
            circuit = recupereCircuit(id)
            self.nom.data = circuit[0]
            self.description.data = circuit[1]
            self.nbrplaces.data = circuit[2]
            self.prixinscription.data = int(circuit[3])
            self.dateDepart.data = circuit[4]
            self.duree.data = circuit[5]
            self.LieuDepart.data = circuit[6]
            self.LieuArrivee.data = circuit[7]
            self.urlImg.data = circuit[8]


    @app.route('/valac/editer-un-circuit/<idCircuit>/<idUser>', methods=['GET', 'POST'])
    def editionCircuit(idCircuit, idUser):
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)
        # Introduction du formulaire qui permet de prendre les données entrées.
        formEdition = FormulaireEditionCircuit()
        formEdition.preremplir(idCircuit)
        if formEdition.submit.data == True:
            formEdition = FormulaireEditionCircuit()
            if verificationVilleDejaExistante(formEdition.LieuDepart.data) == True and verificationVilleDejaExistante(
                    formEdition.LieuArrivee.data) == True:
                villeDepId = recuperIdVille(formEdition.LieuDepart.data)
                villeArrId = recuperIdVille(formEdition.LieuArrivee.data)
                sql = "UPDATE circuit join medias on medias.idAssociation=circuit.idCircuit  SET nomCircuit = %s, descriptif = %s, nbrPlacesDispo = %s,  " \
                      "prixInscription = %s, dateDepart = %s,duree = %s, villeDepart_idVille = %s, " \
                      "villeArrivee_idVille = %s, url = %s WHERE circuit.idCircuit = %s and associationTable='circuit';"  # .format(db=mysql_db, table=circuit)

                params: tuple = (formEdition.nom.data, formEdition.description.data, formEdition.nbrplaces.data,
                                 formEdition.prixinscription.data, str(formEdition.dateDepart.data),
                                 formEdition.duree.data,
                                 villeDepId, villeArrId, formEdition.urlImg.data, idCircuit)
                db.query(sql, False, params)
                # return redirect('/valac/choix-etape-modification/' + id)
            else:
                return redirect("/valac/ajout-ville/" + idUser)
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'> <a href='http://127.0.0.1:5000/valac/choix-etape-modification/" + idCircuit + "/" + idUser + "'>Editer les etapes</a></li> "
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retour au menu édition</a></li>"
        netape = nbEtapes(idCircuit)[0] + 1
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' ><a href='http://127.0.0.1:5000/valac/ajouter-une-etape/" + idCircuit + "/" + str(
            netape) + "/" + idUser + "'>Ajouter Une Etape</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'style=background-color:#C11;><a href='http://127.0.0.1:5000/valac/suppression-circuit/" + idCircuit + "/" + idUser + "'>Suppression</a></li>"

        return render_template("formulaire.php", form=formEdition, image=selectionneUneImageAleatoire(),
                               boutonsBarreNav=boutonsBarreNav)


    @app.route("/valac/choix-etape-modification/<idCircuit>/<idUser>", methods=['GET', 'POST'])
    def menuEtapes(idCircuit, idUser):
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)
        sql = "SELECT label,ville.nom,url,medias.nom,ordre FROM `lieudevisite` join ville on lieudevisite.ville_idVille=ville.idVille " \
              "join etape on lieudevisite.codeLieu=etape.lieuDeVisite_codeLieu join circuit on " \
              "circuit.idCircuit=etape.circuit_idCircuit join medias on medias.idAssociation=lieudevisite.codeLieu " \
              "where circuit.idCircuit=%s and medias.associationTable='lieudevisite';"
        params: tuple = (idCircuit,)
        db.query(sql, False, params)
        html = ""
        compteur = 0
        for etapes in db.result:
            compteur = compteur + 1
            nomEtape = stri(etapes[0])
            nomVille = stri(etapes[1])
            urlImg = stri(etapes[2])
            ordre = stri(etapes[4])
            if compteur == 1:
                classs = "item active"
            else:
                classs = "item"
            html = html + "<div onclick='lienEtape(" + idCircuit + "," + ordre + "," + idUser + ")' class='" + classs + "'style='width:100%;background-image:url(" + urlImg + ");background-size: cover;height:96vh;background-position:center;'><div class='carousel-caption'><h3>" + nomEtape + "</h3><p>" + nomVille + "</p></div></div> "
        boutonsBarrenav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarrenav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/editer-un-circuit/" + idCircuit + "/" + idUser + "'>Retour</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Menu principal</a></li>"
        return render_template("carousel.php", elements=html, boutonsBarreNav=boutonsBarreNav)


    class FormulaireEditionEtape(FlaskForm):
        ordre = IntegerField("Ordre de l'étape(inverse avec l'ancienne étape a cette position)",
                             validators=[DataRequired()])
        ville = StringField('Ville visitée', validators=[DataRequired()])
        nom = StringField('Nom du lieu de visite', validators=[DataRequired()])
        description = StringField('description', validators=[DataRequired()])
        dateVisite = DateField('Date de la visite', validators=[DataRequired()])
        duree = StringField('Durée', validators=[DataRequired()])
        prixVisite = IntegerField('Prix visite', validators=[DataRequired()])
        urlImg = StringField("URL de l'image", validators=[DataRequired()])
        submit = SubmitField('Valider', validators=[DataRequired()])

        def preremplir(self, idCircuit, ordreEtape):
            etape = recupereEtape(idCircuit, ordreEtape)
            self.ordre.data = etape[1]
            self.ville.data = etape[2]
            self.nom.data = etape[3]
            self.description.data = etape[4]
            self.dateVisite.data = etape[5]
            self.duree.data = etape[6]
            self.prixVisite.data = int(etape[7])
            self.urlImg.data = etape[8]


    @app.route('/valac/editer-une-etape/<idCircuit>/<ordreEtape>/<idUser>', methods=['GET', 'POST'])
    def editerEtapes(idCircuit, ordreEtape, idUser):
        idEtape = recupereEtape(idCircuit, ordreEtape)[0]
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/choix-etape-modification/" + idCircuit + "/" + idUser + "'>Retour</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Menu principal</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'style=background-color:#C11;><a href='http://127.0.0.1:5000/valac/suppression-etape/" + str(
            idEtape) + "/" + idUser + "'>Supprimer étape</a></li>"
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)
        formEtapesEdit = FormulaireEditionEtape()
        formEtapesEdit.preremplir(idCircuit, ordreEtape)
        if formEtapesEdit.submit.data == True:
            formEtapesEdit = FormulaireEditionEtape()
            ordreAInserer = formEtapesEdit.ordre.data
            if verificationVilleDejaExistante(formEtapesEdit.ville.data) == False:
                return redirect("/valac/ajout-ville/" + idUser)
            if ordreEtape != ordreAInserer:
                # verifiordreEtapee que ce n'est pas un ordre trop grand
                sql = "SELECT ordre,idEtape FROM etape where circuit_idCircuit=%s and ordre=(SELECT max(ordre) FROM etape where circuit_idCircuit=%s);"
                params: tuple = (idCircuit, idCircuit,)
                db.query(sql, False, params)
                if ordreAInserer > db.result[0][0]:
                    ordreAInserer = db.result[0][0]
                sql = "SELECT ordre,idEtape FROM etape where circuit_idCircuit=%s and ordre=(SELECT min(ordre) FROM etape where circuit_idCircuit=%s);"
                params: tuple = (idCircuit, idCircuit,)
                db.query(sql, False, params)
                if ordreAInserer < db.result[0][0]:
                    ordreAInserer = db.result[0][0]
                if ordreAInserer > int(ordreEtape):
                    sql = "UPDATE `etape` SET `ordre` = ordre-1 WHERE circuit_idCircuit=%s and ordre>%s and ordre<=%s;"
                    params: tuple = (idCircuit, ordreEtape, ordreAInserer)
                    db.query(sql, False, params)
                if ordreAInserer < int(ordreEtape):
                    sql = "UPDATE `etape` SET `ordre` = ordre+1 WHERE circuit_idCircuit=%s and ordre<%s and ordre>=%s;"
                    params: tuple = (idCircuit, ordreEtape, ordreAInserer)
                    db.query(sql, False, params)
            villeId = recuperIdVille(formEtapesEdit.ville.data)
            sql = "UPDATE etape join lieudevisite on etape.lieuDeVisite_codeLieu=lieudevisite.codeLieu join medias on medias.idAssociation=lieudevisite.codeLieu set ordre=%s," \
                  "etape.ville=%s,lieudevisite.label=%s,lieudevisite.descriptif=%s,etape.dateEtape=%s,etape.duree=%s," \
                  "lieudevisite.prixVisite=%s,url=%s where idEtape=%s and medias.associationTable='lieudevisite'"
            params: tuple = (ordreAInserer, villeId, formEtapesEdit.nom.data, formEtapesEdit.description.data,
                             formEtapesEdit.dateVisite.data, formEtapesEdit.duree.data, formEtapesEdit.prixVisite.data,
                             formEtapesEdit.urlImg.data, idEtape)
            db.query(sql, False, params)
            return redirect("/valac/editer-une-etape/" + idCircuit + "/" + str(ordreAInserer) + "/" + idUser)

        return render_template("formulaire.php", form=formEtapesEdit, image=selectionneUneImageAleatoire(),
                               boutonsBarreNav=boutonsBarreNav)


    class FormulaireVille(FlaskForm):
        ville = StringField('ville', validators=[DataRequired()])
        pays = StringField('Pays de la ville', validators=[DataRequired()])
        submit = SubmitField('Valider')


    @app.route('/valac/ajout-ville/<idUser>', methods=['GET', 'POST'])
    def ajoutVille(idUser):
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)
        formVille = FormulaireVille()
        if formVille.validate_on_submit():
            if verificationVilleDejaExistante(formVille.ville.data) == False:
                pays: tuple = (formVille.pays.data,)
                if verificationPaysDejaExistant(formVille.pays.data) == False:
                    sql = "INSERT INTO pays (nom) VALUES (%s)"
                    db.query(sql, False, pays)
                sql = "SELECT idPays from pays WHERE nom = %s"
                db.query(sql, False, pays)
                idPays = stri(db.result[0])
                ville: tuple = (formVille.ville.data, idPays)
                sql = "INSERT INTO ville (nom,pays_idPays) VALUES (%s, %s);"
                db.query(sql, False, ville)
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retour</a></li>"
        return render_template("formulaire.php", form=FormulaireVille(), image=selectionneUneImageAleatoire(),
                               boutonsBarreNav=boutonsBarreNav)


    @app.route('/valac/connexion-user')
    def index():
        return render_template('index.html')


    @app.route('/valac/main')
    def main():
        return render_template('profile.html')


    class FormulaireHumains(FlaskForm):
        prenom = StringField('Prénom', validators=[DataRequired()])
        nom = StringField('nom', validators=[DataRequired()])
        adresseMail = StringField('Adresse Email', validators=[DataRequired()])
        mdp = StringField('Mot de passe', validators=[DataRequired()])
        identifiant = StringField('Pseudonyme', validators=[DataRequired()])
        ddn = DateField('Date de naissance', validators=[DataRequired()])
        admin = BooleanField('Est admin?')
        submit = SubmitField('Valider')


    @app.route('/valac/ajout-humain/<idUser>', methods=['GET', 'POST'])
    def ajoutUtilisateur(idUser):
        if estAdmin(idUser) == False:
            return redirect('/valac/acces-refusé/' + idUser)
        form = FormulaireHumains()
        if form.validate_on_submit():
            if form.validate_on_submit():
                password = form.mdp.data.encode("utf-8")
                hashed = bcrypt.hashpw(password, bcrypt.gensalt(15))
                date = str(form.ddn.data)
                params: tuple = (
                    form.nom.data, form.prenom.data, form.adresseMail.data,
                    hashed, form.admin.data, form.identifiant.data, date,)

                if UtilisateurExistant(form.adresseMail.data, form.identifiant.data) == False:
                    sql = "INSERT INTO user (nom, prenom, adresseEmail, motDePasse,role,identifiant,dateDeNaissance) VALUES (%s,%s,%s,%s,%s,%s,%s); "
                    db.query(sql, False, params)
                else:
                    print("existe déja ")
        image = selectionneUneImageAleatoire()
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "' style='padding:0;'><img src='https://document-export.canva.com/cklo0/DAE5Qacklo0/51/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20220319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220319T120803Z&X-Amz-Expires=48641&X-Amz-Signature=5169e741508c5f459e8e60a5a46a9c74192fe4ea091234cfe8edb582d09560db&X-Amz-SignedHeaders=host&response-expires=Sun%2C%2020%20Mar%202022%2001%3A38%3A44%20GMT' style='height:6vh;'></a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retouraj au menu édition</a></li>"

        return render_template('formulaire.php', form=form, image=image, boutonsBarreNav=boutonsBarreNav)

        # Fonction de suppression d'un utilisateur par un admin

    class FormulaireSuppression(FlaskForm):
        prenom = StringField('Prenom', validators=[DataRequired()])
        nom = StringField('Nom', validators=[DataRequired()])
        identifiant = StringField('Identifiant', validators=[DataRequired()])
        submit = SubmitField('Valider')

    @app.route('/valac/supprimer-humain/<idUser>', methods=['GET', 'POST'])
    def suppressionHumain(idUser):
        formSuppr = FormulaireSuppression()
        if formSuppr.validate_on_submit():
            if formSuppr.identifiant.data == recupUser(idUser)[3]:
                erreur = 'style ="display:block;"'
                print(erreur)
                return render_template('formulaire.php', form=formSuppr, erreur=erreur,image=selectionneUneImageAleatoire())
            else:
                sql = "DELETE FROM user WHERE identifiant = %s"
                param: tuple = (formSuppr.identifiant.data,)
                db.query(sql, False, param)
        boutonsBarreNav ="<li class='element-barre-de-navigation' style='float:right'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Retour au menu édition</a></li>"
        return render_template('formulaire.php', boutonsBarreNav=boutonsBarreNav,form=formSuppr, image=selectionneUneImageAleatoire())

    class FormulaireConnexion(FlaskForm):
        identifiant = StringField('Pseudonyme', validators=[DataRequired()])
        mdp = StringField('Mot de passe', validators=[DataRequired()])
        ddn = DateField('Date de naissance', validators=[DataRequired()])
        submit = SubmitField('Valider')


    @app.route('/valac/login', methods=['GET', 'POST'])
    def login():
        formCo = FormulaireConnexion()
        if formCo.validate_on_submit():
            password = formCo.mdp.data.encode("utf-8")
            if UtilisateurEnregistre(formCo.identifiant.data, password) == True:
                return redirect('/valac/home/' + recupIdUser(formCo.identifiant.data))
            else:
                return redirect('/valac/login')

        image = selectionneUneImageAleatoire()
        return render_template('login.html', form=formCo, image=image)


    @app.route('/valac/signup')
    def signup():
        return render_template('signup.html')


    @app.route('/valac/logout')
    def logout():
        return redirect("/valac/login")


    @app.route("/valac/suppression-<table>/<idTable>/<idUser>")
    def suppression(table, idTable, idUser):
        if estAdmin(idUser) == False:
            return redirect("/valac/acces-refusé/")
        if table == "circuit":
            idCircuit = idTable
            params: tuple = (idCircuit,)
            sql = "SELECT idEtape,lieuDeVisite_codelieu FROM etape where circuit_idCircuit=%s"
            db.query(sql, False, params)
            sql = "DELETE FROM circuit where idCircuit=%s"
            db.query(sql, False, params)
            sql = "DELETE FROM etape where circuit_idCircuit=%s"
            db.query(sql, False, params)
            sql = "DELETE FROM medias where idAssociation=%s and associationTable='circuit'"
            db.query(sql, False, params)
            params: tuple = ()
            # selectionne les id des ldv non associés
            sql = """SELECT e.codeLieu from     lieudevisite e 
                WHERE
                codeLieu IN(
                SELECT
                        ldv.codeLieu
                    FROM
                        lieudevisite ldv
                    LEFT JOIN `etape` ON ldv.`codeLieu` = `etape`.`lieuDeVisite_codeLieu`
                    WHERE
                        `etape`.`idEtape` IS NULL);"""
            db.query(sql, False, params)
            for idldvASup in db.result:
                sql = "DELETE FROM medias where idAssociation=%s and associationTable='lieudevisite'"
                params: tuple = (stri(idldvASup),)
                db.query(sql, False, params)
            sql = """DELETE
                            e.*
                        FROM
                            lieudevisite e
                        WHERE
                            codeLieu IN(
                            SELECT
                                codelieu
                            FROM
                                (
                                SELECT
                                    ldv.codeLieu
                                FROM
                                    lieudevisite ldv
                                LEFT JOIN `etape` ON ldv.`codeLieu` = `etape`.`lieuDeVisite_codeLieu`
                                WHERE
                                    `etape`.`idEtape` IS NULL
                            ) X
                        );"""
            params: tuple = ()
            db.query(sql, False, params)
            return redirect("/valac/menu-edition/tout/" + idUser)
        else:
            idEtape = idTable
            params: tuple = (idEtape,)
            sql = "SELECT lieuDeVisite_codeLieu from etape where idEtape=%s"
            db.query(sql, False, params)
            params2: tuple = (stri(db.result[0]),)
            sql = "DELETE FROM medias where idAssociation=%s and associationTable='lieudevisite'"
            db.query(sql, False, params2)
            sql = "DELETE FROM etape WHERE idEtape=%s "
            db.query(sql, False, params)
            sql = """DELETE
                            e.*
                        FROM
                            lieudevisite e
                        WHERE
                            codeLieu IN(
                            SELECT
                                codelieu
                            FROM
                                (
                                SELECT
                                    ldv.codeLieu
                                FROM
                                    lieudevisite ldv
                                LEFT JOIN `etape` ON ldv.`codeLieu` = `etape`.`lieuDeVisite_codeLieu`
                                WHERE
                                    `etape`.`idEtape` IS NULL
                            ) X
                        );"""
            params: tuple = ()
            db.query(sql, False, params)
            return redirect("/valac/menu-edition/tout/" + idUser)


    @app.route("/valac/afficher-detail-etape/<idCircuit>/<ordre>/<idUser>")
    def AfficherDetailEtape(idCircuit, ordre, idUser):
        Etape = recupereEtape(idCircuit, ordre)
        nom = Etape[2]
        ville = Etape[3]
        desc = Etape[4]
        date = str(Etape[5])
        duree = Etape[6]
        prix = str(Etape[7]) + "€"
        image = Etape[8]
        html = "<div class='enveloppe'><h1 class = titre-circuit>" + nom + "</h1></br><p class = description-circuit> Description :</br></br> " + desc + "</p></br><p class = info> Date de visite : " + date + " Pour " + duree + "</br><p class = info> Region/ville :" + ville + "</p></br><p class = info> Cout de la visite : " + prix + "</p> "
        elements = "<div class='item active' style='width:60vw;background-image:url(" + image + ");background-size: cover;height:50vh;background-position:center;'><div class='carousel-caption'><h3>" + nom + "</h3><p>" + ville + "</p></div></div> "

        boutonsBarreNav = boutonBackend(idUser)
        boutonsBarreNav=boutonsBarreNav+"<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "'>Home</a></li>"
        boutonsBarreNav=boutonsBarreNav+"<li class='element-barre-de-navigation'><a href='/valac/afficher-circuit/"+idCircuit+ "/"+ idUser + "'>Retour</a></li>"
        return render_template("AffichageCircuit.php", elements=elements, text=html, image=image,
                               css="style=display:none;", boutonsBarreNav=boutonsBarreNav)


    @app.route("/valac/afficher-circuit/<idCircuit>/<idUser>")
    def afficherDetailCircuit(idCircuit, idUser):
        ElementsCarousel = carouselEtape(idCircuit, idUser)
        titre = stri(recupereCircuit(idCircuit)[0])
        descriptif = stri(recupereCircuit(idCircuit)[1])
        date = stri(recupereCircuit(idCircuit)[4])
        nbPlaces = stri(recupereCircuit(idCircuit)[2])
        duree = stri(recupereCircuit(idCircuit)[5])
        prix = stri(prixTotal(idCircuit)[2])
        html = ""
        html = html + "<div class='enveloppe'><h1 class = titre-circuit>" + titre + "</h1></br><p class = description-circuit> Description :</br> " + descriptif + "</p></br><p class = info> Date de départ : " + date + "<p class = info> Nombre de places restantes :" + nbPlaces + "</p><p class = info> Durée du voyage : " + duree + "</p><p class= info> Somme totale des étapes : " + prix + " €</p><p class= info>Départ: " + \
               recupereCircuit(idCircuit)[6] + " et arrivée à: " + recupereCircuit(idCircuit)[7] + "</p>"
        image = recupereCircuit(idCircuit)[8]
        boutonsBarreNav = boutonBackend(idUser)
        boutonsBarreNav=boutonsBarreNav+"<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "'>Home</a></li>"
        boutonsBarreNav=boutonsBarreNav+"<li class='element-barre-de-navigation'><a href='/valac/afficher-tout-les-circuits/tout/"+ idUser + "'>Retour</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/formulaire-de-reservation/" + idCircuit + "/" + idUser + "'>Reserver ce circuit dès Maintenant !</a></li>"
        return render_template("AffichageCircuit.php", text=html, elements=ElementsCarousel, image=image,
                               boutonsBarreNav=boutonsBarreNav)


    @app.route("/valac/afficher-tout-les-circuits/<idPays>/<idUser>")
    def afficherToutLesCircuit(idPays, idUser):
        menuDeroulantPays = menuDeroulant(idUser, "afficher-tout-les-circuits")
        if idPays == "tout":
            sql = "SELECT `idCircuit`, `nomCircuit`, VD.nom AS villedepart, VA.nom AS villearrivee,`url`,medias.nom FROM circuit join " \
                  "`ville` `VD` ON (circuit.villeDepart_idVille = VD.idVille) JOIN `ville` `VA` ON (" \
                  "circuit.villeArrivee_idVille = VA.idVille)  RIGHT JOIN medias ON medias.idAssociation=circuit.idCircuit where " \
                  "associationTable='circuit'; "
            params: tuple = ()
        else:
            sql = "SELECT `idCircuit`, `nomCircuit`, VD.nom AS villedepart, VA.nom AS villearrivee,`url`,medias.nom,idPays FROM " \
                  "circuit join `ville` `VD` ON (circuit.villeDepart_idVille = VD.idVille) JOIN `ville` `VA` ON ( " \
                  "circuit.villeArrivee_idVille = VA.idVille)  JOIN medias ON " \
                  "medias.idAssociation=circuit.idCircuit inner join ville on " \
                  "circuit.villeDepart_idVille=ville.idVille inner JOIN pays on ville.pays_idPays=pays.idPays where " \
                  "associationTable='circuit' and idPays=%s; "
            params: tuple = (idPays,)

        db.query(sql, False, params)
        html = ""
        compteur = 0
        for circuit in db.result:
            compteur = compteur + 1
            idCircuit = stri(circuit[0])
            nomCircuit = stri(circuit[1])
            nomVilleDepart = stri(circuit[2])
            nomVilleArrivee = stri(circuit[3])
            urlImg = stri(circuit[4])
            nomImg = stri(circuit[5])
            if compteur == 1:
                classs = "item active"
            else:
                classs = "item"
            html = html + "<div onclick='lienAfficherCircuitEnDetail(" + idCircuit + "," + idUser + ")' class='" + classs + "'style='width:100%;'><img src='" + urlImg + "' alt='" + nomImg + "' style='width:100%;height:95vh;'><div class='carousel-caption'><h3>" + nomCircuit + "</h3><p>Départ: " + nomVilleDepart + " Arrivée: " + nomVilleArrivee + "</p></div></div> "
        dropbtn = "style='display:block;'"
        boutonsBarreNav=boutonBackend(idUser)
        boutonsBarreNav=boutonsBarreNav+"<li class='element-barre-de-navigation'><a href='/valac/home/" + idUser + "'>Home</a></li>"

        return render_template("carousel.php", menuDeroulantPays=menuDeroulantPays, elements=html, dropbtn=dropbtn,boutonsBarreNav=boutonsBarreNav)

        # Page d'accueil de VALAC


    class FormulaireReservation(FlaskForm):
        nom = StringField('Nom', validators=[DataRequired()])
        prenom = StringField('Prénom', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired()])
        identifiant = StringField('Identifiant', validators=[DataRequired()])
        nbr_pers = IntegerField('Nombre de voyageurs', validators=[DataRequired()])
        submit = SubmitField('Submit')

        def prerempli(self, id):
            user = recupUser(id)
            self.nom.data = user[0]
            self.prenom.data = user[1]
            self.email.data = user[2]
            self.identifiant.data = user[3]

        # Page d'accueil de VALAC


    @app.route('/valac/home/<idUser>')
    def home(idUser):
        boutonsBarreNav = boutonBackend(idUser)
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' ><a " \
                                            "href='http://127.0.0.1:5000/valac/logout'>Se déconnecter</a></li> "
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation' style='float:right'><a " \
                                            "href='http://127.0.0.1:5000/valac/afficher-tout-les-circuits/tout/" + idUser + "'>Afficher les circuits</a></li> "
        sql="SELECT circuit_idCircuit from reservation where user_idUser=%s"
        param:tuple=(idUser,)
        db.query(sql,False,param)
        reservations="<h3>Vous avez reservé:</h3>"
        print(db.result        )
        if db.result==[]:
            reservations="Faites tout de suite une réservation"
        else:
            for idCircuit in db.result[0]:
                reservations=reservations+"<p>"+recupereCircuit(idCircuit)[0]+"</p></br>"


        return render_template('home.html', boutonsBarreNav=boutonsBarreNav, image=selectionneUneImageAleatoire(),reservations=reservations)

        # Formulaire de réservation d'un circuit, les champs connu sont prérempli et l'utilisateur
        # peut choisir combien de personne vont faire le voyage sur cette réservation


    @app.route('/valac/formulaire-de-reservation/<idCircuit>/<idUser>', methods=['GET', 'POST'])
    def liste(idUser, idCircuit, ):

        formReservation = FormulaireReservation()
        formReservation.prerempli(idUser)
        boutonsBarreNav = "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/choix-etape-modification/" + idUser + "'>Retour</a></li>"
        boutonsBarreNav = boutonsBarreNav + "<li class='element-barre-de-navigation'><a href='http://127.0.0.1:5000/valac/menu-edition/tout/" + idUser + "'>Menu principal</a></li>"

        if formReservation.submit.data:
            sql1 = "INSERT INTO reservation (user_idUser, circuit_idCircuit, nbr_places) " \
                   "VALUES (%s, %s, %s)"

            sql2 = "UPDATE circuit SET nbrPlacesDispo = nbrPlacesDispo-%s WHERE circuit.idCircuit = %s"

            reservation: tuple = (idUser, idCircuit, int(formReservation.nbr_pers.data))
            majPlaceDispo: tuple = (int(formReservation.nbr_pers.data), idCircuit,)

            db.query(sql1, False, reservation)
            db.query(sql2, False, majPlaceDispo)
            redirect('home.html')
        else:
            redirect('home.html')
        return render_template('formulaire.php', form=formReservation, boutonsBarreNav=boutonsBarreNav,
                               image=selectionneUneImageAleatoire())


    @app.route('/valac')
    def redirection():
        return redirect('/valac/login')


    app.run(debug=True)
