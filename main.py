# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Ce programme calcule les gammes et leurs chromatismes.

import inspect
from typing import Callable
# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def print_hi(base_intervalles):
    """Programme de traitement du dictionnaire des intervalles établis par Grok.
    -   Les intervalles servent à positionner les notes musicales :
            Do, Ré, Mi, Fa, Sol, La, Si = [C, D, E, F, G, A, B] = not_mus.
            À l'aide des signes d'altérations bémol et dièse :
                #, ##, ###, ####, ##### = ["+", "x", "^", "+^", "x^"] = sig_not[:5]
                bbbbb, bbbb, bbb, bb, b = ["o*", "-*", "*", "o", "-"] = sig_not[5:]
    On a besoin des notes musicales, des signes d'altérations et des ordres chromatiques.
        L'ordre chromatique inférieur = ord_chr[0] = [(2, 3, 5, 6, 7)].
        L'ordre chromatique supérieur = ord_chr[1] = [(1, 2, 4, 5, 6)].
    Commentaire : les 462 modulations ont toutes les tonalités en Do avec un maximum de cinq signes altératifs."""

    "# Listes des notes, des signes d'altérations et des ordres chromatiques"
    not_mus = ["C", "D", "E", "F", "G", "A", "B"]  # Les notes naturelles.
    sig_not = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]  # Les signes d'altération.
    # Indice inversé de '-' = sig_not.index('-') - len(sig_not).
    ord_chr = [(2, 3, 5, 6, 7), (1, 2, 4, 5, 6)]  # Les ordonnances chromatiques (inf/sup).
    (lineno(), not_mus, "Bémols", sig_not[5:], "Dièses", sig_not[:5], "\nOrdres", ord_chr)
    # 27 ['C', 'D', 'E', 'F', 'G', 'A', 'B'] Bémols ['o*', '-*', '*', 'o', '-'] Dièses ['+', 'x', '^', '+^', 'x^']
    # Ordres [(2, 3, 5, 6, 7), (1, 2, 4, 5, 6)]
    (lineno(), "Longueur bases :", len(base_intervalles.keys()))  # 30 Longueur base : 66

    # Établir une boucle de lecture des clefs du dictionnaire : base_intervalles.
    "# Table des intervalles majeurs"
    int_maj = (2, 2, 1, 2, 2, 2, 1)  # Même typage que base_intervalles[key].
    gam_notes, dic_rang = {}, {}
    for key in base_intervalles:
        k_bi = base_intervalles[key]  # Copie du degré modal en cours.
        gam_notes[key, k_bi] = []  # Initialisation du support modal.
        dic_rang[key] = []
        (lineno(), "key, k_bi", key, k_bi)
        # 42 key, k_bi 1 (1, 1, 1, 1, 1, 1, 6)
        ("# Commencer par le premier élément du dictionnaire : base_intervalles."
         "Pour les renversements des modes diatoniques.")
        for i in range(len(k_bi)):
            "# Renversement par modulation diatonique, le premier égale l'original."
            mod_rang = k_bi[len(k_bi) - i:] + k_bi[:len(k_bi) - i]
            dic_rang[key].append(mod_rang)
            i, im = 0, [(0, "C")]
            cum_m, cum_g = 0, 0
            y = 0
            while y < 6:
                "# Découverte du nombre de signe par note :"
                cum_m += int_maj[y]  # Ajoute la valeur de l'intervalle majeur.
                cum_g += mod_rang[y]  # Ajoute la valeur de l'intervalle modal.
                res_mg = cum_g - cum_m  # Calcule la différence pour obtenir le signe d'altération.
                sig_mg = sig_not[res_mg]  # Sélection du signe dans la liste des altérations sig_not.
                res_sig = sig_mg, not_mus[y+1]  # Couple du signe et de la note.
                im.append(res_sig)
                y += 1
                if len(im) == 7:
                    gam_notes[key, k_bi].append(im)  # Mémorisation de tous les modèles diatoniques altérés
                    (lineno(), "mod_rang", mod_rang, "im", im)
        (lineno(), "Lecture base :", k_bi, int_maj, "\ngam_notes", gam_notes)
        # break

    "# Lecture du dictionnaire gam_notes, afin d'en déterminer les signatures des 462 modes."
    deg, dc = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], 0  # Les degrés de la gamme
    gam_gam = {}  # Gammes classées par modulations diatoniques de I à VII.
    dic_sig = {}  # Dictionnaire contenant les cumuls modaux.
    for key in gam_notes.keys():
        (lineno(), "key", key)  # 72 key (1, (1, 1, 1, 1, 1, 1, 6))
        dic_sig[key[1]] = []
        for lm in gam_notes[key]:
            (lineno(), dc, key, lm)
            # 72 0 [(0, 'C'), ('-', 'D'), ('o', 'E'), ('o', 'F'), ('*', 'G'), ('-*', 'A'), ('o*', 'B')] 	 I
            lis_sig = []  # Capture les cumuls et formate le dictionnaire dic_sig.
            dc += 1  # Compte jusqu'à 462.
            mc = 0  # Compte les degrés modaux
            "# Lm-tuple(signe, note)."
            for sn in lm:  # , sn[0] = signe d'altération.
                mc += 1
                # Indice inversé de '-' = sig_not.index('-') - len(sig_not)
                # Et ; sig_not[6:] = ['o*', '-*', '*', 'o', '-'].
                sig_sig = sn[0]
                if sig_sig == 0:
                    sig_sig = ""
                if sig_sig in sig_not[6:]:  # L'altération est mineure.
                    ind_sig = sig_not.index(sig_sig) - len(sig_not)
                else:  # L'altération est augmentée.
                    ind_sig = sig_not.index(sig_sig)
                lis_sig.append((mc, ind_sig))
                if len(lis_sig) == 7:
                    dic_sig[key[1]].append(lis_sig)
                    (lineno(), "dic_sig[key[1]]", key[1], dic_sig[key[1]])
                    # 93 lis_sig [(1, 0), (2, -1), (3, -2), (4, -2), (5, -3), (6, -4), (7, -5)]
                if len(dic_sig[key[1]]) == 7:
                    (lineno(), "dic_sig[key[1]]", key[1], dic_sig[key[1]])
                (lineno(), "lis_sig", lis_sig)
        # break

    def func_gam(don):
        """Compte le nombre d'altérations des notes hors et en inclusions altéractives.
        Recevoir un tuple (degré, indice_altération), le coupler pour l'adapter au dictionnaire des altéractions.
        Renvoyer le comptage avec le tuple (degré, adaptions_signées)."""
        (lineno(), "Don", don)
        # 104 Don [(1, 0), (2, -1), (3, -2), (4, -2), (5, 2), (6, 1), (7, 0)]
        # sig_not = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]  # Les signes d'altération.
        # Construire un dictionnaire des forces altéractives.
        alteractions = {
            2: [["x2", "+3", "+4"], ["^2", "x3", "x4", "+5"], ["+^2", "^3", "^4", "x5", "+6"]],
            3: [["+3", "+4"], ["x3", "x4", "+5"], ["^3", "^4", "x5", "+6"], ["o3", "-2"]],
            4: [["x4", "+5"], ["^4", "x5", "+6"], ["o4", "o3", "-2"], ["-4", "-3"]],
            5: [["x5", "+6"], ["o5", "-4", "-3"], ["*5", "o4", "o3", "-2"]],
            6: [["o6", "-5"], ["*6", "o5", "-4", "-3"], ["-*6", "*5", "o4", "o3", "-2"]],
            7: [["o7", "-6"], ["*7", "o6", "-5"], ["-*7", "*6", "o5", "-4", "-3"],
                ["o*7", "-*6", "*5", "o4", "o3", "-2"]]}
        "# Cycles des traitements : adaptations et formations."
        don_deg = [sig_not[d[1]] + str(d[0]) for d in don]  # Liste des degrés signés. Exemple : "x5"
        sig_liste, sec_liste = [], []  # Afin d'en retourner le résultat. De garder le résultat.
        for vd in don:
            if vd[0] != 1:  # On passe le premier degré tonique.
                sig = sig_not[vd[1]]  # Présentation du signe d'altération.
                tup = (sig, vd[0])  # Représentation du tuple (signe, degré)
                loc = sig + str(tup[1])  # Construction du degré signé, ex : x5.
                (lineno(), "VD", vd, "Signe", sig, "Tuple", tup, "Loc", loc)
                # 125 VD (2, -1) Signe - Tuple ('-', 2) Loc -2
                # Rechercher dans le dictionnaire alteractions
                for va in alteractions[vd[0]]:  # vd[0] = le degré absolu.
                    (lineno(), vd[0], "VA", va, len(alteractions[vd[0]]))
                    if loc == va[0]:  # Si le degré signé n'est pas en tête de liste,
                        for lv in va:  # Lire le contenu de la liste du dictionnaire alteractions[vd[0]]
                            if lv not in sig_liste:  # La liste complète les degrés signés
                                sig_liste.append(lv)
                            if loc not in sec_liste:  # La liste des degrés significatifs
                                sec_liste.append(loc)
                                (lineno(), loc, "sec_liste", sec_liste, "LV", lv)
                            (lineno(), loc, "sig_liste", sig_liste, "sec_liste", sec_liste, "LV", lv)

        "# Construire la liste de lecture appartenant à sec_liste"
        lec_liste = [int(lsl[-1]) for lsl in sec_liste]
        for i28 in lec_liste:
            for ai28 in alteractions[i28]:
                ai = ai28[0]
                if ai in sec_liste:
                    (lineno(), "ai", ai, "ai28", ai28)  # 150 ai o3 ai28 ['o3', '-2']
                    for a2 in ai28:
                        (lineno(), "a2", a2)  # x2, +3, +4...
                        if a2 != ai and a2 in sec_liste:
                            sec_liste.remove(a2)
                            (lineno(), "ai", ai, "a2", a2, "ai28", ai28, sec_liste)
                            # 151 ai o4 a2 o3 ai28 ['o4', 'o3', '-2'] ['o4', 'x5']
        ("# Comparer la liste originale[don_deg] avec la découverte[sig_liste],"
         "afin d'ajouter la différence à la liste[sec_liste]. Uniquement, les notes altérées.")
        for dd in don_deg:  # Lire la liste des degrés signés.
            if dd not in sig_liste and dd not in (str(1), str(7)) and len(dd) > 1:
                sec_liste.append(dd)
        (lineno(), "sig_liste", sig_liste, "sec_liste", sec_liste)
        # 158 sig_liste ['o3', '-2', 'o4', 'x5', '+6'] sec_liste ['o4', 'x5'] hors_liste [] 3
        return "Effets", sig_liste, "Forces", sec_liste


    "# Traitement pour déterminer les gammes."
    "# Quelle règle utiliser pour choisir les gammes ?"
    "La grande majorité des gammes fondamentales n'excèdent pas les doubles altérations (bb, ##)."
    # lire en boucle le dictionnaire dic_sig contenant les degrés et les indices des signes
    # de chaque mode de gam_not[signe+note].
    dic_max = {}  # Dico{Max}.
    # dic_retours = {}  # Dico{Retours}
    for k_sig in dic_sig.keys():
        lis_retours = []
        keys_max = [(k_sig, x) for x in range(1, 8)]  # Bâtir les clés modales
        keys_cop = keys_max.copy()
        c_mod, c_max = 0, []
        k_key = [k[0] for k in gam_notes.keys() if k_sig in k]
        print(lineno(), "\n================== k_sig", k_sig, "k_key", k_key, "Lecture par mode tonique.")
        # 117  k_sig (1, 1, 1, 1, 1, 1, 6) Lecture par mode tonique.
        # La gamme primordiale = mode tonique. Et, dic_sig[k_sig] contient les sept modulations diatoniques.
        ("# Création d'un dictionnaire répertoriant maximums ordonnés, afin d'en trier les traitements."
         "Quand un moindre taux maximum remplit la fonction par la règle : simplifier la gamme fondamentale.")
        lis_poids, fix_poids = {}, []  # Dico{Cumuls triés}. Liste[Rangée].
        # Bouclage de tonification
        for v_sig in dic_sig[k_sig]:
            c_mod += 1
            dic_max[(k_sig, c_mod)] = []  # Enregistrement des maximums diatoniques dans dic_max{}.
            mem_sig = [abs(n[1]) for n in v_sig]
            max_mem = max(mem_sig)
            mix_mem = max_mem, c_mod
            c_max.append(mix_mem)  # Mémorisation des maximums modaux.
            ", mix_gob contient : mem_sig=poids de l'altération absolu. , max_mem="
            (lineno(), "MG = mem_sig", mem_sig, "max_mem", max_mem, "v_sig", v_sig, "CM", c_mod)
            mix_gob = (mem_sig.copy(), max_mem, v_sig, c_mod)  # MG = mix_gob
            dic_max[(k_sig, c_mod)].append(mix_gob)  # DM = dic_max
            fix_poids.append(max_mem)  # Fixation du maximum à trier avec son mode attribué.
            (lineno(), "DM", dic_max[(k_sig, c_mod)], "k_sig", k_sig, c_mod)  # DM = dic_max
            # 135 DM [([0, 1, 2, 2, 3, 4, 5], 5, [(1, 0), (2, -1), (3, -2), (4, -2), (5, -3), (6, -4), (7, -5)], 1)] 1
        # Ordonner la lecture du dico{dic_max}
        fix_poids.sort()  # Max en ordre croissant pour un mode léger.
        (lineno(), "* fix_poids", fix_poids)  # 196 * fix_poids [1, 1, 1, 1, 1, 1, 2]

        "# Lecture du dico{dic_max} selon l'ordonnance de fix_poids ordonné."
        rem_deg = [y for y in range(1, 8)]  # Notifications des suppressions sur les degrés de 1 à 7.
        rem_max = [y[0] for y in c_max]  # Mémorisation des maximums : lire autant de modes que de mêmes max.
        # Bouclage des poids altératifs, afin de trouver le sujet primordial.
        fin_for_fip = False
        for fip in fix_poids:
            long_fip = rem_max.count(fip)  # Décide du nombre de modes aux mêmes max.
            (lineno(), " ******* fip", fip, "rem_max", rem_max, "long_fip", long_fip)
            # 147  ******* fip 2 rem_max [5, 4, 3, 3, 2, 3, 4] long_fip 1
            # keys_max = [(k_sig, x) for x in range(1, 8)]. Imite la clé dic_max par section diatonique.
            while long_fip:
                for cdm in keys_max:
                    ("# Conditionner le traitement aux mêmes max :"
                     "      Dic_max = fip et s'il est dans rem_deg, c'est que dic_max n'a pas été traité.")
                    if dic_max[cdm][0][1] == fip and dic_max[cdm][0][-1] in rem_deg:
                        rem_deg.remove(dic_max[cdm][0][-1])
                        (lineno(), rem_deg)  # 155 [1, 2, 3, 4, 6, 7]
                        (lineno(), "DM", dic_max[cdm])
                        # [([0, 1, 2, 2, 2, 1, 0], 2, [(1, 0), (2, -1), (3, -2), (4, -2), (5, 2), (6, 1), (7, 0)], 5)]
                        "# Maintenant, il faut savoir si ce choix est valable."
                        if dic_max[cdm][0][2][-1][1] == 0:  # La septième doit être majeure pour une gamme primordiale.
                            if fip == 0:  # C'est le mode tonique de la gamme majeure.
                                # Rechercher la gamme correspondante via notes_gam = gam_notes.keys()
                                if k_sig in cdm and cdm in keys_cop:
                                    dm = dic_max[cdm][0][-1]
                                    gam_ton = [gt[1] for gt in gam_notes[(k_key[0], k_sig)][dm-1]]
                                    gam_gam[cdm] = gam_ton
                                    keys_cop.remove(cdm)
                                    print(lineno(), "_0) GM", gam_notes[(k_key[0], k_sig)][dm-1])
                                    (lineno(), "_0) DR", dic_max[cdm][0])
                            elif fip in (1, 2, 3) and k_sig != (1, 2, 2, 1, 2, 2, 2):
                                # Rechercher la gamme correspondante via notes_gam = gam_notes.keys()
                                if k_sig in cdm and cdm in keys_cop:
                                    retour = func_gam(dic_max[cdm][0][2])
                                    pont = retour, dic_max[cdm][0], (k_key[0], k_sig)
                                    lis_retours.append(pont)
                                    keys_cop.remove(cdm)
                                    (lineno(), "_ GM", gam_notes[(k_key[0], k_sig)][cdm[1] - 1])
                                    (lineno(), "_ dic_max", dic_max[cdm][0][2], "\nretour", retour)
                ("# Traitement de la liste[lis_retours] par fin de cycle diatonique :"
                 "      Liste_retour[0] = Retour. [effets, forces]"
                 "      Liste_retour[1] = Dic_max[(k_sig, mode)]. [poids]"
                 "      Liste_retour[2] = K_sig qui signe le tempérament diatonique. [cle]")
                effets, forces, poids, modes, clefs = [], [], [], [], []
                c_lis = 0
                if not rem_deg:  # Break While long_fip
                    long_rd = len(lis_retours)
                    print(lineno(), "long_rd", long_rd)
                    for flr in lis_retours:  # Cycle de la liste des retours.
                        c_lis += 1
                        (lineno(), "_0 ", flr[0], "\n", flr[1], "\n", flr[2])
                        effets.append(flr[0][1])
                        forces.append(flr[0][3])
                        poids.append(flr[1][1])
                        modes.append((flr[1][2], flr[1][3]))
                        clefs.append(flr[2])
                        if c_lis == long_rd:  # Afficher quand les listes sont complétées.
                            print(lineno(), "effets", effets)
                            ("Les effets incluent les automatismes altératifs, ceux qui"
                             "  annulent des importances pesantes des altérations.")
                            print(lineno(), "forces", forces)
                            ("Les forces sont produites par les fortes altérations."
                             "  Le nombre d'altéractions le moins fort est prioritaire.")
                            print(lineno(), "poids", poids)
                            "Les poids les plus légers sont prioritaires."
                            print(lineno(), "modes", modes)
                            "La représentation modale de la signature est nécessaire par conformité."
                            print(lineno(), "clefs", clefs)
                            "# Partie du traitement conditionnel des évènements."

                            "# Trouver de faibles forces définitives."
                            # Trouver le poids altératif minimal
                            mini_forces, count_fo = [], 0
                            gam_mini = None
                            for fo in forces:
                                mfi = len(fo), count_fo
                                mini_forces.append(mfi)  # Enregistrement des poids des forces.
                                count_fo += 1
                            mini_fo = min(o[0] for o in mini_forces)
                            reso_fo = [o for o in mini_forces if mini_fo == o[0]]
                            # Affecter un mode à cette mini-force.
                            for rf in reso_fo:
                                # Comparaison proportionnelle des effets.
                                if not effets[rf[1]]:
                                    print("\t***", lineno(), "effets", effets[rf[1]], "\n\t*** forces", forces[rf[1]])
                                    gam_mini = modes[rf[1]]
                            print(lineno(), "_\nmini_forces", mini_forces, "reso_fo", reso_fo, "gam_mini", gam_mini)

                    fin_for_fip = True
                    (lineno(), "lis_retours", lis_retours, "k_sig", k_sig, "Ajouter mode = dic_max[cdm][0][-1]")
                    break
                long_fip -= 1
            if fin_for_fip:  # for fip in fix_poids:
                break
        # break  # for k_sig in dic_sig.keys(): Ne réalise qu'une boucle des modes diatoniques à la première gamme.
    print(lineno(), "gam_gam", gam_gam)
    (lineno(), gam_notes[(66, (1, 2, 2, 1, 2, 2, 2))])


# Presser le triangle vert pour exécuter le script.
if __name__ == '__main__':
    intervalles_grok = {
        1: (1, 1, 1, 1, 1, 1, 6), 2: (1, 1, 1, 1, 1, 2, 5), 3: (1, 1, 1, 1, 1, 3, 4), 4: (1, 1, 1, 1, 1, 4, 3),
        5: (1, 1, 1, 1, 1, 5, 2), 6: (1, 1, 1, 1, 2, 1, 5), 7: (1, 1, 1, 1, 2, 2, 4), 8: (1, 1, 1, 1, 2, 3, 3),
        9: (1, 1, 1, 1, 2, 4, 2), 10: (1, 1, 1, 1, 3, 1, 4), 11: (1, 1, 1, 1, 3, 2, 3), 12: (1, 1, 1, 1, 3, 3, 2),
        13: (1, 1, 1, 1, 4, 1, 3), 14: (1, 1, 1, 1, 4, 2, 2), 15: (1, 1, 1, 1, 5, 1, 2), 16: (1, 1, 1, 2, 1, 1, 5),
        17: (1, 1, 1, 2, 1, 2, 4), 18: (1, 1, 1, 2, 1, 3, 3), 19: (1, 1, 1, 2, 1, 4, 2), 20: (1, 1, 1, 2, 2, 1, 4),
        21: (1, 1, 1, 2, 2, 2, 3), 22: (1, 1, 1, 2, 2, 3, 2), 23: (1, 1, 1, 2, 3, 1, 3), 24: (1, 1, 1, 2, 3, 2, 2),
        25: (1, 1, 1, 2, 4, 1, 2), 26: (1, 1, 1, 3, 1, 1, 4), 27: (1, 1, 1, 3, 1, 2, 3), 28: (1, 1, 1, 3, 1, 3, 2),
        29: (1, 1, 1, 3, 2, 1, 3), 30: (1, 1, 1, 3, 2, 2, 2), 31: (1, 1, 1, 3, 3, 1, 2), 32: (1, 1, 1, 4, 1, 1, 3),
        33: (1, 1, 1, 4, 1, 2, 2), 34: (1, 1, 1, 4, 2, 1, 2), 35: (1, 1, 1, 5, 1, 1, 2), 36: (1, 1, 2, 1, 1, 2, 4),
        37: (1, 1, 2, 1, 1, 3, 3), 38: (1, 1, 2, 1, 1, 4, 2), 39: (1, 1, 2, 1, 2, 1, 4),  40: (1, 1, 2, 1, 2, 2, 3),
        41: (1, 1, 2, 1, 2, 3, 2), 42: (1, 1, 2, 1, 3, 1, 3), 43: (1, 1, 2, 1, 3, 2, 2), 44: (1, 1, 2, 1, 4, 1, 2),
        45: (1, 1, 2, 2, 1, 1, 4), 46: (1, 1, 2, 2, 1, 2, 3), 47: (1, 1, 2, 2, 1, 3, 2), 48: (1, 1, 2, 2, 2, 1, 3),
        49: (1, 1, 2, 2, 2, 2, 2), 50: (1, 1, 2, 2, 3, 1, 2), 51: (1, 1, 2, 3, 1, 1, 3), 52: (1, 1, 2, 3, 1, 2, 2),
        53: (1, 1, 2, 3, 2, 1, 2), 54: (1, 1, 3, 1, 1, 3, 2), 55: (1, 1, 3, 1, 2, 1, 3), 56: (1, 1, 3, 1, 2, 2, 2),
        57: (1, 1, 3, 1, 3, 1, 2), 58: (1, 1, 3, 2, 1, 2, 2), 59: (1, 1, 3, 2, 2, 1, 2), 60: (1, 1, 4, 1, 2, 1, 2),
        61: (1, 2, 1, 2, 1, 2, 3), 62: (1, 2, 1, 2, 1, 3, 2), 63: (1, 2, 1, 2, 2, 1, 3), 64: (1, 2, 1, 2, 2, 2, 2),
        65: (1, 2, 1, 3, 1, 2, 2), 66: (1, 2, 2, 1, 2, 2, 2)}
    print_hi(intervalles_grok)
