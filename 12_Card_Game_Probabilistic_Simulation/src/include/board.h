/**
 * @file board.h
 *
 * This file declares the abstract type \b board and the interface for managing a game board, including teams, players, scores, and out-of-game cards :
 * - \b create_board(): Creates a new game board with no teams and no out-of-game cards.
 * - \b free_board(b): Frees memory allocated for the board and its associated data.
 * - \b add_team(b): Adds a new team to the board, initially empty with a score of zero.
 * - \b get_number_of_teams(b): Returns the number of teams currently present on the board.
 * - \b add_player_to_team(b, team_id, p): Adds a player to the specified team, assigning them an index.
 * - \b get_number_of_players_in_team(b, team_id): Returns the number of players in the specified team.
 * - \b get_player(b, team_id, player_index): Retrieves a player from a team using their index.
 * - \b get_score_of_team(b, team_id): Returns the current score of the specified team.
 * - \b set_score_of_team(b, team_id, score): Updates the score of the specified team to the given value.
 * - \b add_out_of_game_card(b, c): Adds a card to the set of out-of-game cards without affecting hands or table cards.
 * - \b get_number_of_out_of_game_cards(b): Returns the total number of out-of-game cards.
 * - \b get_out_of_game_card(b, card_index): Retrieves an out-of-game card using its index.
 * - \b remove_out_of_game_card(b, c): Removes a specified card from the set of out-of-game cards and updates indices accordingly.
 */

#ifndef BOARD_H
#define BOARD_H

#include "card.h"
#include "player.h"

/**
 * @brief \b Abstract type representing the game board, managing teams, scores, and out-of-game cards.
 */
typedef struct board_* board;

/**
 * @brief \b Creates a new board with no teams and no out-of-game cards.
 * @return The new board instance.
 */
board create_board();

/**
 * @brief \b Frees the memory allocated for the board and all its associated data.
 * @param b The board to free.
 */
void free_board(board b);

/** 
 * @brief \b Adds a new team to the board. The team starts empty with a score of zero.
 * @param b The board where the team is added.
 */
void add_team(board b);

/**
 * @brief \b Gets the number of teams currently present on the board.
 * @param b The board.
 * @return The number of teams.
 */
int get_number_of_teams(const board b);

/**
 * @brief \b Adds a player to the specified team, assigning them an index.
 * @param b The board where the player is added.
 * @param team_id The ID of the team.
 * @param p The player to add.
 */
void add_player_to_team(board b, int team_id, player p);

/**
 * @brief \b Gets the number of players in the specified team.
 * @param b The board.
 * @param team_id The ID of the team.
 * @return The number of players in the team.
 */
int get_number_of_players_in_team(const board b, int team_id);

/**
 * @brief \b Gets a player from a team using their index.
 * @param b The board.
 * @param team_id The ID of the team.
 * @param player_index The index of the player in the team.
 * @return The player at the given index.
 */
player get_player(const board b, int team_id, int player_index);

/**
 * @brief \b Gets the current score of a specified team.
 * @param b The board.
 * @param team_id The ID of the team.
 * @return The score of the team.
 */
int get_score_of_team(const board b, int team_id);

/**
 * @brief \b Updates the score of a specified team to the given value.
 * @param b The board.
 * @param team_id The ID of the team.
 * @param score The new score to set.
 */
void set_score_of_team(board b, int team_id, int score);

/**
 * @brief \b Adds a card to the set of out-of-game cards without affecting hands or table cards.
 * @param b The board.
 * @param c The card to add.
 */
void add_out_of_game_card(board b, card c);

/**
 * @brief \b Gets the total number of out-of-game cards.
 * @param b The board.
 * @return The number of out-of-game cards.
 */
int get_number_of_out_of_game_cards(const board b);

/**
 * @brief \b Retrieves an out-of-game card using its index.
 * @param b The board.
 * @param card_index The index of the card.
 * @return The card at the given index.
 */
card get_out_of_game_card(const board b, int card_index);

/**
 * @brief \b Removes a specified card from the set of out-of-game cards and updates indices accordingly.
 * @param b The board.
 * @param c The card to remove.
 */
void remove_out_of_game_card(board b, card c);

// ===== [Ajout Lot E] : Cartes Spéciales =====

/**
 * @brief Applique l'effet d'une carte spéciale sur le plateau de jeu.
 * @param b Le plateau de jeu.
 * @param p La joueuse qui a joué la carte spéciale.
 * @param c La carte spéciale à appliquer.
 */
void apply_special_card_effect(board b, player p, card c); // [Ajout - carte spéciale]


/**
 * @brief Définit le nombre de tours restants dans la partie.
 */
void set_remaining_rounds(board b, int n);

/**
 * @brief Récupère le nombre de tours restants.
 */
int get_remaining_rounds(board b);

// ===== [Ajout Lot E] : Jetons d'équipe =====

/**
 * @brief Calcule la somme totale de jetons possédés par toutes les joueuses d'une équipe.
 * @param b Le plateau de jeu.
 * @param team_id L'identifiant de l'équipe.
 * @return Le total de jetons de l'équipe.
 */
int get_total_tokens_of_team(const board b, int team_id); // [Ajout Lot E]


#endif // BOARD_H

