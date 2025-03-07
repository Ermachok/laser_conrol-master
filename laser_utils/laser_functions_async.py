import asyncio
import socket
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_command(server_address, command, command_name, timeout=3):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(*server_address), timeout=timeout)
        writer.write(command)
        await writer.drain()
        logger.info(f'Sent {command_name}')
        answer_serv = await asyncio.wait_for(reader.read(1024), timeout=timeout)
        logger.info(f'Received: {answer_serv}')
        return answer_serv
    except asyncio.TimeoutError as e:
        logger.error(f'Timeout sending {command_name}: {e}')
        raise TimeoutError(f'Cannot connect to laser: {e}')
    except Exception as e:
        logger.error(f'Error sending {command_name}: {e}')
        raise Exception
    finally:
        writer.close()
        await writer.wait_closed()
        raise Exception(f'Error sending {command_name}: {e}')



async def arm(server_address, timeout=3):
    try:
        await send_command(server_address, b'\x23\x03\x53\x00\x79', 'idling on', timeout)
        await asyncio.sleep(0.01)
        await send_command(server_address, b'\x23\x03\x43\x00\x69', 'start', timeout)
        return True
    except TimeoutError as e:
        logger.error(f'Arming failed: {e}')
        raise


async def disarm(server_address, timeout=3):
    try:
        await send_command(server_address, b'\x23\x03\x44\x00\x70', 'stop', timeout)
        await asyncio.sleep(0.01)
        await send_command(server_address, b'\x23\x03\x73\x00\x99', 'idling off', timeout)
        return True
    except TimeoutError as e:
        logger.error(f'Disarming failed: {e}')
        raise


async def fire(server_address):
    try:
        await send_command(server_address, b'\x23\x03\x42\x00\x68', 'laser generator on')
    except TimeoutError as e:
        logger.error(f'Firing failed: {e}')
        raise


async def fire_stop(server_address):
    try:
        await send_command(server_address, b'\x23\x03\x62\x00\x88', 'laser generator off')
    except TimeoutError as e:
        logger.error(f'Stopping fire failed: {e}')
        raise
