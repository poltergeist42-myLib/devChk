#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Nom du fichier:     devChk.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170902

####

    :dépôt GitHub:       https://github.com/poltergeist42-myLib/devChk
    :documentation:      https://poltergeist42-mylib.github.io/devChk/
    :Licence:            CC-BY-NC-SA
    :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev langage:       Python 3.4

####

List des Libs
=============

    * os
    * time
    * functools

####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 matrice
   
####

"""

from os import system, remove
import time
import functools

__all__ = ["C_DebugMsg", "C_Benchmark", "C_GitChk"]

class C_DebugMsg(object) :
    """ **C_DebugMsg(object)**
    
        Class permettant d'afficher les message de debug.

        Cette Class peut être utilisée en tan que décorateur à placer avant l'appel de
        la fonction. 
        
        Appel du décorateur : ::
        
            @C_DebugMsg(0)  --> affichage désactiver
            @C_DebugMsg(1)  --> affichage activer
        
        
        Cette class peut aussi être instancier :
        Elle doit être instancier dans la fonction **__init__()** pour une Class
        et instancier en premier dans la fontion **main()** pour les fonctions
        n'appartenenant pas a une Class.
                
        Le constructeur a un argument par defaut de type **booleen** qui est predefinis
        sur **True**. Si se parametres est a **False**,
        l'ensemble des messages seront masques.
        
        Creation de l'instance :
        ::
        
            i_monIstanceDbg = C_DebugMsg( [booleen (facultatif si == True)] )
    """
    d_adr = {}
        # variable de class, elle est commune à toute les instance de la class
    v_clsAffichage = False
    def __init__( self,  *argsDecoratorIst, **kwargsDecoratorIst) :
        """ Init variables """
        self.argsDecoratorIst            = argsDecoratorIst
            # positional arguments passés au décorateur
        self.kwargsDecoratorIst          = kwargsDecoratorIst
            # default arguments passés au décorateur

        self._v_funcName        = ""
        self._v_outputFn       = ()
        self._v_inputFnArgs     = 0
        self._v_inputFnKwargs   = 0
        

        ## Control des positional arguments
        if self.argsDecoratorIst :
            for arg in self.argsDecoratorIst :
                if isinstance(arg, bool) :
                    C_DebugMsg.v_clsAffichage       = bool(arg)
                else :
                    C_DebugMsg.v_clsAffichage       = bool(arg)

        ## Control des default arguments
        if "affichage" in self.kwargsDecoratorIst :
            C_DebugMsg.v_clsAffichage      = bool(self.kwargsDecoratorIst["affichage"])

        self.debugNumber        = 0
        self.d_fnNumber         = {}
        
        ## retrocompatibilité
        self.dbgPrint           = self.f_dbgPrint
        self.dbgDel             = self.f_dbgDel
        
    def __call__( self, v_func ) :
        @functools.wraps(v_func)
        def f_appelFonc( *args, **kwargs ) :
            """ méthode appelée à chaque appel de la fonction décorée """
            ## av Fonction décorée
            self.f_setFuncName( v_func )
            self.f_setInputFnArgs( args )
            self.f_setInputFnKwargs( kwargs )
            
            ## Fonction décorée
            v_functionDecoree = v_func( *args, **kwargs )
            
            ## ap Fonction décorée
            self.f_setOutputFn( v_functionDecoree )
            self.f_dbgDecoratorPrint()
            
            return v_functionDecoree
            self.__class__.adr[v_func.__name__] = self
        return f_appelFonc

    def f_setInputFnArgs( self, l_args ) :
        """ Récupère l'ensenble des 'positional arguments' passés à la fonction """
        self._v_inputFnArgs  = l_args
        
    def f_getInputFnArgs( self ) :
        """ Retourne '_v_inputFnArgs' """
        return self._v_inputFnArgs
        
    def f_setInputFnKwargs( self, d_kwargs ) :
        """ Récupère les 'default arguments' passés à la fonction """
        self._v_inputFnKwargs = d_kwargs

    def f_getInputFnKwargs( self ) :
        """ Retourne '_v_inputFnKwargs' """
        return self._v_inputFnKwargs
    
    def f_setFuncName( self, v_func ) :
        """ récupère le nom de la fonction """
        self._v_funcName = v_func.__name__
    
    def f_getFuncName( self ) :
        """ retourne '_v_funcName' """
        return self._v_funcName

    def f_setAffichage( self, v_bool ) :
        """ **f_setAffichage( bool )**
        
            permet d'activer ( True ) ou de desactiver ( False ) l'affichage.
        """
        C_DebugMsg.v_clsAffichage = bool( v_bool )
        
    def f_getAffichage( self ) :
        """ retourne 'C_DebugMsg.v_clsAffichage' """
        return C_DebugMsg.v_clsAffichage

    def f_setOutputFn( self, v_funcRetun ) :
        """ permet de récupérer se que retourne la fonction décorée """
        self._v_outputFn = v_funcRetun

    def f_getOutputFn( self ) :
        """ retourne '_v_outputFn' """
        return self._v_outputFn

    def f_dbgDecoratorPrint( self ) :
        """ Permet d'afficher les informations générées par la fonction décorée """
        if self.f_getAffichage() :
            print( "dbgMsg[ {} ] :".format(self.f_getFuncName()))
            # if self.f_getInputFnArgs() :
            print( "\t* Input :" )
            for i  in self.f_getInputFnArgs() :
                print( "\t\t--> {} - {}".format( type(i), i))
                    
            # if self.f_getInputFnKwargs( self ) :
            for k in self.f_getInputFnKwargs() :
                print( "\t\t--> {} - {}={}".format(
                    type(self.f_getInputFnKwargs()[k]),
                    k, self.f_getInputFnKwargs()[k]))
                    
            print( "\t* Ouput :" )
            # if isinstance( self.f_getOutputFn(), NoneType) :
                # print( "\t\t--> {} - {}".format( 
                    # type(self.f_getOutputFn()), self.f_getOutputFn()))
            try :
                if isinstance(self.f_getOutputFn(), str) :
                    print( "\t\t--> {} - {}".format( 
                    type(self.f_getOutputFn()), self.f_getOutputFn()))
                else :
                    for i in self.f_getOutputFn() :
                        print( "\t\t--> {} - {}".format( type(i), i))
            except TypeError:
                print( "\t\t--> {} - {}".format( 
                    type(self.f_getOutputFn()), self.f_getOutputFn()))
                        
    def f_dbgPrint(self, v_chk, v_varName, v_varValue, v_endOfLine = "") :
        """
            Intercept les messages pour les formater de facon homogene.
            
            Pour permettre de masquer les messages d'une seule fonction a la fois,
            il est conseille d'ajouter une variable local initialisee a **True**
            et de l'appeler a chaque fois que le debug et necessaire. Cette variable doit etre
            mise a **False** pour que l'affichage local soit desactive.
            
            Ex: ::
                    
                    # Affichage active
                    v_dbg = True
                    i_monIstanceDbg.f_dbgPrint(   v_dbg, 
                                                ["chaine_de_caractere"],
                                                [la_variable_a_controller]
                                            )
                                        
                    # Affichage desactive
                    v_dbg = False
                    i_monIstanceDbg.f_dbgPrint(   v_dbg, 
                                                ["chaine_de_caractere"],
                                                [la_variable_a_controller]
                                            )
                                        
            Pour desactiver l'affichage d'un seul message a la fois, on peut remplacer la
            variable locale par une valeur **booleen**. On peut aussi simplement commenter
            la ligne du message de debug.
            
            Ex: ::
            
                    # Affichage desactive par une valeur booleen
                    v_dbg = True
                    i_monIstanceDbg.f_dbgPrint(   False, 
                                                ["chaine_de_caractere"],
                                                [la_variable_a_controller]
                                            )
                                        
                    # Affichage desactive en commentant la ligne
                    v_dbg = True
                    # i_monIstanceDbg.f_dbgPrint(   v_dbg, 
                                            # ["chaine_de_caractere" ou varialbe_de_reference],
                                            # [la_variable_a_controller]
                                        # )
                                        
            Pour faciliter la lecture lors du debug un numero unique est attribue
            a chaque fonction.
        """
        if v_chk and C_DebugMsg.v_clsAffichage :
            if not self.d_fnNumber :
                self.d_fnNumber[v_varName] = self.debugNumber
                print( "dbgMsg[ {} ] : {} - {}{}".format(self.d_fnNumber[v_varName], v_varName, v_varValue, v_endOfLine) )
                
            if v_varName in self.d_fnNumber.keys() :
                if self.debugNumber :
                    print( "dbgMsg[ {} ] : {} - {}{}".format(self.d_fnNumber[v_varName], v_varName, v_varValue, v_endOfLine) )
                
            else :
                self.debugNumber += 1
                self.d_fnNumber[v_varName] = self.debugNumber
                print( "dbgMsg[{}] : {} - {}{}".format(self.d_fnNumber[v_varName], v_varName, v_varValue, v_endOfLine) )
                
    def f_dbgDel( self, v_chk, v_varValue ) :
        """ permet d'informer de la fin d'une instannce ( methode : '__del__')"""
        if v_chk and C_DebugMsg.v_clsAffichage :
                print( "\n\t\tL'instance de la class {} est terminee".format( v_varValue ))
                
##########################################################################################
    
class C_Benchmark( object ) :
    """ **C_Benchmark( object )**
    
        Calss permettant d'effectuer des mesures sur une fonction

        - si "time" est passé comme premier argument, la classe renvaira le temps
          d'éxécution de la fonction décorée.
    """
    d_adr = {}
        # variable de class, elle est commune à toute les instance de la class
        
    v_clsAffichage = False
        
    def __init__( self, *argsDecoratorIst, **kwargsDecoratorIst ) :
        """ Déclaration des variable global """
        self.argsDecoratorIst      = argsDecoratorIst
            # positional arguments passés au décorateur
        self.kwargsDecoratorIst    = kwargsDecoratorIst
            # default arguments passés au décorateur
            
        ## Control des positional arguments
        if self.argsDecoratorIst :
            for arg in self.argsDecoratorIst :
                if isinstance(arg, bool) :
                    C_Benchmark.v_clsAffichage       = bool(arg)

                elif isinstance(arg, str) :
                    if arg.lower() == "time" :
                        self.v_timeChk      = True
                        self.v_CPUChk       = False

                    if arg.lower() == "cpu" :
                        self.v_timeChk      = False
                        self.v_CPUChk       = True

                else :
                    C_Benchmark.v_clsAffichage       = bool(arg)

            
        self._v_funcName        = ""
        self._v_startTime       = 0
        self._v_tmpEcoule       = 0
        self._v_tmpCumule       = 0
        self._v_tmpMoyen        = 0
        self._v_nbeAppel        = 0
            
    def __call__( self, v_func ) :
        @functools.wraps(v_func)
        def f_appelFonc( *args, **kwargs ) :
            """ méthode appelée à chaque appel de la fonction décorée """
            ## av Fonction décorée
            self.f_setFuncName( v_func )
            if self.v_timeChk :
                self.f_setNbeAppel()
                self.f_setStartTime()
                
            if self.v_CPUChk :
                pass
                
            ## Fonction décorée
            v_functionDecoree = v_func(*args, **kwargs)
            
            ## ap Fonction décorée
            if self.v_timeChk :
                self.f_setTempEcoule()
                self.f_setTmpCumule()
                self.f_setTmpMoyen()
                
                self.f_timePtrMsg()
                                
            if self.v_CPUChk :
                pass
                
            return v_functionDecoree
            self.__class__.adr[v_func.__name__] = self
            print( ":: " )
        return f_appelFonc

    def f_setAffichage( self, v_bool ) :
        """ **f_setAffichage( bool )**
        
            permet d'activer ( True ) ou de desactiver ( False ) l'affichage.
        """
        C_Benchmark.v_clsAffichage = bool( v_bool )
        
    def f_getAffichage( self ) :
        """ retourne 'C_Benchmark.v_clsAffichage' """
        return C_Benchmark.v_clsAffichage

    def f_setFuncName( self, v_func ) :
        """ récupère le nom de la fonction """
        self._v_funcName = v_func.__name__
    
    def f_getFuncName( self ) :
        """ retourne '_v_funcName' """
        return self._v_funcName

    def f_setStartTime( self ) :
        """ récupère le début d'éxécution de la fonction décorée """
        self._v_startTime = time.clock()
        
    def f_getStartTime( self ) :
        """ retourne '_v_startTime' """
        return self._v_startTime

    def f_setTempEcoule( self ) :
        """ calcul le temp ecoulé depuis le début de fonctionnement de la fonction """
        self._v_tmpEcoule = time.clock() - self.f_getStartTime()

    def f_getTempEcoule( self ) :
        """ retourne '_v_tmpEcoule' """
        return self._v_tmpEcoule
        
    def f_setTmpCumule( self ) :
        """ Calcul le temp total d'éxécution de la fonction (addition des temps de
            chaque appel)
        """
        self._v_tmpCumule += self.f_getTempEcoule()
        
    def f_getTmpCumule( self ) :
        """ retourne '_v_tmpCumule' """
        return self._v_tmpCumule

    def f_setTmpMoyen( self ) :
        """" calcul la durée moyenne d'éxécution de la fonction décorée """
        self._v_tmpMoyen = self.f_getTmpCumule() / self.f_getNbeAppel()

    def f_getTmpMoyen( self ) :
        """ retourne '_v_tmpMoyen' """
        return self._v_tmpMoyen

    def f_setNbeAppel( self ) :
        """ compte le nombre d'appel fait sur la fonction """
        self._v_nbeAppel += 1

    def f_getNbeAppel( self ) :
        """ retourne '_v_nbeAppel' """
        return self._v_nbeAppel

    def f_timePtrMsg( self ) :
        """ affiche à l'écran le résultat du décorator 'time' """
        if self.f_getAffichage() :
            print(  "timMsg[ {0} ] : durée : {1} - moyenne : {2} - "\
                    "Nbe d'appel : {3} - total : {4}".format(
                        self.f_getFuncName(), self.f_getTempEcoule(),
                        self.f_getTmpMoyen(), self.f_getNbeAppel(),
                        self.f_getTmpCumule() 
                        ))

##########################################################################################
        
class C_GitChk(object) :
    """**C_GitChk(object)**
    
    Class permettant de tester la branch (git) sur la quelle on se trouve. Un message est
    affiché sur la console pour nous indiquer la branch courante.
    
    
    Cette Class peut être instancier dans la fonction **main()**, ou utilisée comme décorateur.
    
    - les arguments str('d') et str('f') permettent d'indiquer la branche courante au
      "d"ébut ou à la "f"in de la fonction décorée. Ces argument ne sont pas pris en
      compte dans une instance classique.
      
    - Les arguments booléin (0-False : 1-True) permettent de désactiver ou d'activer le
      controle de la branch.

    """
    d_adr = {}
        # variable de class, elle est commune à toute les instance de la class
        
    def __init__( self, *argsDecoratorIst, **kwargsDecoratorIst ) :
        """ Déclaration des variable global """
        self.argsDecoratorIst         = argsDecoratorIst
            # positional arguments passés au décorateur
        self.kwargsDecoratorIst       = kwargsDecoratorIst
            # default arguments passés au décorateur

        ## valeur par défaut si aucun argument n'est passé
        self.v_ctrl                 = True
        self.v_debutFin             = "d"
            
        ## Control des positional arguments
        if self.argsDecoratorIst :
            for arg in self.argsDecoratorIst :
                if isinstance(arg, bool) :
                    self.v_ctrl     = arg
                
                elif isinstance(arg, str) :
                    if(arg.lower() == 'd') or (arg.lower() == 'f') :
                        self.v_debutFin = arg

                else :
                    self.v_ctrl     = bool(arg)

        ## Control des default arguments pour les clef "ctrl" et "df"
        if "ctrl" in self.kwargsDecoratorIst :
            self.v_ctrl             = bool(self.kwargsDecoratorIst["ctrl"])

        if "df" in self.kwargsDecoratorIst :
            self.v_debutFin         = self.kwargsDecoratorIst["df"].lower()

    def __del__(self) :
        """destructor
        
            il faut utilise :
            ::
            
                del [nom_de_l'_instance]
        """
        try :
            remove( "./chkBranch" )
        except FileNotFoundError :
            pass
            
    def __call__( self, v_func ) :
        @functools.wraps(v_func)
        def f_appelFonc( *args, **kwargs ) :
            """ méthode appelée à chaque appel de la fonction décorée """
            ## av Fonction décorée
            if self.v_debutFin == "d" :
                self.f_gitBranchChk()
            
            ## Fonction décorée
            v_functionDecoree = v_func( *args, **kwargs )
            
            ## ap Fonction décorée
            if self.v_debutFin == "f" :
                self.f_gitBranchChk()
            
            return v_functionDecoree
            self.__class__.adr[v_func.__name__] = self
        return f_appelFonc

    def f_gitBranchChk(self):
        """ 
        identifie la branch courante et emet une alerte
        si elle est differente de '* master'
        
        """
        if self.v_ctrl :
            v_chkFile = "./chkBranch"
            system("git branch > {}".format(v_chkFile))
            v_char = "*"
            v_chk = True
            v_chaineIsTrue = True
            
            with open(v_chkFile) as v_localLib :
                for line in v_localLib : 
                    if v_char in line : 
                        v_activeBranch = line[:-1]
 
            v_spaceAv = (40-len(v_activeBranch))//2
            v_spaceAp = 40-(v_spaceAv+len(v_activeBranch))
            print   (   """
                ##########################################
                #                                        #
                #  Attention, vous êtes sur la branch :  #
                #                                        #
                #{}{}{}#
                #                                        #
                ##########################################
                        """.format((" "*v_spaceAv), v_activeBranch,(" "*v_spaceAp))
                    )

        else :
            print("\n## le control de branch est desactive")
    
##########################################################################################

@C_DebugMsg() 
@C_Benchmark("time")
@C_GitChk(1, 'f')
def main():
    """ 
    Fonction principale 
    
    Cette Fonction ne sert que pour tester les differentes Class
    et methode de ce projet.
    """
    C_DebugMsg(1)
    C_Benchmark(1)
    
    #################################
    # Test de la class 'C_DebugMsg' #
    #################################
    i_debugTest = C_DebugMsg()
    
    v_dbg = True
    i_debugTest.f_dbgPrint(   v_dbg, 
                            "chaine_de_caractere",
                            main
                        )
                        
    ###############################
    # Test de la class 'C_GitChk' #
    ###############################
    i_git = C_GitChk(False)
    i_git.f_gitBranchChk()
    
if __name__ == '__main__':
    main()
