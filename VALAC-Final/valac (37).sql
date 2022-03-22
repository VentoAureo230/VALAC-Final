-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 21 mars 2022 à 23:54
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `valac`
--

-- --------------------------------------------------------

--
-- Structure de la table `circuit`
--

DROP TABLE IF EXISTS `circuit`;
CREATE TABLE IF NOT EXISTS `circuit` (
  `idCircuit` int(11) NOT NULL AUTO_INCREMENT,
  `descriptif` mediumtext NOT NULL,
  `nbrPlacesDispo` int(10) UNSIGNED NOT NULL,
  `duree` varchar(45) NOT NULL,
  `prixInscription` double NOT NULL,
  `dateDepart` date NOT NULL,
  `villeDepart_idVille` int(11) NOT NULL,
  `villeArrivee_idVille` int(11) NOT NULL,
  `nomCircuit` varchar(128) NOT NULL,
  PRIMARY KEY (`idCircuit`),
  UNIQUE KEY `idcircuit_UNIQUE` (`idCircuit`),
  KEY `fk_Circuit_Ville1_idx` (`villeDepart_idVille`),
  KEY `fk_Circuit_Ville2_idx` (`villeArrivee_idVille`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `circuit`
--

INSERT INTO `circuit` (`idCircuit`, `descriptif`, `nbrPlacesDispo`, `duree`, `prixInscription`, `dateDepart`, `villeDepart_idVille`, `villeArrivee_idVille`, `nomCircuit`) VALUES
(10, 'Face à l’immensité atlantique, ce voyage dans les Provinces de l\'Atlantique vous emportera plus par l’émotion que par la foule, entre villages de pêcheurs et littoral rocheux balayé par les marées, où l’on respire l’iode à pleine bouffée. La Nouvelle-Écosse, l’Île-du-Prince-Édouard et le Nouveau-Brunswick recèlent bien des trésors, à commencer par les parcs truffés de plages et de forêts, refuges des ours et de la gent ailée. Tandis que les baleines croisent au large, ce trio bucolique vous plonge entre terre et mer dans un bain unique de culture et de vestiges de colonies, dans des coins aussi jolis que Lunenburg ou la baie de Fundy. En bastion canadien anglophone, ce road trip traverse aussi les belles cités de l’Acadie.', 17, '20 jours', 4150, '2022-07-13', 18, 18, 'Confidences maritimes'),
(11, 'Archipel énigmatique, pays des samouraïs, des élégantes cités d’art, des paysages et jardins harmonieux, des immenses mégapoles... Les Japonais assimilent les nouvelles technologies en préservant leurs valeurs traditionnelles. Un pays qui n’a pas fini de vous surprendre. Le circuit idéal pour une première visite de ce pays étonnant. Vous découvrirez ses villes incontournables : Tokyo, Kyoto et Hiroshima et la culture nippone.', 2, '12 jours', 2899, '2022-03-01', 19, 20, 'Circuit Japon, pays du Soleil Levant'),
(12, 'Reculé, sauvage, ancestral… le Kimberley se garde bien de dévoiler ses secrets à la Terre entière. Dans ce Far West australien, où seuls les baobabs repoussent les limites du temps en terres arides, les vallées cachées du bush réservent leurs colosses de grès aux émérites aventuriers, rompus aux kilomètres, avides d’ailleurs et d’authenticité. Dans la ferveur du groupe, au coin de l’âtre, on nourrit les flammes d’histoires et d’anecdotes sur la journée passée, dans les gorges, bassins naturels et canyons exceptionnels marqués au fer par le soleil. Le long de la Gibb River Road, où le rouge écrase l’azur comme une brique, la terre battue s’étale à l’infini sous les roues agiles des crocodile dundees.', 5, '16 jours', 2790, '2022-03-03', 26, 31, 'C\'est Aussie le Far West');

-- --------------------------------------------------------

--
-- Structure de la table `etape`
--

DROP TABLE IF EXISTS `etape`;
CREATE TABLE IF NOT EXISTS `etape` (
  `idEtape` int(11) NOT NULL AUTO_INCREMENT,
  `ordre` int(11) NOT NULL,
  `ville` int(11) NOT NULL,
  `dateEtape` date NOT NULL,
  `duree` varchar(45) NOT NULL,
  `lieuDeVisite_codeLieu` int(11) NOT NULL,
  `circuit_idCircuit` int(11) NOT NULL,
  PRIMARY KEY (`idEtape`,`ordre`,`lieuDeVisite_codeLieu`,`circuit_idCircuit`),
  KEY `fk_Etape_LieuDeVisite1_idx` (`lieuDeVisite_codeLieu`),
  KEY `fk_Etape_Circuit1_idx` (`circuit_idCircuit`),
  KEY `fk_idVille` (`ville`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `etape`
--

INSERT INTO `etape` (`idEtape`, `ordre`, `ville`, `dateEtape`, `duree`, `lieuDeVisite_codeLieu`, `circuit_idCircuit`) VALUES
(24, 1, 18, '2022-07-14', '2 jours', 5, 10),
(25, 2, 18, '2022-07-16', '1 jour', 6, 10),
(26, 3, 15, '2022-07-17', '1 jour', 7, 10),
(27, 4, 15, '2022-07-18', '1 jour', 8, 10),
(28, 5, 15, '2022-07-19', '2 jours', 9, 10),
(29, 6, 16, '2022-07-21', '2 jours', 10, 10),
(30, 7, 16, '2022-07-23', '1 jour', 11, 10),
(31, 8, 17, '2022-07-24', '2 jours', 12, 10),
(32, 9, 17, '2022-07-26', '2 jours', 13, 10),
(33, 10, 17, '2022-07-28', '2 jours', 14, 10),
(34, 11, 18, '2022-07-30', '1 jour', 15, 10),
(35, 12, 18, '2022-03-31', '3 jours', 16, 10),
(36, 1, 19, '2022-03-01', '1 jour', 17, 11),
(37, 2, 19, '2022-03-02', '1 jour', 18, 11),
(38, 3, 25, '2022-03-03', '1 jour', 19, 11),
(39, 4, 21, '2022-03-04', '1 jour', 20, 11),
(40, 5, 22, '2022-03-05', '1 jour', 21, 11),
(41, 6, 23, '2022-03-06', '1 jour', 22, 11),
(42, 7, 24, '2022-03-07', '1 jour', 23, 11),
(43, 8, 20, '2022-03-08', '3 jours', 24, 11),
(44, 1, 26, '2022-04-03', '2 jours', 25, 12),
(46, 2, 27, '2022-04-05', '1 jour', 27, 12),
(47, 3, 28, '2022-04-06', '1 jour', 28, 12),
(48, 4, 29, '2022-03-07', '2 jours', 29, 12),
(49, 5, 28, '2022-04-09', '2 jours', 30, 12),
(50, 6, 29, '2022-04-11', '1 jour', 31, 12),
(51, 7, 29, '2022-04-12', '1 jour', 32, 12),
(52, 8, 30, '2022-04-15', '1 jour', 33, 12),
(53, 9, 31, '2022-04-16', '2 jours', 34, 12);

-- --------------------------------------------------------

--
-- Structure de la table `lieudevisite`
--

DROP TABLE IF EXISTS `lieudevisite`;
CREATE TABLE IF NOT EXISTS `lieudevisite` (
  `codeLieu` int(11) NOT NULL AUTO_INCREMENT,
  `label` mediumtext NOT NULL,
  `descriptif` longtext NOT NULL,
  `prixVisite` double NOT NULL,
  `ville_idVille` int(11) NOT NULL,
  PRIMARY KEY (`codeLieu`,`ville_idVille`),
  KEY `fk_LieuDeVisite_Ville1_idx` (`ville_idVille`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `lieudevisite`
--

INSERT INTO `lieudevisite` (`codeLieu`, `label`, `descriptif`, `prixVisite`, `ville_idVille`) VALUES
(5, 'Halifax', 'Votre découverte des provinces maritimes commence en capitale de Nouvelle-Écosse, à Halifax. Après avoir récupéré votre voiture de location, vous filerez à votre hôtel situé à proximité du centre-ville pour vous reposer du voyage.  Une balade en front de mer est une parfaite entrée en matière, le long des bâtisses victoriennes en regard sur l’horizon et les bateaux qui mouillent au loin. Ne manquez pas le musée maritime puis la citadelle, perchée en haut d’une petite colline. Au large de la ville, des croisières sont organisées pour aller observer les baleines et la faune marine.', 0, 18),
(6, 'Charlos Cove', 'En rejoignant la communauté acadienne de Charlos Cove par la côte sud, une petite halte à Liscomb Mills vous ouvrira de jolis sentiers de randonnée entre rivière et forêt. En bord de mer, le parc régional de Tor Bay est une belle idée pour un pique-nique, avant de rejoindre votre adresse en pleine nature.', 0, 18),
(7, 'Louisbourg', 'Située sur l’île du Cap-Breton, Louisbourg abritait autrefois une immense forteresse française… entièrement détruite par les Britanniques en 1760. Qu’à cela ne tienne, les Canadiens ont entrepris, deux cents ans plus tard, d’en reconstruire une partie. Et le résultat est bluffant ! Avec son architecture fidèle et ses figurants en tenue d’époque, vous ne trouverez pas meilleur monument pour fortifier vos connaissances de ce chapitre de l’histoire canadienne.', 0, 15),
(8, 'Ingonish Beach', 'Le Cabot Trail est une magnifique route qui serpente entre mer et forêts sur la pointe nord de l’île. Ce ruban sinueux vous conduira dans le sillage de villages de pêcheurs comme Ingonish, une des portes d’entrée du parc national des Hautes-Terres-du-Cap-Breton. Falaises escarpées, lacs immenses, profonds canyons taillés dans un plateau boisé… les amoureux des grands espaces ne sauront où donner de la tête. Si un orignal ne retient pas votre attention par quelques élans d’affection, prenez le temps d’une balade bucolique sur la plage de sable d’Ingonish Beach, à quelques pas de votre lodge.', 0, 15),
(9, 'Chéticamp', 'Le Cabot Trail se poursuit à travers le parc national des Hautes-Terres-du-Cap-Breton, en passant près de nombreux belvédères et sentiers de randonnée où vous pourrez vous arrêter à votre guise. Celui de la Skyline offre à lui seul des points de vue fantastiques sur le littoral. Pour le déjeuner, on craque inévitablement pour un plat de homard, la star locale, avant de couper le contact à Chéticamp, le principal village acadien de la région.  Jamais fatigué des marches en forêt, vous avez une journée pour prolonger votre exploration de la réserve naturelle. Un passage dans les petits villages vous donnera l’occasion de vous imprégner de la culture acadienne, en admirant les tapis houqués, en goûtant la purée chiard ou tout simplement en discutant en français avec les habitants. À l’appel du large, les marins d’un jour pourront quant à eux embarquer à la rencontre des baleines. Tant va le cachalot qu’à la fin il se montre !', 0, 15),
(10, 'Charlottetown', 'En ferry ou via le pont de la Confédération, vous rejoindrez l’Île-du-Prince-Édouard, direction Charlottetown, sa capitale. C’est ici, en effet, que le projet de confédération canadienne a vu le jour ! Un lieu historique majeur, mais aussi une ville fort charmante avec ses maisons en bois colorées. Vous poserez vos valises en plein cœur de Charlottetown pour arpenter le centre historique et dîner dans les petits restos, où les fruits de mer inondent des plateaux.  Au nord de Charlottetown s’étend l’un des parcs nationaux les plus populaires du Canada, celui de l’Île-du-Prince-Édouard… dont les joyaux prennent ici les traits de falaises de grès et de plages de sable rouge-orangé. Plusieurs de chemins vous permettront d’explorer le parc, et même de vous baigner. Sur les plages, les férus d’histoire ont la fibre artistique : peut-être construiriez-vous avec eux un château de sable rouge pour clôturer cette étape prolifique.', 0, 16),
(11, 'West point', 'Au sud-ouest de l’Île-du-Prince-Édouard, le parcours vous mène dans la région Évangeline, le bastion acadien de l’île. Pour en apprendre davantage sur nos cousins francophones, poussez les portes du musée de Miscouche, l’église de Mont-Carmel et le centre communautaire d’Abram-Village, ouvert en été. La journée se terminera à West Point, dans son phare où la salle de la lanterne vous éclairera sur ses rouages, pleins feux sur le large.', 0, 16),
(12, 'Parc de Kouchibouguac', 'De l’autre côté du pont de la Confédération se trouve le Nouveau-Brunswick, une troisième province maritime pleine de surprises. Une pause s’impose à Bouctouche, une petite ville à la croisée de trois rivières et trois cultures : celles des Acadiens, des descendants britanniques et des Indiens micmacs. À la sortie repose une dune insolite, une bande de sable qui change de forme au gré du vent et des marées. Vous prendrez vos aises dans une maison d’hôtes plus au nord, aux abords du parc Kouchibouguac.  Derrière ce nom imprononçable, se cache un parc national pétri de marais salés, de plages de sable clair, de forêts et tourbières. Ce territoire se parcourt à pied, à vélo ou en kayak. L\'occasion d\'aller observer les colonies de phoques et de sternes qui animent le littoral. Les candidats à la baignade pourront se rendre sur la plage de Kellys, où l’eau est plus chaude que partout ailleurs au Canada. Un argument de poids !', 0, 17),
(13, 'Parc national de Fundy', 'Cap sur Fundy, le deuxième parc national du Nouveau-Brunswick. Vous vous installerez dans un chalet tout équipé au cœur du parc et tout près de l’ancienne « baie de France » des Acadiens. Une situation parfaite pour contempler le va-et-vient des marées, parmi les plus grandes au monde ! Réputée pour ses ciels étoilés, la baie de Fundy est un témoin privilégié des vœux pieux, avant de filer au lit.  Le parc national de Fundy présente deux visages. À l’intérieur des terres, on randonne dans des paysages de forêts, lacs et prés verdoyants, où les oiseaux cohabitent en nombre avec les chevreuils, les orignaux et quelques ours noirs. En bord de mer, le littoral déroule ses plages et ses falaises rocheuses dans un décor exceptionnel, reconnu comme réserve de la biosphère par l’Unesco.', 0, 17),
(14, 'Saint-Andrews-by-the-sea', 'La baie de Fundy se prolonge jusqu\'à la frontière américaine du Maine, dans la petite ville côtière de Saint-Andrews. Un lieu hors du temps, un brin champêtre, truffé de maisons en bois et de petits jardins. Nous vous conseillons de visiter le jardin botanique Kingsbrae, où l’on peut goûter tout ce qui y pousse dans le « jardin comestible ». Vous apprécierez également votre adresse, une agréable demeure avec un potager et de jolies vues sur la baie. Bio et beau !  Au large de Saint-Andrews se trouvent trois îles que l’on peut rejoindre en traversier : Grand Manan, Deer et Campobello. Leurs points communs : de coquets villages de pêcheurs et un littoral sauvage peuplé de phoques et d’oiseaux. Pour admirer les cétacés, rien de mieux qu’une excursion au large de la baie. Les plus chanceux verront des baleines à bosse, des rorquals et des marsouins… des nageurs incomparables.', 0, 17),
(15, 'Smith\'s Cove', 'On ne se lasse pas de la baie de Fundy, à tel point que nous vous proposons de la découvrir depuis les rives de Nouvelle-Écosse. Une traversée en traversier et hop ! Rendez-vous à Digby depuis Saint-John’s. Après vous être installé dans votre auberge à Smith’s Cove, Digby est un joli théâtre de flânerie, tout comme Annapolis Royal, l’ancienne capitale provinciale, pour ses jardins historiques et les vestiges de son fort.', 0, 18),
(16, 'Lunenbourg', 'Accrochée à flanc de colline, la vieille ville de Lunenburg, classée au patrimoine mondial de l’Unesco, dévoile un florilège de beaux attraits, de maisons colorées du XVIIIe- XIXe siècles jusqu’à son coquet petit port, où l’on peut admirer à quai la réplique de la goélette Bluenose, qui orne la pièce canadienne de 10 cents.  Avant de rejoindre l’aéroport d’Halifax (à moins de 2h de Lunenburg), faites escale dans le petit bourg de Mahone Bay, où les boutiques d’artisanat regorgent de souvenirs. Peggy’s Cove vous aimantera également du côté de son phare blanc et rouge, ses maisons sur pilotis et son port typique.  Décollage à Halifax, arrivée en France le lendemain.', 0, 18),
(17, ' Temple Senso-ji à Asakusa', 'Accueil à l’arrivée. Transfert, déjeuner dans un restaurant local. Tour de Tokyo incluant la découverte du temple Senso-ji à Asakusa et la rue Nakamise. Puis, du quartier branché d’Harajuku fréquenté par les jeunes Japonais aux styles exubérants. En fin de journée, installation pour 2 nuits à l’hôtel Keihan Tsukiji Ginza Grande 3* pour 2 nuits. Dîner.', 0, 19),
(18, 'Visite du musée Edo ', 'Journée et repas libres. Une visite optionnelle vous sera proposée : journée de découverte de Tokyo en transport en commun. Départ pour la visite du musée Edo (si femerture et lundi ou mardi, visite du Meiji shrine). Puis, balade dans le quartier de Shibuya, quartier de la mode et de la jeunesse tokyoïte. Temps libre pour le déjeuner (repas libre). Visite du jardin japonais Hama-Rikyu, fin de journée dans le quartier Ginza, le quartier chic où vous pourrez également découvrir des édifices contemporains. Temps libre pour le déjeuner (libre). Visite du jardin japonais Hama-Rikyu, fin de la journée dans le quartier Shibuya, quartier de la mode et de la jeunesse tokyoïte, retour à l’hôtel. Inscription le jour d’arrivée et règlement sur place. Nous consulter.', 0, 19),
(19, 'Visite du mont Fuji', 'Départ pour le parc du mont Fuji (120 km). Traversée de la vallée des Fumerolles de Owakudani, puis vous prendrez le téléphérique afin d’apprécier le panorama. Déjeuner, puis balade en bateau sur le lac Ashi (40 min) d’où l’on peut admirer le mont Fuji (3 776 m) qui se dresse au-dessus de l’eau dans un beau décor de collines (voir la rubrique A noter). Départ vers la ville de Hamanako. Installation à l’hôtel The Hamanako 4*. Dîner', 0, 25),
(20, 'découverte du temple d’Ise', 'Départ pour la péninsule d’Ise où se cache l’un des sites les plus sacrés du Japon, le temple d’Ise, un sanctuaire shinto qui abrite l’un destrois symboles impériaux. Dissimulé dans la forêt, il ne se visite pas, mais on peut en admirer la belle architecture de bois. Il est reconstruit à l’identique tous les 20 ans depuis des siècles. Passage par la rue bordée d’échoppes d’Okage et déjeuner. Découverte des rochers-époux reliés par une corde et visite de l’île Mikimoto réputée pour ses huitres perlières. Transfert et installation dans les chambres de style japonais du \"ryokan\" Misugi Resort annex 3*. Dîner japonais traditionnel.', 0, 21),
(21, 'Visite du plus ancien chateau du japon', 'Le matin, départ pour Himeji. À l’arrivée, déjeuner dans un restaurant local. L’après-midi, visite du château médiéval (14e siècle), le plus ancien du Japon, ayant échappé aux incendies et restauré récemment. Puis, balade au pied du château, le long de la rivière, pour aller visiter le Jardin Kokoen. Installation à l’hôtel Nikko Himeji 3*. Dîner et nuit.', 0, 22),
(22, 'Visite de la ville d\'Hiroshima', 'Départ vers Hiroshima. Arrivée pour le déjeuner. Tour général d’Hiroshima, ville récente du fait de son histoire tragique. Vous découvrirez le site et le mémorial de la bombe atomique qui détruisit la ville le 6 août 1945. La visite du musée retraçant cet évènement dramatique. Installation pour la nuit au Aki Grand Hotel 3*. Dîner.', 0, 23),
(23, 'Ile sacrée de Miyajima', 'Depuis le port des ferry-boats, traversée vers l’île sacrée de Miyajima, célèbre pour son \"torii\" flottant et le temple shinto d’Itsukushima construit sur pilotis. Admirez l’harmonie entre les bâtiments de couleur vermillon, les collines boisées, les lanternes de pierre et le décor marin. Retour à terre et route vers Kyoto, ancienne capitale impériale du Japon. Déjeuner en cours de route. A l’arrivée à Kyoto, balade à pied dans le quartier de Gion, un des quartiers traditionnels de la ville. Transfert et installation pour 3 nuits à l’Urban hotel Kyoto Shijo Premium 3*. Dîner dans un restaurant local.', 0, 24),
(24, 'Kyoto', 'Cette journée sera consacrée à la visite de Kyoto, l’ancienne capitale impériale, qui compte plus de 2 000 temples bouddhistes ou shintoïstes. Découverte du sanctuaire Kiyomizu-dera, consacré à Kannon, la déesse de la Compassion, qui domine la ville au sommet d’une colline. Puis, découverte du château de Nijo-jo (17 e siècle), ancien palais du shogun. Déjeuner et visite du fameux temple zen de Ryoan-ji, célèbre pour son jardin de pierres. Enfin, découverte du Kinkaku-ji et son Pavillon d’Or au bord d’un étang. Retour à l’hôtel et fin de journée libre. Dîner libre.', 0, 20),
(25, 'Darwin', 'Vol de nuit pour l\'Australie. Arrivé sur le tarmac de Darwin, vous profiterez d’une petite soirée de détente avant de dormir dans la tente tout au long du périple. Votre évolution en aventurier commence dans un lit, et ça n’a rien d’une théorie.  Paquetage sur le dos, l’heure est venue de rencontrer vos compagnons de route, avec qui vous partagerez la toile sous les étoiles. Le Kimberley fait son cinéma à ciel ouvert, du p’tit déj jusqu’à la nuit tombée. Vous le découvrirez en 4 × 4 en toute convivialité, en compagnie d’un groupe d’une vingtaine d’aventuriers, avides de grands espaces et d’épopée dans ce Far West australien.', 19, 26),
(27, 'Parc national de Nitimiluk', '« The Big River Country », pour les intimes, compte parmi les coins les plus reculés de l’Australie. Un premier mystère pour les aventuriers, qui en perceront quelques-uns du côté d’Edith Falls, dans le Top End, et des gorges de Katherine dans le parc national de Nitmiluk, où les tentes sont déjà dressées pour votre nuitée. En attendant, il ne vous faudra pas longtemps pour sauter dans les grandes baignoires naturelles au creux des falaises et vous balader dans la brousse... Une belle brochette de paysages à vous raconter le soir au coin du feu.', 23, 27),
(28, 'Visite de Kununurra', 'Après quelques bavardages matinaux autour d’une timbale de café chaud, vous rejoindrez les rives du plus grand lac artificiel d’Australie, Argyle, créé par le barrage d’Ord River. De nombreuses espèces de poissons viennent y trouver refuge, pour le plus bonheur des crocodiles d’eau douce et oiseaux migrateurs qui y patrouillent. Une très jolie carte postale de falaises rouges échouées tout autour, qui vous donnera l’envie de sillonner les environs.', 23, 28),
(29, 'Parc national de Purnululu', 'Par-delà les vitres du 4 × 4, des paysages de brousse à perte de vue, d’où émergent soudain les incroyables formations géologiques du parc national de Purnululu, traversé par la chaîne des Bungle Bungle. Au milieu des arbres épars et des touffes d’herbe sèche, 50 nuances de grès se déploient sur les dômes rocheux, géants millénaires longtemps restés à l’ombre des curieux. Après une première exploration de ces fantastiques collines noir et ocre semblables à des ruches géantes, vous profiterez du calme de votre campement pour admirer le soleil couchant… dans un crépuscule flamboyant.  Dans l’ambiance martienne du petit matin, vous pénétrerez plus en profondeur les Bungle Bungle, où se cache le gouffre d’Echidna Chasm à l’issue d’une promenade pierreuse. Avalé par les immenses parois de plus de 200 m de haut, le sentier étroit vous entraîne dans un dédale de falaises vertigineuses, où même la lumière a du mal à percer. À quelques mètres s’élève l’énorme Cathedral Gorge, où l’on se prend à quelques vocalises dans une belle acoustique, tout près d’un opportun bassin d’eau naturelle.', 67, 29),
(30, 'El Questro', 'Un air de Far West américain, des falaises ocre, des nuées de poussière aux couleurs de terre de Sienne, d’innombrables gorges… l’Outback âpre, somptueux et indomptable dessine ses reliefs sur la piste rouge. Les robustes paysages de Carr Boyd vous font de l’œil jusqu’à El Questro, dans le Kununurra, terre ancestrale, sauvage et majestueuse, truffée de forêts tropicales, gorges profondes, sources thermales et chutes en cascade. Avant de vous y frotter, repos du guerrier au camping de la station, une vraie tanière de baroudeurs.  En bon aventurier, vous marcherez dans les pas des premiers aborigènes qui foulèrent le sol aride des Cockburn Ranges, une randonnée sur fond de falaises orangées et plateaux accidentés, piqués ça et là d’endurants baobabs, qui ont tout l’espace pour s’étaler. Dans son décor d’oasis, la cascade d’Emma Gorge dévale les hauteurs… source de plaisir divine pour les baigneurs.', 19, 28),
(31, 'Mont Barnett', 'Ceux qui préfèrent les douches en plein air plongeront avec avidité dans les gorges de Manning, dans le sillage du mont Barnett, votre nouveau terrain d’expédition. Dans un large et inlassable débit, la chute inonde les escaliers rocheux de toute part, planqués sous une écume couleur de lait. Au hasard du bush, vous ferez connaissance avec la faune qui grouille à l’ombre des gorges de Galvans, ou la sieste sous les racines d’un géant. Aux heures où le soleil décline, vous rejoindrez votre campement au bord d’une rivière, dont le clapotis vous bercera jusqu’à la nuit.', 6, 29),
(32, 'Parc national de Windjana gorge', 'Dernière frontière de l\'Ouest australien, le parc national de Windjana Gorge vous déroulera un spectacle de gorges ocre, nourries de nappes et de cascades à la saison des pluies. Lorsque le soleil tape fort, subsistent les chutes, les piscines cristallines et les billabongs pour étancher la soif des oiseaux, des chauves-souris et des crocodiles d’eau douce, dont l’écorce ondule pour briser l’illusion du bois mort.', 0, 29),
(33, 'Tunnel Creek', 'Broome Broome… on lève le camp, pleins phares sur votre nouvelle destination. Votre pilote vous guidera tout droit vers Tunnel Creek, lieu d’une profonde cavité creusée par une rivière sous la roche. Un endroit féerique perdu au milieu de nulle part, qui séduira spéléologues en herbe ou chevronnés, dernière carte postale du Kimberley avant de rejoindre votre adresse à Broome. Adieux les nuits autour du feu et les échanges passionnés sous les étoiles… Arrivé à Broome, le lit remplace la toile.', 28, 30),
(34, 'Perth', 'Vol pour Perth, et retour à la civilisation. À vous les plages, musées et une jolie balade au vert dans le parc national de Yanchep, au nord de la ville. Plus hospitaliers qu’un croco, les koalas sont ici maîtres en leur royaume, plus à l’aise sur un eucalyptus que sur un baobab. Bavard, le cacatoès n’est jamais avare d’une petite causette, surtout pour balancer quelques ragots sur les wallabies.  Après un petit pique-nique du côté de Cervantes, rendez-vous dans le désert des Pinnacles, dans le parc national de Nambung. Au menu de votre voyage, cette belle escapade lunaire vous guidera à la rencontre d’une armée de pierres en rangs serrés, dressées comme des stèles sur l’horizon de l’océan Indien.  Traversée en bateau pour l\'île de Rottnest, un petit caillou à explorer à dos de petite reine. Comme elle n\'est paas bien grande, quelques heures suffisent pour en faire le tour, cheveux au vent, en prenant son temps. L’île abrite l’une des plus adorables créatures de la planète, le quokka, petit marsupial à l’expression toujours joviale. Les yeux dans les vagues, on lézarde sur les plages avant de reprendre le bateau, rendez-vous à Perth pour l’apéro !', 48, 31);

-- --------------------------------------------------------

--
-- Structure de la table `medias`
--

DROP TABLE IF EXISTS `medias`;
CREATE TABLE IF NOT EXISTS `medias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idAssociation` int(11) NOT NULL,
  `url` varchar(10000) DEFAULT NULL,
  `image` blob,
  `nom` varchar(128) NOT NULL,
  `associationTable` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `medias`
--

INSERT INTO `medias` (`id`, `idAssociation`, `url`, `image`, `nom`, `associationTable`) VALUES
(6, 5, 'https://photo.comptoir.fr/asset/voyage/17231/canada/halifax/halifax-nouvelle-ecosse-canada-536606-1401x1080.jpg', NULL, 'Photo Halifax', 'lieudevisite'),
(7, 6, 'https://photo.comptoir.fr/asset/voyage/17233/canada/charlos-cove/hebergement-a-charlos-cove-canada-564169-1411x942.jpg', NULL, 'CHARLOS COVE\r\n', 'lieudevisite'),
(8, 7, 'https://live.staticflickr.com/8438/7876436294_1976d5442e_b.jpg', NULL, 'LOUISBOURG', 'lieudevisite'),
(19, 17, 'https://th.bing.com/th/id/R.876daf361127b3f40254ebc11364c79e?rik=pCeMZXe8mzsSDw&pid=ImgRaw&r=0', NULL, 'Temple Senso-Ji', 'lieudevisite'),
(9, 8, 'https://photo.comptoir.fr/asset/voyage/17235/canada/cabot-trail-province-de-la-nouvelle-ecosse-canada-603367-1495x1080.jpg', NULL, 'INGONISH BEACH\r\n', 'lieudevisite'),
(10, 9, 'https://photo.comptoir.fr/asset/voyage/17236/canada/cheticamp/observation-des-baleines-nouvelle-ecosse-canada-566989-1620x1080.jpg', NULL, 'CHÉTICAMP', 'lieudevisite'),
(11, 10, 'https://photo.comptoir.fr/asset/voyage/17238/canada/parc-national-de-l-ile-du-prince-edouard-%E2%80%93-secteur-de-cavendish/plage-de-cavendish-ile-du-prince-edouard-canada-570176-1631x1080.jpg', NULL, 'CHARLOTTETOWN', 'lieudevisite'),
(12, 11, 'https://photo.comptoir.fr/asset/voyage/17240/canada/o-leary/phare-de-west-point-o-leary-canada-561731-1629x1080.jpg', NULL, 'WEST POINT', 'lieudevisite'),
(13, 12, 'https://live.staticflickr.com/5629/30037598393_c7f20418ec_k.jpg', NULL, 'PARC DE KOUCHIBOUGUAC', 'lieudevisite'),
(14, 13, 'https://photo.comptoir.fr/asset/voyage/17243/canada/baie-de-fundy/hopewell-rocks-baie-de-fundy-nouveau-brunswick-canada-383855-1623x1080.jpg', NULL, 'PARC NATIONAL DE FUNDY', 'lieudevisite'),
(15, 14, 'https://photo.comptoir.fr/asset/voyage/17245/canada/grand-manan-island/le-grand-manan-depuis-un-bateau-grand-manan-island-nouveau-brunswick-canada-566987-1626x1080.jpg', NULL, 'SAINT-ANDREWS-BY-THE-SEA', 'lieudevisite'),
(16, 15, 'https://photo.comptoir.fr/asset/voyage/17247/canada/annapolis-royal/fort-anne-annapolis-royal-nouvelle-ecosse-canada-568861-1624x1080.jpg', NULL, 'SMITH’S COVE', 'lieudevisite'),
(17, 16, 'https://photo.comptoir.fr/asset/voyage/17248/canada/lunenburg/lunenburg-nouvelle-ecosse-maritimes-canada-410581-1506x1080.jpg', NULL, 'LUNENBURG', 'lieudevisite'),
(18, 10, 'https://photo.comptoir.fr/photos/voyage/3341/canada/parc-national-des-hautes-terres-du-cap-breton-%E2%80%93-sect-cheticamp/coucher-de-soleil-sur-la-skyline-trail-parc-national-des-hautes-terres-du-cap-breton-canada-561727-1600x800.jpg', NULL, 'Confidences maritimes', 'circuit'),
(20, 18, 'https://res.cloudinary.com/www-virgin-com/virgin-com-prod/sites/virgin.com/files/Articles/Travel/tokyo.jpg', NULL, 'Tokyo de nuit', 'lieudevisite'),
(21, 19, 'https://www.voyagejapon.com/cdn/jp-public/city_around_kawaguchi_lake_mont_fuji_japan.jpg', NULL, 'image mont fuji', 'lieudevisite'),
(22, 20, 'https://www.tullyluxurytravel.com/wp-content/uploads/2019/11/AdobeStock_69687415-aspect-ratio-2500x1400.jpeg', NULL, 'peninsule d\'ise', 'lieudevisite'),
(23, 21, 'https://th.bing.com/th/id/R.4688c3d3c77ff0a7567020adf2698948?rik=GL032BCcsjSw3Q&riu=http%3a%2f%2fjapancastles.weebly.com%2fuploads%2f1%2f1%2f8%2f9%2f118921979%2f576005980_orig.jpg&ehk=3uF9kkW%2bi76sAQdFDy9hrJwNTKuReB1%2bSMr8xCyBjuU%3d&risl=&pid=ImgRaw&r=0', NULL, 'chateau d\'himeji', 'lieudevisite'),
(24, 22, 'https://media.tenor.com/images/1814ab536b91674669159f806d420da5/tenor.png', NULL, 'hiroshima', 'lieudevisite'),
(25, 23, 'https://monsoondiaries.com/wp-content/uploads/2018/09/miyajima.jpg', NULL, 'Miyajima', 'lieudevisite'),
(26, 24, 'https://media.routard.com/image/85/5/kyoto.1553855.jpg', NULL, 'Kyoto', 'lieudevisite'),
(27, 11, 'https://th.bing.com/th/id/R.fbce805d370e32d32dd4d3c6e611a423?rik=WUDqk7Da%2bmsrrg&pid=ImgRaw&r=0', NULL, 'Japon', 'circuit'),
(29, 12, 'https://photo.comptoir.fr/photos/voyage/2429/australie/broome/kimberley-australie-609386-1600x800.jpg', NULL, 'C\'est Aussie le Far West', 'circuit'),
(30, 26, 'https://photo.comptoir.fr/asset/voyage/12619/australie/camping-car-4x4-en-australie-609376-1624x1080.jpg', NULL, 'Darwin', 'lieudevisite'),
(31, 27, 'https://photo.comptoir.fr/asset/voyage/12621/australie/katherine/304714-1620x1080.jpg', NULL, 'Parc national de Nitimiluk', 'lieudevisite'),
(32, 28, 'https://photo.comptoir.fr/asset/voyage/12622/australie/lac-argyle-kimberley-australie-occidentale-australie-609381-1920x944.jpg', NULL, 'Visite de Kununurra', 'lieudevisite'),
(33, 29, 'https://photo.comptoir.fr/asset/voyage/12623/australie/kununurra/parc-national-de-purnululu-kununurra-australie-364085-1613x1080.jpg', NULL, 'Parc national de Purnululu', 'lieudevisite'),
(34, 30, 'https://photo.comptoir.fr/asset/voyage/12625/australie/emma-gorge-kimberley-australie-occidentale-australie-609384-1620x1080.jpg', NULL, 'El Questro', 'lieudevisite'),
(35, 31, 'https://photo.comptoir.fr/asset/voyage/12627/australie/derby/manning-gorge-australie-occidentale-australie-609385-1626x1080.jpg', NULL, 'Mont Barnett', 'lieudevisite'),
(36, 32, 'https://photo.comptoir.fr/asset/voyage/12628/australie/faune-de-la-windjana-gorge-petit-crocodile-de-johnston-parc-national-windjana-gorge-kimberley-553558-1920x1080.jpg', NULL, 'Parc national de Windjana gorge', 'lieudevisite'),
(37, 33, 'https://photo.comptoir.fr/asset/voyage/12629/australie/tunnel-creek-parc-national-tunnel-creek-kimberley-australie-553556-1620x1080.jpg', NULL, 'Tunnel Creek', 'lieudevisite'),
(38, 34, 'https://photo.comptoir.fr/asset/voyage/12630/australie/le-desert-des-pinnacles-australie-396293-1620x1080.jpg', NULL, 'Perth', 'lieudevisite');

-- --------------------------------------------------------

--
-- Structure de la table `pays`
--

DROP TABLE IF EXISTS `pays`;
CREATE TABLE IF NOT EXISTS `pays` (
  `idPays` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(45) NOT NULL,
  PRIMARY KEY (`idPays`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `pays`
--

INSERT INTO `pays` (`idPays`, `nom`) VALUES
(2, 'Grèce'),
(3, 'Maroc'),
(6, 'Canada'),
(7, 'Japon'),
(8, 'Australie');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `user_idUser` int(11) NOT NULL,
  `circuit_idCircuit` int(11) NOT NULL,
  `nbr_places` int(3) UNSIGNED ZEROFILL DEFAULT NULL,
  PRIMARY KEY (`user_idUser`,`circuit_idCircuit`),
  KEY `fk_User_has_Circuit_Circuit1_idx` (`circuit_idCircuit`),
  KEY `fk_User_has_Circuit_User_idx` (`user_idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `idUser` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(45) NOT NULL,
  `prenom` varchar(45) NOT NULL,
  `adresseEmail` varchar(55) NOT NULL,
  `motDePasse` varchar(255) NOT NULL,
  `role` tinyint(1) UNSIGNED ZEROFILL NOT NULL,
  `identifiant` varchar(45) NOT NULL,
  `dateDeNaissance` date NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`idUser`, `nom`, `prenom`, `adresseEmail`, `motDePasse`, `role`, `identifiant`, `dateDeNaissance`) VALUES
(1, 'root', 'root', 'root@root', '$2b$15$9PAHgHJQ7QKouPeEHS0ekO0P61x7T2emkCstiSERfW45wahWbQa1y', 1, 'root', '2022-03-22');

-- --------------------------------------------------------

--
-- Structure de la table `ville`
--

DROP TABLE IF EXISTS `ville`;
CREATE TABLE IF NOT EXISTS `ville` (
  `idVille` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(45) NOT NULL,
  `pays_idPays` int(11) NOT NULL,
  PRIMARY KEY (`idVille`),
  KEY `fk_Ville_Pays1_idx` (`pays_idPays`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ville`
--

INSERT INTO `ville` (`idVille`, `nom`, `pays_idPays`) VALUES
(3, 'Paros', 2),
(4, 'Santorin', 2),
(5, 'Marrakech', 3),
(6, 'Casablanca', 3),
(15, 'Ile du Cap Breton', 6),
(16, 'Ile du prince Edward', 6),
(17, 'Nouveau-Brunswick', 6),
(18, 'Nouvelle Écosse', 6),
(19, 'Tokyo', 7),
(20, 'Kyoto', 7),
(21, 'Péninsule d’Ise', 7),
(22, 'Himeji', 7),
(23, 'Hiroshima', 7),
(24, 'Miyajima', 7),
(25, 'Hakone', 7),
(26, 'Darwin', 8),
(27, 'Northern Territory', 8),
(28, 'Kununurra', 8),
(29, 'Western Australia', 8),
(30, 'Broome', 8),
(31, 'Perth', 8);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `circuit`
--
ALTER TABLE `circuit`
  ADD CONSTRAINT `fk_Circuit_Ville1` FOREIGN KEY (`villeDepart_idVille`) REFERENCES `ville` (`idVille`),
  ADD CONSTRAINT `fk_Circuit_Ville2` FOREIGN KEY (`villeArrivee_idVille`) REFERENCES `ville` (`idVille`);

--
-- Contraintes pour la table `etape`
--
ALTER TABLE `etape`
  ADD CONSTRAINT `fk_Etape_Circuit1` FOREIGN KEY (`circuit_idCircuit`) REFERENCES `circuit` (`idCircuit`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Etape_LieuDeVisite1` FOREIGN KEY (`lieuDeVisite_codeLieu`) REFERENCES `lieudevisite` (`codeLieu`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_idVille` FOREIGN KEY (`ville`) REFERENCES `ville` (`idVille`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `lieudevisite`
--
ALTER TABLE `lieudevisite`
  ADD CONSTRAINT `fk_LieuDeVisite_Ville1` FOREIGN KEY (`ville_idVille`) REFERENCES `ville` (`idVille`);

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `fk_User_has_Circuit_Circuit1` FOREIGN KEY (`circuit_idCircuit`) REFERENCES `circuit` (`idCircuit`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_User_has_Circuit_User` FOREIGN KEY (`user_idUser`) REFERENCES `user` (`idUser`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `ville`
--
ALTER TABLE `ville`
  ADD CONSTRAINT `fk_Ville_Pays1` FOREIGN KEY (`pays_idPays`) REFERENCES `pays` (`idPays`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
