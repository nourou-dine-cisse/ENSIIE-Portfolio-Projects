/**
 * \file interface.h
 * 
 * Interface for communication with the physical player.
 * 
 * This file contains function signatures for displaying the game,
 * collecting player input, and managing interactions with the interface.
 * Only the interface is allowed to call display functions such as printf and scanf.
 * 
 * Functions:
 * - \b display_board : Displays all game information.
 * - \b ask_gamble : Asks the player to place a bet.
 * - \b ask_number_of_played_cards : Asks the player how many cards they want to play.
 * - \b ask_card : Asks the player to choose a card to play.
 * - \b display_end_game : Displays the end-of-game message.
 * - \b display_message : Displays a given message.
 */

#ifndef INTERFACE_H
#define INTERFACE_H

#include "board.h"
#include "player.h"
#include "card.h"

/**
 * \brief Displays all game information, including the board, players, 
 * teams, scores, hands, and bets.
 * 
 * \param b Pointer to the game board structure.
 */
void display_board(board b);

/**
 * \brief Asks the player to place a bet.
 * 
 * \param p Pointer to the player structure.
 * \return int The integer representing the player's bet.
 */
int ask_gamble(player p);

/**
 * \brief Asks the player how many cards they want to play.
 * 
 * \param p Pointer to the player structure.
 * \return int The number of cards the player wishes to play.
 */
int ask_number_of_played_cards(player p);

/**
 * \brief Asks the player to choose a card from their hand to play.
 * 
 * \param p Pointer to the player structure.
 * \return card Pointer to the selected card.
 */
card ask_card(player p);

/**
 * \brief Displays an end-of-game message with associated information.
 * 
 * \param b Pointer to the game board structure.
 */
void display_end_game(board b);

/**
 * \brief Displays a given message.
 * 
 * \param message Character string containing the message to display.
 */
void display_message(const char *message);


// ===== [Ajout Lot E] : Cartes Spéciales =====

/**
 * @brief Demande si la joueuse souhaite jouer sa carte spéciale.
 * @param p La joueuse.
 * @return 1 si oui, 0 sinon.
 */
int ask_play_special_card(player p); // [Ajout - carte spéciale]

/**
 * \brief Permet à une joueuse de choisir une carte parmi les cartes mises de côté (hors spéciales).
 *
 * \param b Le plateau de jeu.
 * \return La carte choisie par la joueuse.
 */
card ask_card_from_out_of_game(board b);

// ===== [Ajout Lot E] : Saisie de la mise en jetons =====

/**
 * \brief Demande à la joueuse combien de jetons elle mise.
 * 
 * \param p La joueuse concernée.
 * \return Le nombre de jetons misés.
 */
int ask_token_bet(player p); // [Ajout Lot E]

#endif // INTERFACE_H

