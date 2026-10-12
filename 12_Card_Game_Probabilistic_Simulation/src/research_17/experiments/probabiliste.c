#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "probabiliste.h"
#include "../../include/board.h"
#include "../../include/player.h"
#include "../../include/card.h"

/**
 * @brief Trouve la carte avec la valeur maximale dans la main du joueur.
 * 
 * @param p Le joueur dont on veut trouver la carte maximale.
 * 
 * @return L'indice de la carte avec la valeur maximale dans la main du joueur.
 */
int trouver_max(player p) {
    int taille_main = get_size_of_hand(p);  // Récupérer la taille de la main du joueur.
    int max_index = 0;
    if (taille_main == 0) {
        return -1;  // Si la main est vide, retourner -1.
    }
    card max = get_card_in_hand(p, 0);  // Initialiser la première carte comme la max.

    // Parcours de la main du joueur pour trouver la carte avec la valeur maximale.
    for (int i = 1; i < taille_main; i++) {
        card c = get_card_in_hand(p, i);
        if (get_value(c) > get_value(max)) {  // Comparer la valeur de la carte courante à la max.
            max = c;
            max_index = i;
        }
    }
    return max_index;  // Retourner l'indice de la carte maximale.
}

/**
 * @brief Trouve la carte avec la valeur minimale dans la main du joueur.
 * 
 * @param p Le joueur dont on veut trouver la carte minimale.
 * 
 * @return L'indice de la carte avec la valeur minimale dans la main du joueur.
 */
int trouver_min(player p) {
    int taille_main = get_size_of_hand(p);  // Récupérer la taille de la main du joueur.
    int min_index = 0;
    if (taille_main == 0) {
        return -1;  // Si la main est vide, retourner -1.
    }
    card min = get_card_in_hand(p, 0);  // Initialiser la première carte comme la min.

    // Parcours de la main du joueur pour trouver la carte avec la valeur minimale.
    for (int i = 1; i < taille_main; i++) {
        card c = get_card_in_hand(p, i);
        if (get_value(c) < get_value(min)) {  // Comparer la valeur de la carte courante à la min.
            min = c;
            min_index = i;
        }
    }
    return min_index;  // Retourner l'indice de la carte minimale.
}

/**
 * @brief Fonction de stratégie agressive : jouer la carte maximale si la condition est remplie,
 * sinon jouer la carte minimale.
 * 
 * @param p Le joueur qui applique la stratégie agressive.
 */
void agressif(player p) {
    int min_index = trouver_min(p);  // Trouver la carte minimale.
    int max_index = trouver_max(p);  // Trouver la carte maximale.
    if (min_index == -1 || max_index == -1) {
        return;  // Si la main est vide, ne rien faire.
    }
    card min = get_card_in_hand(p, min_index);
    card max = get_card_in_hand(p, max_index);

    int A = get_value(min);  // Valeur de la carte minimale.
    int B = get_value(max);  // Valeur de la carte maximale.

    int taille_main2 = get_size_of_hand(p);
   
    // Condition pour jouer la carte maximale ou minimale.
    if ((A - 1) >= 5 - B) {
        set_slate(p, 1);  // Victoire (1).
        play_card(p, max);  // Jouer la carte maximale.
        remove_card_from_hand(p, max);  // Retirer la carte de la main.
        taille_main2 = get_size_of_hand(p);
        
        // Si le joueur a encore des cartes, jouer une autre carte maximale.
        if (taille_main2 != 0) { 
            int max_index2 = trouver_max(p);
            card max2 = get_card_in_hand(p, max_index2);
            play_card(p, max2);
            remove_card_from_hand(p, max2);
        }
    } else {
        set_slate(p, 0);  // Défaite (0).
        play_card(p, min);  // Jouer la carte minimale.
        remove_card_from_hand(p, min);  // Retirer la carte de la main.
    }
}

/**
 * @brief Fonction de stratégie probabiliste : jouer une ou deux cartes en fonction de la moyenne des cartes adverses.
 * 
 * @param p Le joueur qui applique la stratégie probabiliste.
 * @param b Le plateau de jeu (board).
 * @param methode La méthode de jeu (probabiliste ou agressive).
 */
void probabiliste(player* p, board b, char* methode) {
    // Si la méthode choisie est "agressive", appeler la fonction agressive.
    if (strcmp(methode, "agressive") == 0) {
        agressif(*p);
    }
    else if (strcmp(methode, "probabiliste") == 0) {
        
        int nb_team = get_number_of_teams(b);  // Nombre d'équipes dans le jeu.
        int m = 0;
        
        // Calcul de la somme des valeurs des cartes des autres joueurs.
        for (int i = 0; i < nb_team; i++) {
            for (int j = 0; j < get_number_of_players_in_team(b, i); j++) {
                player q = get_player(b, i, j);
                
                // Si ce n'est pas le joueur courant, ajouter les valeurs de ses cartes.
                if (get_player_id(*p) != j) {
                    for (int l = 0; l < get_size_of_hand(q); l++) {
                        m += get_value(get_card_in_hand(q, l));
                    }
                }
            }
        }

        // Calcul de la moyenne des cartes des autres joueurs.
        float M = (float)m / 3;

        int taille_main = get_size_of_hand(*p);  // Taille de la main du joueur.
        int combi_trouvee = 0;
        int res = 0;
        if (taille_main == 0) {
            return;  // Si la main est vide, ne rien faire.
        }

        // Essayer de jouer une carte qui dépasse la moyenne M.
        for (int k = 0; k < taille_main; k++) {
            card c1 = get_card_in_hand(*p, k);
            if (get_value(c1) > M) {
                set_slate(*p, 1);  // Victoire (1).
                res = 1;
                combi_trouvee = 1;
                play_card(*p, c1);  // Jouer la carte.
                remove_card_from_hand(*p, c1);  // Retirer la carte de la main.
                break;    
            }
        }

        if (!res) {
            // Si aucune carte ne dépasse M, essayer avec une combinaison de deux cartes.
            for (int k = 0; k < taille_main; k++) {
                for (int l = k + 1; l < taille_main; l++) {
                    card c1 = get_card_in_hand(*p, k);
                    card c2 = get_card_in_hand(*p, l);
                    if (get_value(c1) + get_value(c2) > M) {
                        set_slate(*p, 1);  // Victoire (1).
                        play_card(*p, c1);  // Jouer la première carte.
                        play_card(*p, c2);  // Jouer la deuxième carte.
                        remove_card_from_hand(*p, c1);  // Retirer les cartes de la main.
                        remove_card_from_hand(*p, c2);
                        combi_trouvee = 1;
                        break;
                    }
                }
                if (combi_trouvee) break;
            }
        }

        if (!combi_trouvee) {
            // Si aucune combinaison ne dépasse M, jouer la plus petite carte.
            set_slate(*p, 0);  // Défaite (0).
            int min_index = trouver_min(*p);  // Trouver la carte minimale.
            card min = get_card_in_hand(*p, min_index);

            play_card(*p, min);  // Jouer la carte minimale.
            remove_card_from_hand(*p, min);  // Retirer la carte de la main.
        }
    }
}