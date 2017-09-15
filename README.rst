=============================
Informations générales devChk
=============================

:Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
:Projet:             devChk
:dépôt GitHub:       https://github.com/poltergeist42-myLib/devChk
:documentation:      https://poltergeist42-mylib.github.io/devChk/
:Licence:            CC BY-NC-SA 4.0
:Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

Déscription
===========

 Librairie servant a l'assistance au developpement.
    
    Trois Class la composent :
    
        **C_DebugMsg**
            Pour afficher les messages débug en cours de développement.
            
        **C_Benchmark**
            permettant d'effectuer des mesures sur une fonction
        
        **C_GitChk**
            Pour tester la branch (git) sur la quelle on se trouve, a fin d’éviter
            les operations malheureuses.
            
            
Installation
============

 Depuis une invite de commande, ce placer dans le dossier "_3_software\devchk_pac" puis
 excuter la commande setup : ::
 
    cd .\_3_software\devchk_pac
    python setup.py install
    
**N.B** : vous devez être Root / administrateur pour effectuer cette opération.

Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref descriptif de
l'arborescence de se projet.Cette arborescence est à reproduire si vous récupérez ce dépôt
depuis GitHub. ::

	openFile               # Dossier racine du projet (non versionner)
	|
	+--project             # (branch master) contient l'ensemble du projet en lui même
	|  |
	|  +--_1_userDoc       # Contiens toute la documentation relative au projet
	|  |   |
	|  |   \--source       # Dossier réunissant les sources utilisées par Sphinx
	|  |
	|  +--_2_modelisation  # Contiens tous les plans et toutes les modélisations du projet
	|  |
	|  +--_3_software      # Contiens toute la partie programmation du projet
	|  |
	|  \--_4_PCB           # Contient toutes les parties des circuits imprimés (routage,
	|                      # implantation, typon, fichier de perçage, etc
	|
	\--webDoc              # Dossier racine de la documentation qui doit être publiée
	   |
	   \--html             # (branch gh-pages) C'est dans se dossier que Sphinx va
	                       # générer la documentation à publié sur internet
