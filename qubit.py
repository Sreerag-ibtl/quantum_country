import numpy as np

class CBasisState:

    """
    A class that implements computational basis state.
    A computational basis state is a 2-D vector repr-
    sented as:

    |0> := [ 1, 0 ]^T

    The notation |and> is called the ket notation. The
    ket objects are called kets. Simply said a ket is a
    vector.

    There is another computational basis state, denoted:
    
    |1> := [ 0, 1 ]^T

    The computational basis states |0> and |1> are two
    possible states for a qubit. Many more states are
    possible.
    """

    def __init__( self ):

        # |0> and |1> is implemented as a numpy array.
        self.ket_0 = np.array( [[1], [0]] )
        self.ket_1 = np.array( [[0], [1]] )

class QState( CBasisState ):

    """
    A Quantum State is composed of Computational Basis
    States. An example is:

    0.6|0> + 0.8|1>

    In usual vector notation this is:

    0.6[ 1, 0 ]^T + 0.8[ 0, 1 ] =
    [ 0.6, 0 ]^T + [ 0, 0.8 ]^T =
    [ 0.6, 0.8 ]^T

    But for a general quantum state, the entries can be
    complex numbers. For example:

    ( (1+i)/2 )|0> + ( i/sqrt(2) )|1>

    The co-efficients of the basis states are known as
    amplitudes. For a quantum state the constraint is
    that:

    amplitude_0^2 + amplitude_1^2 = 1
    """

    def __init__( self, ket0_comp, ket1_comp ):

        CBasisState.__init__( self )

        # Convert to complex number if necessary.
        ket0_comp = self.toComplex( ket0_comp )
        ket1_comp = self.toComplex( ket1_comp )

        # Make sure sum of amplitudes are one.
        assert ( abs(ket0_comp)**2 + abs(ket1_comp)**2 ) == 1.

        # ket<n>_comp is how much we scale basis.
        self.ket0_comp = ket0_comp
        self.ket1_comp = ket1_comp

        # Component along each axis.
        self.qb0 = self.ket0_comp * self.ket_0
        self.qb1 = self.ket1_comp * self.ket_1

        # Compute state.
        self.state = self.qb0 + self.qb1

    def toComplex( self, comp ):

        """
        Convert to a complex number if necessary.
        """

        if type(comp) == complex:
            return comp
        else:
            return complex( comp )

    def show( self ):

        """
        Display the vector.
        """

        x = self.state[ 0 ]
        y = self.state[ 1 ]

        u = np.array( (0) )
        v = np.array( (0) )

        
            

        
