class Directions:
   North = 0
   East = 1
   South = 2
   West = 3
   Count = 4

def get_moves( s ):
   return list( map( lambda x: ( x[ 0 ], int( x[ 1 : ] ) ), map( lambda x: x.strip().upper(), s.split( "," ) ) ) )

def compute_offset( s, starting_direction = Directions.North ):
   moves = get_moves( s )

   orientation = Directions.North
   offsets = [ 0, 0 ]

   for index, move in enumerate( moves ):
      direction, quantity = move

      if direction == "L":
         orientation = ( orientation - 1 + Directions.Count ) % Directions.Count
      elif direction == "R":
         orientation = ( orientation + 1 ) % Directions.Count

      if orientation == Directions.East:
         offsets[ 0 ] += quantity
      elif orientation == Directions.West:
         offsets[ 0 ] -= quantity
      elif orientation == Directions.North:
         offsets[ 1 ] += quantity
      elif orientation == Directions.South:
         offsets[ 1 ] -= quantity

   if starting_direction == Directions.East or starting_direction == Directions.West:
      offsets = [ offsets[ 1 ], offsets[ 0 ] ]

   return offsets

def compute_distance( offset ):
    return sum( map( lambda x: abs( x ), offset ) )

def compute_move_path( s, starting_direction = Directions.North, starting_location = ( 0, 0 ), granularity = 1 ):
   moves = get_moves( s )
   orientation = starting_direction
   current_location = list( starting_location )

   result = [ tuple( current_location ) ]

   for index, move in enumerate( moves ):
      direction, quantity = move

      if direction == "L":
         orientation = ( orientation - 1 + Directions.Count ) % Directions.Count
      elif direction == "R":
         orientation = ( orientation + 1 ) % Directions.Count

      if orientation == Directions.East:
         update_info = ( 0, granularity )
      elif orientation == Directions.West:
         update_info = ( 0, -granularity )
      elif orientation == Directions.North:
         update_info = ( 1, granularity )
      elif orientation == Directions.South:
         update_info = ( 1, -granularity )

      initial_value = current_location[ update_info[ 0 ] ]
      for i in range( 0, int( math.ceil( float( quantity ) / granularity ) ) ):
         current_location[ update_info[ 0 ] ] = initial_value + ( i + 1 ) * update_info[ 1 ]
         result.append( tuple( current_location ) )

   return result

def locate_repeated_locations( s, starting_direction = Directions.North, starting_location = ( 0, 0 ), granularity = 1 ):
   """
   Locates the repeated locations in order.
   """

   locations = compute_move_path( s, starting_direction, starting_location, granularity )

   result = []

   for oi, ol in enumerate( locations[ : -1 ] ):
      for il in locations[ oi + 1 : ]:
         if ol == il:
            result.append( ol )

   return result

def process_strings( *strs ):
   for input_str in strs:
      print( "Path: '{}', Offset: {}, Distance: {}, Repeated Locations: {}, Repeated Location Distances: {}".format( input_str, str( compute_offset( input_str ) ), str( compute_distance( compute_offset( input_str ) ) ), str( locate_repeated_locations( input_str ) ), str( [ compute_distance( location ) for location in locate_repeated_locations( input_str ) ] ) ) )

strs = [ "R2, L3", "R2, R2, R2", "R5, L5, R5, R3", "R8, R4, R4, R8", "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1" ]

process_strings( *strs )
