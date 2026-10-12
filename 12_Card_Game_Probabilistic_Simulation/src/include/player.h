#ifndef PLAYER_H
#define PLAYER_H

#include "card.h" 

/**
 * @file player.h
 *
 *  Ce fichier définit le type abstrait \b player et fournit des fonctions pour gérer les cartes en main, les cartes jouées et les paris des joueuses.
 *
 * - \b  create_player() : Crée une nouvelle joueuse avec un identifiant unique.
 * - \b  free_player(player p) : Libère la mémoire allouée à une joueuse.
 * - \b  get_player_id(player p) : Retourne l'identifiant unique d'une joueuse.
 * - \b  get_player_by_id(int id) : Retourne une joueuse à partir de son identifiant.
 * - \b  add_card_to_hand(player p, card c) : Ajoute une carte à la main d'une joueuse.
 * - \b  get_size_of_hand(player p) : Retourne le nombre de cartes dans la main d'une joueuse.
 * - \b  get_card_in_hand(player p, int card_index) : Retourne une carte spécifique de la main d'une joueuse.
 * - \b  remove_card_from_hand(player p, card c) : Supprime une carte de la main d'une joueuse.
 * - \b  play_card(player p, card c) : Joue une carte et l'ajoute aux cartes posées sur la table.
 * - \b  get_number_of_played_cards(player p) : Retourne le nombre de cartes jouées sur la table.
 * - \b  get_played_card(player p, int card_index) : Retourne une carte spécifique jouée sur la table.
 * - \b  remove_played_card(player p, card c) : Supprime une carte posée sur la table par une joueuse.
 * - \b  get_slate(player p) : Retourne le pari d'une joueuse inscrit sur son ardoise.
 * - \b  set_slate(player p, int bet) : Définit ou modifie le pari d'une joueuse sur son ardoise.
 */


/**
 * @brief Type abstrait représentant une joueuse.
 *
 * Contient les informations sur les cartes en main, les cartes posées sur la table et l'ardoise.
 */
typedef struct player_s* player;

/**
 * @brief Crée une nouvelle joueuse avec un identifiant unique.
 *
 * La joueuse est initialement sans carte en main, sans carte posée sur la table et avec une ardoise vide.
 * @return Un nouvel objet player alloué dynamiquement.
 */
player create_player();

/**
 * @brief Libère toute la mémoire allouée à une joueuse.
 * @param p La joueuse à libérer.
 */
void free_player(player p);

/**
 * @brief Retourne l'identifiant de la joueuse.
 * @param p La joueuse concernée.
 * @return L'identifiant entier de la joueuse.
 */
int get_player_id(player p);

/**
 * @brief Retourne une joueuse à partir de son identifiant.
 * @param id L'identifiant de la joueuse.
 * @return La joueuse correspondante.
 */
player get_player_by_id(int id);

/**
 * @brief Ajoute une carte à la main de la joueuse.
 * @param p La joueuse concernée.
 * @param c La carte à ajouter.
 */
void add_card_to_hand(player p, card c);

/**
 * @brief Retourne le nombre de cartes dans la main de la joueuse.
 * @param p La joueuse concernée.
 * @return Le nombre de cartes en main.
 */
int get_size_of_hand(player p);

/**
 * @brief Retourne une carte spécifique de la main de la joueuse.
 * @param p La joueuse concernée.
 * @param card_index L'index de la carte dans la main.
 * @return La carte correspondante.
 */
card get_card_in_hand(player p, int card_index);

/**
 * @brief Supprime une carte de la main de la joueuse et réattribue les indices.
 * @param p La joueuse concernée.
 * @param c La carte à supprimer.
 */
void remove_card_from_hand(player p, card c);

/**
 * @brief Joue une carte et l'ajoute aux cartes posées sur la table par la joueuse.
 * @param p La joueuse concernée.
 * @param c La carte à jouer.
 */
void play_card(player p, card c);

/**
 * @brief Retourne le nombre de cartes jouées posées sur la table par la joueuse.
 * @param p La joueuse concernée.
 * @return Le nombre de cartes posées.
 */
int get_number_of_played_cards(player p);

/**
 * @brief Retourne une carte spécifique jouée et posée sur la table par la joueuse.
 * @param p La joueuse concernée.
 * @param card_index L'index de la carte parmi celles posées.
 * @return La carte correspondante.
 */
card get_played_card(player p, int card_index);

/**
 * @brief Supprime une carte posée sur la table par la joueuse et réattribue les indices.
 * @param p La joueuse concernée.
 * @param c La carte à supprimer.
 */
void remove_played_card(player p, card c);

/**
 * @brief Retourne le pari de la joueuse inscrit sur son ardoise.
 * @param p La joueuse concernée.
 * @return L'entier représentant le pari.
 */
int get_slate(player p);

/**
 * @brief Définit le pari de la joueuse sur son ardoise.
 * @param p La joueuse concernée.
 * @param bet L'entier représentant le nouveau pari.
 */
void set_slate(player p, int bet);


// ===== [Ajout Lot E] : Gestion des jetons =====

/**
 * @brief Retourne le nombre de jetons que possède la joueuse.
 * @param p La joueuse concernée.
 * @return Le nombre de jetons.
 */
int get_tokens(player p); // [Ajout Lot E]

/**
 * @brief Définit le nombre de jetons de la joueuse.
 * @param p La joueuse concernée.
 * @param tokens Le nouveau nombre de jetons.
 */
void set_tokens(player p, int tokens); // [Ajout Lot E]

/**
 * @brief Ajoute des jetons à la joueuse.
 * @param p La joueuse concernée.
 * @param tokens Le nombre de jetons à ajouter.
 */
void add_tokens(player p, int tokens); // [Ajout Lot E]

/**
 * @brief Retire des jetons à la joueuse.
 * @param p La joueuse concernée.
 * @param tokens Le nombre de jetons à retirer.
 */
void remove_tokens(player p, int tokens); // [Ajout Lot E]

/**
 * @brief Définit la mise courante de la joueuse.
 * @param p La joueuse concernée.
 * @param tokens Le montant de la mise.
 */
void set_bet_amount(player p, int tokens); // [Ajout Lot E]

/**
 * @brief Retourne la mise courante de la joueuse.
 * @param p La joueuse concernée.
 * @return Le montant misé lors du dernier pari.
 */
int get_bet_amount(player p); // [Ajout Lot E]

#endif 