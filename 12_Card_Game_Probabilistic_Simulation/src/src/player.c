#include "../include/player.h"
#include <stdlib.h>

struct player_s
{
    int id;
    card *hand;
    int hand_size;
    card *played_cards;
    int played_size;
    int slate;

    // ===== [Ajout Lot E] =====
    int tokens;         // Nombre de jetons possédés
    int current_bet;    // Montant de la mise courante
};


static int next_id = 0;
#define MAX_PLAYERS 100
static player player_list[MAX_PLAYERS] = {NULL};

player create_player()
{
    if (next_id >= MAX_PLAYERS)
        return NULL;
    player p = (player)malloc(sizeof(struct player_s));
    if (!p)
        return NULL;

    p->id = next_id;
    p->hand = NULL;
    p->hand_size = 0;
    p->played_cards = NULL;
    p->played_size = 0;
    p->slate = 0;
    player_list[next_id++] = p;
    p->tokens = 20;         // [Ajout Lot E] Initialisation à 20 jetons
    p->current_bet = 0;     // [Ajout Lot E] Mise à 0 au départ
    return p;
}

void free_player(player p)
{
    if (!p)
        return;
    free(p->hand);
    free(p->played_cards);
    player_list[p->id] = NULL;
    free(p);
}

int get_player_id(player p)
{
    return p ? p->id : -1;
}

player get_player_by_id(int id)
{
    if (id < 0 || id >= next_id || !player_list[id])
        return NULL;
    return player_list[id];
}

void add_card_to_hand(player p, card c)
{
    if (!p)
        return;
    p->hand = (card *)realloc(p->hand, (p->hand_size + 1) * sizeof(card));
    if (!p->hand)
        return;
    p->hand[p->hand_size++] = c;
}

int get_size_of_hand(player p)
{
    return p ? p->hand_size : 0;
}

card get_card_in_hand(player p, int card_index)
{
    if (!p || card_index < 0 || card_index >= p->hand_size)
        return NULL;
    return p->hand[card_index];
}

void remove_card_from_hand(player p, card c)
{
    if (!p || p->hand_size == 0)
        return;
    int index = -1;
    for (int i = 0; i < p->hand_size; i++)
    {
        if (p->hand[i] == c)
        {
            index = i;
            break;
        }
    }
    if (index == -1)
        return;
    for (int i = index; i < p->hand_size - 1; i++)
    {
        p->hand[i] = p->hand[i + 1];
    }
    p->hand_size--;
    p->hand = (card *)realloc(p->hand, p->hand_size * sizeof(card));
}

void play_card(player p, card c)
{
    if (!p)
        return;
    p->played_cards = (card *)realloc(p->played_cards, (p->played_size + 1) * sizeof(card));
    if (!p->played_cards)
        return;
    p->played_cards[p->played_size++] = c;
}

int get_number_of_played_cards(player p)
{
    return p ? p->played_size : 0;
}

card get_played_card(player p, int card_index)
{
    if (!p || card_index < 0 || card_index >= p->played_size)
        return NULL;
    return p->played_cards[card_index];
}

void remove_played_card(player p, card c)
{
    if (!p || p->played_size == 0)
        return;
    int index = -1;
    for (int i = 0; i < p->played_size; i++)
    {
        if (p->played_cards[i] == c)
        {
            index = i;
            break;
        }
    }
    if (index == -1)
        return;
    for (int i = index; i < p->played_size - 1; i++)
    {
        p->played_cards[i] = p->played_cards[i + 1];
    }
    p->played_size--;
    p->played_cards = (card *)realloc(p->played_cards, p->played_size * sizeof(card));
}

int get_slate(player p)
{
    return p ? p->slate : 0;
}

void set_slate(player p, int bet)
{
    if (!p)
        return;
    p->slate = bet;
}

// ===== [Ajout Lot E] : Fonctions de gestion des jetons =====

int get_tokens(player p)
{
    return p ? p->tokens : 0;
}

void set_tokens(player p, int tokens)
{
    if (p)
        p->tokens = tokens;
}

void add_tokens(player p, int tokens)
{
    if (p)
        p->tokens += tokens;
}

void remove_tokens(player p, int tokens)
{
    if (p && p->tokens >= tokens)
        p->tokens -= tokens;
}

void set_bet_amount(player p, int tokens)
{
    if (p)
        p->current_bet = tokens;
}

int get_bet_amount(player p)
{
    return p ? p->current_bet : 0;
}
