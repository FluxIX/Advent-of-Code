#! /usr/bin/env python3

import hashlib

def get_hash( message ):
   h = hashlib.md5()
   h.update( message.encode() )
   return h.hexdigest()

def locate_passcode( door_id, code_length, starting_iteration = 0, compare_length = 5 ):
   comps = [ None for i in range( code_length ) ]

   compare_prefix = compare_length * '0'

   digits_located = 0
   iteration = starting_iteration
   while digits_located < code_length:
      message = "{}{:d}".format( door_id, iteration )

      hash = get_hash( message )
      if hash[ : compare_length ] == compare_prefix:
         try:
            code_digit_pos = int( hash[ compare_length ] )
         except ValueError:
            pass # Invalid digit position, ignoring.
         else:
            code_digit = hash[ compare_length + 1 ]

            if code_digit_pos < code_length and comps[ code_digit_pos ] is None:
               comps[ code_digit_pos ] = code_digit
               digits_located += 1
               print( "Digit {:d} located on iteration {:d}: {}".format( code_digit_pos, iteration, code_digit ) )

      iteration += 1

   result = "".join( comps )

   return result

DOOR_ID = "uqwqemis"

print( "Door '{}': {}".format( DOOR_ID, locate_passcode( DOOR_ID, 8 ) ) )
