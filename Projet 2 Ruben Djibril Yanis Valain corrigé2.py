# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:42:42 2024

@author: rubenboussa
"""



import random
from tkinter import*
from tkinter.messagebox import *
from tkinter import ttk



q98=("Quel est le nom du plus long os du corps humain ?","Tibia","Humérus","Radius","Fémur","giul")
#FAIT
q99=("Quel est l'organe responsable de la production de l'insuline ?","Foie","Rein","Estomac","Pancréas","rqze")
#FAIT
q117=("Quel temps verbal est utilisé dans la phrase 'Il mange une pomme' ?","Imparfait","Passé composé","Futur","Présent","uyfky")

q116=("Quel est le nom de l'héroïne du roman 'Madame Bovary' ?","Anna Karenina","Jane Eyre","Elizabeth Bennet","Emma Bovary","ass")
#FAIT
q109=("Quel est le nom du processus chimique de conversion d'un gaz en liquide ?","Vaporisation","Sublimation","Fusion","Condensation","bvng")
#FAIT
q100=("Quelle est la formule générale d'un acide ?","NaOH","H2SO4", "C6H12O6","HCl","aze")
#FAIT
q111=("Quel est le rôle d'une clé étrangère dans une base de données relationnelle ?","Assurer l'unicité des enregistrements","Accéder à un élément spécifique dans une table","Supprimer des enregistrements","Établir une relation entre deux tables","rfg")
#FAIT
q57=("Quel est le modèle de référence pour les réseaux informatiques qui définit sept couches ?","Modèle TCP/IP","Modèle HTTP","Modèle Ethernet","Modèle OSI")

q58=("Quelle est la phase du cycle cellulaire pendant laquelle les chromosomes sont visibles et la cellule se divise ?","Interphase","Anaphase","Télophase","Métaphase")

q59=("Quelle est la couche externe de la Terre composée de plaques qui se déplacent ?","Manteau supérieur","Noyau externe","Asthenosphère","Croûte terrestre")

q101=("Quel est le symbole chimique de l'or ?","Ag","Fe", "Cu","Au","tfg")
#FAIT
#niveau4

q97=("Quel roi de France a été exécuté pendant la Révolution française ?","Louis XIV","Louis XV","Louis-Philippe","Louis XVI","opl")
#FAIT
q62=("Quelle guerre a conduit à la création de la Déclaration des droits de l'homme et du citoyen en 1789 ?","Guerre de Cent Ans"," Guerre de Sécession","Guerre franco-allemande","Révolution américaine")

q102=("Quel pays est traversé par le fleuve Amazone ?","Colombie","Pérou","Venezuela","Brésil","fvb")
#FAIT
q104=("Quelle est la capitale la plus haute du monde ?","Bogota","Quito","Kathmandu","La Paz","thg")
#FAIT
q103=("Quelle est la somme des angles intérieurs d'un pentagone ?","450","540","720","360","dfr")
#FAIT
q107=("Quel est le produit de tous les nombres premiers entre 1 et 10 ?","210", "420","630","120","aze")
#FAIT
q67=("Quelle est la capitale du Nigeria ?","Lagos","Abuja","Kano","Ibadan","Abuja")

q68=("Quelle est la capitale de l'Argentine ?","Rio de Janeiro","Lima","Santiago","Buenos Aires")

q105=("Quelle est la fonction principale du système lymphatique ?","Transporter l'oxygène","Réguler la température","Digestion des graisses","Défendre contre les infections","uhb")
#FAIT
q70=("Quelle partie du cerveau est responsable de la régulation de la respiration et du rythme cardiaque ?","Cervelet","Hippocampe","Cerveau limbique","Tronc cérébral","tehz")

q95=("Quel écrivain français a écrit 'L'Étranger' ?","Jean-Paul Sartre","François Mauriac","Gustave Flaubert","Albert Camus","rg")
#FAIT
q72=("Quelle figure de style consiste à répéter la même consonne au début de plusieurs mots successifs ?","Anaphore","Assonance","Paronomase","Allitération","zrg")

q73=("Quel est le principe fondamental de la thermodynamique qui énonce que l'énergie totale d'un système isolé est constante ?","Deuxième principe de la thermodynamique","Troisième principe de la thermodynamique","Principe d'Archimède","Premier principe de la thermodynamique")

q96=("Quelle est l'équation chimique représentant la réaction de photosynthèse ?","C6H12O6 + 6O2 → 6CO2 + 6H2O","2H2 + O2 → 2H2O","N2 + 3H2 → 2NH3","6CO2 + 6H2O → C6H12O6 + 6O2","erhg")
#FAIT


q76=("Quel est le principe fondamental de la cryptographie asymétrique ?","Utilisation d'une seule clé pour le chiffrement et le déchiffrement","Chiffrement basé sur des algorithmes de substitution","Chiffrement basé sur des algorithmes de permutation","Utilisation de deux clés distinctes, une pour le chiffrement et une pour le déchiffrement")

q94=("Quelle est la théorie qui explique l'évolution des espèces par la sélection naturelle ?","Théorie de la relativité","Théorie du Big Bang","Théorie cellulaire","Théorie de l'évolution","trh")
#FAIT
q78=("Quelle est l'hormone produite par le pancréas qui régule la concentration de glucose dans le sang ?","Glucagon","Adrénaline","Thyroxine","Insuline","tgb")

q92=("Qui a écrit 'Le Contrat Social' ?","Voltaire",  "Montesquieu",  "Denis Diderot","Jean-Jacques Rousseau","oul")
#FAIT
q108=("Quelle planète est souvent appelée la 'planète rouge' ?","Jupiter","Vénus","Saturne","Mars","eyg")
#FAIT
q81=("Quelle est la date de la signature du Traité de Versailles mettant fin à la Première Guerre mondiale ?","1917","1918","1920","1919","zz")

q82=("Quel explorateur français a revendiqué la région de la Louisiane pour la France au 17e siècle ?","Jacques Cartier","Samuel de Champlain","Louis Jolliet","René-Robert Cavelier de La Salle")

q110=("Quelle île est le plus grand État du monde en termes de superficie ?","Borneo","Australie","Nouvelle-Guinée","Groenland","rty")
#FAIT
q90=("Quel est le détroit qui sépare l'Asie de l'Afrique ?","Détroit de Gibraltar","Détroit de Béring","Détroit de Malacca", "Détroit de Bab el Mandeb","yy")
#FAIT
q85=("Quelle est la limite de la suite (1/n) lorsque n tend vers l'infini ?","1","∞","indéfini","0","ee")

q115=("Quelle est la dérivée de la fonction sin(x) par rapport à x ?","tan(x)","sin(x)","-cos(x)","cos(x)","ss")
#FAIT
q87=("Quelle est la capitale de l'Afghanistan ?","Téhéran","Islamabad","Bagdad","Kaboul","eq(th")

q88=("Quelle est la capitale de la Nouvelle-Zélande ?","Auckland","Christchurch","Hamilton","Wellington","etq(h")

q91=("Quel est le nom scientifique de l'os de la cuisse ?","Tibia","Fibula","Patella","Fémur","eqhy")
#FAIT
q106=("Quel est le rôle des plaquettes dans le sang ?","Transport de l'oxygène","Défense immunitaire","Élimination des déchets","Coagulation sanguine","eqr")
#FAIT
q89=("Quel est le sens de l'expression latine 'Carpe Diem' ?","Lève-toi et marche","Il faut aimer pour être aimé","L'habit ne fait pas le moine","Cueille le jour","eqrh")
#FAIT
q93=("Quel écrivain a inventé le personnage de Sherlock Holmes ?","Agatha Christie","Edgar Allan Poe","G.K. Chesterton","Arthur Conan Doyle","teqh")
#FAIT
q114=("Quel est le nombre d'Avogadro ?","6.624 × 10^-34","9.81","3.1416","6.022 × 10^20","rzg")
#FAIT
q113=("Quelle est la constante de Planck ?","c","G","e","h","e(rhy")
#FAIT
q95=("Quel est le protocole de communication sécurisée utilisé pour le transfert de données sur Internet ?","FTP","SSH","SMTP","HTTPS","teqh")

q88=("Quelle est la complexité temporelle du tri fusion ('Merge Sort') ?","O(n)","O(n^2)","O(log n)","O(n log n)","eth")
#FAIT



q87=("Qu'est-ce que le chat de Schrödinger illustre dans la physique quantique ?","La dualité onde-particule", "L'effet tunnel", "L'intrication quantique", "Le paradoxe quantique","zqr")
#FAIT
q112= ("Qui est l'auteur de 'Crime et Châtiment' ?", "Leo Tolstoï", "Victor Hugo", "Jane Austen","Fiodor Dostoïevski","tee")
#FAIT
q86=("Quel est le résultat de 8 multiplié par 6 ?","36","42","54","48","t")
#FAIT
q7=("Quelle est la capitale des États-Unis ?","New York","Los Angeles", "Chicago","Washington D.C.","r")

q8=("Quelle est la capitale de la France ?","Berlin","Londres","Madrid","Paris","teh")

q84=("Quelle est la principale fonction des chloroplastes dans les cellules végétales ? ","Respiration cellulaire","Division cellulaire","Digestion","Photosynthèse","teh")
#FAIT
q85=("Quelle est la formule chimique de l'eau ?","H2O2","CO2","CH4","H2O","rjyt")
#FAIT
q83=("Quel est le symbole chimique de l'oxygène ?","O2","O3","Oh","O","th")
#FAIT
q82=("Quel langage de programmation est largement utilisé pour le développement web ?","Python","Java","C++","HTML","teh")
#FAIT


q81=("Qui a remporté la coupe du monde de football en 1998 ?","L'Italie","L'Allemagne","Le Brésil","La France","teh")
q79=("Quel est le plus grand animal terrestre ?","Éléphant","Hippopotame","Rhinocéros","Girafe ","teh")
#FAIT
q80=("Qui a composé 'La Traviata' ?", "Wolfgang Amadeus Mozart","Gioachino Rossini","Giacomo Puccini","Giuseppe Verdi","teh")
#FAIT
q77=("Quel est le plus haut sommet du monde ?","Kilimandjaro","Mont McKinley","Mont Blanc","Mont Everest","te")
#FAIT
q76=("Qui a écrit 'Le Petit Prince' ?","Albert Camus","Marcel Proust","Victor Hugo","Antoine de Saint-Exupéry","tr")
#FAIT
q75=("Qui a découvert l'Amérique ?","Vasco de Gama", "Marco Polo", "Ferdinand Magellan","Christophe Colomb","et")
#FAIT
q74=("Quel est le pays le plus grand du monde en termes de superficie ?", "Le Canada","La Chine", "Les États-Unis","la Russie","te")
#FAIT
q78=("Quel est le plus grand désert du monde ?","Gobi","Kalahari","Arctique","Sahara","ytjht")
#FAIT
q33=("Quel est le point d'ébullition de l'eau?","50°","Mont Blanc","Océan Pacifique","100°","hte")
#FAIT
q32=("Quel président américain a été assassiné lors de son défilé?","Barack Obama","Bol Bol","Ruben Dias","John Fitzgerald Kennedy","terh")
#FAIT
q31=("Que met on dans une piscine pour la désinfecter?","Du Pipi","Javel","Détergent","Chlore","tt")
#FAIT
q30=("Par quelle unité de mesure estime-t-on la valeur d'un diamant?","Joule","Berry","Dinar","Carat","te")
#FAIT
q34=("En quelle année le métro de Londres a-t-il été ouvert ?","en 1900","en 1950","en 1860","en 1863","heh")
#FAIT
q73=("Hawaï appartient à quel pays?","France","Espagne","Mexique","États-Unis","rrh")
#FAIT
q72=("Combien d'États y-a-t-il aux États-Unis ?","51","48","49","50","tre")
#FAIT
q71=("En quelle année a été signée la déclaration des droits de l homme et du citoyen ?","1800","1780","1779","1789","teq")
#FAIT
q70=("Quel est le plus long fleuve de France ?","la Loire","la Seine","le Rhône","le Rhin","teqh")
#FAIT
q69=("Quel est le plus grand océan du monde ?","l'océan arctique","l'Atlantique","L'océan indien","le Pacifique","stry")
#FAIT
q68=("Quel est le nom de la capitale du Laos ?","Vang Viang","Muang La","Sékong","Vientiane","teqjh")
#FAIT
q67=("A quelle date la 5 ème république a-t-elle été proclamée ?","14 juillet 1958","28 novembre 1958","11 septembre 1958","4 octobre 1958","te")
#FAIT
q66=("Où la première bombe atomique a-t-elle été utilisée ?","Nagasaki","Fukushima","Kawasaki","Hiroshima","tjh")
#FAIT
q65=("Quand la Seconde Guerre mondiale a-t-elle pris fin ?","1914","1918","1939","1945","teh")
#FAIT
q64=("Comment Hitler est-il mort ?","vieillesse.","maladie.","torture.","suicide.","tjt")
#FAIT
q63=("Où sont les ruines d'Angkor ?","Phnom Penh","Sihanoukville","Battambang","A Siem Reap","sqterjt")
#FAIT
q62=("Quand le premier homme a-t-il atterri sur la lune ?","En 1950","En1945","En 1978","En 1969","tjhsterj")
#FAIT
q61=("Qui a inventé l'avion ?","Philip Avion","Bruce Avion","Les soeurs Wings","Les frères Wright","tsjtj")
#FAIT
q60=("Quelle est la langue parlée en Suisse ?","le français","l'italien","le romanche","l'allemand ","trjtj")
#FAIT
q59=("En quelle année a eu lieu la découverte de l Amérique ?","En 1692","En 1500","En 1502","En 1492","teheth")
#FAIT
q58=("En quelle année l'invasion arabe de l'Espagne a-t-elle commencé ?","l'an 710","l'an 720","ça n'a jamais été une invasion","l'an 711","teheth")
#FAIT
q57=("Quel est le pays le plus peuplé du monde?","L'Inde","Le Japon","Les Etats Unis","la Chine","tjqetjh")
#FAIT
q56=("Quel est le premier film de Disney ?","Mary Poppins","Mickey Mouse","Hecule","Blanche-neige","trjhqjh")
#FAIT
q55=("Qui a écrit l Odyssée ?","Omer","Omar","Thalès","Homère","grggr")
#FAIT
q54=("De quel groupe est la chanson 'Let it be' ?","Maroon 5","4Keus","Nirvana","The Beatles","hererhhter")
#FAIT
q53=("Quelle est la langue d origine du français ?","Anglais","Allemand","Peul","Latin","eqrhqrh")
#FAIT
q52=("D'où viennent les jeux olympiques ?","Des Olympiades","d'Olympe de Gouges","D'Ulysse","De la Grèce antique dans la ville Olympe","tjheqt")
#FAIT
q51=("Comment s appelle le stade de football du Real Madrid ?","Madrida","Rivalto","Santiago","Santiago Barnabeu","etqherh")
#FAIT
q50=("Que signifie le sigle FIFA ?","fédération internationale de football","frappe intercontinental des forces anglaises","frame introspective d'une fenêtre A","fédération sportive internationale de football","etqheqh")
#FAIT
q49=("Combien de ligue des champions a gagné Paris ?","5","1","2","0","trjtj")
#FAIT
q48=("Combien de ligue des champions a gagné Marseille ?","0","2","3","1","tjeqt")
#FAIT
q47=("Combien de ligue des champions a gagné le Real Madrid ?","Maintenant, 15","12","10","13","tjtjh")
#FAIT
q46=("Qui a gagné le coupe du monde de football en 2014 ?","Le Brésil","Le Ghana","L'Italie","L'Allemagne","etjhqhr")
#FAIT
q45=("Combien de point vaut un lancer franc au basket-ball ?","deux","0,5","3","Un","tejhqet")
#FAIT
q44=("Combien de temps dure un match de football ?","120mn","100mn","95mn","90 mn","teqhqeh")
#FAIT
q43=("En combien de jours la Terre tourne-t-elle autour du Soleil ?","360","1000","500","365","ehreq")
#FAIT
q42=("Lequel des empires suivants n avait pas de langue écrite?","aztèque","égyptien", "l'empire romain","inca","tjeqheqt")
#FAIT
q41=("Jusqu’en 1923, comment s’appelait la ville turque d’Istanbul ?","Byzante","Babylone","Taplimoun","Constantinople","tejheqh")
#FAIT
q40=("Quel est le plus petit pays du monde ?","La Tunisie","La Gambie","Monaco","le Vatican","teheqth")
#FAIT
q39=("Quelle est la capitale du Canada ?","Montréal","Toronto","Vancouver","Ottawa","ytrjtrj")
#FAIT
q38=("Quel est le nom du plus long fleuve du monde ?","La loire","L'amazone","Le mississippi","le Nil","thqth")
#FAIT
q37=("Quel est le nom de la série de livres la plus vendue du 21e siècle?","Le Hobbit","Dragon Ball","One Piece","Harry Potter","strjeqtj")
#FAIT
q36=("Quelle langue comprend le plus grand nombre de mots selon les entrées du dictionnaire ?","Le mandarin","Le français","Le latin","l'anglais","ghsth")
#FAIT
q35=("Quel artiste a peint le plafond de la chapelle Sixtine à Rome ?","Léonard de Vinci","Raphaël","Melozzo da Forlì","Michel-Ange","terheqtrh")
#FAIT
q1=("Quelle pièce est absolument à protéger dans un jeu d’échec ?","La Reine","Le Prince","Le Fou","Le Roi","teqhqeht")
#FAIT
q2=("Quelle est la capitale de l’Australie ?","Sydney","Darwin","Melbourne","Canberra","erheqh")
#FAIT
q3=("Quelle année a suivi l'an 1 avant JC ?","Celle de la guerre sainte", "an 1", "l'anné des Empereurs","L'an 1 après JC","rs")
#FAIT
q5=("Qui anime Secret Story?","Patrick Bruel","Ardisson","Adrien Quatennens","Benjamin Castaldi","tjersjh")
#FAIT
q7=("Combien de nouvelles chaînes sont apparus grâce à la TNT ?","15","35","20","12","tjqehq")
#FAIT
q9=("Combien y a-t-il de signes astrologiques chinois ?","20","30","25","12","tjtjh")
#FAIT
q10=("Quel est le 2ème nom de l’hippocampe ?","le cheval des océans","le poisson des mers","Bambi océanique","Le cheval de mer","tjheth")
#FAIT
q11=("En quelle année est mort John Fitzgerald Kennedy ?","1960","1965","1970","1963","etheqtrh")
#FAIT
q12=("Combien de dieu trône a l’Olympe ?","13","20","15","12","theth")
#FAIT
q13=("Qu’appelle-t-on la canopée ?","La forêt amazonienne","Le bout d'une flûte","L'objectif d'un appareil photo","Le sommet de la forêt amazonienne","thteh")
#FAIT
q14=("Quelle est le dernier album de Britney Spears ?","Glory","Blackout","Britney","Circus","ththehtr")
#FAIT
q15=("Quel est l’équivalent du pape au Tibet ?","Bảo Đại","Le Patriark","K'ien-long","Le dallai lama","thetqhh")
#FAIT
q16=("Quelle est la différence entre le chameau et le dromadaire ?","Le crachat","La résistance à la chaleur","La vitesse de déplacement","Le nombre de bosses","teheqth")
#FAIT
q17=("Quel précipité observe-t-on quand on mélange du nitrate d’argent avec du chlore ?","de l'eau iodée","un précipité bleu","un précipité rouille","Un précipité blanc qui se noircit","tehteh")
#FAIT
q18=("Quelle est la voiture dans Retour vers le futur?","Octane","Zentorno","Light Cycle","Doloréanne","rheqr")
#FAIT
q20=("Comment s’appelle l’équivalent du musée Grévin à Londres ?","musée London","museum of stars's wax statues","Adam's museum","musée de Madame Tussaud","reher")
#Fait
q21=("1+2+3+4 ?","3", "8", "5", "10","rehger")
#FAIT
q23=("Quel ville est surnommé « big Apple » aux USA ?","Chicago","Las Vegas","Los Angeles","New York","rehehr")
#FAIT
q24=("De combien de syllabes est composé un alexandrin ?","8","6","1","12","thetr")
#FAIT
q25=("De qui est amoureux Juliette ?","Anis", "Richarlison","Julien","Roméo","etrh")
#FAIT
q26=("Quel est la 1ère émission de télé réalité a avoir été diffuser en France ?","Secret Story", "LE BLOC","Plus Belle La Vie","Loft story","th")
#FAIT
q27=("Qui a écrit les misérables ?","José Mourinho", "Frank Lucas","Francisco Da Vicente de la Roche","Victor Hugo","th")
#FAIT
q29=("Comment appelle-t-on la lumière qui se rapproche le plus de la lumière du soleil ?","La lumière noire","La blancheur","lightover","La lumière blanche","yj")
#FAIT

#les listes de questions
liste1=[q33,q32,q31,q75,q21,q3,q25,q27,q45,q52,q85]
liste2=[q73,q72,q24,q48,q1,q2,q39,q43,q50,q65,q83,q116]
liste3=[q23,q49,q15,q37,q74,q30,q77,q78,q79,q81,q86,q109]
liste4=[q53,q64,q36,q38,q51,q46,q55,q57,q82,q102]
liste5=[q71,q9,q26,q44,q16,q35,q41,q84,q89,q91,q108]
liste6=[q34,q18,q40,q59,q68,q69,q70,q93,q97,q103]
liste7=[q20,q10,q66,q56,q47,q90,q92,q96,q98,q104]
liste8=[q54,q29,q12,q42,q60,q76,q95,q99,q105,q110,q115]
liste9=[q62,q14,q11,q5,q67,q80,q100,q106,q107,q11,q114]
liste10=[q63,q13,q7,q61,q58,q87,q88,q101,q112,q113]
#liste1 mise à part spécialement pour la fonction choix qui lance le jeu
listes=[liste2,liste3,liste4,liste5,liste6,liste7,liste8,liste9,liste10]


def Exit():
    """Lorsque le joueur souhaite quitter le jeu."""
    global gainde
    #affichage d'un messagebox qui confirme la sortie du jeu
    msgbox=askquestion("Quitter la partie","Vous quittez vraiment ? Vous partez avec un gain de " +(gainde.get()), icon="error")
    if msgbox=="yes":
        fenetre.destroy()
    else:
        showinfo("Merci de rester", "T'es chaud")

def mvreponse():
    """Lorsque c'est la mauvaise réponse la fonction fait recommencer le jeu"""
    global reponse4
    global r4_clicks
    #affichage d'un messagebox qui contient la bonne réponse
    msgbox2=askretrycancel("MAUVAISE REPONSE","C'est la mauvaise réponse !!!!!Dommage, vous perdez tout.C'était "+(reponse4.get()),)
    if msgbox2==True:
        choix()
        r4_clicks=0
        cinquante_cinquante["state"]=NORMAL
        appeler_un_ami["state"]=NORMAL
        r1.grid()
        r2.grid()
    else:
        fenetre.destroy()
def cinq_cinq():
    """Fonction qui enlève deux réponses de la question actuelle et fait disparaitre le bouton 50/50."""
    r2.grid_forget()
    r3.grid_forget()
    cinquante_cinquante["state"]=DISABLED
    r2["state"]=NORMAL
    r3["state"]=NORMAL
def ipl_ami():
    """Fonction qui retourne une variable z contenant une réponse parmi les quatres réponses."""
    global reponse1,reponse2,reponse3,reponse4
    List=[reponse1.get(),reponse2.get(),reponse3.get(),reponse4.get()]
    z.set(random.choices(List,weights=(10,10,10,20),k=1))
    return z


def  ami():
    """appel la fonction ipl_ami et donne la réponse de l'ami et fait disparaitre le bouton appeler un ami."""
    ipl_ami()
    #l'ami est un messagebox
    showinfo("Ami","je pense que la réponse est......"+(z.get()),)
    appeler_un_ami["state"]=DISABLED


def choix():
    """Fonction qui lance le jeu et pioche dans la liste1."""
    #récupère une question et affiche ses éléments via l'indice
    a=random.choice(liste1)

    b=a[0]
    c=a[1]
    d=a[2]
    e=a[3]
    f=a[4]
    affichage_question.set("Question 1/10 +500 euros")
    gainde.set("0 euros")
    return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)

#Le nombre de clics sur la bonne réponse
r4_clicks=0
def progression():
    """Fonction qui progresse au fur et à mesure dans les listes lorsque la bonne réponse est cliquée et met à jour toutes les variables importantes sur l'écran de jeu."""
    global r4_clicks

    r4_clicks=r4_clicks+ 1
    if r4_clicks==1:
        #affichage d'un message de réussite
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste2))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 2/10 +1000 euros")
        gainde.set("500 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==2:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste3))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 3/10 +3500 euros")
        gainde.set("1500 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==3:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste4))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 4/10 +5000 euros")
        gainde.set("5000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==4:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste5))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 5/10 +20000 euros")
        gainde.set("10000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==5:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste6))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 6/10 +700 000 euros")
        gainde.set("30000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==6:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste7))

        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 7/10 +1000000 euros")
        gainde.set("730 000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==7:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste8))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 8/10 +2000000 euros")
        gainde.set("1730000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==8:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste9))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 9/10 +4000000 euros")
        gainde.set("3730000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==9:
        showinfo("GG","C'était la bonne réponse, bien joué!!!!!")
        placement()
        a=(random.choice(liste10))
        b=a[0]
        c=a[1]
        d=a[2]
        e=a[3]
        f=a[4]
        affichage_question.set("Question 10/10 +5000000 euros")
        gainde.set("7730000 euros")
        return question.set(b), reponse1.set(c),  reponse2.set(d), reponse3.set(e), reponse4.set(f)
    elif r4_clicks==10:
        gainde.set("19300000 euros")
        #message de fin
        showinfo("T'es le Boss","GGGGGGGG!!!!!!!!Vous avez terminé le jeu, trop fort. Vous repartez avec un gain de " +(gainde.get())+("!!!!!  Vous avez brassé!!!"))
        fenetre.destroy()



def placement():
    """Fonction qui permute les placements des réponses à chaque question."""
    global progression
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    random.shuffle(positions)

    for i,element in enumerate(boutons):
        (ligne,colonne)=positions[i]
        element.grid(row=ligne, column=colonne,**grid_dict)
        

#Création de la fenêtre
fenetre=Tk()
fenetre.title("Qui veut être milliardaire?")
fenetre.state("zoomed")
fenetre['bg']='#800F2F'
#Preimière utilisation de la méthode grid pour configurer la grille de la fenetre et qui sera utilisée de nombreuses fois
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)
fenetre.grid_rowconfigure(3, weight=1)
fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure(2, weight=1)
#Dictionnaires pas trop utiles
grid_dict = { "padx":10, "pady":10, "ipadx":20,"ipady":20,}
grid2_dict={"padx":10, "pady":10}
#Création des variables Stringvar permettant d'avoir des variables qui peuvent être mises à jour qu'on va affecter plus tard
z=StringVar()
affichage_question=StringVar()
gainde=StringVar()
question=StringVar()
reponse1=StringVar()
reponse2=StringVar()
reponse3=StringVar()
reponse4=StringVar()
#Le LabelFrame qui occupe la partie supérieur de l'écran de jeu et affiche la question
demarrage= LabelFrame(fenetre, bg='#FFBD74', relief=SUNKEN,fg='white',  text="Qui veut être milliardaire ",font=("Comic Sans MS", 10), padx=20, pady=20)
demarrage.grid(sticky='nsew',column=0, row=0,columnspan=3, ipadx=50, ipady=50, padx=100)
#La Question actuelle
Label1=Label(demarrage,bg='#FFBD74',textvariable=question, font=("Arial Black", 15))
Label1.pack()
#La Question actuelle sur les 10 et affiche le gain à gagné
Label2=Label(demarrage,bg='#FFBD74',textvariable=affichage_question, font=("Arial Black", 10))
Label2.pack(side=BOTTOM)
#Le deuxième LabelFrame qui occupe la partie gauche de l'écran de jeu et affiche le gain actuelle
affichage_gain= LabelFrame(fenetre, bg='#FFBD74', relief=SUNKEN,fg='white',  text="Votre Gain actuelle",font=("Comic Sans MS", 10))
affichage_gain.grid(column=0, row=3, rowspan=1, ipadx=5, ipady=5, )
#Le Gain Actuelle
Labelgain=Label(affichage_gain,bg='#FFBD74',textvariable=gainde,font=("",15))
Labelgain.pack()
# frame 2 située au milieu de l'écran de jeu contenant les réponses à la question
Frame2 = Frame(fenetre,bg='#212529',  borderwidth=5, relief=SUNKEN)
#Utilisation de la méthode grid pour placer la Frame2 dans la fenetre comme pour les autres widgets présents dans la fenêtre et pour créer sa grille
Frame2.grid(column=1, row=3, ipadx=100, ipady=100, **grid2_dict)
Frame2.grid_rowconfigure(0, weight=1)
Frame2.grid_rowconfigure(1, weight=1)
Frame2.grid_columnconfigure(0, weight=1)
Frame2.grid_columnconfigure(1, weight=1)
#Placement et personnalisation des réponses dans la grille de la Frame2
r1=ttk.Button(Frame2,takefocus=False, textvariable=reponse1,command=mvreponse)
r1.grid(column=0, row=0,**grid_dict )
r2=ttk.Button(Frame2,takefocus=False, textvariable=reponse2,command=mvreponse)
r2.grid(column=0, row=1,**grid_dict)
r3=ttk.Button(Frame2,takefocus=False, textvariable=reponse3,command=mvreponse)
r3.grid(column=1, row=0,**grid_dict)
r4=ttk.Button(Frame2,takefocus=False, textvariable=reponse4,command=progression)
r4.grid(column=1, row=1,**grid_dict)
boutons=[r1,r2,r3,r4]
#Frame3 située à droite de l'écran de jeu et contient les trois boutons pour quitter le jeu, pour le cinquante cinquante, et pour appeler un ami
Frame3=Frame(fenetre,bg='#800F2F',)
#Utilisation de la méthode grid comme pour la Frame2 et les autres widgets présents dans la fenetre
Frame3.grid(sticky='ns', column=2, row=3, rowspan=4,columnspan=1, ipadx=10,)
Frame3.grid_columnconfigure(0, weight=1)
Frame3.grid_rowconfigure(0, weight=1)
Frame3.grid_rowconfigure(1, weight=1)
Frame3.grid_rowconfigure(2, weight=1)
#Placement et personnalisation des boutons dans la Frame3
bouton_quitter=Button(Frame3,bg='#800F2F', text='QUITTER LE JEU', relief=FLAT, fg='white',font=("Comic Sans MS", 20), command=Exit)
bouton_quitter.grid(column=0, row=2,**grid_dict)
appeler_un_ami=Button(Frame3,bg='#800F2F',text='APPELER UN AMI', relief=FLAT, fg='white',font=("Comic Sans MS", 20), command=ami)
appeler_un_ami.grid(column=0, row=1,**grid_dict)
cinquante_cinquante=Button(Frame3, bg='#800F2F',text='50/50', relief=FLAT, fg='white',font=("Comic Sans MS", 20), command=cinq_cinq)
cinquante_cinquante.grid(column=0, row=0,**grid_dict)
#Appel de certaines fonctions
choix()
placement()
fenetre.mainloop()