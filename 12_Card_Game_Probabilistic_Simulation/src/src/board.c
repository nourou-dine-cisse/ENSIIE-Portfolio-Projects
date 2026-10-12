
#include "../include/board.h"
#include "../include/card.h"
#include "../include/interface.h"  // [Ajout pour Lawanda Gaydu]

#include <stdlib.h>

struct team
{
    int id;
    int score;
    player *players;
    int num_players;
};

struct board_
{
    struct team *teams;
    int num_teams;
    card *out_of_game_cards;
    int num_out_of_game_cards;

    // [Ajout - pour effet Valentin/Fetia]
    int remaining_rounds; 
};


board create_board()
{
    board b = malloc(sizeof(struct board_));
    if (!b)
        return NULL;
    b->teams = NULL;
    b->num_teams = 0;
    b->out_of_game_cards = NULL;
    b->num_out_of_game_cards = 0;

    b->remaining_rounds = 3; // [Ajout - nombre de tours initial]
    return b;
}

void free_board(board b)
{
    if (!b)
        return;
    for (int i = 0; i < b->num_teams; i++)
    {
        free(b->teams[i].players);
    }

    free(b->teams);
    free(b->out_of_game_cards);
    free(b);
}

void add_team(board b)
{
    b->teams = realloc(b->teams, (b->num_teams + 1) * sizeof(struct team));
    if (!b->teams)
        return;
    b->teams[b->num_teams].id = b->num_teams;
    b->teams[b->num_teams].score = 0;
    b->teams[b->num_teams].players = NULL;
    b->teams[b->num_teams].num_players = 0;
    b->num_teams++;
}

int get_number_of_teams(board b)
{
    return b ? b->num_teams : 0;
}

void add_player_to_team(board b, int team_id, player p)
{
    if (!b || team_id >= b->num_teams)
        return;
    struct team *t = &b->teams[team_id];
    t->players = realloc(t->players, (t->num_players + 1) * sizeof(player));
    if (!t->players)
        return;
    t->players[t->num_players] = p;
    t->num_players++;
}

int get_number_of_players_in_team(board b, int team_id)
{
    return (b && team_id < b->num_teams) ? b->teams[team_id].num_players : 0;
}

player get_player(board b, int team_id, int player_index)
{
    if (!b || team_id >= b->num_teams || player_index >= b->teams[team_id].num_players)
        return NULL;
    return b->teams[team_id].players[player_index];
}
// ===== [Modifié Lot E] : Le score est maintenant le total de jetons
int get_score_of_team(board b, int team_id)
{
    return get_total_tokens_of_team(b, team_id);
}


void set_score_of_team(board b, int team_id, int score)
{
    if (!b || team_id >= b->num_teams)
        return;
    b->teams[team_id].score = score;
}

void add_out_of_game_card(board b, card c)
{
    if (!b)
        return;
    b->out_of_game_cards = realloc(b->out_of_game_cards, (b->num_out_of_game_cards + 1) * sizeof(card));
    if (!b->out_of_game_cards)
        return;
    b->out_of_game_cards[b->num_out_of_game_cards] = c;
    b->num_out_of_game_cards++;
}

int get_number_of_out_of_game_cards(board b)
{
    return b ? b->num_out_of_game_cards : 0;
}

card get_out_of_game_card(board b, int card_index)
{
    if (!b || card_index >= b->num_out_of_game_cards)
        return NULL;
    return b->out_of_game_cards[card_index];
}

void remove_out_of_game_card(board b, card c)
{
    if (!b)
        return;
    int found_index = -1;
    for (int i = 0; i < b->num_out_of_game_cards; i++)
    {
        if (b->out_of_game_cards[i] == c)
        {
            found_index = i;
            break;
        }
    }
    if (found_index == -1)
        return;
    for (int i = found_index; i < b->num_out_of_game_cards - 1; i++)
    {
        b->out_of_game_cards[i] = b->out_of_game_cards[i + 1];
    }
    b->num_out_of_game_cards--;
    b->out_of_game_cards = realloc(b->out_of_game_cards, b->num_out_of_game_cards * sizeof(card));
}

#include <string.h> // [Ajout - pour strcmp]

// [Ajout - Effet de carte spéciale]
void apply_special_card_effect(board b, player p, card c)
{
    if (!b || !p || !c || !is_special_card(c))
        return;

    int effect_id = get_card_effect_id(c);

    switch (effect_id)
    {
        case 0: // Laurence Bourard — Inverse les paris
            for (int i = 0; i < get_number_of_teams(b); i++)
            {
                int nb_players = get_number_of_players_in_team(b, i);
                for (int j = 0; j < nb_players; j++)
                {
                    player current = get_player(b, i, j);
                    int bet = get_slate(current);
                    set_slate(current, bet == 1 ? 0 : 1); // inverse Victoire/Defaite
                }
            }
            break;

        case 1: // Vincent Fagnon — inverse cartes de valeur 2 <-> 5
            for (int i = 0; i < get_number_of_teams(b); i++)
            {
                int nb_players = get_number_of_players_in_team(b, i);
                for (int j = 0; j < nb_players; j++)
                {
                    player current = get_player(b, i, j);

                    // Main
                    for (int k = 0; k < get_size_of_hand(current); k++)
                    {
                        card tmp = get_card_in_hand(current, k);
                        int v = get_value(tmp);
                        if (v == 2) set_value(tmp, 5);
                        else if (v == 5) set_value(tmp, 2);
                    }

                    // Cartes posées
                    for (int k = 0; k < get_number_of_played_cards(current); k++)
                    {
                        card tmp = get_played_card(current, k);
                        int v = get_value(tmp);
                        if (v == 2) set_value(tmp, 5);
                        else if (v == 5) set_value(tmp, 2);
                    }
                }
            }
            break;
        
        case 2: // Thuy Vo — transforme une carte posée en 1 rouge
            {
            for (int i = 0; i < get_number_of_teams(b); i++)
            {
                int nb_players = get_number_of_players_in_team(b, i);
                for (int j = 0; j < nb_players; j++)
                {
                    player pj = get_player(b, i, j);
                    int num_played = get_number_of_played_cards(pj);
                    if (num_played > 0)
                    {
                        card target = get_played_card(pj, 0); // prend la première carte jouée
                        if (!is_special_card(target))
                        {
                            set_value(target, 1);
                            // [TODO FUTUR] Ajouter couleur = rouge si la couleur est gérée
                            return;
                        }
                    }
                }
            }
            break;
        }

        case 3: // Fetia Bannour — retirer un tour de jeu
        {
            int current = get_remaining_rounds(b);
            if (current > 1)
                set_remaining_rounds(b, current - 1);
            else
                set_remaining_rounds(b, 0); // termine la partie
            break;
        }

        case 4: // Lawanda Gaydu — permet de rejouer une carte mise de côté
        {
            card chosen = ask_card_from_out_of_game(b);
            if (chosen != NULL)
            {
                remove_out_of_game_card(b, chosen);
                play_card(p, chosen);
            }
            break;
        }

        case 5: // Valentin Honoré — ajoute un tour
        {
            int current = get_remaining_rounds(b);
            set_remaining_rounds(b, current + 1);
            break;
        }




        default:
            // [Ajout] Aucun effet implémenté pour cet ID
            break;
    }
}

// [Ajout - get/set nombre de tours]
void set_remaining_rounds(board b, int n)
{
    if (b) b->remaining_rounds = n;
}

int get_remaining_rounds(board b)
{
    return b ? b->remaining_rounds : 0;
}

// ===== [Ajout Lot E] : Total des jetons d'une équipe =====

int get_total_tokens_of_team(const board b, int team_id)
{
    if (!b || team_id < 0 || team_id >= b->num_teams)
        return 0;

    int total = 0;
    struct team *t = &b->teams[team_id];

    for (int i = 0; i < t->num_players; i++)
    {
        player p = t->players[i];
        total += get_tokens(p);
    }

    return total;
}


