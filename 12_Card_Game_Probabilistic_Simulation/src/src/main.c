#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../include/board.h"
#include "../include/player.h"
#include "../include/card.h"
#include "../include/interface.h"

#define TOTAL_SPECIAL_CARDS 6

void display_card(card c) {
    if (is_special_card(c)) {
        printf("\n");
        printf("\x1b[35m┌──────────────┐\x1b[0m\n");
        printf("\x1b[35m│ SPECIAL CARD │\x1b[0m\n");
        printf("\x1b[35m│ %-12s │\x1b[0m\n", get_card_name(c));
        printf("\x1b[35m│ %-12s │\x1b[0m\n", get_card_description(c));
        printf("\x1b[35m└──────────────┘\x1b[0m\n");
    } else {
        printf("\n");
        printf("┌──────────┐\n");
        printf("│ %2d       │\n", get_value(c));
        printf("│          │\n");
        printf("│          │\n");
        printf("│       %2d │\n", get_value(c));
        printf("└──────────┘\n");
    }
}

void prepare_special_cards(card *special_cards) {
    special_cards[0] = create_special_card("Laurence", "Inverse bets", 0);
    special_cards[1] = create_special_card("Vincent", "2 <-> 5", 1);
    special_cards[2] = create_special_card("Thuy Vo", "1 rouge", 2);
    special_cards[3] = create_special_card("Fetia", "-1 tour", 3);
    special_cards[4] = create_special_card("Lawanda", "Rejoue carte", 4);
    special_cards[5] = create_special_card("Valentin", "+1 tour", 5);

    for (int i = TOTAL_SPECIAL_CARDS - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        card tmp = special_cards[i];
        special_cards[i] = special_cards[j];
        special_cards[j] = tmp;
    }
}

int *melange_carte() {
    int *result = malloc(20 * sizeof(int));
    for (int i = 0; i < 20; i++)
        result[i] = i % 5 + 1;
    for (int i = 0; i < 20; i++) {
        int j = rand() % 20;
        int temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }
    return result;
}

int main() {
    srand(time(NULL));
    board board = create_board();
    set_remaining_rounds(board, 3);

    add_team(board);
    add_team(board);

    for (int i = 0; i < 4; i++) {
        player p = create_player();
        add_player_to_team(board, (i % 2 == 0) ? 0 : 1, p);
    }

    int *cartes = melange_carte();
    card special_cards[TOTAL_SPECIAL_CARDS];
    prepare_special_cards(special_cards);

    for (int i = 0; i < 4; i++) {
        int team = (i % 2 == 0) ? 0 : 1;
        int index = i;
        player p = get_player(board, team, index / 2);
        printf("Cartes du joueur %d (equipe %d) :\n", index, team);
        for (int j = 0; j < 5; j++) {
            card c = create_card();
            set_value(c, cartes[i * 5 + j]);
            add_card_to_hand(p, c);
            display_card(c);
        }
        card special = special_cards[i];
        add_card_to_hand(p, special);
        display_card(special);
    }
    free(cartes);

    int round = 0;
    while (get_remaining_rounds(board) > 0) {
        printf("\n--- Debut du tour %d ---\n", round + 1);

        for (int i = 0; i < 4; i++) {
            int team = (i % 2 == 0) ? 0 : 1;
            int index = i;
            player p = get_player(board, team, index / 2);

            int pari = ask_gamble(p);
            set_slate(p, pari);

            int mise = ask_token_bet(p);
            set_bet_amount(p, mise);
            remove_tokens(p, mise);
        }

        int somme_0 = 0, somme_1 = 0;
        for (int i = 0; i < 4; i++) {
            int team = (i % 2 == 0) ? 0 : 1;
            int index = i;
            player p = get_player(board, team, index / 2);

            int special_card_available = 0;
            for (int k = 0; k < get_size_of_hand(p); k++) {
                if (is_special_card(get_card_in_hand(p, k))) {
                    special_card_available = 1;
                    break;
                }
            }

            int cards_played = 0;
            if (special_card_available && ask_play_special_card(p)) {
                for (int k = 0; k < get_size_of_hand(p); k++) {
                    card c = get_card_in_hand(p, k);
                    if (is_special_card(c)) {
                        play_card(p, c);
                        remove_card_from_hand(p, c);
                        apply_special_card_effect(board, p, c);
                        cards_played++;
                        break;
                    }
                }
            }

            int max_cards = 2 - cards_played;
            int num_cards = ask_number_of_played_cards(p);
            if (num_cards > max_cards) num_cards = max_cards;

            for (int j = 0; j < num_cards; j++) {
                card c = ask_card(p);
                play_card(p, c);
                remove_card_from_hand(p, c);
                if (team == 0) somme_0 += get_value(c);
                else somme_1 += get_value(c);
            }
        }

        for (int i = 0; i < 4; i++) {
            int team = (i % 2 == 0) ? 0 : 1;
            int index = i;
            player p = get_player(board, team, index / 2);
            int pari = get_slate(p);
            int mise = get_bet_amount(p);

            if (somme_0 > somme_1) {
                if (team == 0 && pari == 1) add_tokens(p, 2 * mise);
                else if (team == 1 && pari == 0) add_tokens(p, 2 * mise);
            } else if (somme_1 > somme_0) {
                if (team == 1 && pari == 1) add_tokens(p, 2 * mise);
                else if (team == 0 && pari == 0) add_tokens(p, 2 * mise);
            }
        }

        display_board(board);

        printf("\nCartes mises de cote ce tour :\n");
        for (int i = 0; i < 4; i++) {
            int team = (i % 2 == 0) ? 0 : 1;
            int index = i;
            player p = get_player(board, team, index / 2);
            while (get_number_of_played_cards(p) > 0) {
                card c = get_played_card(p, 0);
                display_card(c);
                remove_played_card(p, c);
                add_out_of_game_card(board, c);
            }
        }

        set_remaining_rounds(board, get_remaining_rounds(board) - 1);
        round++;
    }

    int tokens_0 = get_total_tokens_of_team(board, 0);
    int tokens_1 = get_total_tokens_of_team(board, 1);
    printf("\n===== FIN DU JEU =====\n");
    printf("Equipe 0 : %d jetons\n", tokens_0);
    printf("Equipe 1 : %d jetons\n", tokens_1);

    if (tokens_0 > tokens_1)
        printf("🎉 Equipe 0 gagne avec %d jetons !\n", tokens_0);
    else if (tokens_1 > tokens_0)
        printf("🎉 Equipe 1 gagne avec %d jetons !\n", tokens_1);
    else
        printf("🤝 Match nul avec %d jetons chacun !\n", tokens_0);

    free_board(board);
    return 0;
}