#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Librairie servant a l'assistance au developpement.
    
    Trois Class la composent :
    
        **C_DebugMsg**
            Pour afficher les messages debug en cours de devellopement.
            
        **C_Benchmark**
            permettant d'effectuer des mesures sur une fonction
        
        **C_GitChk**
            Pour tester la branch (git) sur la quelle on se trouve, a fin d'eviter
            les operations malheureuses.
"""

__version__= "20170915"

from devchk_pac.devchk import C_DebugMsg
from devchk_pac.devchk import C_Benchmark
from devchk_pac.devchk import C_Benchmark