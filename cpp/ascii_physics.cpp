#include <iostream>
#include <cstdint>
#include <vector>


using std::vector;


enum class ObjectType {
    None,   // basically air
    Sand,   // ., standard falling object
    Water,  // ~, sand but faster
    Lava,   // =, sand but slower
    Stone,  // @, the man who can't be moved, water + lava
    Wood,   // %, stone but flammable by lava
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
    SandObject() : Object(ObjectType::Sand, 2, '.') {};
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


const uint16_t GRID_X = 50;     // width
const uint16_t GRID_Y = 10;     // height
const int16_t GRAVITY = 1;      // characters per second

const char X_SYMBOL = '|';
const char Y_SYMBOL = '-';


vector<Object> objects(GRID_Y * GRID_X);
vector<char> grid(GRID_Y * GRID_X);


int main() {

    std::string world;

    while (true) {

        // Draw world
        for (uint16_t y = 0; y < GRID_Y; y++) {
            for (uint16_t x = 0; x < GRID_X; x++) {

                uint16_t index = y * GRID_X + x;

                // Top and bottom walls
                if (y == 0 || y == GRID_Y - 1) {
                    if (x == GRID_X - 1) {
                        grid[index] = Y_SYMBOL;
                        world += Y_SYMBOL;
                        world += '\n';
                    } else {
                        grid[index] = Y_SYMBOL;
                        world += Y_SYMBOL;
                    }

                // Right walls
                } else if (x == GRID_X - 1) {
                    grid[index] = X_SYMBOL;
                    world += X_SYMBOL;
                    world += '\n';

                // Left walls
                } else if (x == 0) {
                    grid[index] = X_SYMBOL;
                    world += X_SYMBOL;

                // Inside the walls
                } else {
                    Object obj = objects[index];
                    grid[index] = obj.symbol;
                    world += obj.symbol;
                }
            } // width (x) loop
        } // height (y) loop

        std::cout << world;
        world = "";

        break;

    } // main while loop

    return 0;
}
