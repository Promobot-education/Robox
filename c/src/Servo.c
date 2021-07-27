#include "Servo.h"


const char *errors_list[9] = {
	"COMMUNICATION",
    "HALL_BOARD",
    "WRONG_DIRECTION",
    "OVERCURRENT",
    "MAGNET_ERROR",
    "ENCODER",
    "DRV_ERR",
    "DISABLED",
    "REBOOTED"
};



int set_torque(int addr,bool state) 
{

	int ret;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_register( ctx, TORQUE_REG, state );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

} 



int set_command(int addr,int16_t command) 
{

	int ret;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_register( ctx, COMMAND_REG, command );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}



int set_point(int addr,int16_t setpoint) 
{

	int ret;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_register( ctx, SETPOINT_REG, setpoint );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}




int set_Pos_PID_P(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;


	if (_check_input_PID_value(value) < 0) {

		return -1;
	}

    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_POS_P_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}


int set_Pos_PID_I(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;

	if (_check_input_PID_value(value) < 0) {

		return -1;
	}

    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_POS_I_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}


int set_Pos_PID_D(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;

	if (_check_input_PID_value(value) < 0) {

		return -1;
	}
	
    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_POS_D_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}


int set_Speed_PID_P(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;

	if (_check_input_PID_value(value) < 0) {

		return -1;
	}
	
    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_SPEED_P_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}




int set_Speed_PID_I(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;

	if (_check_input_PID_value(value) < 0) {

		return -1;
	}
	
    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_SPEED_I_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}




int set_Speed_PID_D(int addr,float value) 
{

	int ret;	
	union {
        float f;
        uint16_t i[2];
    } f;

	if (_check_input_PID_value(value) < 0) {

		return -1;
	}
	
    f.f = value;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_registers( ctx, PID_SPEED_D_REG, 2, f.i);
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}





struct servo_data get_servo_data(int addr)
{

	int ret;
	uint16_t regData[50];
	struct servo_data output_data;
	union {
        float f;
        int i;
    } f;

	modbus_set_slave(ctx, addr);
	ret = modbus_read_registers( ctx, 0, 50, regData );

	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return;
	}
	else
	{ 
		output_data.ID          =  regData[0];
		output_data.torque      =  regData[TORQUE_REG];
		output_data.command 	=  regData[COMMAND_REG];
		output_data.setpoint 	=  (int16_t)regData[SETPOINT_REG];
		output_data.position 	=  (int16_t)regData[POS_REG];
		output_data.speed 		=  (int16_t)regData[SPEED_REG];
		output_data.current     =  (int16_t)regData[CURRENT_REG];

		f.i = regData[PID_POS_P_REG] |  (regData[PID_POS_P_REG + 1] <<16);
		output_data.pos_PID_P = f.f;	

		f.i = regData[PID_POS_I_REG] |  (regData[PID_POS_I_REG + 1] <<16);
		output_data.pos_PID_I = f.f;

		f.i = regData[PID_POS_D_REG] |  (regData[PID_POS_D_REG + 1] <<16);
		output_data.pos_PID_D = f.f;	

		f.i = regData[PID_SPEED_P_REG] |  (regData[PID_SPEED_P_REG + 1] <<16);
		output_data.speed_PID_P = f.f;

		f.i = regData[PID_SPEED_I_REG] |  (regData[PID_SPEED_I_REG + 1] <<16);
		output_data.speed_PID_I = f.f;	

		f.i = regData[PID_SPEED_D_REG] |  (regData[PID_SPEED_D_REG + 1] <<16);
		output_data.speed_PID_D = f.f;

		for (int i = 0; i < 9; i++){

		if (regData[ERRORS_REG] & (1 << i))
		{
			output_data.errors[i] = errors_list[i];
		}	
		else 
		{
			output_data.errors[i] = "a ";
		}
		}

		return output_data;
	}
}  



int set_PID_mode(int addr,int mode)
{
	int ret;
	uint16_t regData[1];

	modbus_set_slave(ctx, addr);

	ret = modbus_read_registers( ctx, MODE_1_REG, 1, regData );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}

	if (mode == NORMAL)
	{
		regData[0] = regData[0] | (1<<1);
		regData[0] = regData[0] | (1<<2);
	}	


	if (mode == PWM)
	{
		regData[0] = regData[0] & ~(1<<1);
		regData[0] = regData[0] & ~(1<<2);
	}

	if (mode == SPEED)
	{
		regData[0] = regData[0] | (1<<1);
		regData[0] = regData[0] & ~(1<<2);
	}

	ret = modbus_write_register( ctx, MODE_1_REG, regData[0] );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}

	return 0;

}



int init_servo(int addr)
{

	int ret;
	uint16_t regData[1];

	modbus_set_slave(ctx, addr);

	ret = modbus_read_registers( ctx, MODE_2_REG, 1, regData );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}


	regData[0] =  regData[0] & ~(1<<0);

	ret = modbus_write_register( ctx, MODE_2_REG, regData[0] );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}

	return 0;

}


int _check_input_PID_value(float value)
{

    if (value > PID_MAX_VALUE || value < PID_MIN_VALUE) 
    {
    	fprintf(stderr, "ERROR. Desired PID value out of range: %f\n\n", value);
		return -1;
    }

    return 0;

}
