#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "tree.h"

#define SLEN 50

void readFileToTree(const char *filename, Tree *pt);
void printCat(const Item item);
void uppercase(char *str);

int main(void) {
    Tree pets;
    InitializeTree(&pets);

    printf("Loading cats from file...\n");
    readFileToTree("petkind.txt", &pets);

    printf("Total number of cats: %d\n", TreeItemCount(&pets));
    printf("List of cats:\n");
    Traverse(&pets, printCat);

    DeleteAll(&pets);
    printf("Done!\n");

    return 0;
}

void readFileToTree(const char *filename, Tree *pt) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Could not open file %s\n", filename);
        exit(1);
    }

    char line[100];
    Item temp;

    while (fgets(line, sizeof(line), file)) {
        char *comma = strchr(line, ',');
        if (!comma) continue;

        *comma = '\0';
        strncpy(temp.petname, line, SLEN);
        strncpy(temp.petkind, comma + 1, SLEN);

        char *newline = strchr(temp.petkind, '\n');
        if (newline) *newline = '\0';

        uppercase(temp.petname);
        uppercase(temp.petkind);

        if (!AddItem(&temp, pt)) {
            fprintf(stderr, "Error adding item to tree: %s, %s\n", temp.petname, temp.petkind);
        }
    }

    fclose(file);
}

void printCat(const Item item) {
    printf("Name: %s, Breed: %s\n", item.petname, item.petkind);
}

void uppercase(char *str) {
    while (*str) {
        *str = toupper((unsigned char)*str);
        str++;
    }
}



