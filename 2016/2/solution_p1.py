GRID_DIMENSIONS = ( 3, 3 )
GRID = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]

def compute_next_position( movement, initial_position = ( 1, 1 ) ):
   current_position = list( initial_position )

   for move in movement:
      if move == 'U':
         if current_position[ 1 ] > 0:
            current_position[ 1 ] -= 1
      elif move == 'D':
         if current_position[ 1 ] < ( GRID_DIMENSIONS[ 1 ] - 1 ):
            current_position[ 1 ] += 1
      elif move == 'L':
         if current_position[ 0 ] > 0:
            current_position[ 0 ] -= 1
      elif move == 'R':
         if current_position[ 0 ] < ( GRID_DIMENSIONS[ 0 ] - 1 ):
            current_position[ 0 ] += 1
      else:
         raise ValueError( "Invalid move: '{}'".format( move ) )

   return tuple( current_position )

def process_code( *movements ):
   current_position = ( 1, 1 )

   result = []

   for movement in movements:
      new_position = list( compute_next_position( movement, current_position ) )
      result.append( GRID[ new_position[ 1 ] ][ new_position[ 0 ] ] )
      current_position = new_position

   return result

def process_codes( *movement_sets ):
   for movements in movement_sets:
      code = process_code( *movements )
      print( "Code: {}".format( "".join( map( lambda x: str( x ), code ) ) ) )

movement_sets = [ [ "ULL", "RRDDD", "LURDL", "UUUUD" ], """RLRDDRLLDLRLUDDULLDRUUULDDLRLUDDDLDRRDUDDDLLURDDDLDDDRDURUDRDRRULUUDUDDRRRLRRRRRLRULRLLRULDRUUDRLRRURDDRLRULDLDULLLRULURRUULLRLLDDDDLLDURRUDLDLURDRDRDLUUUDDRDUUDDULLUURRDRLDDULURRRUDLLULULDLLURURUDRRRRUDRLRDLRRLDDRDDLULDLLLURURDUDRRRRUULURLRDULDRLUDRRUDDUULDURUDLDDURRRDLULLUUDRLLDUUDLDRUDDRLLLLLLDUDUDDLRDLRRDRUDDRRRLLRRDLLRLDDURUURRRDDLDUULLDLDLRURDLLLDDRUUDRUDDDDULRLLDUULRUULLLULURRRLLULDLDUDLDLURUDUDULLDLLUUDRRDRLUURURURURDLURUUDLDRLUDDUUDULDULULLLDLDDULLULLDULRRDRULLURRRULLDDDULULURLRDURLLURUDDULLRUDLRURURRDRDUULDRUUDURDURDDLRDUUULDUUDRDURURDRRRURLLDDLLLURURULULUDLRDLDRDRURLRLULRDLU
UDLDURRULDRDDLDUULUDLDUULUURDDRUDRURRRUDRURLLDDRURLDLRDUUURDLLULURDDUDDDRRRURLLDLDLULRDULRLULDLUUDLLRLDLRUUULDDUURDLDDRRDLURLDUDDRURDRRURDURRRLUULURDDLRDLDRRRLDUDRLRLLRLDDUULDURUUULLLRRRRRRRDRRRDRLUULDLDDLULDRDUDLLUDRRUDRUUDULRLUURDDDDRRUUDLURULLLURDULUURDRDDURULRUDRRDLRDUUUUUDDDRDRDDRUDRDDDRLRUUDRDRDDDLUDRDRLDRDDRULURDRLDRUDUDRUULRLLUDRDRLLLLDUDRRLLURDLLLDRRUDDUDRLRLDUDRLURRUUULURDDRUURRLDRLRRRUUDLULDDDRDLDUUURLLUULDDRRUDLDDRUDUDUURURDDRDULLLLLULRRRDLRRRDDDLURDDDDLUULLLRDDURRRRLURRLDDLRUULULRDRDDDDLDUUUUUUDRRULUUUDD
UURDRRUDLURRDDDLUDLRDURUDURDLLLLRDLRLRDDRDRDUUULRDLLDLULULRDUDDRRUUDURULDLUDLRDRUDLDDULLLDDRDLLDULLLURLLRDDLDRDULRRDDULRDURLLRUDRLRRLUDURLDRDLDLRLLLURLRRURDLDURDLUDULRDULLLDRDDRDLDRDULUULURDRRRLDRRUULULLDDRRLDLRUURLRUURLURRLLULUUULRLLDDUDDLRLDUURURUDLRDLURRLLURUDLDLLUDDUULUUUDDDURDLRRDDDLDRUDRLRURUUDULDDLUUDDULLDDRRDDRRRUDUDUDLDLURLDRDLLLLDURDURLRLLLUUDLRRRRUDUDDLDLRUURRLRRLUURRLUDUDRRRRRRRLDUDDRUDDLUDLRDDDRLDUULDRDRRDLDRURDLDRULRLRLUDRDLRRUURUUUUDLDUUULLLRRRRRDLRRURDDLLLLUULDLLRULLUDLLDLLUDLRLRRLRURDDRRL
URDRDLLRDDDLLLDDLURLRURUURRRLUURURDURRLLUDURRLRLDLUURDLULRRDRUDDLULDLDRLDLRLRRLLLDDDUDDDLRURURRLLDRRRURUDLRDDLLDULDDLDRLUUUDRRRULDUULRDDDLRRLLURDDURLULRDUDURRLLDLLRLDUDDRRDDLRLLLDUDRLUURRLLDULRLDLUUUUUDULUDLULUDDUURRURLDLDRRLDLRRUDUDRRDLDUDDLULLDLLRDRURDRDRRLDDDDRDDRLLDDDLLUDRURLURDRRRRRUDDDUDUDDRDUUDRRUDUDRLULDDURULUURUUUURDRULRLRULLDDRRRUULRRRRURUDLDLRDLLDRLURLRUULLURDUDULRRURLRLLRRLLLURULRRRLDDUULLUUULRRDRULUUUUDRDRRDLRURLRLLRLRRRDRDRLDLUURUURULLDLULRRLRRDRULRRLLLDDURULLDLDLDLUUURDLDLUUDULRLLUDDRRDLLDLDLDURLUURRDDRRURDRLUDRLUUUDLDULDLUDRLDUDDLLRUDULLLLLDRRLLUULLUUURRDDUURDLLRDDLRLLU
LDUDRRDLUUDDRLLUUULURLDUDLUDLRLDRURLULRLLDDLRRUUUDDDDRDULDDUUDLRUULDRULLRDRUDDURLDUUURRUDUDRDRDURRDLURRRDRLDLRRRLLLRLURUURRDLLRDLDDLLRDUDDRDUULRULRRURLUDDUDDDUULLUURDULDULLLLRUUUDDRRRLDDDLDLRRDRDRDLUULRLULDRULDLRDRRUDULUDLLUDUULRDLRRUUDDLLDUDDRULURRLULDLDRRULDDRUUDDLURDLRDRLULRRLURRULDUURDLUDLLDRLDULLULDLLRDRDLLLUDLRULLRLDRDDDLDDDLRULDLULLRUUURRLLDUURRLRLDUUULDUURDURRULULRUUURULLLRULLURDDLDRLLRDULLUDLDRRRLLLLDUULRRLDURDURDULULDUURLDUDRLRURRDLUUULURRUDRUUUDRUR""".split( "\n" ) ]

process_codes( *movement_sets )
