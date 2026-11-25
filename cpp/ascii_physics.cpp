#include <iostream>
#include <cstdint>
#include <vector>


using std::cout;
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
        char _symbol = '.'
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


const uint16_t WORLD_X = 50;    // width
const uint16_t WORLD_Y = 10;    // height
const int16_t GRAVITY = 1;      // characters per second

const char X_SYMBOL = '|';
const char Y_SYMBOL = '-';


vector<vector<Object>> objects(WORLD_Y, vector<Object> (WORLD_X));
vector<vector<char>> world(WORLD_Y, vector<char> (WORLD_X));


int main() {

    // Initialize world
    for (int16_t y = 0; y < WORLD_Y; y++) {
        for (int16_t x = 0; x < WORLD_X; x++) {

            if (y == 0 || y == WORLD_Y - 1) {
                if (x == WORLD_X - 1) {
                    world[y][x] = Y_SYMBOL;
                    cout << Y_SYMBOL << '\n';
                } else {
                    world[y][x] = Y_SYMBOL;
                    cout << Y_SYMBOL;
                }

            } else if (x == WORLD_X - 1) {
                world[y][x] = X_SYMBOL;
                cout << X_SYMBOL << '\n';

            } else if (x == 0) {
                world[y][x] = X_SYMBOL;
                cout << X_SYMBOL;

            } else {
                Object obj = objects[y][x];
                world[y][x] = obj.symbol;
                cout << obj.symbol;
            }
        }
    }

    return 0;
}
