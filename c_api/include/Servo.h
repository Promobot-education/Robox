
#ifndef SERVO_H
#define SERVO_H

#include "bus_handler.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <stdbool.h>


#define TORQUE_REG         41
#define SETPOINT_REG       42
#define POS_REG            47
#define SPEED_REG          48

#define MODE_1_REG         3
#define MODE_2_REG         4
#define COMMAND_REG        40
#define ERRORS_REG         45
#define CURRENT_REG        49


#define PID_SPEED_P_REG    10
#define PID_SPEED_I_REG    12
#define PID_SPEED_D_REG    14


#define PID_POS_P_REG      16
#define PID_POS_I_REG      18
#define PID_POS_D_REG      20


#define PID_MAX_VALUE      20.0
#define PID_MIN_VALUE      0.0

struct servo_data {
   int16_t ID;
   bool torque;
   int16_t setpoint;
   int16_t position;
   int16_t speed;
   int16_t command;
   int16_t current;
   float   pos_PID_P;
   float   pos_PID_I;
   float   pos_PID_D;
   float   speed_PID_P;
   float   speed_PID_I;
   float   speed_PID_D;   
   char    *errors[9];    

};

enum PID_mode {
    NORMAL,
    PWM,
    SPEED
};

extern const char *errors_list[9];

struct servo_data servo_data;

int set_torque(int addr,bool state); 
int set_point(int addr,int16_t setpoint); 
int set_command(int addr,int16_t command);
int init_servo(int addr);
int set_PID_mode(int addr,int mode);

int set_Pos_PID_P(int addr,float value);
int set_Pos_PID_I(int addr,float value);
int set_Pos_PID_D(int addr,float value);

int set_Speed_PID_P(int addr,float value);
int set_Speed_PID_I(int addr,float value);
int set_Speed_PID_D(int addr,float value);

struct servo_data get_servo_data(int addr);
int _check_input_PID_value(float value); 


#endif 