/**
 * \file card.h
 * 
 * Card management module.
 * 
 * This file defines the abstract type \b card and provides function signatures 
 * for creating, accessing, and modifying cards in the game.
 * 
 * 1 Definition:
 * - \b card :
 * 
 * 6 Functions:
 * - \b create_card : Creates a card with no initial value and assigns it a unique ID.
 * - \b free_card : Frees the memory allocated for a card.
 * - \b get_card_id : Retrieves the unique identifier of a card.
 * - \b get_card_by_id : Retrieves a card based on its ID.
 * - \b get_value : Retrieves the value of a card.
 * - \b set_value : Modifies the value of a card.
 */

#ifndef CARD_H
#define CARD_H



/**
 * \brief Definition of the abstract type card.
 * 
 * A variable of type card allows access to all information related to a card.
 */
typedef struct card_* card;

/**
 * \brief Creates a card without a value and assigns it a unique identifier.
 * 
 * \return card* Pointer to the newly created card.
 */
card create_card();

/**
 * \brief Frees the memory allocated for a card.
 * 
 * \param c Pointer to the card to be freed.
 */
void free_card(card c);

/**
 * \brief Returns the unique identifier of a card.
 * 
 * \param c Pointer to the card whose identifier is to be retrieved.
 * \return int The unique identifier of the card.
 */
int get_card_id(card c);

/**
 * \brief Returns a card based on its identifier.
 * 
 * \param id Identifier of the desired card.
 * \return card* Pointer to the card corresponding to the given identifier.
 */
card get_card_by_id(int id);

/**
 * \brief Returns the value written on a card.
 * 
 * \param c Pointer to the card whose value is to be ridetrieved.
 * \return int The value of the card.
 */
int get_value(card c);

/**
 * \brief Modifies the value written on a card.
 * 
 * \param c Pointer to the card to be modified.
 * \param value New card value.
 */
void set_value(card c, int value);

// ===== [Ajout Lot E] : Cartes Spéciales =====

/**
 * @brief Vérifie si la carte est une carte spéciale.
 */
int is_special_card(card c); // [Ajout - carte spéciale]

/**
 * @brief Retourne le nom de la carte spéciale.
 */
const char* get_card_name(card c); // [Ajout - carte spéciale]

/**
 * @brief Retourne la description de la carte spéciale.
 */
const char* get_card_description(card c); // [Ajout - carte spéciale]

/**
 * @brief Retourne l'identifiant de l'effet associé à la carte spéciale.
 */
int get_card_effect_id(card c); // [Ajout - carte spéciale]

/**
 * @brief Crée une carte spéciale avec un nom, une description et un ID d'effet.
 */
card create_special_card(const char* name, const char* description, int effect_id); // [Ajout - carte spéciale]

#endif // CARD_H
