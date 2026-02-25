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
                    (lineno(), "mod_rang", mod_rang, "im", im, "\ndic_rang", "key", key, dic_rang[key])
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

    "# Construire un dictionnaire des forces altéractives."
    alteractions = {
        2: [["x2", "+3", "+4"], ["^2", "x3", "x4", "+5"], ["+^2", "^3", "^4", "x5", "+6"]],
        3: [["+3", "+4"], ["x3", "x4", "+5"], ["^3", "^4", "x5", "+6"], ["o3", "-2"]],
        4: [["x4", "+5"], ["^4", "x5", "+6"], ["o4", "o3", "-2"], ["-4", "-3"]],
        5: [["x5", "+6"], ["o5", "-4", "-3"], ["*5", "o4", "o3", "-2"]],
        6: [["o6", "-5"], ["*6", "o5", "-4", "-3"], ["-*6", "*5", "o4", "o3", "-2"]],
        7: [["o7", "-6"], ["*7", "o6", "-5"], ["-*7", "*6", "o5", "-4", "-3"], ["o*7", "-*6", "*5", "o4", "o3", "-2"]]}

    def func_gam(don):
        """Compte le nombre d'altérations des notes hors et en inclusions altéractives.
        Recevoir un tuple (degré, indice_altération), le coupler pour l'adapter au dictionnaire des altéractions.
        Renvoyer le comptage avec le tuple (degré, adaptions_signées)."""

        # 104 Don [(1, 0), (2, -1), (3, -2), (4, -2), (5, 2), (6, 1), (7, 0)]
        # sig_not = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]  # Les signes d'altération.
        "# Cycles des traitements : adaptations et formations."
        don_deg = [sig_not[d[1]] + str(d[0]) for d in don]  # Liste des degrés signés. Exemple : "x5"
        ("\n", lineno(), "Don", don)
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
                                ("# C'est ici que se rétablissent les limites des effets enregistrés."
                                 "Valable quand, cette liste a un autre point altéractif dominant."
                                 "Sans ça, sig_liste va perturber les réponses suivantes.")
                                sig_liste.append(lv)
                                (lineno(), loc, "sig_liste", sig_liste, "LV", lv)
                            if loc not in sec_liste:  # La liste des degrés significatifs
                                sec_liste.append(loc)
                                (lineno(), loc, "sec_liste", sec_liste, "LOC", loc)
        (lineno(), don, "sig_liste", sig_liste, "sec_liste", sec_liste)

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
    dic_gen = {}  # Dico{Général}
    for k_sig in dic_sig.keys():
        dic_gen[k_sig] = []  # Chaque gamme-Grok contient (dic_sig, gam_notes, dic_rang)
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
                        (lineno(), "DM", cdm, dic_max[cdm])  # cdm = ((1, 2, 2, 1, 2, 2, 2), 7)
                        # [([0, 1, 2, 2, 2, 1, 0], 2, [(1, 0), (2, -1), (3, -2), (4, -2), (5, 2), (6, 1), (7, 0)], 5)]
                        "# Maintenant, il faut savoir si ce choix est valable."
                        if dic_max[cdm][0][2][-1][1] == 0:  # La septième doit être majeure pour une gamme primordiale.
                            if fip == 0:  # C'est le mode tonique de la gamme majeure.
                                # Rechercher la gamme correspondante via notes_gam = gam_notes.keys()
                                if k_sig in cdm and cdm in keys_cop:
                                    dm = dic_max[cdm][0][-1]
                                    gam_ton = [gt[1] for gt in gam_notes[(k_key[0], k_sig)][dm-1]]
                                    gam_ton.append('Maj')
                                    gam_gam[dic_rang[k_key[0]][6]] = gam_ton
                                    keys_cop.remove(cdm)
                                    (lineno(), "_0) GM", gam_notes[(k_key[0], k_sig)][dm-1], "\ncdm", cdm)
                                    (lineno(), "_0) DR", dic_max[cdm][0])
                            elif fip in (1, 2, 3) and k_sig != (1, 2, 2, 1, 2, 2, 2):
                                # Rechercher la gamme correspondante via notes_gam = gam_notes.keys()
                                if k_sig in cdm and cdm in keys_cop:
                                    retour = func_gam(dic_max[cdm][0][2])
                                    pont = retour, dic_max[cdm][0], (k_key[0], k_sig)
                                    lis_retours.append(pont)
                                    keys_cop.remove(cdm)
                                    (lineno(), "_ GM", gam_notes[(k_key[0], k_sig)][cdm[1] - 1], "cdm", cdm)
                                    (lineno(), "_ dic_max", dic_max[cdm][0][2], "\nretour", retour)
                                    (lineno(), "_ lis_retours", lis_retours)
                ("# Traitement de la liste[lis_retours] par fin de cycle diatonique :"
                 "      Liste_retour[0] = Retour. [effets, forces]"
                 "      Liste_retour[1] = Dic_max[(k_sig, mode)]. [poids]"
                 "      Liste_retour[2] = K_sig qui signe le tempérament diatonique. [cle]")
                effets, forces, poids, modes, clefs = [], [], [], [], []
                c_lis = 0
                if not rem_deg:  # Break While long_fip
                    long_rd = len(lis_retours)
                    (lineno(), "long_rd", long_rd)  # 248 long_rd 3
                    for flr in lis_retours:  # Cycle de la liste des retours.
                        c_lis += 1
                        (lineno(), "_0 ", flr[0], "\n", flr[1], "\n", flr[2])
                        effets.append(flr[0][1])
                        forces.append(flr[0][3])
                        poids.append(flr[1][1])
                        modes.append((flr[1][2], flr[1][3]))
                        clefs.append(flr[2])
                        if c_lis == long_rd:  # Afficher quand les listes sont complétées.
                            (lineno(), "EFFETS", effets)
                            ("Les effets incluent les automatismes altératifs, ceux qui"
                             "  annulent des importances pesantes des altérations.")
                            (lineno(), "FORCES", forces, "\t POIDS", poids)
                            ("Les forces sont produites par les fortes altérations."
                             "  Le nombre d'altéractions le moins fort est prioritaire.")
                            (lineno(), "POIDS", poids)
                            "Les poids les plus légers sont secondaires."
                            (lineno(), "MODES", "modes")
                            "La représentation modale de la signature est nécessaire par conformité."
                            (lineno(), "CLEFS", "clefs", "clefs=(k_key, k_sig)")
                            "# Partie du traitement conditionnel des évènements."

                            "# Trouver de faibles forces définitives. Moins lourd = plus léger."
                            # Trouver le poids altératif minimal
                            mini_forces, count_fo = [], 0
                            gam_mini = None
                            for fo in forces:
                                mfi = len(fo), count_fo  # Enregistrement des volumes des forces : len(fo).
                                mini_forces.append(mfi)
                                count_fo += 1
                                (lineno(), "FO", fo, "MFI", mfi)
                            mini_fo = min(o[0] for o in mini_forces)  # Mesures de longueurs des forces.
                            mini_lo = list(o[0] for o in mini_forces)  # Mesures de longueurs des forces.

                            "# Boucle sélectionnant les plus faibles longueurs."
                            (lineno(), "KG_alt", poids, "\tmini_fo_alt", mini_fo, "\tmini_lo_len", mini_lo)
                            # 284 KG_alt [1, 1, 1] 	mini_fo_alt 1 	mini_lo_len [1, 3, 2]
                            res_fo, cfo = [], []
                            for et in mini_forces:
                                if et[0] == mini_fo:  # Petites longueurs.
                                    (lineno(), "# if et[0]== mini_fo: Petites longueurs.", et[0])
                                    if poids[et[1]] == min(poids):  # Petites altérations.
                                        (lineno(), "## if poids[et[1]]== min(poids): Petites altérations.", et[0])
                                        res_fo.append(et)
                                        pfo = poids[et[1]]  # Prise de l'index de 'et'.
                                        if pfo not in cfo:
                                            cfo.append(pfo)
                                        (lineno(), "________ 0 et", et, "*** \t PCfo", pfo, cfo)
                                    elif et[0] == min(mini_lo):  # Petites longueurs.
                                        (lineno(), "## elif et[0]== min(mini_lo): Petites longueurs.", et[0])
                                        pfo = poids[et[1]]  # Prise de l'index de 'et'.
                                        if not cfo:
                                            res_fo.append(et)
                                            cfo.append(pfo)
                                            (lineno(), "********* 2 ET", et, "*** \t PCfo", pfo, cfo)
                                        elif cfo and pfo <= max(cfo):
                                            res_fo.append(et)
                                            if pfo not in cfo:
                                                cfo.append(pfo)
                                            (lineno(), "********* 3 ET", et, "*** \t PCfo", pfo, cfo)
                                (lineno(), "ET", et, "Kg", min(poids), "mini_fo", mini_fo)
                            (lineno(), "_ mini_forces", mini_forces, mini_fo, "\t res_fo", res_fo)
                            # Affecter un mode à cette mini-force avec et sans effet.
                            ("# On aurait pu se contenter de déclarer les plus petites des forces faibles."
                             "Mais, il y aurait eu un vide descriptif tonal, ce qui a pour conséquence"
                             "d'invisibiliser des notions importantes relatives aux tonalités."
                             "POIDS ABSOLUS[pa] = les poids cumulés non signés."
                             "POIDS GRAVITATIONNELS[pg] = les poids cumulés signés."
                             "  po_tot_pa = poids total absolu (sans signature)."
                             "  po_tot_pg = poids total signé (avec signature)."
                             "  po_fort_pg = poids des forces signées."
                             "  po_fort_pa = poids des forces absolues."
                             "  po_eff_pg = poids des effets signés positifs."
                             "  po_eff_pa = poids des effets signés négatifs."
                             "POURQUOI PA & PG : la gravitation flotte comme la gamme[niveau zéro naturel]"
                             "naturelle avec sons absence de signature. Disons alors que les mineures"
                             "vont vers le négatif et que les augmentées vont vers le positifs,"
                             "un accroissement des précisions géolocales.")
                            po_tot_pa, po_tot_pg, po_fort_pg, po_fort_pa, po_eff_pg, po_eff_pa = 0, 0, 0, 0, 0, 0
                            mf3, mf4, mf0 = None, None, 0  # mf3 stage FORCES _ mf4 stage EFFETS | mf0 count mode
                            lis_mf3, lis_mf4 = [], []  # Mémoire des données mf3 et mf4
                            afficher = 0  # Affiche les différents dictionnaires utiles.
                            for rf in res_fo:
                                # Comparaison proportionnelle en analysant les forces[len(res_fo)] et les effets.
                                # Les effets ont des abs(doubles) produits par les forces altéractives.
                                deg = modes[rf[1]][1] - 1
                                if afficher:
                                    "# Les modes : dico dic_sig[k_sig], gam_notes[k_key, k_sig], dic_rang[key]"
                                    print(lineno(), "RF", rf, "modes", modes[rf[1]])  # Sélection Modes + Degré
                                    print(lineno(), "RF", rf, "dic_sig", dic_sig[k_sig][deg])  # Modes + Degrés
                                    print(lineno(), "RF", rf, "gam_notes", gam_notes[(k_key[0], k_sig)][deg])  # Notes
                                    print(lineno(), "RF", rf, "dic_rang", dic_rang[k_key[0]][deg])  # K_sig diatones
                                d_s = list(dic_sig[k_sig][deg])
                                g_n = list(gam_notes[(k_key[0], k_sig)][deg])
                                d_r = tuple(dic_rang[k_key[0]][deg])
                                pont = d_s, g_n, d_r
                                dic_gen[k_sig].append(pont)
                                mf0 += 1
                                (lineno(), modes[rf[1]][0], "\t Nombre de Modes découverts : mf0", mf0)
                                for pfp in forces[rf[1]]:
                                    for mf in modes[rf[1]][0]:
                                        mf1, mf2 = mf[0], mf[1]  # mf1 = degré et mf2 = altération
                                        if int(pfp[-1]) == mf1:
                                            if mf2 < 0:  # Modification du signe positif en négatif.
                                                mf1 = mf1 - mf1 - mf1
                                            mf3 = mf1 + mf2  # La somme du degré et de son altération
                                            (lineno(), "FORCES mf1=deg", mf1, "mf2=alt", mf2, "mf3", mf3)
                                            # 319 mf1=deg -4 mf2=alt -2 mf3 -6 	pfp o4
                                            # 319 mf1=deg 5 mf2=alt 2 mf3 7 	pfp x5
                                    po_fort_pg += mf3
                                    po_fort_pa += abs(mf3)
                                    pont_mf = "Gr", mf0, "mf3", mf3, [pfp, "FOR_PG", po_fort_pg, "FOR_PA", po_fort_pa]
                                    if pont_mf not in lis_mf3:
                                        lis_mf3.append(pont_mf)
                                        dic_gen[k_sig].append(pont_mf)
                                    (lineno(), "pfp", pfp, "po_fort_PG", po_fort_pg, "\t po_fort_PA", po_fort_pa)
                                for pep in effets[rf[1]]:
                                    for mf in modes[rf[1]][0]:
                                        mf1, mf2 = mf[0], mf[1]
                                        if int(pep[-1]) == mf1:
                                            if mf2 < 0:
                                                mf1 = mf1 - mf1 - mf1
                                            mf4 = mf1 + mf2
                                            (lineno(), "EFFETS mf1=deg", mf1, "mf2=alt", mf2, "mf3", mf3)
                                            # 310 mfs -6 -1 mf3 -7 pfp -6
                                    po_eff_pg += mf4
                                    po_eff_pa += abs(mf4)
                                    pont_mf = "Gr", mf0, "mf4", mf4, [pep, "EFF_PG", po_eff_pg, "EFF_PA", po_eff_pa]
                                    if pont_mf not in lis_mf4:
                                        lis_mf4.append(pont_mf)
                                        dic_gen[k_sig].append(pont_mf)
                                    (lineno(), "pep", pep, "po_eff_PG", po_eff_pg, "\t po_eff_PA", po_eff_pa)
                                print(lineno(), "Rf", rf, "Forces", forces[rf[1]], "Effets", effets[rf[1]])

                            (lineno(), "po_fort_pg", po_fort_pg, "\t po_fort_pa", po_fort_pa)
                            (lineno(), "po_eff_pg", po_eff_pg, "\t po_eff_pa", po_eff_pa)
                            (lineno(), "lis_mf3[forces]", lis_mf3, "\n lis_mf4[effets]", lis_mf4)
                            (lineno(), "gam_mini", gam_mini, k_key)  # 379 gam_mini None [65]
                    (lineno(), "dic_gen", dic_gen[k_sig], "LEN", len(dic_gen[k_sig]))
                    # 396 dic_gen [([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, -1), (7, 0)], [(0, 'C'), ('', 'D'),
                    # ('', 'E'), ('', 'F'), ('', 'G'), ('-', 'A'), ('', 'B')], (2, 2, 1, 2, 1, 3, 1)),
                    # ('Gr', 1, 'mf3', -7, ['-6', 'FOR_PG', -7, 'FOR_PA', 7])] LEN 2

                    ("# À partir d'ici, les gammes qui sont dans le dictionnaire[dic_gen] vont être sélectionnées."
                     "Quand, len(dgk) = 3. Ligne mode numérique et alphanumérique et forme de l'intervalle."
                     "Quand, len(dgk) = 5. Ligne des graduations par portée.")
                    cop_dgk = dic_gen[k_sig].copy()
                    len_dgk = len(cop_dgk)
                    tags = [i for i, x in enumerate(cop_dgk) if len(x) == 3]  # Tags = couple fort.
                    # dic_tag = {tag: [] for tag in tags}
                    dt0 = {}  # DT0 = dico[tags].
                    not_mus, nom = ["C", "D", "E", "F", "G", "A", "B"], ""  # Les notes naturelles et le nom.
                    if k_key[0] != 66:  # Capacité en len(dgk) = 5 pour le premier len(dgk) = 3
                        # gam_in = []  # Liste les notes de la gamme sélectionnée.
                        if len(tags) == 1:  # Lorsqu'il n'y a qu'une seule gamme.
                            for t1 in range(len_dgk):
                                dg1 = cop_dgk[t1]
                                if t1 == tags[0]:
                                    dt0[tags[0]] = [dg1]
                                    if len(cop_dgk) <= 3:  # Capte gamme et son nom + sans EFF_PG
                                        gam_in = [(x if isinstance(x, str) else '') + y for x, y in dg1[1]]
                                        print(lineno(), "gam_in", gam_in)
                                        "# À partir des noms alphas, créer des noms numériques. '-E' devient '-3'."
                                        ty = []  # Traiter l'affichage des noms
                                        for tx in gam_in:
                                            if len(tx) > 1:
                                                xx = list(tx)
                                                ind_ax = not_mus.index(xx[-1]) + 1
                                                xx[1] = str(ind_ax)
                                                xx = ''.join(str(y) for y in xx)
                                                ty.append(str(xx))
                                                (lineno(), "TX", tx, "XX", xx, "ind_ax", ind_ax)
                                        if len(ty) > 1:
                                            toy = ty.copy()
                                            ty[1] = ty[1][::-1]  # Changement de position de l'altération
                                            if ty[0][0] == ty[1][1]:
                                                ty[1] = ty[1].replace(ty[1][1], '')
                                                nom = ''.join(str(y) for y in ty)
                                                gam_in.append(nom)
                                                print(lineno(), "if(-==-) TOY", toy, "nom", nom)
                                            else:
                                                nom = ''.join(str(y) for y in ty)
                                                gam_in.append(nom)
                                                print(lineno(), "el(-!=-) TOY", toy, "nom", nom)
                                        else:  # La gamme a une seule note altérée
                                            nom = ''.join(str(y) for y in ty)
                                            gam_in.append(nom)
                                            print(lineno(), "if(ty==1) TY", ty, "nom", nom)
                                    elif len(cop_dgk) >= 4:  # Gamme[59] (-4)(x4)(o6)(o3)
                                        gam_in = [(x if isinstance(x, str) else '') + y for x, y in dg1[1]]
                                        print(lineno(), "gam_in", gam_in)
                                        ty, t_alt, t_tot = [], [], []
                                        for t4 in range(tags[0] + 1, len_dgk):
                                            ("# En même temps tester si la gamme n'a pas de redondance."
                                             "Donnée forte, donnée faible = les notes parues, les notes cachées.")
                                            if "FOR_PG" in cop_dgk[t4][4]:  # Donnée forte du résultat.
                                                ty.append(cop_dgk[t4][4][0])
                                                t_tot.append(cop_dgk[t4][4][0])
                                            if cop_dgk[t4][4][0] not in ty:  # Donnée faible du produit.
                                                t_alt.append(cop_dgk[t4][4][0])
                                                t_tot.append(cop_dgk[t4][4][0])
                                        ox, ind_ox = [oy[1] for oy in t_tot], -1
                                        (lineno(), "**TY", ty, "** OX", ox)
                                        # 460 **TY ['o4', 'o5'] ** OX ['4', '5', '3', '2', '4', '3']
                                        fen = []  # Fen[0] = Forte et fen[1] = Effet
                                        for o in ox:
                                            ind_ox += 1  # Devient l'indice de 'o' dans 'ox'
                                            # fen = []  # Fen[0] = Forte et fen[1] = Effet
                                            if ox.count(o) > 1:  # Il y a un phénomène altéractif.
                                                ("# Chercher l'élément 'o' parmi les altéractions."
                                                 "Si 'o' est dans fort[TY] = note réelle."
                                                 "Si 'o' est un effet[T_ALT]  = note altéractivée."
                                                 "Les gammes concernées : 41, 24, 22, 9, 8."
                                                 "La gamme[9] est particulière :"
                                                 "  480 if(-==-) TY ['o4', '5o'] nom o45o"
                                                 "  471 ** t_tot ['o4', 'o5', 'o3', '-2', '-4', '-3'] "
                                                 "  OX ['4', '5', '3', '2', '4', '3'] O 3 fen ['o4', '-4', 'o3', '-3']")
                                                vi, vii = alteractions[int(o)], ind_ox
                                                (lineno(), "VI", vi)  # Données du dico altéractions.
                                                # [['x4', '+5'], ['^4', 'x5', '+6'], ['o4', 'o3', '-2'], ['-4', '-3']]
                                                for u in vi:
                                                    for a in u:  # U = ['o4', 'o3', '-2']
                                                        if a in ty and t_tot[vii] not in fen:  # Donnée forte.
                                                            fen.append(t_tot[vii])
                                                            (lineno(), "t_tot", t_tot[vii], "TY", ty, "fen", fen)
                                                            # 482 t_tot o4 TY ['o4', 'o5'] fen ['o4']
                                                            for ta in t_alt:  # Donnée faible.
                                                                if ta[-1] == o and ta not in fen:
                                                                    fen.append(ta)
                                                                    (lineno(), "TA", ta, "O", o, "fen", fen)
                                                                    # 487 TA -4 O 4 fen ['o4', '-4']

                                        "# Construire 'ty' selon 'fen'."
                                        if fen:
                                            # sig_not = ["", "+", "x", "^", "+^", "x^", "o*", "-*", "*", "o", "-"]
                                            n_for = [n for n in dg1[0] if n[0] == int(fen[0][-1])]  # Donnée forte
                                            sig = sig_not.index(fen[1][0])  # Index du signe courant.
                                            if sig < 6:  # L'index est dans l'espace augmenté.
                                                n_eff = sig
                                                (lineno(), "sig>5", sig)
                                            else:  # L'index est dans l'espace diminué.
                                                n_eff = sig - len(sig_not)
                                                (lineno(), "sig", sig)
                                            n_res = n_for[0][1] - n_eff
                                            n_not, cc = sig_not[n_res] + fen[0][1], 0
                                            for xy in ty:
                                                if xy[-1] == fen[0][1]:
                                                    ty[cc] = n_not
                                                cc += 1
                                            (lineno(), "f", n_for[0][1], "e", n_eff, "r", n_res, "n", n_not)
                                            (lineno(), "ty", ty, "fen", fen, "dg1", dg1[0])
                                            # 503 f -2 e -1 r -1 n -4
                                            # 489 ty ['o4', 'o5'] fen ['o4', '-4']
                                            # dg1 [(1, 0), (2, -1), (3, -2), (4, -2), (5, -2), (6, 0), (7, 0)]


                                        if len(ty) > 1:
                                            toy = ty.copy()
                                            ty[1] = ty[1][::-1]  # Changement de position de l'altération
                                            if ty[0][0] == ty[1][1]:
                                                ty[1] = ty[1].replace(ty[1][1], '')
                                                nom = ''.join(str(y) for y in ty)
                                                gam_in.append(nom)
                                                print(lineno(), "if(-==-) TOY", toy, "nom", nom)
                                            else:
                                                nom = ''.join(str(y) for y in ty)
                                                gam_in.append(nom)
                                                print(lineno(), "el(-!=-) TOY", toy, "nom", nom)
                                        else:  # La gamme a une seule note altérée
                                            nom = ''.join(str(y) for y in ty)
                                            gam_in.append(nom)
                                            print(lineno(), "if(ty==1) TY", ty, "nom", nom)
                                        (lineno(), "cop_dgk=4_dg1", dg1[1], "len()", len(cop_dgk))
                                        gam_gam[dg1[2]] = gam_in
                                        (lineno(), "cop_dgk>=4", dg1[1], "len(cop_dgk)", len(cop_dgk))
                                (lineno(), "t1", t1, "*G __ \t\t dg1", dg1, "len(cop_dgk)", len(cop_dgk))
                        elif len(tags) == 2:  # Lorsqu'il y a deux gammes.
                            for t1 in range(tags[0], tags[1]):
                                dg1 = cop_dgk[t1]
                                if t1 == tags[0]:
                                    dt0[tags[0]] = [dg1]
                                else:
                                    dt0[tags[0]].append(dg1)
                                print(lineno(), "t1", t1, "*G __ \t\t dg2", dg1)
                            for t2 in range(tags[1], len_dgk):
                                dg2 = cop_dgk[t2]
                                if t2 == tags[1]:
                                    dt0[tags[1]] = [dg2]
                                else:
                                    dt0[tags[1]].append(dg2)
                                print(lineno(), "t2", t2, "*G __ \t\t dg2", dg2[1])
                        elif len(tags) == 3:  # Lorsqu'il y a deux gammes.
                            for t1 in range(tags[0], tags[1]):
                                dg1 = cop_dgk[t1]
                                if t1 == tags[0]:
                                    dt0[tags[0]] = [dg1]
                                else:
                                    dt0[tags[0]].append(dg1)
                                print(lineno(), "t1", t1, "*G __ \t\t dg2", dg1)
                            for t2 in range(tags[1], tags[2]):
                                dg2 = cop_dgk[t2]
                                if t2 == tags[1]:
                                    dt0[tags[1]] = [dg2]
                                else:
                                    dt0[tags[1]].append(dg2)
                                print(lineno(), "t2", t2, "*G __ \t\t dg2", dg2)
                            for t3 in range(tags[2], len_dgk):
                                dg3 = cop_dgk[t3]
                                if t3 == tags[2]:
                                    dt0[tags[2]] = [dg3]
                                else:
                                    dt0[tags[2]].append(dg3)
                                print(lineno(), "t3", t3, "*G __ \t\t dg3", dg3)

                    print(lineno(), "tags", tags)

                    fin_for_fip = True
                    (lineno(), "lis_retours", lis_retours, "k_sig", k_sig, "Ajouter mode = dic_max[cdm][0][-1]")
                    break
                long_fip -= 1
            if fin_for_fip:  # for fip in fix_poids:
                break
        # break  # for k_sig in dic_sig.keys(): Ne réalise qu'une boucle des modes diatoniques à la première gamme.
    (lineno(), "gam_gam", len(gam_gam), "dic_rang[66] =", dic_rang[66][6])  # K_sig diatoniques)
    print(lineno(), gam_gam, "Nombre de gammes solutionnées :", len(gam_gam.keys()))


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
