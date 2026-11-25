#include <iostream>
#include <cstdint>
#include <vector>


using std::vector;


enum class ObjectType {
    None,   // Basically air
    Sand,   // O, Standard falling object
    Water,  // ~, Sand but faster and more dense
    Lava,   // =, Water but slower (slower than sand)
    Stone,  // @, The man who can't be moved, water + lava
    Wood,   // %, Stone but flammable by lava
};


struct Object {
    ObjectType type;
    uint16_t speed;
    char symbol;

    Object(
        ObjectType _type = ObjectType::None, 
        uint16_t _speed = 0,
        char _symbol = ' '
    ) :
        type(_type), 
        speed(_speed),
        symbol(_symbol) {};
};

struct SandObject : Object {
    SandObject() : Object(ObjectType::Sand, 2, 'O') {};
};

struct WaterObject : Object {
    WaterObject() : Object(ObjectType::Water, 3, '~') {};
};

struct LavaObject : Object {
    LavaObject() : Object(ObjectType::Lava, 1, '=') {};
};

struct StoneObject : Object {
    StoneObject() : Object(ObjectType::Stone, 0, '@') {};
};

struct WoodObject : Object {
    WoodObject() : Object(ObjectType::Wood, 0, '%') {};
};


// Includes borders, so the true
// size is (GRID_X - 2) and (GRID_Y - 2)
const uint16_t GRID_X = 50; // Width
const uint16_t GRID_Y = 10; // Height

const int16_t GRAVITY = 1;  // Characters per second, maybe

const char X_SYMBOL = '|';
const char Y_SYMBOL = '-';


vector<Object> objects(GRID_Y * GRID_X);


std::string drawGrid() {
    std::string world;

    for (uint16_t y = 0; y < GRID_Y; y++) {
        for (uint16_t x = 0; x < GRID_X; x++) {

            uint16_t index = y * GRID_X + x;

            // Top and bottom walls
            if (y == 0 || y == GRID_Y - 1) {
                if (x == GRID_X - 1) {
                    world += Y_SYMBOL;
                    world += '\n';
                } else {
                    world += Y_SYMBOL;
                }

            // Right walls
            } else if (x == GRID_X - 1) {
                world += X_SYMBOL;
                world += '\n';

            // Left walls
            } else if (x == 0) {
                world += X_SYMBOL;

            // Inside the walls (the actual grid)
            } else {
                Object obj = objects[index];
                world += obj.symbol;
            }
        } // width (x) loop
    } // height (y) loop

    return world;
}


int main() {

    std::string world;
    std::string inputMenu;

    while (true) {

        world = drawGrid();

        // (inputMenu draw here)


        // Render strings?
        std::cout << world;
        std::cout << inputMenu;

        // Clear strings for next iteration
        world = "";
        inputMenu = "";

        break; // Temporary, to avoid infinite loop

    } // main while loop

    return 0;
}
