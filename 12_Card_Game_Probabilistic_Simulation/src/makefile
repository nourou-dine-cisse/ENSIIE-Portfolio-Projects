CC=gcc
CFLAGS=-Wall -Wextra -std=c99

# Définir les fichiers source
SRC=$(wildcard src/*.c)

# Définir les fichiers objets
OBJ=$(SRC:.c=.o)

.PHONY: all clean rebuild

# Nom de l'exécutable final
EXEC=projet

# Règle par défaut : construire l'exécutable
all: $(EXEC)

# Règle pour compiler l'exécutable
$(EXEC): $(OBJ)
	$(CC) $(CFLAGS) $^ -o $@

# Règle pour compiler les fichiers source en objets
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Règle pour nettoyer les fichiers objets et l'exécutable
clean:
	rm -f $(OBJ) $(EXEC)

rebuild: clean all