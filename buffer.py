# Taken from https://github.com/jaasonw/osu-db-tools/blob/master/buffer.py
import struct

async def read_bool(buffer) -> bool:
    return struct.unpack("<?", await buffer.read(1))[0]

async def read_ubyte(buffer) -> int:
    return struct.unpack("<B", await buffer.read(1))[0]

async def read_ushort(buffer) -> int:
    return struct.unpack("<H", await buffer.read(2))[0]

async def read_uint(buffer) -> int:
    return struct.unpack("<I", await buffer.read(4))[0]

async def read_float(buffer) -> float:
    return struct.unpack("<f", await buffer.read(4))[0]

async def read_double(buffer) -> float:
    return struct.unpack("<d", await buffer.read(8))[0]

async def read_ulong(buffer) -> int:
    return struct.unpack("<Q", await buffer.read(8))[0]

# osu specific
async def read_int_double(buffer):
    await read_ubyte(buffer)
    integer = await read_uint(buffer)
    await read_ubyte(buffer)
    double = await read_double(buffer)
    return (integer, double)

async def read_timing_point(buffer):
    bpm = await read_double(buffer)
    offset = await read_double(buffer)
    inherited = await read_bool(buffer)
    return (bpm, offset, inherited)

async def read_string(buffer, skip=False) -> str:
    strlen = 0
    strflag = await read_ubyte(buffer)
    if (strflag == 0x0b):
        strlen = 0
        shift = 0
        # uleb128
        # https://en.wikipedia.org/wiki/LEB128
        while True:
            byte = await read_ubyte(buffer)
            strlen |= ((byte & 0x7F) << shift)
            if (byte & (1 << 7)) == 0:
                break
            shift += 7
    if skip:
        await buffer.read(strlen)
    else:
        return (struct.unpack("<" + str(strlen) + "s", await buffer.read(strlen))[0]).decode("utf-8")
class WriteBuffer:
    def __init__(self):
        self.offset = 0
        self.data = b""

    def write_bool(self, data: bool):
        self.data += struct.pack("<?", data)

    def write_ubyte(self, data: int):
        self.data += struct.pack("<B", data)

    def write_ushort(self, data: int):
        self.data += struct.pack("<H", data)

    def write_uint(self, data: int):
        self.data += struct.pack("<I", data)

    def write_float(self, data: float):
        self.data += struct.pack("<f", data)

    def write_double(self, data: float):
        self.data += struct.pack("<d", data)

    def write_ulong(self, data: int):
        self.data += struct.pack("<Q", data)

    def write_string(self, data: str):
        if (len(data) > 0):
            self.write_ubyte(0x0b)
            strlen = b""
            value = len(data)
            while value != 0:
                byte = (value & 0x7F)
                value >>= 7
                if (value != 0):
                    byte |= 0x80
                strlen += struct.pack("<B", byte)
            self.data += strlen
            self.data += struct.pack("<" + str(len(data)) +
                                     "s", data.encode("utf-8"))
        else:
            self.write_ubyte(0x0)

    def clear_buffer(self):
        self.data = b""