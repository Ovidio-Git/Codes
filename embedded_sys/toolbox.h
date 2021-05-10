// compiler one time
#ifndef _TOOLBOX_H_
#define _TOOLBOX_H_

// call standart librarys
#include <string.h>


/** Render html template
 *
 *  char file[] -> filename html
 *  char socket[] -> socket for send information
 *  return -> -1 if html file not found
 */
char render(char file[], int socket);

/** Search a varaible  target in chain string
 *
 *  char chain[] -> string
 *  char target[] -> Target variable
 *  Return -> value of variable
 */
void search(char chain[], char target[]);


/** Verfication username and password for login
 *
 *  Return -> 1 user correct
 *  Return -> 0 user incorrect
 */
char login(char username[], char password[]);

#include "toolbox.c"
#endif