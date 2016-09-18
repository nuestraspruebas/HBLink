#!/usr/bin/env python
#
# This work is licensed under the Creative Attribution-NonCommercial-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.

from __future__ import print_function

from bitstring import BitArray

# Does anybody read this stuff? There's a PEP somewhere that says I should do this.
__author__     = 'Cortney T. Buffington, N0MJS'
__copyright__  = 'Copyright (c) 2016 Cortney T. Buffington, N0MJS and the K0USY Group'
__credits__    = 'Jonathan Naylor, G4KLX; Ian Wraith'
__license__    = 'Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported'
__maintainer__ = 'Cort Buffington, N0MJS'
__email__      = 'n0mjs@me.com'

#------------------------------------------------------------------------------
# BPTC(196,96) Decoding routings
#------------------------------------------------------------------------------

mod_181_index = (
0, 181, 166, 151, 136, 121, 106, 91, 76, 61, 46, 31, 16, 1, 182, 167, 152, 137,
122, 107, 92, 77, 62, 47, 32, 17, 2, 183, 168, 153, 138, 123, 108, 93, 78, 63,
48, 33, 18, 3, 184, 169, 154, 139, 124, 109, 94, 79, 64, 49, 34, 19, 4, 185, 170,
155, 140, 125, 110, 95, 80, 65, 50, 35, 20, 5, 186, 171, 156, 141, 126, 111, 96,
81, 66, 51, 36, 21, 6, 187, 172, 157, 142, 127, 112, 97, 82, 67, 52, 37, 22, 7,
188, 173, 158, 143, 128, 113, 98, 83, 68, 53, 38, 23, 8, 189, 174, 159, 144, 129,
114, 99, 84, 69, 54, 39, 24, 9, 190, 175, 160, 145, 130, 115, 100, 85, 70, 55, 40,
25, 10, 191, 176, 161, 146, 131, 116, 101, 86, 71, 56, 41, 26, 11, 192, 177, 162,
147, 132, 117, 102, 87, 72, 57, 42, 27, 12, 193, 178, 163, 148, 133, 118, 103, 88,
73, 58, 43, 28, 13, 194, 179, 164, 149, 134, 119, 104, 89, 74, 59, 44, 29, 14,
195, 180, 165, 150, 135, 120, 105, 90, 75, 60, 45, 30, 15)

# Converts a DMR frame using 98-68-98 (info-sync/EMB-info) into 196 bit array 
def dec_get_binary_19696(_data):
    _data = bytearray(_data)
    _data = BitArray(_data)
    return _data[:98] + _data[-98:]


# Applies interleave indecies de-interleave 196 bit array
def dec_deinterleave_19696(_data):
    deint = BitArray(196)
    for index in range(196):
        deint[index] = _data[(index * 181) % 196]
    return deint

# Applies BTPC error detection/correction routines (INCOMPLETE)
def dec_error_check_19696(_data):
    checked = BitArray(196)

# Returns useable LC data - 9 bytes info + 3 bytes RS(12,9) ECC
def dec_get_data_19696(_data):
    databits = BitArray()
    databits.append(_data[4:12])
    databits.append(_data[16:27])
    databits.append(_data[31:42])
    databits.append(_data[46:57])
    databits.append(_data[61:72])
    databits.append(_data[76:87])
    databits.append(_data[91:102])
    databits.append(_data[106:117])
    databits.append(_data[121:132])
    return databits.tobytes()


#------------------------------------------------------------------------------
# BPTC(196,96) Decoding routings
#------------------------------------------------------------------------------
# not yet implemented
    
    
#------------------------------------------------------------------------------
# Used to execute the module directly to run built-in tests
#------------------------------------------------------------------------------

if __name__ == '__main__':
    
    from binascii import b2a_hex as h
    
    # Validation Example
    data = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20'
    
    bin_data = dec_get_binary_19696(data)
    deint_data = dec_deinterleave_19696(bin_data)
    #err_corrected = dec_error_check_19696(deint_data)
    ext_data = dec_get_data_19696(deint_data)
    
    print('original 33 byte data block:')
    print(h(data))
    print(len(data), 'bytes')
    print()
    
    print('binary data (discarding sync)')
    print(bin_data.len, 'bits')
    print(bin_data)
    print()

    print('deinterleaved binary data')
    print(deint_data.len, 'bits')
    print(deint_data)
    print()

    print('decoded hex data')
    print(len(ext_data), 'bytes')
    print(h(ext_data))