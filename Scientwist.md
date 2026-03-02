---

# ------------------------------------------------------------
# TITRE  
InterGrokPyGammes : Modélisation computationnelle, mathématique et musicologique des gammes et modulations diatoniques

# AUTEUR  
vicenté quantic cabviva

# RÉSUMÉ  
Ce document présente la théorie computationnelle développée dans le programme Python *InterGrokPyGammes*, qui modélise, analyse et classe l’ensemble des 462 modulations diatoniques issues de 66 structures modales fondamentales.  
Le modèle repose sur :  
1. une formalisation mathématique des gammes comme 7‑uplets d’intervalles dans le tempérament égal ;  
2. une géométrie différentielle discrète permettant de calculer les altérations comme écarts cumulatifs ;  
3. une théorie originale des « forces altéractives » modélisant les interactions entre altérations ;  
4. une classification computationnelle fondée sur des poids absolus, signés et gravitationnels.  

Ce travail unifie des perspectives issues de la théorie des groupes, de la combinatoire, de la musicologie tonale et de la cognition musicale.

---

# 1. INTRODUCTION  
Les gammes diatoniques peuvent être décrites comme des structures mathématiques discrètes, organisées par des intervalles dont la somme vaut 12 demi‑tons dans le tempérament égal.  
Le programme *InterGrokPyGammes* explore systématiquement cet espace, génère les 462 modulations possibles, calcule leurs altérations, identifie leurs interactions internes et sélectionne les gammes fondamentales selon des critères minimaux de gravité altérative.

Ce document formalise les concepts mathématiques, musicologiques et computationnels sous‑jacents.

---

# 2. FORMALISATION MATHÉMATIQUE DES GAMMES  

## 2.1 Gammes comme 7‑uplets d’intervalles  
Une gamme diatonique est représentée par un vecteur :

\[
G = (i_1, i_2, \dots, i_7)
\]

où chaque \(i_k\) vaut 1 ou 2 demi‑tons, et :

\[
\sum_{k=1}^7 i_k = 12.
\]

L’ensemble des gammes possibles est :

\[
\mathcal{G} = \{ G \in \{1,2\}^7 \mid \sum i_k = 12 \}.
\]

La gamme majeure est :

\[
M = (2,2,1,2,2,2,1).
\]

## 2.2 Renversements (modes)  
Les modes sont des rotations du vecteur d’intervalles :

\[
\text{mode}_r(G) = (i_r, i_{r+1}, \dots, i_7, i_1, \dots, i_{r-1}).
\]

Le groupe cyclique \(\mathbb{Z}/7\mathbb{Z}\) agit sur \(\mathcal{G}\).

---

# 3. CALCUL DES ALTÉRATIONS PAR GÉOMÉTRIE DIFFÉRENTIELLE DISCRÈTE  

Pour chaque degré \(k\), on compare les cumuls d’intervalles entre :

- la gamme majeure \(M\),
- le mode étudié \(G\).

Définition des cumuls :

\[
C_M(k) = \sum_{j=1}^k M_j,
\qquad
C_G(k) = \sum_{j=1}^k G_j.
\]

L’altération nécessaire est :

\[
\Delta_k = C_G(k) - C_M(k).
\]

Interprétation :

- \(\Delta_k > 0\) : dièses (augmentation)  
- \(\Delta_k < 0\) : bémols (diminution)  
- \(\Delta_k = 0\) : note naturelle  

Cette opération est une **différence discrète** entre deux géométries musicales.

---

# 4. THÉORIE DES FORCES ALTÉRACTIVES  

Le programme introduit un dictionnaire d’interactions altératives, où chaque degré possède :

- des altérations dominantes,  
- des altérations secondaires,  
- des relations de propagation.

Ce système peut être modélisé comme un graphe orienté :

\[
A : \{1,\dots,7\} \to \mathcal{P}(\text{Altérations})
\]

où chaque liste encode un cluster altératif.

Les altérations sont classées en :

- **forces** : altérations structurantes,  
- **effets** : altérations induites par propagation.

Pour chaque gamme, le programme calcule :

- poids absolu :  
\[
P_{\text{abs}} = \sum |a_k|
\]

- poids signé :  
\[
P_{\text{sgn}} = \sum a_k
\]

- poids gravitationnel (forces seules) :  
\[
P_{\text{grav}} = \sum f_k
\]

- poids des effets :  
\[
P_{\text{eff}} = \sum e_k
\]

Ces mesures définissent une **métrique de stabilité tonale**.

---

# 5. COMBINATOIRE DES 462 MODULATIONS  

Le programme explore :

- 66 structures modales fondamentales,  
- 7 renversements chacune,  

soit :

\[
66 \times 7 = 462 \text{ modulations}.
\]

Pour chaque modulation, il calcule :

1. la signature altérative complète ;  
2. les forces altéractives ;  
3. les effets induits ;  
4. les poids cumulés ;  
5. la stabilité tonale ;  
6. la gamme primordiale correspondante.

La sélection finale repose sur une **minimisation lexicographique** :

1. minimiser la longueur des forces ;  
2. minimiser le poids altératif ;  
3. minimiser les effets ;  
4. sélectionner la gamme la plus stable.

---

# 6. CADRE MUSICOLOGIQUE  

Ce modèle s’inscrit dans plusieurs traditions :

- théorie des modes (Antiquité → moderne),  
- signatures tonales (tonalité classique),  
- hiérarchie tonale (Krumhansl),  
- géométrie tonale (Tymoczko),  
- ensembles maximally even (Clough & Douthett).

L’innovation principale est la **physique symbolique des altérations**, qui permet :

- de mesurer la tension interne d’une gamme,  
- de classifier les modes selon leur gravité altérative,  
- d’identifier les gammes fondamentales par optimisation.

---

# 7. ARCHITECTURE COMPUTATIONNELLE  

Le programme Python met en œuvre :

- génération systématique des modes ;  
- calcul cumulatif des altérations ;  
- propagation altéractive via dictionnaires ;  
- classification multi‑critères ;  
- construction de dictionnaires hiérarchiques :  
  - signatures (`dic_sig`),  
  - poids (`dic_max`),  
  - gammes sélectionnées (`dic_gen`).  

Cette architecture constitue un système complet de **musicologie computationnelle**.

---

# 8. CONCLUSION  

*InterGrokPyGammes* propose une théorie computationnelle originale des gammes, fondée sur :

- une géométrie discrète des intervalles,  
- une dynamique des altérations,  
- une combinatoire exhaustive des modulations,  
- une métrique de stabilité tonale.

Ce modèle ouvre la voie à de nouvelles approches analytiques, pédagogiques et compositionnelles.

---

Souhaites‑tu maintenant que je génère **la version LaTeX complète**, prête à compiler, ou une **version Markdown** pour GitHub ?
