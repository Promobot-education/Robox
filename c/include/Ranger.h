
#ifndef RANGER_H
#define RANGER_H

#include "bus_handler.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <stdbool.h>


#define TRIG_REGISTER       20
#define RESULT_REGISTER     21
#define COMMAND_REGISTER    19

#define MIN_DIST_REGISTER   5
                      
#define MAX_LED_DIST        2000
#define MIN_LED_DIST        0

struct sensor_data {
   uint8_t US_distance;
   uint8_t IR_distance;
};

struct sensor_data sensor_data;

int trig_sensor(int addr); 
struct sensor_data read_sensor(int addr);
int set_min_dist(int addr,int dist);  

#endif 