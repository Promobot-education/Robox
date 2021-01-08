/******************************************************************************
     * File: Ranger.c
     * Description: Работа с датчиком расстояния.
******************************************************************************/
#include "Ranger.h"




int set_min_dist(int addr,int dist) 
{

	int ret;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_register( ctx, MIN_DIST_REGISTER, dist );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

} 


int trig_sensor(int addr) 
{

	int ret;

	modbus_set_slave(ctx, addr);

	ret = modbus_write_register( ctx, TRIG_REGISTER, 1 );
	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return -1;
	}
	return 0;

}



struct sensor_data read_sensor(int addr)
{

	int ret;
	uint16_t regData[2];
	struct sensor_data output_data;

	modbus_set_slave(ctx, addr);
	ret = modbus_read_registers( ctx, RESULT_REGISTER, 2, regData );

	if ( ret == -1 ) 
	{
		_dealWithModbusError( ctx, addr);
		return;
	}
	else
	{

		output_data.IR_distance      =  regData[0] / 10;
		output_data.US_distance 	 =  regData[0];

		if (output_data.IR_distance == 819) output_data.IR_distance = 255;
		if (output_data.US_distance == 8100) output_data.US_distance = 255;
		return output_data;
	}
}  