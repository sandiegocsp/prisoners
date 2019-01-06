####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'acasePLTW' # Only 10 chars displayed.
strategy_name = 'Assignment 1.3.10'
strategy_description = 'If the last two moves are the same, stay the same. If not, collude.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
        return 'c'
    else:
        now = their_history[-2:]
        if now == ['c','c']:
            return 'c'
        else:
            if now == ['b', 'b']:
                return 'b'
            else:
                return 'c'
        
    
