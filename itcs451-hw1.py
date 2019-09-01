"""A module for homework 1."""
import random
import copy


class EightPuzzleState:
    """A class for a state of an 8-puzzle game."""

    def __init__(self, board):
        """Create an 8-puzzle state."""
        self.action_space = {'u', 'd', 'l', 'r'}
        self.board = board
        for i, row in enumerate(self.board):
            for j, v in enumerate(row):
                if v == 0:
                    self.y = i
                    self.x = j

    
    def __repr__(self):
        """Return a string representation of a board."""
        output = []
        for row in self.board:
            row_string = ' | '.join([str(e) for e in row])
            output.append(row_string)
        return ('\n' + '-' * len(row_string) + '\n').join(output)

    def __str__(self):
        """Return a string representation of a board."""
        return self.__repr__()

    @staticmethod
    def initializeState():
        """
        Create an 8-puzzle state with a SHUFFLED tiles.
        
        Return
        ----------
        EightPuzzleState
            A state that contain an 8-puzzle board with a type of List[List[int]]: 
            a nested list containing integers representing numbers on a board
            e.g., [[0, 1, 2], [3, 4, 5], [6, 7, 8]] where 0 is a blank tile.
        """
        # TODO: 1
        list = [0,1,2,3,4,5,6,7,8];
        # print(list)
        random.shuffle(list)
        # print(list)
        matrix = []
        x=0
        for i in range(3):
            matrix.append([])
            index = i+x
            matrix[i].append(list[index])
            matrix[i].append(list[index+1])
            matrix[i].append(list[index+2])
            x = x+2
        # print(matrix)
        return EightPuzzleState(matrix)

    def successor(self, action):
        """
        Move a blank tile in the current state, and return a new state.

        Parameters
        ----------
        action:  string 
            Either 'u', 'd', 'l', or 'r'.

        Return
        ----------
        EightPuzzleState or None
            A resulting 8-puzzle state after performing `action`.
            If the action is not possible, this method will return None.

        Raises
        ----------
        ValueError
            if the `action` is not in the action space
        
        """    
        if action not in self.action_space:
            raise ValueError(f'`action`: {action} is not valid.')
        # TODO: 2
        # YOU NEED TO COPY A BOARD BEFORE MODIFYING IT
        new_board = copy.deepcopy(self.board)
        # self.action_space = {'u', 'd', 'l', 'r'}
        #

        if action == 'u':
            # print(self.x)
            # print(self.y)
            # print("lol")
            # print(new_board[self.y][self.x])
            # print(new_board[self.y-1][self.x])
            if self.y == 0 and self.x ==0:
                return None
            if self.y == 0 and self.x ==1:
                return None
            if self.y  == 0 and self.x ==2:
                return None
            temp = new_board[self.y][self.x]
            new_board[self.y][self.x] = new_board[self.y-1][self.x]
            new_board[self.y-1][self.x] = temp

            # print(new_board[self.y][self.x])
            # print(new_board[self.y - 1][self.x])
        if action == 'd':
            if self.y == 2 and self.x ==0:
                return None
            if self.y == 2 and self.x ==1:
                return None
            if self.y == 2 and self.x ==2:
                return None
            temp = new_board[self.y][self.x]
            new_board[self.y][self.x] = new_board[self.y + 1][self.x]
            new_board[self.y + 1][self.x] = temp
        if action == 'l':
            if self.y == 0 and self.x ==0:
                return None
            if self.y == 1 and self.x ==0:
                return None
            if self.y == 2 and self.x ==0:
                return None
            temp = new_board[self.y][self.x]
            new_board[self.y][self.x] = new_board[self.y ][self.x-1]
            new_board[self.y ][self.x-1] = temp
        if action == 'r':
            if self.y == 0 and self.x == 2:
                return None
            if self.y == 1 and self.x == 2:
                return None
            if self.y == 2 and self.x == 2:
                return None
            temp = new_board[self.y][self.x]
            new_board[self.y][self.x] = new_board[self.y][self.x + 1]
            new_board[self.y][self.x + 1] = temp
        return EightPuzzleState(new_board)


    def is_goal(self, goal_board=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
        """
        Return True if the current state is a goal state.

        Parameters
        ----------
        goal_board (optional)
            The desired state of 8-puzzle.

        Return
        ----------
        Boolean
            True if the current state is a goal.

        """

        # TODO: 3
        if self.board[0][0] == 1 and self.board[0][1]==2 and self.board[0][2]==3:
            if self.board[1][0] == 4 and self.board[1][1]==5 and self.board[1][2]==6:
                if self.board[2][0] == 7 and self.board[2][1]==8 and self.board[2][2]==0:
                    return True



        # count = 0
        # print("zzzzzz")
        # for i in range(3):
        #    print("lol")
        #    for j in range(3):
        #        if self.board[i][j] == goal_board[i][j]:
        #            count = count +1
        # if count == 9:
        #     print("count : " + count)
        #     return True
        # print("fgegge")

        return False



class EightPuzzleNode:
    """A class for a node in a search tree of 8-puzzle state."""
    
    def __init__(
            self, state, parent=None, action=None, cost=1):
        """Create a node with a state."""
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        if parent is not None:
            self.path_cost = parent.path_cost + self.cost
        else:
            self.path_cost = 0

    def trace(self):
        """
        Return a path from the root to this node.

        Return
        ----------
        List[EightPuzzleNode]
            A list of nodes stating from the root node to the current node.
                pa
        """
        # TODO: 4

        PathCost = []
        currentNode = self
        while currentNode.parent is not None:
            PathCost.append(currentNode)
            currentNode = currentNode.parent
        return PathCost


        # pass


def test_by_hand():
    """Run a CLI 8-puzzle game."""
    state = EightPuzzleState.initializeState()
    root_node = EightPuzzleNode(state, action='INIT')
    cur_node = root_node
    # print("1")
    print(state)
    action = input('Please enter the next move (q to quit): ')
    while action != 'q':
        new_state = cur_node.state.successor(action)
        cur_node = EightPuzzleNode(new_state, cur_node, action)
        print(new_state)
        if new_state.is_goal():
            print('Congratuations!')
            break
        action = input('Please enter the next move (q to quit): ')

    print('Your actions are: ')
    for node in cur_node.trace():
        print(f'  - {node.action}')
    print(f'The total path cost is {cur_node.path_cost}')

if __name__ == '__main__':
    test_by_hand()