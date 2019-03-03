"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
"""
Squiggle is a mechanism for storing dictionary data within a multitude
of different host environments (for a specific list please look at the
hosts directory).

Squiggle will automatically return the correct dictionary type for your
given host, from which point you can update/edit the dictionary and then
ask for that dictionary to be saved. 

That dictionary will then be stored persistently within the scene/context.

The following example shows how to create a new dictionary:

..code-block:: python
    
    # -- Import squiggle
    import squiggle
    
    # -- Create a dictionary to store information with
    data = squiggle.get('foobar')
    
    # -- Update some data in the ditionary
    data['bing'] = 'bong'
    
    # -- Calling save will trigger the dictionary to be stored
    # -- in the scene persistently.
    data.save()

You can then access the dictionary in exactly the same way, for 
instance:

..code-block:: python

    # -- Import squiggle
    import squiggle
    
    # -- Create a dictionary to store information with
    data = squiggle.get('foobar')
    
    print(data)
    # 'bing': 'bong'}


Note: All data stored using squiggle must be json serialisable.
"""
__author__ = "Michael Malinowski"
__copyright__ = "Copyright (C) 2019 Michael Malinowski"
__license__ = "MIT"
__version__ = "1.0.0"

from .core import get
from .core import SquiggleDictionary
