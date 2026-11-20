# SOMA

Implementácia algoritmu Self-Organizing Migrating Algorithm v Pythone podľa prednášky a schémy SOMA.

## Verzie

- All-To-Random – na začiatku každej migrácie sa náhodne vyberie jeden leader.
- All-To-Best (All-To-One v prednáške) – leader je najlepší jedinec populácie.
- All-To-All – každý jedinec migruje ku všetkým ostatným, vždy zo svojej pôvodnej pozície.

Nová pozícia sa počíta podľa vzorca `x = start + (leader - start) * t * PRTVector`. PRT vektor sa generuje pri každom kroku. Zložka je 1, ak je náhodné číslo menšie ako PRT, inak 0. Jedinec si ponechá najlepšiu nájdenú pozíciu vrátane pôvodnej. Populácia sa aktualizuje po migrácii.

## Parametre

| Parameter | Hodnota |
|---|---|
| PopSize | 25 (Random, Best), 10 (All) |
| Step | 0.22 |
| PathLength | 3 |
| PRT | 0.3 |
| Dimenzia | 6 |
| MAXFES | 20000 |
| Migrations | max. 1000 |

Parametre sú zvolené podľa odporúčaní na strane 32 prednášky, nie podľa ilustračných hodnôt zo schémy. Body mimo hraníc sa neohodnocujú. Pôvodný bod (t = 0) už má známu hodnotu, preto sa nepočíta znova. Ak sa vyčerpá MAXFES počas migrácie, uložia sa dovtedy nájdené zlepšenia a algoritmus skončí. MinDiv je uvedený v schéme, ale jeho použitie nie je definované v pseudokóde; preto sa tu nepoužíva.

## Testovanie

Použité funkcie: Sphere, Rastrigin a súčet absolútnych hodnôt (zo schémy SOMA). Všetky majú minimum 0. Každá kombinácia funkcie a stratégie bola spustená 10-krát so seedmi 0 až 9. Všetkých 90 behov dosiahlo 20000 ohodnotení.

Priemerné výsledky (menšia hodnota je lepšia):

| Funkcia | All-To-Random | All-To-Best | All-To-All |
|---|---:|---:|---:|
| Sphere | 2.3467e-15 | 6.58525e-23 | 6.66944e-09 |
| Rastrigin | 0.0995055 | 0.503161 | 0.298935 |
| Absolute | 8.6541e-08 | 1.22429e-11 | 0.00104503 |

V tomto teste mal All-To-Best najlepší priemer na Sphere a Absolute. Na Rastrigin mal najlepší priemer All-To-Random. All-To-All má viac ciest na jednu migráciu, preto používa menšiu populáciu.
