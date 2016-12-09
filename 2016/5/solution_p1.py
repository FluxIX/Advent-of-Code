#! /usr/bin/env python3

import hashlib

def get_hash( message ):
   h = hashlib.md5()
   h.update( message.encode() )
   return h.hexdigest()

def locate_passcode( door_id, code_length, starting_iteration = 0, compare_length = 5 ):
   comps = []

   iteration = starting_iteration
   while len( comps ) < code_length:
      message = "{}{:d}".format( door_id, iteration )

      hash = get_hash( message )
      if hash[ : compare_length ] == compare_length * '0':
         code_digit = hash[ compare_length ]

         comps.append( code_digit )
         print( "Digit {:d} located on iteration {:d}: {}".format( len( comps ), iteration, code_digit ) )

      iteration += 1

   result = "".join( comps )

   return result

DOOR_ID = "uqwqemis"

print( "Door '{}': {}".format( DOOR_ID, locate_passcode( DOOR_ID, 8 ) ) )
