#include <stdio.h>
#include <string.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"


int main (void) {
    char buff[256];
    int error;
    lua_State *L = luaL_newstate();             /* opens Lua*/
                    /*(containt lua variable to ovoid global declaration)*/
    luaL_openlibs(L);        /* opens the standard libraries */

    while (fgets(buff, sizeof(buff), stdin) != NULL) {
        // Load the string and call(run) it
        error = luaL_loadstring(L, buff) || lua_pcall(L, 0, 0, 0);
        if (error) {
            fprintf(stderr, "%s\n", lua_tostring(L, -1));
            lua_pop(L, 1);  /* pop error message from the stack */
        }
    }

    lua_close(L);
    return 0;
}
